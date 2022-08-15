#Important Modules
from dis import dis
import json
from flask import jsonify
from flask import Flask,render_template, url_for ,flash , redirect
#from forms import RegistrationForm, LoginForm
from sklearn.externals import joblib
from flask import request
import numpy as np



import os
from flask import send_from_directory

import sys
from typing import Any, Callable, List, Mapping, Optional, Sequence, Type, TypeVar, Union, overload



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
    if int(symptomlist[1])<= 100: # glucose
        suggest1="1. You have an ideal blood sugar level, please keep maintaining a limited sugar intake to stay healthy. Check this out to know natural ways of reducing blood sugar level"
        link1="https://www.mindbodygreen.com/articles/how-to-lower-blood-sugar"
    else:
        suggest1="1. You have high blood sugar level, please visit a doctor and reduce you sugar intake immediately!!"
        link1="https://www.healthline.com/health/diabetes/how-to-lower-blood-sugar-quickly-emergency#_noHeaderPrefixedContent"
    if int(symptomlist[2])<90: # blood pressure
        suggest2="2. You have low Blood Pressure, please drink plenty of water and limit alcohol intake. Also, add some salt to your diet. "
        link2="https://www.webmd.com/heart/understanding-low-blood-pressure-basics"
    elif int(symptomlist[2])>=90 and  int(symptomlist[2])<=120: 
        suggest2="2. Your BP is in the normal range, please maintain a balanced diet and keep exercising to stay fit. Check this out to know how you can maintain the same"
        link2="https://www.everydayhealth.com/hypertension/treating/if-your-reading-is-normal.aspx"
    elif int(symptomlist[2])>120 and  int(symptomlist[2])<=129:
        suggest2="2. You have an elevated Blood Pressure level and are likely to develop high BP unless steps are taken to control the condition. Please reduce sodium in your diet, exercise regularly, cut back on caffeine, quit smoking and eat a healthy diet. Also, lose extra pounds and watch your waistline. BP often increases as weight increases. Know more about it here "
        link2="https://www.mayoclinic.org/diseases-conditions/prehypertension/symptoms-causes/syc-20376703"
    elif int(symptomlist[2])>=130 and  int(symptomlist[2])<=139:
        suggest2="2. Your BP is in Hypertension Stage 1 also called as pre-hypertension stage, please consult the doctor immediately. Doctors are likely to prescribe lifestyle changes and may consider adding blood pressure medication based on your risk. Please reduce sodium in your diet, exercise regularly, cut back on caffeine, quit smoking and eat a healthy diet. Know more about it here "
        link2="https://www.webmd.com/hypertension-high-blood-pressure/guide/prehypertension-are-you-at-risk"
    else: 
        suggest2="2. Your BP is in Hypertension Stage 2, please consult the doctor immediately. At this stage of high blood pressure, doctors are likely to prescribe a combination of blood pressure medications and lifestyle changes. Please reduce sodium in your diet, exercise regularly, cut back on caffeine, quit smoking and eat a healthy diet. Also, check this out "
        link2="https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/diagnosis-treatment/drc-20373417"
    if float(symptomlist[4])>2 and float(symptomlist[4])<=10: # insulin
        suggest3="3. You have an optimum insulin level, keep maintaining your intake of fresh fruits and vegetables, whole grains and lean proteins."
        link3="https://www.medicalnewstoday.com/articles/320983"
    else: 
        suggest3="3. You have high insulin level, reduce intake of sugar and grains. Refined grains and fructose-sweetened drinks should be eliminated from the diet and healthy fats and proteins should be included."
        link3="https://www.medicalnewstoday.com/articles/320983"
    if int(symptomlist[5])<18.5: # BMI
        suggest4="4. You are in the underweight range. Try to incorporate healthy meals in your diet. "
        link4=" https://www.diabetes.org.uk/guide-to-diabetes/enjoy-food/eating-with-diabetes/whats-your-healthy-weight/tips-to-gain-weight"
    elif int(symptomlist[5])>=18.5 and  int(symptomlist[5])<=24.9: 
        suggest4="4. You are in the healthy weight range. Continue having a balanced meal along with regular exercise. "
        link4="https://www.nia.nih.gov/health/maintaining-healthy-weight"
    elif int(symptomlist[5])>=25 and  int(symptomlist[5])<=29.9:
        suggest4="4. You are in the overweight range. Cutting down on processed food should be given priority."
        link4="https://www.niddk.nih.gov/health-information/weight-management/adult-overweight-obesity/treatment"
    elif int(symptomlist[5])>=30 and  int(symptomlist[5])<=39.9:
        suggest4="4. You are in the obese range. Reduction of body weight is the need of the hour."
        link4="https://www.doconline.com/what-we-treat/obesity-weight-loss"
    else: 
        suggest4="4. You fall under the category of Class III obesity and you might start experiencing obesity-related health conditions. A combination of dieting, behavior modification therapy and exercise should help."
        link4="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3131844/"
    suggest5=   "5. Long-term complications of diabetes develop gradually. The longer you have diabetes — and the less controlled your blood sugar — the higher the risk of complications like nerve damage, cardiovascular disease, kidney damage, hearing impairment, etc. "
    link5="https://www.gundersenhealth.org/health-wellness/be-well/6-natural-ways-to-prevent-diabetes-before-it-starts/"
   
    return suggest1,suggest2,suggest3,suggest4,suggest5,link1,link2,link3,link4,link5
    

