from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib import messages

from .models import Comment 
from .forms import CommentForm


class HomeView(ListView):
    model = Comment
    template_name = 'guestbook/index.html'
    ordering = ['-date_added']

    # def get(self, request, *args, **kwargs):
    #     comments = Comment.objects.order_by('-date_added')

    #     context = {'comments' : comments}

    #     return render(request, 'guestbook/index.html', context)


class SignView(View):

    def get(self, request, *args, **kwargs):
        form = CommentForm()
        context = {'form' : form}
        return render(request, 'guestbook/sign.html', context)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, 'Form is not valid')
            redirect('sign')
