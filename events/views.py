from django.shortcuts import render
import sqlite3

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def read():
    """This is a function to read the jason data with sqlite3 """
    db = sqlite3.connect("reviews.json")
    mycursor = db.cursor()
    #selecting everything with ascending order by reviewtext
    mycursor.execute("SELECT reviewText, reviewCreatedOn, rating FROM db ") 
    print(mycursor)
    for x in mycursor.fetchall(): # looping through every information
      print(x)
    mycursor.close() 
    db.close() 

# # This is a test if python reads the json file 
# file = open("reviews.json", "r")
# for i in file:
#     print(i)

# file.close()


