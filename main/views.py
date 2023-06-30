from datetime import date

from django.shortcuts import render
from .forms import SubscriberForm


def main_page(request):
    form = SubscriberForm(request.POST or None)
    current_date = date.today()

    context = {
        'form': form,
        'current_date': current_date
    }

    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        new_form = form.save()

    return render(request, 'main/index.html', context)
