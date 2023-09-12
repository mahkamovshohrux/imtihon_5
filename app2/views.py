from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import YangilikSerializer1,YangilikSerializer2
from .models import Yangilikmadel1,Yangilikmadel2
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import datetime

class Listyangilik1(APIView):
    def get(self, request):
        all_yangilik1 = Yangilikmadel1.objects.all()
        yangiliklar1 = YangilikSerializer1(all_yangilik1, many=True)
        return Response(yangiliklar1.data)

class Listyangilik2(APIView):
    def get(self, request):
        all_yangilik2 = Yangilikmadel2.objects.all()
        yangiliklar2 = YangilikSerializer2(all_yangilik2, many=True)
        return Response(yangiliklar2.data)
    
class Detailyangilik1(APIView):
    def get(self, request, *args, **kwargs):
        id_yangi1 = get_object_or_404(Yangilikmadel1, id=kwargs['id_y1'])
        id_yangilik1  = YangilikSerializer1(id_yangi1)
        return Response(id_yangilik1.data)
    
class Detailyangilik2(APIView):
    def get(self, request, *args, **kwargs):
        id_yangi2 = get_object_or_404(Yangilikmadel2, id=kwargs['id_y2'])
        id_yangilik2  = YangilikSerializer2(id_yangi2)
        return Response(id_yangilik2.data)

class Createyangilik1(APIView):
    def post(self, request):
        creat1 = YangilikSerializer1(data=request.data)
        if creat1.is_valid():
            creat1.save()
            return Response(creat1.data)
        return Response(creat1.errors)

class Createyangilik2(APIView):
    def post(self, request):
        creat2 = YangilikSerializer2(data=request.data)
        if creat2.is_valid():
            creat2.save()
            return Response(creat2.data)
        return Response(creat2.errors)

class UpdateYangilik1(APIView):
    def patch(self, request, *args, **kwargs):
        updata1 = get_object_or_404(Yangilikmadel1, id=kwargs['id_y1'])
        updataseller1 = YangilikSerializer1(updata1, data=request.data, partial=True)
        if updataseller1.is_valid():
            updataseller1.save()
            return Response(updataseller1.data)
        return Response(updataseller1.errors)

class UpdateYangilik2(APIView):
    def patch(self, request, *args, **kwargs):
        updata2 = get_object_or_404(Yangilikmadel1, id=kwargs['id_y2'])
        updataseller2 = YangilikSerializer2(updata2, data=request.data, partial=True)
        if updataseller2.is_valid():
            updataseller2.save()
            return Response(updataseller2.data)
        return Response(updataseller2.errors)

class DeleteYangilik1(APIView):
    def delete(self, request, *args, **kwargs):
        delet1 = get_object_or_404(Yangilikmadel1, id=kwargs['id_y1'])

        delet1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeleteYangilik2(APIView):
    def delete(self, request, *args, **kwargs):
        delet2 = get_object_or_404(Yangilikmadel2, id=kwargs['id_y2'])

        delet2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
