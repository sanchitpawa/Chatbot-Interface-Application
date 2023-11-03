from rest_framework import generics
from django.http import JsonResponse
from fuzzywuzzy import fuzz
import re
import requests

class testview(generics.GenericAPIView):

    def get(self,request):
        return

    def post(self,request):
        print(request.data['prompt'])
        return JsonResponse({'response':request.data['prompt']},status=200)
    