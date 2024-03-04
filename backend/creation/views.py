from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.
@csrf_exempt
def UserRegisterApi(request):
    if request.method =='GET':
        selectData = UserRegister.objects.all()
        serializer = UserRegisterserializers(selectData, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserRegisterserializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def OperationByOne(request, pk):
    print('Operation by one')
    try:
       checkdata =UserRegister.objects.get(username=pk)
    except UserRegister.DoesNotExist:
        print('User registration does not exist')
        return JsonResponse(status=404)
    
    if request.method == 'GET':
        print("Entered userRegister")
        serializer = UserRegisterserializers(checkdata)
        return JsonResponse(serializer.data)
    
    elif request.method == 'DELETE':
        deletdata = UserRegister.objects.get(id=pk).delete()
        return JsonResponse({'messega':'data deleted'},)

    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserRegisterserializers(checkdata, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse({'message':'Failed to update'}, serializer.errors)
    
class LoanApi(APIView):
    def get(self, request):
        selectData = Loan.objects.all()
        serializer = LoanSerialiser(selectData, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = LoanSerialiser(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})

    



