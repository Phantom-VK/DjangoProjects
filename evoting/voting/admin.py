from django.contrib import admin
from django.utils.html import format_html
from .models import Voter, Candidate, Vote, Result, Campaign


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('voter_id', 'name', 'age', 'has_voted')
    list_filter = ('age',)
    search_fields = ('name', 'voter_id')
    ordering = ('name',)

    def has_voted(self, obj):
        return Vote.objects.filter(voter=obj).exists()

    has_voted.boolean = True
    has_voted.short_description = 'Has Cast Vote'


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('candidate_id', 'name', 'party', 'vote_count', 'campaign_status')
    list_filter = ('party',)
    search_fields = ('name', 'party')

    def vote_count(self, obj):
        count = Vote.objects.filter(candidate=obj).count()
        return format_html('<strong>{}</strong> votes', count)

    def campaign_status(self, obj):
        campaign = Campaign.objects.filter(candidate=obj).first()
        if campaign:
            return format_html('<span style="color: green;">Active</span>')
        return format_html('<span style="color: red;">No Campaign</span>')

    campaign_status.short_description = 'Campaign Status'


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('vote_id', 'voter_name', 'candidate_name', 'timestamp')
    list_filter = ('timestamp', 'candidate')
    search_fields = ('voter__name', 'candidate__name')
    date_hierarchy = 'timestamp'

    def voter_name(self, obj):
        return obj.voter.name

    def candidate_name(self, obj):
        return obj.candidate.name


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'candidate_name', 'total_votes', 'vote_percentage')
    readonly_fields = ('total_votes',)

    def candidate_name(self, obj):
        return obj.candidate.name

    def vote_percentage(self, obj):
        total_votes = Vote.objects.count()
        if total_votes > 0:
            percentage = (obj.total_votes / total_votes) * 100
            return format_html('{:.2f}%', percentage)
        return '0%'

    def has_add_permission(self, request):
        # Prevent manual creation of results
        return False


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_id', 'candidate_name', 'start_date', 'end_date', 'campaign_duration')
    list_filter = ('start_date', 'end_date')
    search_fields = ('candidate__name', 'details')
    date_hierarchy = 'start_date'

    def candidate_name(self, obj):
        return obj.candidate.name

    def campaign_duration(self, obj):
        duration = obj.end_date - obj.start_date
        return f"{duration.days} days"

    fieldsets = (
        ('Campaign Information', {
            'fields': ('candidate', 'details')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date'),
            'classes': ('collapse',)
        })
    )