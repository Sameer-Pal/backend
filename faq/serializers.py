from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn', 'question_ta', 'answer_ta']
   
        def get_answer(self, obj):
            request = self.context.get('request')
            lang = request.GET.get('lang', 'en')  # Default to English

            translations = {
                'hi': obj.answer_hi,
                'bn': obj.answer_bn,
                'ta': obj.answer_ta
            }

            return translations.get(lang, obj.answer) or obj.answer
