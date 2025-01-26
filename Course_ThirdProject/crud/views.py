from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person
from .forms import PersonForm


# Получение данных из БД
def index(request):
    form = PersonForm()
    people = Person.objects.all()
    return render(request, 'index.html', {'form': form, 'people': people})


# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')


# Изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        form = PersonForm(instance=person)
        return render(request, 'edit.html', {'form': form})


# Удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

    person.delete()
    return HttpResponseRedirect('/')


# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponseNotFound
# from .models import Person
# from .forms import PersonForm
# from django.forms.models import model_to_dict
#
#
# # Получение данных из БД
# def index(request):
#     form = PersonForm()
#     people = Person.objects.all()
#     return render(request, 'index.html', {'form': form, 'people': people})
#
#
# # Сохранение данных в БД
# def create(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             person = Person()
#             person.name = form.cleaned_data['name']
#             person.age = form.cleaned_data['age']
#             person.save()
#     return HttpResponseRedirect('/')
#
#
# # Изменение данных в БД
# def edit(request, id):
#     try:
#         id = request.GET.get('id')
#         person = Person.objects.get(id=id)
#     except Person.DoesNotExist:
#         return HttpResponseNotFound('<h2>Person not found</h2>')
#
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             person.name = form.cleaned_data['name']
#             person.age = form.cleaned_data['age']
#             person.save()
#         return HttpResponseRedirect('/')
#     else:
#         form = PersonForm(model_to_dict(person))
#         return render(request, 'edit.html', {'form': form})
#
#
# # Удаление данных из БД
# def delete(request, id):
#     try:
#         person = Person.objects.get(id=id)
#     except Person.DoesNotExist:
#         return HttpResponseNotFound('<h2>Person not found</h2>')
#
#     person.delete()
#     return HttpResponseRedirect('/')


#EDIT EXAMPLE
# from django.forms.models import model_to_dict
# from django.shortcuts import render
# from django.http import HttpResponseNotFound, HttpResponseRedirect
#
# from main_app.models import User
# from main_app.forms import UserForm
#
#
# def edit_profile(request, id):
#     user = User.objects.filter(id=id)
#     if user:
#         if request.method == 'POST':
#             form = UserForm(request.POST)
#             if form.is_valid():
#                 user.update(**form.cleaned_data)
#             return HttpResponseRedirect(f'/user_profile/{id}/')
#         form = UserForm(model_to_dict(user.first()))
#         return render(request, 'edit_profile.html', {'user_form': form})
#     return HttpResponseNotFound(f'<h2>User profile with id={id} not found</h2>')