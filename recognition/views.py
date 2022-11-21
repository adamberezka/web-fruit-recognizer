from django.shortcuts import render

from prediction.model import FruitModel
from recognition.forms import UploadImageForm


fruits_model = FruitModel()


def recognitionHome(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance
            prediction = fruits_model.predict("./media/" + str(img_object.image))

            return render(request, 'recognitionResult.html', {'form': form, 'img_obj': img_object, 'prediction': prediction})
    else:
        form = UploadImageForm()

    return render(request, 'recognitionUpload.html', {'form': form})
