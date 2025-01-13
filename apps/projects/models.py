from django.db import models
from ..account.models import UserData

# Create your models here.


class Projects(models.Model):
    STATUS_CHOICES = [
        (1, 'Pending'),
        (2, 'In Progress'),
        (3, 'Completed'),
        (4, 'On Hold'),
    ]
    name = models.CharField(max_length=225, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, null=True, blank=True)
    created_by = models.ForeignKey(UserData, on_delete=models.CASCADE, null=True, blank=True, related_name='projects_created')

    def __str__(self):
        return f"{self.id}: {self.name}" if self.name else f"{self.id}: Unnamed Project"



class Tasks(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Critical'),
    ]

    STATUS_CHOICES = [
        (1, 'Pending'),
        (2, 'In Progress'),
        (3, 'Completed'),
        (4, 'On Hold'),
    ]
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True, blank=True, related_name='task_of_projects')
    name = models.CharField(max_length=225, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, null=True, blank=True)
    assigned_to = models.ForeignKey(UserData, on_delete=models.CASCADE, null=True, blank=True, related_name="assigned_projects")

    def __str__(self):
        return f"{self.id}: {self.name}" if self.name else f"{self.id}: Unnamed Project"


class Team(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="teams", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.name}" if self.name else f"{self.id}: Unnamed Project"


class TeamMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="memberships", null=True, blank=True)
    users = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="team_memberships", null=True, blank=True)
    
    def __str__(self):
        return f"{self.users.username} in {self.team.name}"