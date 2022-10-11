from django.shortcuts import render
from django.template import loader
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model
from datetime import datetime
from django.urls import reverse
from pytz import timezone

from .filters import OrderFilter,employeeFilter
import pytz
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.


User = get_user_model()
@login_required
def home(request):
    return render(request,'home.html')

@login_required
def add_agent(request):
    agent_name=agent.objects.all()
    if request.method == 'POST':
        name= request.POST['name']
        crd= request.POST['cdate']
        
        
        agent(
            AGENT_NAME=name,
            DOJ=crd
            ).save()
        return HttpResponseRedirect(reverse('add_agent'))
    return render(request, 'addagent.html',{"ag_name":agent_name})

@login_required
def delete_agent(request, id):
  member = agent.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('add_agent'))



@login_required
def add_clint(request):
    agent_name=agent.objects.all()
    ex_code=clint.objects.all()
    tzn=pytz.all_timezones
   
    if request.method == 'POST':
        g_name = request.POST['g_name']
        agnt = request.POST['agent']
        examcode = request.POST['ex_code']
        ex_data = request.POST['ex_date']
        commnt=request.POST['comment']
        t_zone = request.POST['t_z']
        

        if request.POST['ex_date'] and request.POST['t_z']:
            #to get time in dd/mm/yyyy hh:mm:ss  format
            dt_string=ex_data[8:10] + '/' + ex_data[5:7] + '/' + ex_data[0:4] +' ' + ex_data[11:13]+ ':'+ ex_data[14:16]+':00'
            current_tz = timezone(t_zone)
            india_tz = timezone('Asia/Kolkata')
            date = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
            y=date.year
            m=date.month
            d=date.day
            h=date.hour
            mm=date.minute

            current_t = current_tz.localize(datetime(y, m, d, h, mm, 0))
            fd=current_t.strftime("%d/%m/%Y, %H:%M:%S")
            india_t = current_t.astimezone(india_tz)
            in_d=india_t.strftime("%Y-%m-%d")
            in_t=india_t.strftime("%H:%M:%S")
            
            clint(
                GROUP_NAME =g_name,
                AGENT=agnt,
                EXAM_CODE=examcode,
                DATE=in_d,
                TIME=in_t,
                COMMENT=commnt,
                ACTUALDATE=ex_data,
                T_ZONE=t_zone,
            ).save()

        else:
            clint(
                GROUP_NAME =g_name,
                AGENT=agnt,
                EXAM_CODE=examcode,
                COMMENT=commnt,
                ).save()
        
        return HttpResponseRedirect('/')


    return render(request, 'addclint.html',{"tzn_list":tzn,"ag_name":agent_name,'result':ex_code})

@login_required
def tableview(request):
    orderbyList = ['DATE','TIME']
    stu_v=clint.objects.all().order_by(*orderbyList)
    myFilter=OrderFilter(request.GET, queryset=stu_v)
    stu_v=myFilter.qs

    contaxt={'result':stu_v,'myFilter':myFilter}

    return render(request,'tableview.html',contaxt)
@login_required
def took(request,id):
    member=clint.objects.get(id=id)
    member.STASTUS='revoke'
    member.save()
    return HttpResponseRedirect(reverse('tableview'))
@login_required
def revok(request,id):
    member=clint.objects.get(id=id)
    member.STASTUS='revoked'
    member.save()
    return HttpResponseRedirect(reverse('tableview'))
@login_required
def done(request,id):
    member=clint.objects.get(id=id)
    member.STASTUS='Done'
    member.save()
    return HttpResponseRedirect(reverse('tableview'))
@login_required
def delete(request, id):
  member = clint.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('tableview'))

@login_required
def delete_done(request, id):
  member = clint.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('donetable'))

@login_required
def donetable(request):
    orderbyList = ['DATE','TIME']
    stu_v=clint.objects.filter(STASTUS='Done').order_by(*orderbyList)
    myFilter=OrderFilter(request.GET, queryset=stu_v)
    stu_v=myFilter.qs

    contaxt={'result':stu_v,'myFilter':myFilter}
    return render(request,'donetable.html',contaxt)


