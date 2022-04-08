from django.db import models

# Create your models here.

class Message(models.Model):
    body = models.CharField(max_length=300)
    group = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.body :
            return self.body
        return 'no body '
    def __repr__(self):
        return f"Message() body : {self.body} group : {self.group} date : {self.date}"
    def __add__(self, other):
        if isinstance(other):
            return self.body + " "+ other.body
        return self.body + str(other)
