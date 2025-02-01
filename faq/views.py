from django.shortcuts import render
from googletrans import Translator  
from .forms import FAQForm
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQListAPIView(APIView):   # seeing all the saved FAQ's in datbase 

    def get(self, request, lang='en'):
        faqs = FAQ.objects.all()
        data = []

        for faq in faqs:
            
            data.append({
                'question': faq.get_translated_question(lang),
                'answer': faq.get_translated_answer(lang),
            })

        return Response(data)
    


def add_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            
            translator = Translator()

            faq.question_hi = translator.translate(faq.question, src='en', dest='hi').text
            faq.question_bn = translator.translate(faq.question, src='en', dest='bn').text
            faq.question_ta = translator.translate(faq.question, src='en', dest='ta').text

            faq.answer_hi = translator.translate(faq.answer, src='en', dest='hi').text
            faq.answer_bn = translator.translate(faq.answer, src='en', dest='bn').text
            faq.answer_ta = translator.translate(faq.answer, src='en', dest='ta').text
            

            faq.save() 

            return JsonResponse({
                "status": "success",
                "message": "FAQ saved in successfully!"
            })

        else:
            return JsonResponse({
                "status": "error",
                "errors": form.errors
            }, status=400)

    else:
        form = FAQForm()

    return render(request, 'faq/add_faq.html', {'form': form})

from rest_framework import generics


class FAQRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer