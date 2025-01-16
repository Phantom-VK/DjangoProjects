
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
    return render(request, 'voting/candidates_form.html', {'voter': candidate})


def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    candidate.delete()
    messages.success(request, 'Candidate deleted successfully!')
    return redirect('candi_list')