from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from feedback.form import FeedbackForm
from feedback.models import Feedback
from django.core.mail import send_mail
# Create your views here.

def create_feedback(request):
    if not request.user.is_authenticated:
        return redirect("blog:home")
    else:
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.author = request.user
                f.save()

                # send_mail(
                #     'New Feedback', # subject
                #     'Check the feedback', #message
                #     'neel.thacker@drcsystems.in', # from email
                #     ['neelthacker0@gmail.com',], # to email
                # )
            return redirect("feedback:feedback")
        else:
            form = FeedbackForm()
            data = Feedback.objects.filter(permission=True).order_by('-created')
        return render(request, 'feedback/user_feedback.html', {'form': form, 'data': data})

def update_feedback(request, pk):
    data = Feedback.objects.get(pk=pk)
    form = FeedbackForm(instance=data)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=data)
        if form.is_valid():
            f = form.save(commit=False)
            f.permission = False
            f.save()
            return redirect("feedback:feedback")
    return render(request, 'feedback/update_feedback.html', {'form': form,})