def heart(symptomlist):
    print(symptomlist)
    if int(symptomlist[0])< 65: # age
        suggest1="1. You are not necessarily at a risk of developing a heart disease provided you fulfill the other health parameters. Follow the link to know how you can prevent heart diseases as you age."
        link1="https://www.webmd.com/healthy-aging/heart-over-50/heart-health-aging "
    else: 
        suggest1="1. You are much more likely to develop a heart disease but there are things you can do to delay, lower, or possibly avoid or reverse your risk."
        link1="https://www.nia.nih.gov/health/heart-health-and-aging "
    
    if int(symptomlist[2])==0: # chestpaintype
        suggest2="2. You have asymptomatic myocardial ischemia. It occurs when blood flow to your heart is reduced, preventing the heart muscle from receiving enough oxygen. Check this to know more"
        link2=" https://www.mayoclinic.org/diseases-conditions/myocardial-ischemia/symptoms-causes/syc-20375417"
    elif int(symptomlist[2])==1: 
        suggest2="2. You have atypical angina. Know more about it here"
        link2=" https://www.buoyhealth.com/learn/atypical-chest-pain"
    elif int(symptomlist[2])==2:
        suggest2="2. You have non-anginal pain. It is not a matter of concern but you could opt for healthy substitutes."
        link2=" https://gi.org/topics/non-cardiac-chest-pain/"
    elif int(symptomlist[2])==3:
        suggest2="2. You have typical angina. Know more about it here"
        link2=" https://my.clevelandclinic.org/health/diseases/21847-stable-angina"
   
    if int(symptomlist[3])<120: # resting bp
        suggest3="3. You have a perfectly healthy composition of fats, hence a normal BP level. Read this to know how you can maintain it"
        link3="https://medlineplus.gov/howtopreventhighbloodpressure.html "
    elif int(symptomlist[3])>=120 and  int(symptomlist[3])<=129: 
        suggest3="3. You have a elevated blood pressure level. Regular exercise, healthy diet, limited sodium, stress management might help."
        link3="https://www.healthline.com/health/high-blood-pressure-hypertension/lower-it-fast "
    elif int(symptomlist[3])>=130 and  int(symptomlist[3])<=139:
        suggest3="3. You have high blood pressure (Hypertension Stage 1). Read about it here "
        link3="https://www.webmd.com/hypertension-high-blood-pressure/how-to-lower-blood-pressure "
    elif int(symptomlist[3])>=140 and  int(symptomlist[3])<=180:
        suggest3="3. You have high blood pressure (Hypertension Stage 2). Read about it here"
        link3=" https://www.webmd.com/hypertension-high-blood-pressure/how-to-lower-blood-pressure"
    else: 
        suggest3="3. You have Hypertensive crisis. Consult a doctor immediately. Read about it here"
        link3="https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/expert-answers/hypertensive-crisis/faq-20058491 "
    
    if int(symptomlist[0])>=20: #cholestrol
    
        if int(symptomlist[4])>=125 and int(symptomlist[4])<=200:
            suggest4="4. You have a healthy cholestrol level."
            link4="https://www.nm.org/healthbeat/healthy-tips/down-with-the-bad-up-with-the-good "
        else:
            suggest4="4. You have an unhealthy cholestrol evel."     
            link4="https://www.medicalnewstoday.com/articles/317332 "
    else:
    
        if int(symptomlist[4])<=170:
            suggest4="4. You have a healthy cholestrol level."
            link4=" https://my.clevelandclinic.org/health/articles/11920-cholesterol-numbers-what-do-they-mean"
        else:
            suggest4="4. You have an unhealthy cholestrol level."
            link4=" https://www.medicalnewstoday.com/articles/317332"
    suggest5="Sometimes, heart failure leads to other conditions, such as kidney or liver damage or heart-valve problems. If your doctor thinks you may have heart failure, they may run blood and other tests to check what's going on with your heart and to see what other conditions you might have. Read about how to keep your heart healthy"
    link5="https://health.gov/myhealthfinder/health-conditions/heart-health/keep-your-heart-healthy "
    
    return suggest1,suggest2,suggest3,suggest4,suggest5,link1,link2,link3,link4,link5

