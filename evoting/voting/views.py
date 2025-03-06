
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Voter, Candidate, Vote, Result, Campaign
from django.db.models import Count


def dashboard(request):
    context = {
        'total_voters': Voter.objects.count(),
        'total_candidates': Candidate.objects.count(),
        'total_votes': Vote.objects.count(),
        'recent_votes': Vote.objects.order_by('-timestamp')[:5],
        'results': Result.objects.all().order_by('-total_votes')
    }
    return render(request, 'voting/dashboard.html', context)


# CRUD operations for Voter
def voter_list(request):
    voters = Voter.objects.all()
    return render(request, 'voting/voter_list.html', {'voters': voters})



# CRUD operations for Voter
def view_sggs(request):
    return render(request, 'sggs.html')

def view_hostel(request):
    return render(request, 'hostel.html')


def voter_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        Voter.objects.create(name=name, age=age)
        messages.success(request, 'Voter created successfully!')
        return redirect('voter_list')
    return render(request, 'voting/voter_form.html')


def voter_update(request, pk):
    voter = get_object_or_404(Voter, pk=pk)
    if request.method == 'POST':
        voter.name = request.POST.get('name')
        voter.age = request.POST.get('age')
        voter.save()
        messages.success(request, 'Voter updated successfully!')
        return redirect('voter_list')
    return render(request, 'voting/voter_form.html', {'voter': voter})


def voter_delete(request, pk):
    voter = get_object_or_404(Voter, pk=pk)
    voter.delete()
    messages.success(request, 'Voter deleted successfully!')
    return redirect('voter_list')

#CRUD Operations for candidates/admin

def candidates_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'voting/candidates_list.html', {'candidates': candidates})

def candidate_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        party = request.POST.get('party')
        Candidate.objects.create(name=name, party=party)
        messages.success(request, 'Candidate created successfully!')
        return redirect('candi_list')
    return render(request, 'voting/candidates_form.html')

def candidate_update(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        candidate.name = request.POST.get('name')
        candidate.party = request.POST.get('party')
        candidate.save()
        messages.success(request, 'Candidate updated successfully!')
        return redirect('candi_list')
    return render(request, 'voting/candidates_form.html', {'candidate': candidate})


def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    candidate.delete()
    messages.success(request, 'Candidate deleted successfully!')
    return redirect('candi_list')


# Campaign CRUD Operations
def campaign_list(request):
    campaigns = Campaign.objects.select_related('candidate')
    return render(request, 'voting/campaign_list.html', {'campaigns': campaigns})


def campaign_create(request):
    candidates = Candidate.objects.all()
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        details = request.POST.get('details')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        candidate = get_object_or_404(Candidate, pk=candidate_id)
        Campaign.objects.create(
            candidate=candidate,
            details=details,
            start_date=start_date,
            end_date=end_date
        )
        messages.success(request, 'Campaign created successfully!')
        return redirect('campaign_list')
    return render(request, 'voting/campaign_form.html', {'candidates': candidates})


def campaign_update(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    candidates = Candidate.objects.all()

    if request.method == 'POST':
        campaign.candidate_id = request.POST.get('candidate')
        campaign.details = request.POST.get('details')
        campaign.start_date = request.POST.get('start_date')
        campaign.end_date = request.POST.get('end_date')
        campaign.save()
        messages.success(request, 'Campaign updated successfully!')
        return redirect('campaign_list')

    return render(request, 'voting/campaign_form.html', {
        'campaign': campaign,
        'candidates': candidates
    })


def campaign_delete(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    campaign.delete()
    messages.success(request, 'Campaign deleted successfully!')
    return redirect('campaign_list')


# Result Management
def result_list(request):
    # Calculate results based on vote counts
    results = Candidate.objects.annotate(
        total_votes=Count('vote')
    ).order_by('-total_votes')

    total_votes = sum(result.total_votes for result in results)

    # Calculate percentages
    for result in results:
        result.vote_percentage = (result.total_votes / total_votes * 100) if total_votes > 0 else 0

    return render(request, 'voting/result_list.html', {
        'results': results,
        'total_votes': total_votes
    })


# Voting Process
def cast_vote(request):
    if request.method == 'POST':
        voter_id = request.POST.get('voter')
        candidate_id = request.POST.get('candidate')

        try:
            # Validate that voter hasn't already voted
            existing_vote = Vote.objects.filter(voter_id=voter_id).exists()
            if existing_vote:
                messages.error(request, 'You have already cast your vote!')
                return redirect('cast_vote')

            # Create new vote
            Vote.objects.create(
                voter_id=voter_id,
                candidate_id=candidate_id
            )
            messages.success(request, 'Vote cast successfully!')
            return redirect('result_list')

        except Exception as e:
            messages.error(request, f'Error casting vote: {str(e)}')

    # Prepare data for vote casting form
    voters = Voter.objects.filter(
        vote__isnull=True  # Only show voters who haven't voted
    )
    candidates = Candidate.objects.all()

    return render(request, 'voting/cast_vote.html', {
        'voters': voters,
        'candidates': candidates
    })