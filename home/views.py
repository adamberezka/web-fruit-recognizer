from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import F

from home.forms import SearchForm
from recognition.models import UploadedImage

NUM_OF_RECORDS = 10


def home(request):
    form = SearchForm(request.GET)

    predictions = UploadedImage.objects.all().order_by('-id')

    if form['isPredictionRight'].value() is not None and form['isPredictionRight'].value():
        predictions = predictions.filter(fruit=F('prediction'))

    if form['prediction'].value() is not None and form['prediction'].value() != 'NONE' and form['prediction'].value() != 'None':
        predictions = predictions.filter(prediction=form['prediction'].value())

    if form['actual'].value() is not None and form['actual'].value() != 'NONE' and form['actual'].value() != 'None':
        predictions = predictions.filter(fruit=form['actual'].value())

    page_number = request.GET.get("page")
    if page_number is None:
        page_number = 1

    paginator = Paginator(predictions, NUM_OF_RECORDS)
    page = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page, 'form': form})
