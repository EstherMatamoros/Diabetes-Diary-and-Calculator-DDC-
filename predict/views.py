from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults 

def predict(request) : 
    return render(request, 'predict.html')


def predict_chances(request):
    if request.POST.get('action') == 'post':
        # Receive data from client
        glucose_sp = float(request.POST.get('glucose_sp'))
        glucose = float(request.POST.get('glucose'))
        namemeals = request.POST.get('namemeals')
        meals = float(request.POST.get('meals'))
        exeint = float(request.POST.get('exeint'))

        # Unpickle model

        model = pd.read_pickle(r"F:\Presentacion 1 Marzo\controlDiabetes (1)\controlDiabetes\knearestneighbor.pickle")

        # Make prediction

        result = model.predict([[glucose_sp, glucose, meals, exeint]])

        insulin = result[0]

        PredResults.objects.create(glucose_sp=glucose_sp, glucose=glucose, namemeals=namemeals, meals=meals,
                                   exeint=exeint, insulin=insulin)

        return JsonResponse(
            {'result': insulin, 'glucose_sp': glucose_sp, 'glucose': glucose, 'namemeals': namemeals, 'meals': meals,
             'exeint': exeint}, safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
# def predict_chances(request):
#     if request.POST.get('action') == 'post':
#
#         # Receive data from client
#
#         glucose_sp =float(request.POST.get('glucose_sp'))
#         glucose = float(request.POST.get('glucose'))
#         namemeals = float(request.POST.get('namemeals'))
#         meals =float(request.POST.get('meals'))
#         exeint = float(request.POST.get('exeint'))
#         #insulin =float(request.POST.get('insulin'))
#
#         # glucose_sp:$('#glucose_sp').val(),
#         #         #                 glucose:$('#glucose').val(),
#         #         # 				namemeals:$('#namemeals').val(),
#         #         #                 meals:$('#meals').val(),
#         #         # 				exeint:$('#exeint').val(),
#
#         # Unpickle model
#
#         model = pd.read_pickle (r"F:\Presentacion 1 Marzo\controlDiabetes (1)\controlDiabetes\knearestneighbor3.pickle")
#
#         #Make prediction
#
#         result=model.predict([[glucose_sp,insulin,meals]])
#
#         glucose = result[0]
#
#         # datetimepicker1:$('#datetimepicker1').val(),
#         #                 glucose_sp:$('#glucose_sp').val(),
#         #                 glucose:$('#glucose').val(),
#         # 				namemeals:$('#namemeals').val(),
#         #                 meals:$('#meals').val(),
#         # 				exeint:$('#exeint').val(),
#         #                 csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
#         #                 action: 'post'
#
#         PredResults.objects.create(glucose_sp=glucose_sp, glucose=glucose, namemeals=namemeals, meals=meals, exeint=exeint, insulin=insulin)
#
#         return JsonResponse ({'result':glucose,'glucose_sp':glucose_sp,'insulin':insulin, 'meals':meals},safe=False)
#
# def view_results(request):
#     # Submit prediction and show all
#     data = {"dataset": PredResults.objects.all()}
#     return render(request, "results.html", data)