@login_required
def editepage(request, id):
    mymember = clint.objects.get(id=id)
    agnt=agent.objects.all()
    tzn=pytz.all_timezones
    template = loader.get_template('edite.html')
    context = {
        'mymember': mymember,
        'ag_name':agnt,
        'result':tzn,
    }
    return HttpResponse(template.render(context, request))


@login_required
def edite_table(request,id):
    member=clint.objects.get(id=id)
   
    
    g_name = request.POST['g_name']
    agnt = request.POST['agent']
    examcode = request.POST['ex_code']
    ex_data = request.POST['ex_date']
    commnt=request.POST['comment']
    t_zone = request.POST['t_z']    
    if request.POST['ex_date'] and request.POST['t_z']:
        #to get time in dd/mm/yyyy hh:mm:ss  format
        dt_string=ex_data[8:10] + '/' + ex_data[5:7] + '/' + ex_data[0:4] +' ' + ex_data[11:13]+ ':'+ ex_data[14:16]+':00'
        current_tz = timezone(t_zone)
        india_tz = timezone('Asia/Kolkata')
        date = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
        y=date.year
        m=date.month
        d=date.day
        h=date.hour
        mm=date.minute

        current_t = current_tz.localize(datetime(y, m, d, h, mm, 0))
        fd=current_t.strftime("%d/%m/%Y, %H:%M:%S")
        india_t = current_t.astimezone(india_tz)
        in_d=india_t.strftime("%Y-%m-%d")
        in_t=india_t.strftime("%H:%M:%S")


        member.GROUP_NAME =g_name
        member.AGENT=agnt
        member.EXAM_CODE=examcode
        member.DATE=in_d
        member.TIME=in_t
        member.COMMENT=commnt
        member.ACTUALDATE=ex_data
        member.T_ZONE=t_zone
        member.STASTUS="took"
        member.save()

    else:

        
        member.GROUP_NAME =g_name
        member.AGENT=agnt
        member.EXAM_CODE=examcode
        member.COMMENT=commnt
        member.STASTUS="took"
        member.save()
        
    return HttpResponseRedirect(reverse('tableview'))

@login_required
def admin_home(request):
    return render(request,'admihome.html')


@login_required
def add_employee(request):
    if request.method == 'POST':
        e_name = request.POST['e_name']
        e_id = request.POST['emp_id']
        doj = request.POST['doj']
        pas=request.POST['password']
        u_name=request.POST['username']

        try:
            user = User.objects.create_user(
            username= u_name,
            password=pas,
            is_staff=True,
            )
            user.save()
        
            employee(
                user=user,
                EMP_ID=e_id,
                EMP_NAME=e_name,
                DOJ=doj,      
            ).save()
            return HttpResponseRedirect('/')
        except IntegrityError as e:
            return render(request,'addemployee.html',{'message':'THE USER ALRDY EXIST:'})
    return render(request,'addemployee.html') 

@login_required
def emp_table(request):
    orderbyList = ['DOJ']
    stu_v=employee.objects.all().order_by(*orderbyList)
    myFilter=employeeFilter(request.GET, queryset=stu_v)
    stu_v=myFilter.qs

    contaxt={'result':stu_v,'myFilter':myFilter}
    return render(request,'emp_table.html',contaxt)

@login_required
def delete_emp(request, id):
  member = User.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('emp_table'))


@login_required
def index(request):
    if request.user.is_superuser:
        return render(request, 'admihome.html')
    elif request.user.is_staff:
        return render(request, 'home.html')
    return render(request, 'loging.html')

@login_required
def add_exid(request,id):
    commnt = request.POST['g_name']
    member=clint.objects.get(id=id)
    member.EXAM_ID=commnt
    member.save()
    return HttpResponseRedirect(reverse('tableview'))
