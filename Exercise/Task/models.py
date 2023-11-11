from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.completed}"


class Comment(models.Model):
    comments = models.TextField()
    task = models.ForeignKey(Task, related_name='coms', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comments} - {self.task}"
