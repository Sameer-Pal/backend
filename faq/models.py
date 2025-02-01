from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    question_ta = models.TextField(blank=True, null=True)

    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)
    answer_ta = RichTextField(blank=True, null=True)

    def translate(self):

        cached_translations = cache.get(self.question)
        if cached_translations:
            self.question_hi, self.question_bn, self.question_ta = cached_translations.get('question', (None, None, None))
            self.answer_hi, self.answer_bn, self.answer_ta = cached_translations.get('answer', (None, None, None))
            return  

        translator = Translator()
        self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        self.question_ta = translator.translate(self.question, src='en', dest='ta').text

        self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
        self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text
        self.answer_ta = translator.translate(self.answer, src='en', dest='ta').text

        cache.set(self.question, {
            'question': (self.question_hi, self.question_bn, self.question_ta),
            'answer': (self.answer_hi, self.answer_bn, self.answer_ta),
        }, timeout=3600)  

    def save(self, *args, **kwargs):
        if self.answer or self.question:
            self.translate()
            print(f"Translated Question (HI): {self.question_hi}")  # Log translation for debugging
            print(f"Translated Answer (HI): {self.answer_hi}")
        super().save(*args, **kwargs)

    def get_translated_answer(self, lang='en'):
        translations = {
            'hi': self.answer_hi,
            'bn': self.answer_bn,
            'ta': self.answer_ta
                     }
        return translations.get(lang, self.answer) or self.answer


    def get_translated_question(self, lang='en'):
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
            'ta': self.question_ta,
        }
        return translations.get(lang, self.question) or self.question  # Default to the original question if no translation is found

    def __str__(self):
        return self.question
