from django.contrib import admin
from .models import QuestionSentence, Question, Answer

admin.site.register(QuestionSentence)
admin.site.register(Question)
admin.site.register(Answer)
