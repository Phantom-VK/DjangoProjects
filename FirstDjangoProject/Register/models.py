from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_leader = models.CharField(max_length=100)
    email = models.EmailField()
    members_count = models.IntegerField()

    def __str__(self):
        return self.team_name
