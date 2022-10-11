import datetime
from sqlite3 import Time

import django_filters
from django_filters import DateFilter,TimeFilter
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import *
from django import forms





class DateInput(forms.DateInput):
    input_type = 'date'



class OrderFilter(django_filters.FilterSet):
    DATE=django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
   
    #date=DateFilter(field_name="S_doj",lookup_expr='date')
    class Meta:
        model = clint
        
        fields = '__all__'
        exclude = ['DATE','LOCATION','COMMENT','ACTUALDATE','T_ZONE','EXAM_ID','GROUP_NAME','AGENT','EXAM_CODE','TIME']
        '''
        widgets = {
            'S_doj':AdminDateWidget(),
            'ex_t':AdminTimeWidget(),

         }
            '''

class employeeFilter(django_filters.FilterSet):
    DOJ=django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
   
    #date=DateFilter(field_name="S_doj",lookup_expr='date')
    class Meta:
        model = employee
        
        fields = '__all__'
        exclude = ['user']
