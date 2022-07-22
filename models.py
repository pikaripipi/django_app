from django.db import models




class QuestionSentence(models.Model):
    q_name = models.CharField(max_length=10)
    q_sentence = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.q_name)+str(self.q_sentence)


class Question(models.Model):
    q_name = models.ForeignKey(QuestionSentence,on_delete=models.CASCADE)
    q1 = models.CharField(max_length=200)
    q2 = models.CharField(max_length=200)
    q3 = models.CharField(max_length=200)

    def __str__(self):
        return str(self.q1)+str(self.q2)+str(self.q3)



class Answer(models.Model):
    q_name = models.ForeignKey(QuestionSentence,on_delete=models.CASCADE)
    a1 = models.IntegerField(default=0)
    a2 = models.IntegerField(default=0)
    a3 = models.IntegerField(default=0)

    def __str__(self):
        return str(self.a1)+str(self.a2)+str(self.a2)


