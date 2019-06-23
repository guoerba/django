#from django.shortcuts import render
import django
import datetime
import firstapp.models as model
# Create your views here.

def hello(request):
    t = django.template.loader.get_template('hello.html')
    html = t.render({},request)
    return django.http.HttpResponse(html);

def firsttemplate(request):
    t = django.template.loader.get_template('TestBase.html')
    context = {'name':'Guo','curdatetime':datetime.datetime.now(),}
    html = t.render(context,request)
    return django.http.HttpResponse(html)

def handynasty(request):
    t = django.template.loader.get_template('handynasty.html')
    context = {'state_list':model.HandynastyState.objects.all()}
    html = t.render(context,request)
    return django.http.HttpResponse(html)

def handynastyprefecture(request):
    tdict = {}
    template = ''
    if 'btn' in request.GET:
        valuelist = request.GET.copy().pop('btn')
        stateid = valuelist[0]
        cursor = django.db.connection.cursor()
        cursor.execute(
            "select p.id,p.prefecture,s.state from HanDynasty_Prefecture as p join HanDynasty_State as s on p.state_id=s.id where p.state_id=%s",[stateid])
        row = cursor.fetchall()
        tdict = {'prefecture_list':row}
        template = 'handynastyprefecture.html'
    else:
        tdict = request.GET.dict()
        template = 'hello.html'
    t = django.template.loader.get_template(template)
    return django.http.HttpResponse(t.render(tdict,request))
