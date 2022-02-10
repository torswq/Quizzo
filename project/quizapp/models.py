from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=255, unique=True)
    correspondingToQuiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    bonus = models.BooleanField(default=False)

    rightAnswer = models.CharField(max_length=255)
    def __str__(self):
        return self.question