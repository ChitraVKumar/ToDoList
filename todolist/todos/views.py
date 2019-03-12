from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Todo


def index(request):
    query = request.GET.get('q', None)
    todos = Todo.objects.all()
    if query is not None:
        todos = todos.filter(Q(title__icontains=query) | Q(text__icontains=query))
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)


def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')


def delete(request, id=None):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/todos")


def complete(request, id):
    todo = Todo.objects.get(pk=id)
    if(todo.complete):
        todo.complete = False
    else:
        todo.complete = True
    todo.save()
    return redirect('/todos')
