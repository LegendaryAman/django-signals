# Django Signals Demo

This project demonstrates how to use **Django Signals** to perform actions automatically when certain events occur, such as creating or updating a model instance.

## 📁 Project Structure

django-signals/
│
├── myapp/
│ ├── models.py # Contains the MyModel class
│ ├── signals.py # Contains pre_save, post_save, pre_delete, post_delete signals
│ └── apps.py # Connects the signals
│
├── signal_demo_project/
│ └── settings.py # Includes 'myapp' in INSTALLED_APPS
│
├── manage.py
└── .gitignore

markdown
Copy code

## 🛠️ Features

- Automatically logs actions using `signals.py`:
  - `pre_save`
  - `post_save`
  - `pre_delete`
  - `post_delete`
- Demonstrates use of `threading.get_ident()` to track the caller thread
- Uses Django’s `transaction.atomic()` for safe database operations

## 🚀 How to Run

1. **Create and activate virtual environment**
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
Install dependencies

bash
Copy code
pip install django
Run the server

bash
Copy code
python manage.py runserver
Open Django shell and test signals

bash
Copy code
python manage.py shell
Inside shell:

python
Copy code
import threading
from myapp.models import MyModel
from django.db import transaction

print("Caller Thread ID:", threading.get_ident())

with transaction.atomic():
    MyModel.objects.create(name="Signal Test")
📌 Output Example
bash
Copy code
Caller Thread ID: 14892
PRE_SAVE: Creating a new object
POST_SAVE: Object created
🙋 Author
Aman Maurya
GitHub: @LegendaryAman