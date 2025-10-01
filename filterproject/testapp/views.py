from django.shortcuts import render
from testapp.models import FilterModel

# Create your views here.
def upper(req):
    records = FilterModel.objects.all()
    print('hello world...')
    d = {'records':records}
    return render(req,'testapp/upper.html',d)