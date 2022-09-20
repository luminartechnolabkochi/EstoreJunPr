from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
from api.models import Books,Reviews
from api.serializers import BookSerializer,ReviewSerializer

#
# class ProductsView(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response({"msg": "inside products get"})
#
#
# # localHost:8000/morning
# # get
# # Good Morning
#
# class MorningView(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response({"msg": "good morning"})
#
#
# class EveningView(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response({"mag": "Good Evening"})
#
#
# class AddView(APIView):
#
#    def post(self,request,*args,**kwargs):
#        # hello+hai
#        n1=request.data.get("num1")
#        n2=request.data.get("num2")
#        res=int(n1)+int(n2)
#        return Response({"resu":res})
#
# class SubtractionView(APIView):
#
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)-int(n2)
#         return Response({"result":res})
#


class CubeView(APIView):

    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=n**3
        return Response({"result":res})


class NumberChkView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))

        if(n%2==0):
            res="number is even"
        else:
            res="number is odd"
        return Response({"result":res})


# n=3


class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=1
        for i in range(1,(n+1)):
            res=res*i

        return Response(data=res)

class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        txt=request.data.get("text")
        words=txt.split(" ")
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1

        return Response(data=wc)


class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)

        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
       serializer=BookSerializer(data=request.data)
       if serializer.is_valid():

           Books.objects.create(**serializer.validated_data)
           return Response(data=serializer.data)
       else:
           return Response(data=serializer.errors)

    #status code :2xx success
    #            :4xx client error
    #            :5xx serve error
    #            :

class ProductDetailsView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


# method:get
class ReviewsView(APIView):

    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return  Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
#localhost:8000/reviews/1
class ReviewDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")

