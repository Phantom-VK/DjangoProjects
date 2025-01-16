from django.shortcuts import render, redirect
from .models import Team

def TeamRegister(request):
    if request.method == "POST":
        team_name = request.POST['team_name']
        team_leader = request.POST['team_leader']
        email = request.POST['email']
        members_count = request.POST['members_count']

        # Save to database
        team = Team(
            team_name=team_name,
            team_leader=team_leader,
            email=email,
            members_count=members_count
        )
        team.save()

        return redirect('home')  # Redirect to the home page or a success page

    return render(request, 'team_registration.html')
