# Urls and Routes:

Functions: A block of code can perform some set of task.

```python
def hello_world():
	print("Hello World!")

```

Parameter: we use it during writing function.

Arguments: we use it during calling/invoking the function

## Add new pages:

add new urls page inside the app folder:

```
touch urls.py
```

add path to views page:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("january", views.january),
    path("february", views.february)
]
```

create the views:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("eat no meat for 1 month")

def february(request):
    return HttpResponse("Walk 20 min everyday!")

```
