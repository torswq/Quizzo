from django.db import models
from django.conf import settings

import json

class JSONSupportedModel(models.Model):
    def toJson(obj):
        try:
            return json.dumps(obj)
        except Exception as err:
            print("[!] ERROR CAUGHT IN JSONSupportedModel.toJson")
            print(err)
            return '{"error": "An exception ocurred"}'
    
    def fromJson(str):
        try:
            return json.loads(str)
        except Exception as err:
            print("[!] ERROR CAUGHT IN JSONSupportedModel.fromJson")
            print(err)
            return '{"error": "An exception ocurred"}'
    
    class Meta:
        abstract = True


def quizFromJson(filepath) -> list:
    try:
        with open(filepath, "r") as fp:
            _json = json.load(fp)
    except FileNotFoundError as err:
        if settings.DEBUG:
            print(f"[!] File {file} not found.")
            print(f"[!] Python error: \n{err}")
    except json.JSONDecodeError as jsonerr:
        if settings.DEBUG:
            print(f"[!] Error while decoding the JSON file ({file})")
            print(f"[!] Python error: \n{err}")

    quizList = []
    quizzes = _json["quizzes"]
    for quiz in quizzes:
        questions = []
        _quiz = Quiz(title=quizzes[quiz]["title"])
        quizList.append(_quiz)
        
        _quiz.save()
        try:
            for question in quizzes[quiz]["questions"]:
                options = [
                    
                ]
                _question = Question(
                    question=question["question"],
                    correspondingToQuiz=_quiz,
                    option1 = question["option1"],
                    option2 = question["option2"],
                    option3 = question["option3"],
                    option4 = question["option4"],
                    bonus = question["bonus"],
                    rightAnswer = question["rightAnswer"]
                )
                _question.save()
        except Exception as err:
            if settings.DEBUG:
                print(f"[!] An exception occurred")
                print(f"[!] Python error: \n{err}")
                print("[+] Deleting _quiz object")
                print(f"[+]Object (Quiz) instance: {_quiz}")
                print(f"[+] Object (Quiz) title:{_quiz.title}")
            #Quiz.objects.filter(id=_quiz.id).delete()
            quizList.remove(_quiz)
        print(quiz,"!!!!!!!!!")
    return quizList

class Quiz(JSONSupportedModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    


class Question(JSONSupportedModel):
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