from django.shortcuts import render
from models import *
import json 
# Create your views here.


# 此處抓取所有資料鄉鎮市區ＡＰＩ
def property_asset＿build_area(request):
    assert request.method =='GET'
    api_return = {}
    build_area = build_info.objects.all().values('build_area')
    api_return['build_info'] = build_area
    
    return api_return


# 可以取得總樓層數ＡＰＩ
def property_asset＿number_floor(request ,floor):
    assert request.method =="POST"
    api_return ={}
    total_floor = build_info.objects.filter(total_number_floors = floor).values('total_number_floors')
    api_return[total_floor] = total_floor
    return api_return


#取得建物型態ＡＰＩ
def property_asset＿build_type(request):
    assert request.method =='GET'
    api_return = {}
    build_type = build_info.objects.all().values('build_type')
    api_return['build_type'] = build_type
    
    return api_return