#Important Modules
from flask import Flask,render_template, url_for ,flash , redirect
#from forms import RegistrationForm, LoginForm
from sklearn.externals import joblib
from flask import request
import numpy as np



import os
from flask import send_from_directory

import sys
from typing import Any, Callable, List, Mapping, Optional, Sequence, Type, TypeVar, Union, overload

from django.db.models import Manager, QuerySet
from django.db.models.base import Model
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.http.response import HttpResponsePermanentRedirect as HttpResponsePermanentRedirect
from django.http.response import HttpResponseRedirect as HttpResponseRedirect
from json import JSONEncoder

class _Alias:
    # Class for defining generic aliases for library types.
    def __getitem__(self, typeargs: Any) -> Any: ...

Dict = _Alias()

def render(
    request: HttpRequest,
    template_name: Union[str, Sequence[str]],
    context: Optional[Mapping[str, Any]] = ...,
    content_type: Optional[str] = ...,
    status: Optional[int] = ...,
    using: Optional[str] = ...,
) -> HttpResponse: ...

class JsonResponse(HttpResponse):
    def __init__(
        self,
        data: Any,
        encoder: Type[JSONEncoder] = ...,
        safe: bool = ...,
        json_dumps_params: Optional[Dict[str, Any]] = ...,
        **kwargs: Any
    ) -> None: ...



symptomslist=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes',
                'back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
                'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
                'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
                'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
                'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
                'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
                'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
                'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
                'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
                'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
                'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
                'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
                'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
                'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
                'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
                'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
                'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
                'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
                'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
                'yellow_crust_ooze']
alphabaticsymptomslist = sorted(symptomslist)

#from this import SQLAlchemy
app=Flask(__name__,template_folder='template')

@app.route("/")

@app.route("/home")
def home():
    return render_template("home.html")
 
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cancer")
def cancer():
    return render_template("cancer.html")


@app.route("/diabetes")
def diabetes():
    #if form.validate_on_submit():
    return render_template("diabetes.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")


@app.route("/liver")
def liver():
    #if form.validate_on_submit():
    return render_template("liver.html")

@app.route("/kidney")
def kidney():
    #if form.validate_on_submit():
    return render_template("kidney.html")

@app.route("/general")
def general():
    return render_template("general.html",list2=alphabaticsymptomslist)

def diabetes(symptomlist):
    print(symptomlist)
    suggest1="Please use less sugar"
    suggest2="Exercise Regularly"
    suggest3="Eat healthy vegetables"
    suggest4="you have high bp"
    return suggest1,suggest2,suggest3,suggest4

def heart(symtomlist):
    print(symtomlist)
    suggest1="Eat healthy vegetables"
    suggest2="Exercise Regularly"
    return suggest1,suggest2

def cancer(symtomlist):
    print(symtomlist)
    suggest1="Eat healthy vegetables"
    suggest2="Exercise Regularly"
    return suggest1,suggest2

def kidney(symtomlist):
    print(symtomlist)
    suggest1="Eat healthy vegetables"
    suggest2="Exercise Regularly"
    return suggest1,suggest2

def liver(symtomlist):
    print(symtomlist)
    suggest1="Eat healthy vegetables"
    suggest2="Exercise Regularly"
    return suggest1,suggest2

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==8):#Diabetes
        loaded_model = joblib.load("models/model1")
        result = loaded_model.predict(to_predict)
    elif(size==30):#Cancer
        loaded_model = joblib.load("models/model")
        result = loaded_model.predict(to_predict)
    elif(size==12):#Kidney
        loaded_model = joblib.load("models/model3")
        result = loaded_model.predict(to_predict)
    elif(size==10):
        loaded_model = joblib.load("models/model4")
        result = loaded_model.predict(to_predict)
    elif(size==11):#Heart
        loaded_model = joblib.load("models/model2")
        result =loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ["POST"])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==30):#Cancer
            result = ValuePredictor(to_predict_list,30)
            dis="Breast Cancer"
            suggest=cancer(to_predict_list)
        elif(len(to_predict_list)==8):#Daiabtes
            result = ValuePredictor(to_predict_list,8)
            dis="Diabetes"
            suggest=diabetes(to_predict_list)
        elif(len(to_predict_list)==12):
            result = ValuePredictor(to_predict_list,12)
            dis="Kidney Disease"
            suggest=kidney(to_predict_list)
        elif(len(to_predict_list)==11):
            result = ValuePredictor(to_predict_list,11) 
            dis="Heart Disease"
            suggest=heart(to_predict_list)
        elif(len(to_predict_list)==10):
            result = ValuePredictor(to_predict_list,10)
            dis="Liver Disease"
            suggest=liver(to_predict_list)
    """if(int(result)==1):
        prediction=1
    else:
        prediction=0 """
    return(render_template("result.html", pred=result, dis=dis,suggest=suggest))

@app.route("/generalpredict", methods = ['POST', 'GET'])
def generalPredictPage():
    try:
              
        if request.method == 'POST':
            model = joblib.load('models/trained_model')
            inputno = int(request.POST["noofsym"])
            #inputno=5
            test=app.logger.warning(request.values.get('noofsym'))
            print(test)
            print(inputno)
            if (inputno == 0 ) :
                return JsonResponse({'predicteddisease': "none",'confidencescore': 0 })
                #
            else :
                
                 #psymptoms = ['cramps','cough','back_pain','mild_fever','congestion']
                 psymptoms = request.POST.getlist("symptoms[]")
       
                 print(psymptoms)

                 #main code start from here...
     
                 testingsymptoms = []
        #append zero in all coloumn fields...
                 for x in range(0, len(symptomslist)):
                     testingsymptoms.append(0)


        #update 1 where symptoms gets matched...
                 for k in range(0, len(symptomslist)):

                     for z in psymptoms:
                         if (z == symptomslist[k]):
                             testingsymptoms[k] = 1


                 inputtest = [testingsymptoms]

                 print(inputtest)
                 predicted = model.predict(inputtest)
                 print("predicted disease is : ")
                 print(predicted)
                 y_pred_2 = model.predict_proba(inputtest)
                 confidencescore=y_pred_2.max() * 100
                 print(" confidence score of : = {0} ".format(confidencescore))
                 confidencescore = format(confidencescore, '.0f')
                 predicted_disease = predicted[0]
                 return JsonResponse({'predicteddisease': predicted_disease ,'confidencescore':confidencescore})
        #            
    except:
        message = "Please enter valid Data"
        return render_template("home.html", message = message)

    



if __name__ == "__main__":
    app.run(debug=True)
