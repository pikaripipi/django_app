import re
from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

import random

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView

from heart.models import Answer, Question, QuestionSentence
from heart.forms import AnswerForm


def index(request):    
    num = random.randint(1,10)
    # question = Question.objects.get(id=num)

    # if (request.method == 'POST'):
    #     return redirect(to='/question')
    params = {
        'title' : 'みんなのきもち',
        'id': num,
    }
    return render(request, 'heart/index.html', params)




def get_question(request, num):
    num = random.randint(1,10)
    for i in range(5):
        
            question = Question.objects.get(id=num)
            question_sentence = QuestionSentence.objects.get(id=num)
    # if (request.method == 'POST'):
    #     ur_ans = AnswerForm(request.POST, instance=num)
    #     return redirect(to='/question')  
        # question+num?になるように！↑後で必要
        
            params = {
                'title': 'みんなのきもち',
                'id': num,
                'q': question,
                'qs' : question_sentence,
                'form': AnswerForm(),
            }
            return render(request, 'heart/question.html', params)

    return render(request, 'heart/result.html', params)


#sns good
# def good(request, good_id):
#     # good_msg = Message.objects.get(id=good_id)
#     is_good = Good.objects.filter(owner=request.user) \
#             .filter(message=good_msg).count()

#     if is_good > 0:
#         messages.success(request, '既にメッセージにはGoodしています。')
#         return redirect(to='/sns')
    
#     good_msg.good_count += 1
#     good_msg.save()
#     good = Good()
#     good.owner = request.user
#     good.message = good_msg
#     good.save()
#     messages.success(request, 'メッセージにGoodしました！')
#     return redirect(to='/sns')



# #sns POST
# def post(request):
#     if request.method == 'POST':
#         gr_name = request.POST['groups']
#         content = request.POST['content']
#         group = Group.objects.filter(owner=request.user) \
#                 .filter(title=gr_name).first()
#         if group == None:
#             (pub_user, group) = get_public()
#         msg = Message()
#         msg.owner = request.user
#         msg.group = group
#         msg.content = content
#         msg.save()
#         messages.success(request, '新しいメッセージを投稿しました！')
#         return redirect(to='/sns')
    
#     else:
#         form = PostForm(request.user)
    
#     params = {
#         'login_user':request.user,
#         'form':form,
#     }
#     return render(request, 'sns/post.html', params)


#教科書ほぼコピー
# def __init__(self):
#     self.params = {
#         'form': AnswerForm(),
#         'result': None
#     }

# def get(self,request):
#     return render(request, 'heart/question.html',self.params)

# def post(self, request):
#     ch = request.POST['choice']
#     self.params['form'] = AnswerForm(request.POST)
#     return render(request,'heart/question',self.params)
    

    # def get_question(self, request):
    #     num = random.randint(1,10)
    #     question = Question.objects.get(id=num)
    #     params = {
    #         'title' : 'みんなのきもち',
    #         'q': question,
    #     }
    #     return render(request, 'question.html', self.params)

    # def submit_answer(self, request):
    #     self.params = {
    #         'form' : AnswerForm(),
    #     }
    #     self.params['form'] = AnswerForm(request.POST)
    #     return render(request, 'heart/result.html', self.params)





# import random
# from re import X
# from turtle import title
# from django.shortcuts import redirect, render
# from heart.forms import AnswerForm
# from heart.models import Answer, Question

# #def random_page(request):
#     # x = ["question1", "question2", "question3", "question4", "question5",\
#     #     "question6", "question7", "question8", "question9", "question10"]
#     # random_page.choice(x)
#     # params = {
#     #     'x' : 'x',
#     # }
#     # return render(request, 'heart/index.html', params)


# def index(request):
#     qes = Question.objects.all()
#     params = {
#         'x' : 'x',
#     }
#     return render(request, 'heart/index.html', params)

# def set_num(request, num):
#     ans = Answer.objects.get(id=num)
#     if (request.method == 'POST'):
#         anser = AnswerForm(request.POST, instance=ans)
#         anser.save()
#         return redirect(to='/hello')
#     params = {
#         'title': 'Hello',
#         'id':num,
#         'form': AnswerForm(instance=ans),
#     }
#     return render(request, 'hello/edit.html', params)


# def form(request):
#     num = random.randint(1,10)
#     params = {
#         'form': AnswerForm()
#     }
#     return render(request, 'question', params)
