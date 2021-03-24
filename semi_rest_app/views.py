from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

# Create your views here.


def root(request):
    return redirect("/shows")


def shows(request):
    shows = Show.objects.all()
    context = {"shows": shows}
    return render(request, "shows.html", context)


def shows_new(request):
    return render(request, "shows_new.html")


def create_show(request):
    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("shows_new.html")
    else:
        show = Show.objects.create(
            title=request.POST["add_title"],
            network=request.POST["add_network"],
            release_date=request.POST["release_date"],
            desc=request.POST["add_desc"],
        )
    return redirect(f"/shows/{show.id}")


def show_results(request, show_id):
    new_show = Show.objects.get(id=show_id)
    context = {"show": new_show}
    return render(request, "show_details.html", context)


def show_update(request):
    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("edit_show")
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST["title"]
        show.network = request.POST["network"]
        show.release_date = request.POST["release_date"]
        show.desc = request.POST["desc"]
        show.save()
    return redirect(f"/shows/{show.id}")


def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect("/")
