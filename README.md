# FAQ Application - Multilingual Support with Django

## Overview
This project is a **Django-based FAQ application** with support for multilingual content, WYSIWYG editor integration, caching for translations, and an efficient REST API. The application allows users to create and manage FAQs in multiple languages and store translations with the help of Google Translate API. The solution also integrates **django-ckeditor** for a rich text editing experience and uses **Redis** to cache translations for improved performance.

## Requirements

### 1. Model Design
- Create a model to store FAQs.
- Each FAQ should have:
  - A question (TextField)
  - An answer (RichTextField for WYSIWYG editor support)
  - Language-specific translations (`question_hi`, `question_bn`, etc.).
- Implement a model method to retrieve translated text dynamically.

### 2. WYSIWYG Editor Integration
- Use `django-ckeditor` to allow users to format answers properly.
- Ensure the WYSIWYG editor supports multilingual content.

### 3. API Development
- Create a **REST API** for managing FAQs.
- Support language selection via the `?lang=` query parameter.
- Ensure responses are fast and efficient using pre-translation caching.

### 4. Caching Mechanism
- Implement a **cache framework** to store translations.
- Use **Redis** for improved performance.

### 5. Multi-language Translation Support
- Use Google Translate API or `googletrans` for translations.
- Automate translations during object creation.
- Provide a fallback to English if translation is unavailable.

### 6. Admin Panel
- Register the FAQ model in the Admin site or create a custom admin interface.
- Enable a user-friendly admin interface for managing FAQs.

### 7. Unit Tests & Code Quality
- Write unit tests using `pytest`.
- Ensure tests cover model methods and API responses.
- Follow PEP8 guidelines for Python and use `flake8` for linting.

### 8. Documentation
- Write a detailed README with:
  - Installation steps.
  - API usage examples.
  - Contribution guidelines.
- Ensure the README is well-structured and easy to follow.

### 9. Git & Version Control
- Use Git for version control.
- Follow conventional commit messages:
  - `feat: Add multilingual FAQ model`
  - `fix: Improve translation caching`
  - `docs: Update README with API examples`
- Ensure atomic commits with clear commit messages.

### 10. Deployment & Docker Support (Bonus)
- Provide a `Dockerfile` and `docker-compose.yml`.
- Deploy the application to Heroku or AWS (optional).

---

## Installation

### Prerequisites
1. Python 3.x
2. Django 5.x
3. Redis
4. Google Translate API or `googletrans`
5. Django CKEditor

### Step 1: Clone the Repository
Clone the project from GitHub:
```bash
git clone https://github.com/yourusername/faq-application.git
cd faq-application
