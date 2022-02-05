from django.db import models

# decalred ORM Information (Object Relation Mapping)
class Question(models.Model):
    question_test = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # FK 연결
    
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)    
