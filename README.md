# FAQ Application - Multilingual Support using Django

## Overview
This project is a **Django-based FAQ application** with support for multilingual content, WYSIWYG editor integration, caching for translations, and an efficient REST API. The application allows users to create and manage FAQs in multiple languages and store translations with the help of Google Translate API. The solution also integrates **django-ckeditor** for a rich text editing experience and uses **Redis** to cache translations for improved performance.

## Table of Contents
- [Installation](#Installation)
- [demoVideo](https://youtu.be/sssU93mXWMU)
- [Optimization](#Optimization)
- [Tests](#UnitTests)


## Features
- **WYSIWYG Editor Support** using django-ckeditor for Formatting Answer
- **Multi-Language Translation** (Supports English, Hindi, Bengali,Tamil etc.)
- **REST API** for FAQs with language selection via query parameter
- **Admin Panel** for easy FAQ management for FAQ's
- **Caching** with Redis for optimized performance
- **Unit Tests** to ensure functionality and their efficiency




### Prerequisites
- Python 3.12+
- Django 5+
- Redis (for caching)

## Installation

### Prerequisites
1. Python 3.x
2. Django 5.x
3. Redis
4. Google Translate API or `googletrans`
5. Django CKEditor

### Steps
1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-project-folder>
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

2. **Installing Django in virtual enviromtne**
    ```bash
    pip install django
    ```
3. **Starting Project**
    ```bash
    django-admin startproject <name_of_project>
    ```
   
4. **Creating App inside Project**
    ```bash
    python manage.py startapp <app_name>
    ```
5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

7. **Creating  superuser:**
    ```bash
    python manage.py createsuperuser
    ```

9. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## API Usage

### Fetch FAQs in English (Default)
```bash
curl http://localhost:8000/api/faqs/

``` 
### Fetch FAQs in Hindi
``` 

curl http://localhost:8000/api/faqs/?lang=hi
``` 

### Fetch FAQs in Bengali
``` 

curl http://localhost:8000/api/faqs/?lang=bn
```


### Fetch FAQs in Tamil
``` 

curl http://localhost:8000/api/faqs/?lang=tm
```

## UnitTests
### For Running Test Cases 
``` 
pytest tests.py

```

## Optimization

In this project, several optimizations have been implemented to improve performance and ensure efficient data access:

1. **Dictionary in Python for Fast Access**  
   A dictionary is used to store FAQ data, which provides **O(1) average time complexity** for lookups. This ensures fast access to FAQ data during translation and retrieval, reducing the need for repeated queries to the database.

2. **Cache Memory for Faster Access**  
   To further enhance performance, Redis is used for caching frequently accessed data, especially translations. The cache stores the translated FAQ fields (e.g., `question_hi`, `question_bn`, etc.), ensuring that they can be retrieved quickly without needing to call external translation APIs or database queries every time. This reduces latency and improves overall response time for the application.
   
## Optimization

**Sameer2319** and **Sameer Pal** are same accounts, 
**Sameerpal2319** is **github student developer pack enabled account** and **sameer pal** is my **personal account**,


## GitHub Account Clarification
The commits for this project are made from the Sameer2319 and Sameer Pal account. However, both Sameer2319 and Sameerpal2319 belong to the Same Person:

Sameer-Pal – This is the account where my code repository is hosted.
Sameer2319 - Vs Code is configured with this account.

However, both accounts belong to me, and I can verify ownership if needed