def cancer(symptomlist):
    print(symptomlist)
    
    suggest1="1. Avoid becoming overweight. Obesity raises the risk of breast cancer after menopause, the time of life when breast cancer most often occurs. Avoid gaining weight over time, and try to maintain a body-mass index of 25 or less (calculators can be found online)."  
    suggest2="2. Eat healthy to avoid tipping the scale. Embrace a diet high in vegetables and fruit and low in sugared drinks, refined carbohydrates and fatty foods. Eat lean protein such as fish or chicken breast and eat red meat in moderation, if at all. Eat whole grains. Choose vegetable oils over animal fats."
    suggest3="3. Keep physically active. Research suggests that increased physical activity, even when begun later in life, reduces overall breast-cancer risk by at least 10 percent. All it takes is moderate exercise like a 30-minute walk five days a week to get this protective effect. "
    suggest4="4. Drink little or no alcohol. Alcohol use is associated with an increased risk of breast cancer. Women should limit intake to no more than one drink per day, regardless of the type of alcohol."
    suggest5="5. Early identification of breast cancer increases the chances of survival. Know more about it here"
    link1="https://www.cancer.org/latest-news/how-your-weight-affects-your-risk-of-breast-cancer.html"
    link2="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5982158/"
    link3="https://www.frontiersin.org/articles/10.3389/fnut.2020.557997/full"
    link4="https://www.mdanderson.org/publications/focused-on-health/alcohol-breast-cancer-risk-what-to-know.h30Z1591413.html"
    link5="https://www.cdc.gov/cancer/dcpc/prevention/index.htm"
    return suggest1,suggest2,suggest3,suggest4,suggest5,link1,link2,link3,link4,link5
    
