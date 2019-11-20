from django.shortcuts import render, render_to_response
from member.models import MemTable
import MySQLdb
from django.http.response import HttpResponseRedirect
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'kic1234',
    'database':'dbmember',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

# Create your views here.
def Main(request):
    return render_to_response('main.html')

def ListFunc(request):
    datas = MemTable.objects.all()
    return render(request, 'list.html',{'members':datas})

def InsertFunc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        #print(request.POST.get('name'))
        MemTable(
            memid = request.POST.get('memid'),
            passwd = request.POST.get('passwd'),
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            zipcode = request.POST.get('zipcode'),
            address = request.POST.get('address'),
            job = request.POST.get('job'),
        ).save()
        return HttpResponseRedirect('/member/list')
    else:
        return render(request, 'error.html')

def IdcheckFunc(request):
    memid = request.GET.get('memid')
    isRegister = False;
    try:
        #data = MemTable.objects.get(memid=memid)    원래이거
        
        # sql문도 가능 *
        sql = "select * from member_memtable where memid='{}'".format(memid)
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor();
        cursor.execute(sql)
        data = cursor.fetchone()
        
        if data != None:
            isRegister = True
            
        cursor.close() #sql*
        conn.close()  #sql*
    except Exception as e:
        print('err : ', e)
    
    return render(request, 'idcheck.html', {'memid':isRegister})

def ZipcheckFunc(request):
    check = request.GET.get('check')
    return render(request, 'zipcheck.html', {'check':check})

def ZipcheckOkFunc(request):  # 동 이름으로 시작되는 레코드 찾기
    area3 = request.POST.get('area3')
    #sql
    sql = "select * from member_ziptab where area3 like '{0}%'".format(area3)
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'zipcheck.html', {'check':'n', 'datas':datas})