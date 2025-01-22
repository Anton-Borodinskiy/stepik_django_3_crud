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