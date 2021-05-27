from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Leave_Form
from .forms import ProfileForm, LeaveForm
# Create your views here.

def myIndex(request):
    return render(request, 'leaveapp/welcome.html')

def dashboard(request):
    return render(request, 'leaveapp/index.html')

def layout(request):
    return render(request, 'leaveapp/layout.html')

def approved(request):
    return render(request, 'leaveapp/approved.html')

def w_a_approved(request):
    return render(request, 'leaveapp/w_a_approved.html')

def disapproved(request):
    return render(request, 'leaveapp/disapproved.html')

def stats(request):
    return render(request, 'leaveapp/stats.html')

def leave_form(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = LeaveForm()
    return render(request, 'leaveapp/leave_form.html', {'form': form})

def members(request):
    return render(request, 'leaveapp/members.html')

def edit_profile(request):
    return render(request, 'leaveapp/edit_profile.html')

def approved_report(request):
    return render(request, 'leaveapp/approved_report.html')

def w_a_approved_report(request):
    return render(request, 'leaveapp/w_a_approved_report.html')

def disapproved_report(request):
    return render(request, 'leaveapp/disapproved_report.html')

def members_setting(request):
    return render(request, 'leaveapp/members_setting.html')

def sort_setting(request):
    return render(request, 'leaveapp/sort_setting.html')

def department_setting(request):
    return render(request, 'leaveapp/department_setting.html')

def sort_edit(request):
    return render(request, 'leaveapp/sort_edit.html')

def loginForm(request):
    return render(request, 'leaveapp/login.html')

'''def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('loginForm')
        else:
            messages.info(request, 'ไม่มีชื่อผู้ใช้งาน')
            return redirect('loginForm')
            
    return render(request, 'leaveapp/login.html')'''

'''def logout(request):
    auth.logout(request)
    return redirect('/')'''

def signupForm(request):
    return render(request, 'leaveapp/signup_form.html')

def signup(request):

    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username = username).exists():
            messages.info(request, 'Duplicate UserName')
            return redirect('/signupForm')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'Duplicate Email')
            return redirect('/signupForm')
        else:
            user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
            first_name = firstname,
            last_name = lastname,
            )

        user.save()
        return redirect('/')
    else:
        messages.info(request, 'Password does not match')
        return redirect('/signupForm')

def forget_password(request):
    return render(request, 'leaveapp/forget_password.html')

# Data for Previews

def profile_view(request):
    context = {}

    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "leaveapp/profile_view.html", context)
    
# Testing LeaveForm
def add(request):
    form = LeaveForm()
    return render(request, 'leaveapp/form_add.html', {'form': form})