from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):

    context = {
        "reviews": Review.objects.all().order_by("id"),
    }

    return render(request, "day6/index.html", context)


def create(request):
    return render(request, "day6/create.html")
    # 함수 만들고


def created(request):

    title = request.GET.get("title")
    content = request.GET.get("content")

    Review.objects.create(title=title, content=content)

    return redirect("day6:index")


def detail(request, pk):

    context = {
        "review": Review.objects.get(pk=pk),
    }
    return render(request, "day6/detail.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("day6:index")


def edit(request, pk):
    context = {"edit": Review.objects.get(pk=pk)}
    return render(request, "day6/edit.html", context)


def editted(request, pk):

    new_title = request.GET.get("edit-title")
    new_content = request.GET.get("edit-content")

    review = Review.objects.get(pk=pk)

    review.title = new_title
    review.content = new_content
    review.save()
    return redirect("day6:index")


    
           