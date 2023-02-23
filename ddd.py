from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import csv
import pymongo
# from gui_stuff import*
def database():
    try:
        #replace username and password into your details
        #client = pymongo.MongoClient("mongodb://firstdb:firstdb*123@ac-ivr7dce-shard-00-00.7slgycv.mongodb.net:27017,ac-ivr7dce-shard-00-01.7slgycv.mongodb.net:27017,ac-ivr7dce-shard-00-02.7slgycv.mongodb.net:27017/?ssl=true&replicaSet=atlas-kv7sdh-shard-0&authSource=admin&retryWrites=true&w=majority")
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['database2']
        #db=client.database1#creating a databbse
        #db = client.your_database_name  #other way to create database
        collection = db['collection2']
        #collection=db.collection1#create a collection from the database
        return collection  #return database so that functions from button can perform CRUD operation
    except pymongo.errors.ConfigurationError:
        #database can be accessed only if you have active internet connection, this will prompt user the error, if user is not connected to internet
        messagebox.showerror("Network Error","No internet connection")

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
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

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']
#back pain
#BACKPAIN
#i am back pain
l2=[]
for x in range(0,len(l1)):
    l2.append(0)

df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
l=[]
def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
   

    #psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    psymptoms=[]
    for i in range(len(ll)):
        psymptoms.append(ll[i].get())
    
    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        #t1.delete("1.0", END)
        #t1.insert(END, disease[a])
        l.append(disease[a])
    else:
        #t1.delete("1.0", END)
        #t1.insert(END, "Not Found")
        l.append("not found")
    return psymptoms

def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
  
    psymptoms=[]
    for i in range(len(ll)):
        psymptoms.append(ll[i].get())
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        #t2.delete("1.0", END)
        #t2.insert(END, disease[a])
        l.append(disease[a])
    else:
        #t2.delete("1.0", END)
        #t2.insert(END, "Not Found")
        l.append("not found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
   

   
    psymptoms=[]
    for i in range(len(ll)):
        psymptoms.append(ll[i].get())
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        #t3.delete("1.0", END)
        #t3.insert(END, disease[a])
        l.append(disease[a])
    else:
        #t3.delete("1.0", END)
        #t3.insert(END, "Not Found")
        l.append("not found")
def all():
    document=dict()
    document['name']=NameEn.get()
    
    age=value_inside.get()
    document['age_group']=age
    
    dis=''
    lll=DecisionTree()
    randomforest()
    NaiveBayes()
    document['symptomss']=lll
    if(len(l)==len(set(l))):
       
       t1.delete("1.0",END)
       t1.insert(END,l[2])
       dis=l[2]
    elif(len(set(l))==1):
        
       t1.delete("1.0",END)
       t1.insert(END,l[0])
       dis=l[0]
    else:
        s=set(l)
        for ele in s:
            if (l.count(ele)==2):
                
                t1.delete("1.0",END)
                t1.insert(END,ele)
                dis=ele
    with open('disdrug.csv') as f:
        r=csv.reader(f)
        for rr in r:
            if(rr[0]==dis):
                if(age=='kids'):
                    drug=rr[1]
                    t2.insert(END,rr[1])
                elif(age=='teens'):
                    drug=rr[2]
                    t2.insert(END,rr[2])
                elif(age=='adults'):
                    drug=rr[3]
                    t2.insert(END,rr[3])
                break
    document['disease']=dis
    document['drug']=drug
    collect=database()
    collect.insert_one(document)
    #return dis

# gui_stuff

root = Tk()
#root.configure()

root.geometry('700x800')
root.title('disease-drug prediction')
img=PhotoImage(file=r'C:\Users\saphalya peta\OneDrive\Desktop\SEM 5 CBIT Workspace\Panace\Disease-prediction-using-Machine-Learning-master\img1.png')
photo=img.subsample(3,3)
la=Label(master=root,text='Disease predictor and drug recommendation system',font=("Arial",20),image=img)
la.place(x=0,y=0)
# entry variables

Name = StringVar()




# labels
NameLb = Label(root, text="Name of the Patient", fg="black",font=("Arial",15))
NameLb.grid(row=6, column=0, pady=15, sticky=W)


S1Lb = Label(root, text="Symptoms", fg="black",font=("Arial",15))
S1Lb.grid(row=7, column=0, pady=10, sticky=W)
cat = Label(root, text="age cateory ",fg="black",font=("Arial",15))
cat.grid(row=14, column=0, pady=10,sticky=W)
options_list = ["kids", "teens", "adults"]

value_inside = StringVar(root)
# Set the default value of the variable
value_inside.set("Select an Option")
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
question_menu = OptionMenu(root, value_inside, *options_list)
question_menu.grid(row=14,column=1,pady=10)
res = Label(root, text="Final Predicted Disease",fg="black",font=("Arial",15))
res.grid(row=15, column=0, pady=10,sticky=W)
dru = Label(root, text="FDA stadardized Drug", fg="black",font=("Arial",15))
dru.grid(row=17, column=0, pady=10,sticky=W)


ll=[]
li=[]
c=0
def addd():
    global root,li,c
    for _ in range(1):
        ll.append('a')
        ll[-1]=StringVar()
        ll[-1].set(None)
        c=c+1
        li.append(OptionMenu(root,ll[c],*OPTIONS))
        li[-1].grid(row=7+c,column=1)
def ddel():
    li[-1].destroy()
    li.remove(li[-1])
    c=c-1
    
# entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)
ll.append('a')
ll[-1]=StringVar()
ll[-1].set(None)
S1En = OptionMenu(root, ll[0],*OPTIONS)
S1En.grid(row=7, column=1)
bb=Button(root,text="add symptoms",command=addd,bg='green',fg='yellow')
bb.grid(row=9,column=3)
bbb=Button(root,text="del symptoms",command=ddel,bg='green',fg='yellow')
bbb.grid(row=10,column=3)

dst = Button(root, text="submit", command=all,bg="green",fg="yellow")
dst.grid(row=8, column=3)

'''rnf = Button(root, text="Randomforest", command=randomforest,bg="green",fg="yellow")
rnf.grid(row=9, column=3,padx=10)

lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="green",fg="yellow")
lr.grid(row=10, column=3,padx=10)'''

#textfileds
t1 = Text(root, height=1, width=40,bg="white",fg="black")
t1.grid(row=15, column=1, padx=10)
t2 = Text(root, height=1, width=40,bg="white",fg="black")
t2.grid(row=17, column=1, padx=10)
'''dis = t1.get(1.0, "end-1c")
lbl = Label(root, text = "")
lbl.grid(row=17, column=0, pady=10,sticky=W)
lbl.config(text = "Provided Input: "+dis)'''
'''t2 = Text(root, height=1, width=40,bg="orange",fg="black")
t2.grid(row=17, column=1 , padx=10)

t3 = Text(root, height=1, width=40,bg="orange",fg="black")
t3.grid(row=19, column=1 , padx=10)'''

root.mainloop()
