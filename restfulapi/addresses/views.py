from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser

# # Create your views here.
# @csrf_exempt
# def address_list(request):
#     if request.method == 'GET':
#         query_set = Address.objects.all()
#         serializer = AddressSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = AddressSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def address(request, pk):
#
#     obj = Address.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         serializer = AddressSerializer(obj)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = AddressSerializer(obj, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method =='DELETE':
#         obj.delete()
#         return HttpResponse(status=204)
#
#
#
# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         search_name = data['name']
#         obj = Address.objects.get(name=search_name)
#
#         if data['phone_number'] == obj.phone_number:
#             return HttpResponse(status=200)
#         else:
#             return HttpResponse(status=400)
#

@csrf_exempt
def app_login(request):
    if request.method == 'POST':
        id = request.POST.get('userId','')
        pw = request.POST.get('userPassword','')

        obj = User.objects.get(userId=id)

        # result = authenticate(userId=id, userPassword=pw)

        if obj.userPassword == pw:
            print('로그인 성공')
            return JsonResponse({'code':'0000', 'msg':'로그인에 성공하셨습니다.'}, status=200)
        else:
            print('로그인 실패')
            return JsonResponse({'code':'1001', 'msg':'로그인에 실패하셨습니다.'}, status=200)

@csrf_exempt
def app_register(request):
    if request.method == 'POST':
        id = request.POST.get('userId')
        pw = request.POST.get('userPassword')
        name = request.POST.get('userName')
        age = request.POST.get('userAge')

        try:
            obj = User.objects.get(userId=id)

        except:
            # data = JSONParser().parse(request)
            serializer = UserSerializer(data ={'userId':id,'userPassword':pw,'userName':name,'userAge':int(age)})
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'code': '0000', 'msg': '회원가입에 성공하셨습니다.'}, status=200)
            return JsonResponse({'code': '1001', 'msg': '회원가입에 실패하셧습니.'}, status=400)
        return JsonResponse({'code': '2002', 'msg': '이미 존재하는 아이디 입니다.'}, status=200)

@csrf_exempt
def app_board(request):
    if request.method == 'GET':
        query_set = Board.objects.all()
        serializer = BoardSerializer(query_set, many=True)
        return JsonResponse({'code':'0000','msg':'간다이쌔끼야.'}, status=200)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'code':'0000','msg':'게시글이 성공적으로 저장 되었습니다.'}, status=200)
        return JsonResponse({'code':'1001','msg':'게시글 저장에 실패 하였습니다.'}, status=400)









