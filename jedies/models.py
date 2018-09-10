from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "%s"%(self.name)

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    age = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return "%s"%(self.name)



class Jedi(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE)
    def __str__(self):
        return "%s из планеты %s"%(self.name, self.planet)

class Test(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    question = models.TextField()
    def __str__(self):
        return "%s"%(self.question)

class Answer(models.Model):
    CHOICES = (
        ('Y', 'Да'),
        ('N', 'Нет'),
    )
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    question = models.ForeignKey(Test, on_delete=models.CASCADE)
    answer = models.CharField(max_length=3, choices = CHOICES)

