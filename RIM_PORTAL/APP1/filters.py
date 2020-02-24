from .models import Issue,Data
import django_filters
from django.contrib.auth.models import User , auth
from django_filters import DateFilter,CharFilter



class IssueFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="sys_creation_date" , lookup_expr='gte')
    end_date=DateFilter(field_name="sys_creation_date" , lookup_expr='lte')
    desc=django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    example_inc= django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Issue
        fields = ['id','title','resolution','desc','example_inc','resolution','user_id']
        exclude=['img','show']



class IssueFilter1(django_filters.FilterSet):
    if User.is_authenticated:
        user = User.username
        start_date = DateFilter(field_name="sys_creation_date", lookup_expr='gte')
        end_date = DateFilter(field_name="sys_creation_date", lookup_expr='lte')
        desc = django_filters.CharFilter(lookup_expr='icontains')
        title = django_filters.CharFilter(lookup_expr='icontains')
    else:
        pass
    class Meta:
        model = Issue
        fields = ['id','title','resolution','desc','example_inc','resolution','user',]
        exclude=['show']



