from django.urls import path
from . import views

urlpatterns = [
    # path('faqs/', views.faq_list_view, name='faq_list'),
    path('api/faqs/', views.FAQListAPIView.as_view(), name='faq-api'),  # For the API
    path('add/', views.add_faq, name='add_faq'),
    path('api/faqs/<int:pk>/', views.FAQRetrieveUpdateDestroyAPIView.as_view(), name='faq-detail'),  # Retrieve, Update & Delete FAQ
]
