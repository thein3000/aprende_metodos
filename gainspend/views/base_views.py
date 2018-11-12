from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import is_safe_url
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
import datetime
import json
from gainspend.forms import UserMethodForm

@login_required
def main_dashboard(request):
    methods = Method.objects.all()
    completed_list = []
    for method in methods:
        completed = len(UserMethod.objects.filter(user=request.user, method=method))
        last_completed_value = completed
        if completed >= 1:
            completed_list.append(True)
        else:
            completed_list.append(False)
    completed_list.insert(0,True)
    methods_list = zip(methods, completed_list)
    context = {
        "methods_list": methods_list
    }
    return render(request, 'gainspend/pages/main_dashboard.html', context)

@login_required
def successful_excercise(request):

    context = {
    }
    return render(request, 'gainspend/pages/successful_excercise.html', context)


@login_required
def register_method_completion(request):
    if request.method == 'POST':
        form = UserMethodForm(request.POST)
        if form.is_valid():
            post_seconds = form.cleaned_data['seconds']
            print(form.cleaned_data['method_id'])
            post_method = Method.objects.get(field_id = form.cleaned_data['method_id'])
            print(post_method)
            user_method = UserMethod(
                user = request.user,
                method = post_method,
                completed = True,
                seconds = post_seconds
            )
            user_method.save()
            # If next method is a subject, then mark it as completed to enable it in main_dashboard
            try:
                next_method = Method.objects.get(field_id = (post_method.field_id + 1))
            except Exception as e:
                print(e)
                return redirect("successful_excercise")
            if next_method.is_subject:
                next_user_method = UserMethod(
                    user = request.user,
                    method = next_method,
                    completed = True,
                    seconds = 0
                )
                next_user_method.save()
            return redirect("successful_excercise")
        else:
            return redirect("main_dashboard")
    else:
        return redirect("main_dashboard")
