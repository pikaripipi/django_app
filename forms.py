from secrets import choice
from django import forms, views
from.models import Question, Answer







# # class AnswerForm(forms.Form):

#     data= [
#         ('qes1', '1ばんめ'),
#         ('qes2', '2ばんめ'),
#         ('qes3', '3ばんめ'),
#     ]

#     your_answer = forms.ChoiceField(label='きみのこたえ', \
#     widget=forms.RadioSelect(choices=data))


    # data= [
    #     ('1' 'q1'),
    #     ('2', 'q2'),
    #     ('3', 'q3'),
    # ]
# class AnswerForm(forms.Form):

#     def __init__(self, num, *args, **kwargs):
#         super(AnswerForm, self).__init__(*args, **kwargs)
#         qes = Question.objects.filter(num=id)#<-usernameじゃなくnum
#         self.fields['q'] = forms.MultipleChoiceField(\
#             choices=[(i.question, i.question) \
#                 for i in Question.objects.filter(num=id)], \
#             widget=forms.RadioSelect(),#<-radio
#         )


#SNS Group Check Form
# class GroupCheckForm(forms.Form):
#     def __init__(self, user, *args, **kwargs):
#         super(GroupCheckForm, self).__init__(*args, **kwargs)
#         public = User.objects.filter(username='public').first()
#         self.fields['groups'] = forms.MultipleChoiceField(
#             choices=[(item.title, item.title) for item in \
#                 Group.objects.filter(owner__in=[user,public])],
#             widget=forms.CheckboxSelectMultiple(),
#         )



class AnswerForm(forms.Form):

    data= [
        ('qes1', '1ばんめ'),
        ('qes2', '2ばんめ'),
        ('qes3', '3ばんめ'),
    ]

    choice = forms.ChoiceField(label='きみのこたえ', choices=data,\
    widget=forms.RadioSelect())





# class GroupCheckForm(forms.Form):
#     def __init__(self, user, *args, **kwargs):
#         super(GroupCheckForm, self).__init__(*args, **kwargs)
#         qes = Question.objects.filter(num='q')#<-usernameじゃなくnum
#         self.fields['groups'] = forms.MultipleChoiceField(#<-groups変える
#             choices=[(item.title, item.title) for item in \
#                 Group.objects.filter(owner__in=[user,public])],
#             widget=forms.RadioSelect(),#<-radio