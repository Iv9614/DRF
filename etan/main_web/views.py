from django.http import JsonResponse
from django.shortcuts import render
from  main_web.models import *
import json 
from django.http import HttpResponse

# Create your views here.

# 阿拉伯數字轉為中文
def int_to_chine(request):
    inp_num=145
    num = {0:"零", 1:"一",2:"二",3:"三",4:"四",5:"五",6:"六", 7:"七",8:"八",9:"九",}
    tmp = []
    floor=''
    while inp_num !=0:
        get_number = inp_num %10
        if get_number in num:
            tmp.append(num[get_number])
        inp_num = inp_num//10
    floor+=''.join( tmp[::-1])
    print(floor)
    # floor = json.dumps( {'floor' : floor} )
    # print('floor===' , floor)
    return JsonResponse ( {'floor' : floor})

# 此處抓取所有資料鄉鎮市區ＡＰＩ
def property_asset＿build_area(request,floor):
    assert request.method =='GET'
    api_return = {}
    
    build_area = build_info.objects.all().values('build_area')
    api_return['build_info'] = build_area
    
    return JsonResponse(api_return)


# 可以取得總樓層數ＡＰＩ
def property_asset＿number_floor(request ,floor):
    assert request.method =="POST"
    api_return ={}
    build_floor = int_to_chine(floor)
    total_floor = build_info.objects.filter(total_number_floors__contains =  build_floor).values('total_number_floors')
    api_return[total_floor] = total_floor
    return JsonResponse (api_return)


#取得建物型態ＡＰＩ
def property_asset＿build_type(request):
    assert request.method =='GET'
    api_return = {}
    build_type = build_info.objects.all().values('build_type')
    api_return['build_type'] = build_type
    
    return JsonResponse (api_return)