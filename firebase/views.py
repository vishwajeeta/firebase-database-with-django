from django.shortcuts import render
import pyrebase
config={
  "apiKey": "AIzaSyBJkCHJrRZkFY5EPAWWiSJwxXAch_QC8Qw",
  "authDomain": "civil-rarity-334615.firebaseapp.com",
  "databaseURL":"https://civil-rarity-334615-default-rtdb.firebaseio.com/",
  "projectId": "civil-rarity-334615",
  "storageBucket": "civil-rarity-334615.appspot.com",
  "messagingSenderId": "236062693460",
  "appId": "1:236062693460:web:cb660ef804e7329ea2f5c1",
  "measurementId": "G-CL483BC6X3"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def home(request):
    Name = database.child('name').get().val()
    Framework = database.child('framework').get().val()
    context={
        'name':Name,
        'framework':Framework
    }
    return render(request,"Home.html",context)