def kidney(symptomlist):
    print(symptomlist)
    if float(symptomlist[4])<= 100: # glucose
        suggest1="1. You have an ideal blood glucose level, please keep maintaining a limited sugar intake to stay healthy."
        link1=" https://www.kidney.org/atoz/content/managing-blood-sugar-for-kidney-health"
    else:
        suggest1="1. You have high blood glucose level, please reduce you sugar intake immediately!!"
        link1="https://www.kidney.org/atoz/content/managing-blood-sugar-for-kidney-health "
    
    if int(symptomlist[1])<90: # blood pressure
        suggest2="2. You have low Blood Pressure, please drink plenty of water and limit alcohol intake. Also, add some salt to your diet. "
        link2=" https://www.niddk.nih.gov/health-information/kidney-disease/high-blood-pressure"
    elif int(symptomlist[1])>=90 and  int(symptomlist[2])<=120: 
        suggest2="2. Your BP is in the normal range, please maintain a balanced diet and keep exercising to stay fit."
        link2=" https://www.niddk.nih.gov/health-information/kidney-disease/chronic-kidney-disease-ckd/prevention"
    elif int(symptomlist[1])>120 and  int(symptomlist[2])<=129:
        suggest2="2. You have an elevated Blood Pressure level and are likely to develop high BP unless steps are taken to control the condition. Please reduce sodium in your diet, exercise regularly, cut back on caffeine, quit smoking and eat a healthy diet. Also, lose extra pounds and watch your waistline. BP often increases as weight increases. "
        link2=" https://www.niddk.nih.gov/health-information/kidney-disease/high-blood-pressure"
    elif int(symptomlist[1])>=130 and  int(symptomlist[2])<=139:
        suggest2="2. Your BP is in Hypertension Stage 1, please consult the doctor immediately. Doctors are likely to prescribe lifestyle changes and may consider adding blood pressure medication based on your risk. Please reduce sodium in your diet, exercise regularly, cut back on caffeine, quit smoking and eat a healthy diet. "
        link2="https://www.heart.org/en/health-topics/high-blood-pressure/health-threats-from-high-blood-pressure/how-high-blood-pressure-can-lead-to-kidney-damage-or-failure "
    else: 
        suggest2="2. Your BP is in Hypertension Stage 2, please consult the doctor immediately. At this stage of high blood pressure, doctors are likely to prescribe a combination of blood pressure medications and lifestyle changes. Please reduce sodium in your diet, exercise regularly, cut back on caffeine, quit smoking and eat a healthy diet. "
        link2=" https://www.heart.org/en/health-topics/high-blood-pressure/health-threats-from-high-blood-pressure/how-high-blood-pressure-can-lead-to-kidney-damage-or-failure"
    
    if float(symptomlist[2])>=3.3 and  float(symptomlist[2])<=5.5: #albumin
        suggest3=" You have optimum Albumin levels in your blood. Please drink more water and exercise regularly to stay healthy."
        link3="https://www.healthline.com/health/kidney-health "
    elif float(symptomlist[2])<=3.3:
        suggest3="3. You have Lower-than-normal albumin levels in your blood (hypoalbuminemia) which may indicate: Infection. Inflammation due to sepsis, surgery or another condition."
        link3=" https://www.kidney.org/content/kidney-failure-risk-factor-serum-albumin"
    else:
        suggest3="3. You have Higher than normal albumin levels in your blood (hyperalbuminemia) which may indicate: dehydration and severe diarrhea." 
        link3="https://www.kidney.org/content/kidney-failure-risk-factor-serum-albumin "

    
    if float(symptomlist[0])<60 : #age
        suggest4="4. You are not likely to have a kidney disease but watch out for early symptoms "
        link4=" https://www.kidney.org/atoz/content/sixstepshealthprimer"
    elif float(symptomlist[0])>=60 and  int(symptomlist[0]) < 75:
        suggest4="4. Disease progression occurs slowly over a period of time and as a person ages. Early precautions can help you from not developing the disease."
        link4="https://www.betterhealth.vic.gov.au/health/conditionsandtreatments/kidneys-age-related-problems "
    else:
        suggest4="4. More than 50 percent of seniors over the age of 75 are believed to have kidney disease. Please consult a doctor and get a checkup done. "
        link4="https://medlineplus.gov/ency/article/007466.htm "
    
    suggest5="5. Diabetes is the leading cause of chronic kidney disease and kidney failure. Please take the diabetes test to check the probability. Diabetes should be screened regularly for kidney disease. "
    link5="https://www.cdc.gov/diabetes/managing/eat-well/what-to-eat.html "



    return suggest1,suggest2,suggest3,suggest4,suggest5,link1,link2,link3,link4,link5


