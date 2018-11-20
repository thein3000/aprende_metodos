from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from gainspend.forms import UserMethodForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def main_dashboard(request):
    methods = Method.objects.all()
    completed_list = []
    seconds_list = []
    second_tag_colors = []
    for method in methods:
        user_methods = UserMethod.objects.filter(user=request.user, method=method)
        completed = len(user_methods)
        if completed >= 1:
            completed_list.append(True)
            seconds = user_methods.order_by('seconds').first().seconds
            seconds_list.append(seconds)
            if seconds <= 180:
                second_tag_colors.append("green")
            elif seconds <= 360:
                second_tag_colors.append("yellow darken-4")
            else:
                second_tag_colors.append("red")
        else:
            completed_list.append(False)
            seconds_list.append(0)
            second_tag_colors.append("")
    completed_list.insert(0,True)
    completed_list[1] = True
    methods_list = zip(methods, completed_list, seconds_list, second_tag_colors)
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
                    seconds = 0
                )
                next_user_method.save()
            return redirect("successful_excercise")
        else:
            return redirect("main_dashboard")
    else:
        return redirect("main_dashboard")
