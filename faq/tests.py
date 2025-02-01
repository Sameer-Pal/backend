import pytest
from unittest.mock import patch, MagicMock
from django.core.cache import cache
from faq.models import FAQ  # Adjust this import to match your model's location
from googletrans import Translator

@pytest.mark.django_db
def test_translate_with_cache_hit():
    # Create an instance of the model
    faq = FAQ(question="What is Django?", answer="Django is a web framework.")

    cache.set(faq.question, {
        'question': ('Django के बारे में क्या है?', 'ডjango সম্পর্কে কি?', 'ட்ஜாங் பற்றி என்ன?'),
        'answer': ('Django एक वेब फ्रेमवर्क है।', 'ডjango একটি ওয়েব ফ্রেমওয়ার্ক।', 'ட்ஜாங் ஒரு வலைமை அமைப்பாகும்.'),
    }, timeout=3600)


    # Call translate method
    faq.translate()

    # Assert translations are fetched from cache
    assert faq.question_hi == 'Django के बारे में क्या है?'
    assert faq.question_bn == 'ডjango সম্পর্কে কি?'
    assert faq.question_ta == 'ட்ஜாங் பற்றி என்ன?'
    assert faq.answer_hi == 'Django एक वेब फ्रेमवर्क है।'
    assert faq.answer_bn == 'ডjango একটি ওয়েব ফ্রেমওয়ার্ক।'
    assert faq.answer_ta == 'ட்ஜாங் ஒரு வலைமை அமைப்பாகும்.'


@pytest.mark.django_db
def test_translate_with_cache_miss():
    faq = FAQ(question="What is Python?", answer="Python is a programming language.")

    with patch.object(Translator, 'translate', return_value=MagicMock(text="पायथन एक प्रोग्रामिंग भाषा है।")):
        faq.translate()

    assert faq.question_hi == 'पायथन एक प्रोग्रामिंग भाषा है।'

@pytest.mark.django_db
def test_translate_with_cache_expiration():
    # Create an instance of the model
    faq = FAQ(question="What is Flask?", answer="Flask is a web framework.")

    # Set cache with a short timeout
    cache.set(faq.question, {
        'question': ('Flask क्या है?',),
        'answer': ('Flask एक वेब फ्रेमवर्क है।',),
    }, timeout=0.1) 
    import time
    time.sleep(0.2)  # Sleep to allow the cache to expire

    with patch.object(Translator, 'translate', return_value=MagicMock(text="Flask is a web framework.")):
        faq.translate()

    assert faq.question_hi == 'Flask is a web framework.'
    assert faq.answer_hi == 'Flask is a web framework.'