def liver(symptomlist):
    print(symptomlist)
    if float(symptomlist[1])<=1.2 and  float(symptomlist[1])>0.1 : # total bilirubin
        suggest1="1. Your Total Bilirubin levels are in optimum range. Please drink more water to maintain the liver health."
        link1="https://labpedia.net/bilirubin-part-1-total-bilirubin-direct-and-indirect-bilirubin-classification-of-jaundice-neonatal-jaundice/ "
    else:
        suggest1="1. You have elevated bilirubin levels, you should take steps to lower them and promote liver health by making several changes to your diet. These changes include drinking more water, cutting back on your alcohol consumption, and eating more fruits and vegetables and fewer processed foods."
        link1=" https://www.healthline.com/health/high-bilirubin"
    if float(symptomlist[2])<=0.4 : # direct bilirubin
        suggest2="2. Your Direct Bilirubin levels are normal. Maintain a healthy diet and drink more water to stay healthy. "
        link2="https://www.webmd.com/hepatitis/ss/slideshow-keep-liver-healthy "
    else:
        suggest2="2. You have high direct bilirubin levels. Bilirubin levels may increase with stress, strain, dehydration, fasting, infection or exposure to cold. Please be careful and add Vitamin D to the diet."
        link2=" https://www.insider.com/guides/health/treatments/how-to-lower-bilirubin"
    if float(symptomlist[3])<=240 and  float(symptomlist[3])>47 :#alkaline phosphatose
        suggest3="3. Your alkaline phosphatase (ALP) levels are normal. Keep exercising regularly to maintain optimum ALP levels."
        link3=" https://medlineplus.gov/lab-tests/alkaline-phosphatase/"
    else:
        suggest3="3. You have High alkaline phosphatase (ALP) levels. In a nutshell, you should take targeted liver-protective herbs and nutrients while adapting your diet and reducing alcohol intake. Add Omega-3 Fatty Acids to your diet and cut down on caffeine. Get more sun exposure or take vitamin D supplements."
        link3="https://labs.selfdecode.com/blog/alkaline-phosphatase/ "
    if float(symptomlist[6])<=8.3 and  float(symptomlist[6])>=6.0 : #total proteins
        suggest4="4. Your Total Proteins are in normal range. Consume foods high in protein which include meat, fish, poultry, eggs, legumes, and soy products like tofu or tempeh."
        link4="https://www.healthline.com/health/total-protein "
    elif float(symptomlist[6])<6.0:
        suggest4="4. You have low protein levels, which may suggest liver disease, malnutrition, malabsorption disorders or congestive heart failure. Consume foods high in protein which include meat, fish, poultry, eggs, legumes, and soy products like tofu or tempeh."
        link4=" https://medlineplus.gov/ency/article/002441.htm"
    else:
        suggest4="4. You have high protein levels, which may indicate liver disease, chronic kidney disease, cancers such as multiple myeloma. Please consult doctor! "
        link4=" https://medlineplus.gov/ency/article/002441.htm"
    suggest5="5. Read about the ways to a healthy liver"
    link5="https://liverfoundation.org/resource-center/blog/13-ways-to-a-healthy-liver/ "

    return suggest1,suggest2,suggest3,suggest4,suggest5,link1,link2,link3,link4,link5

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
            link=suggest[5:10]
        elif(len(to_predict_list)==8):#Daiabtes
            result = ValuePredictor(to_predict_list,8)
            dis="Diabetes"
            suggest=diabetes(to_predict_list)
            link=suggest[5:10]
        elif(len(to_predict_list)==12):
            result = ValuePredictor(to_predict_list,12)
            dis="Kidney Disease"
            suggest=kidney(to_predict_list)
            link=suggest[5:10]
        elif(len(to_predict_list)==11):
            result = ValuePredictor(to_predict_list,11) 
            dis="Heart Disease"
            suggest=heart(to_predict_list)
            link=suggest[5:10]
        elif(len(to_predict_list)==10):
            result = ValuePredictor(to_predict_list,10)
            dis="Liver Disease"
            suggest=liver(to_predict_list)
            link=suggest[5:10] 
    """if(int(result)==1):
        prediction=1
    else:
        prediction=0 """
    return(render_template("result.html", pred=result, dis=dis,suggest=suggest,link=link))

@app.route("/generalpredict", methods = ['POST', 'GET'])
def generalPredictPage():
    try:
              
        if request.method == 'POST':
            model = joblib.load('models/trained_model')
            """input_no=request.get_json()
            print(input_no)
            print(type(input_no))
            inputno=json.loads(input_no)       """
            input_sym=request.get_json()
            print(input_sym)
            print(type(input_sym))
            psymptoms=json.loads(input_sym)
            print(type(psymptoms))
                 #psymptoms = ['cramps','cough','back_pain','mild_fever','congestion']
            print(psymptoms)
            inputno=len(psymptoms)
            print(inputno)
            if (inputno == 0 ) :
                 return jsonify({'predicteddisease': "none",'confidencescore': 0 })
                #
            else :
                

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
                 return jsonify({'predicteddisease': predicted_disease ,'confidencescore':confidencescore})
                   
    except:
        message = "Please enter valid Data"
        return render_template("home.html", message = message)

@app.route("/resultlink", methods = ['POST', 'GET'])
def resultlinkpage():
    try:
        print("this is result link func")      
        if request.method == 'POST':
            disease=dis
            input_sym=request.get_json()
            print(input_sym)

            return jsonify({'predicteddisease': disease})
                   
    except:
        message = "Please enter valid Data"
        return render_template("home.html", message = message)

if __name__ == "__main__":
    app.run(debug=True)