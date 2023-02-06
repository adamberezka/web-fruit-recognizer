from django.shortcuts import render, get_object_or_404

from prediction.model import FruitModel
from recognition.forms import UploadImageForm
from recognition.models import UploadedImage

fruits_model = FruitModel()


def recognitionHome(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance
            prediction = fruits_model.predict("./media/" + str(img_object.image))
            form.instance.prediction = prediction.upper()
            form.save()

            return render(request, 'recognitionResult.html', {'form': form, 'img_obj': img_object})
    else:
        form = UploadImageForm()

    return render(request, 'recognitionUpload.html', {'form': form})


def recognitionDetail(request, id):
    prediction = get_object_or_404(UploadedImage, id=id)
    return render(request, 'recognitionResult.html', {'img_obj': prediction})
