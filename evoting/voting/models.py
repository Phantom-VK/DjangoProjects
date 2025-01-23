# models.py
from django.db import models
from django.core.validators import MinValueValidator


class Voter(models.Model):
    voter_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    def __str__(self):
        return f"{self.name} (ID: {self.voter_id})"


class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.party}"


class Vote(models.Model):
    vote_id = models.AutoField(primary_key=True)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['voter']  # Ensures one vote per voter

    def __str__(self):
        return f"Vote by {self.voter.name} for {self.candidate.name}"


class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.candidate.name}: {self.total_votes} votes"


class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Campaign for {self.candidate.name}"



