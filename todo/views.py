from todo.models import todo
from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        id = request.user.id
        items = todo.objects.filter(user1=id)
        count = todo.objects.filter(user1=id).count()
        return render(request, 'index.html', {'items': items, 'count':count})
        
    else:
        return redirect('/')

def additem(request):    
    if request.user.is_authenticated:
        if request.method == 'POST':
    
            text = request.POST.get('text')
            added_date = timezone.localtime(timezone.now())
            priority = request.POST.get('priority')
           
            if priority == 'Select Priority':
                messages.info(request, 'Please Select Priority')
                return redirect('/todo')
                
            else:
                if priority == str(1):
                    priority = 'HIGH PRIORITY'
                elif priority == str(2):
                    priority = 'MEDIUM PRIORITY'
                else:
                    priority = 'LOW PRIORITY'

                id = request.user.id

                inst = todo(user1_id=id, text=text,
                            added_date=added_date, priority=priority)
                inst.save()
                messages.info(
                    request, 'Task added successfully')
                return redirect('/todo')
        else:
            return render(request,'index.html')
    else:
        return redirect('/')
    
def delitem(request, id):
    if request.user.is_authenticated:
        object = todo.objects.get(id=id)
        object.delete()
        return redirect('/todo')
    else:
        return redirect('/')


def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(
                    request, 'Your password was successfully updated!')
                return redirect('/todo')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'changepass.html', {
            'form': form
    })
    else:
        return redirect('/')
