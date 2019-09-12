from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Count
import datetime
# Create your views here.

from rest_framework import generics
import datetime
from .models import Click
from .serializers import CustomSerializer


class CustomClickView(generics.ListAPIView):
    value = None
    serializer_class = CustomSerializer
    columns = ["date","channel","country","os","impressions","clicks","installs","spend","revenue", "cpi"]
    field_vals = dict()
    def get_queryset(self):

        """
        Prarse Query parameters and split to get items with mmultiple values
        Format Dates, handle empty params and sort,group by and filter
        """
        for param in self.request.GET.keys():
            if(param in self.columns):
                self.field_vals[param] =  self.request.GET.get(param)
        flds = list()

        if(self.request.GET.get('fields')):
            flds = self.request.GET.get('fields').split(",")
        if(self.request.GET.get('date_from') != None):
            f_date = self.request.GET.get('date_from').split("-")
        else:
            f_date = '2017-05-17'.split("-")
        if(self.request.GET.get('date_to') != None):
            t_date = self.request.GET.get('date_to').split("-")
        else:
            t_date = '2017-06-15'.split("-")

        f_date =  [ int(x) for x in f_date]
        t_date =  [ int(x) for x in t_date]
        sort_by = self.request.GET.get('sort_by')
        group_by = self.request.GET.get('group_by')
        temp_sort = list()
        sort_fields = list()
        if(sort_by):
            temp_sort = sort_by.split(",")

        grp_fields= None
        if(self.request.GET.get('group_by')):
            grp_fields = self.request.GET.get('group_by').split(",")

        sum_fields= list()
        sfi = dict()
        queryset = None
        if(self.request.GET.get('sum_fields')):
            sum_fields = self.request.GET.get('sum_fields').split(",")
            for item in sum_fields:
                sfi['aggr_'+item]= Sum(item)
                if(item in temp_sort):
                    sort_fields.append('aggr_'+item)
                elif('-'+item in temp_sort):
                    sort_fields.append('-aggr_'+item)

        if(bool(self.field_vals)):
            if(not queryset):
                queryset = Click.objects.filter(**self.field_vals)
            else:
                queryset = queryset.filter(**self.field_vals)
        if(f_date or t_date):
            if(queryset):
                queryset = queryset.filter(date__gte=datetime.date(*f_date), date__lte=datetime.date(*t_date))
            else:
                queryset = Click.objects.filter(date__gte=datetime.date(*f_date), date__lte=datetime.date(*t_date))
        if(flds and grp_fields):
            grp_fields.extend(flds)
        if(sum_fields and group_by):
             if(not queryset):
                 queryset = Click.objects.values(*grp_fields).annotate(**sfi)
             else:
                 queryset = queryset.values(*grp_fields).annotate(**sfi).order_by(*sort_fields)
        print("+++-----HELLL---;", queryset)
        return queryset

