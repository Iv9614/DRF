from django.http import JsonResponse
from django.shortcuts import render
from  main_web.models import *
import json 
from django.http import HttpResponse
from main_web.common import int_to_chine

# 此處抓取所有資料鄉鎮市區ＡＰＩ
def property_asset＿build_area(request):
    assert request.method =='GET'
    api_return = {}
    build_area = build_info.objects.all().values('build_area')
    api_return['build_info'] = build_area
    return JsonResponse(api_return)


# 可以取得總樓層數ＡＰＩ
def property_asset＿number_floor(request ,trans_num):
    assert request.method =="POST"
    api_return ={}
    build_floor = int_to_chine(trans_num)  # 由common.py中取用阿拉伯數字轉換中文數字函式
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