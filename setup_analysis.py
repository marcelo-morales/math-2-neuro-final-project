import json
import csv
import random
import setup_analysis
import numpy as np # matrices, arrays, operators,
import matplotlib.pyplot as plt # basic visualization took
import seaborn as sns # visualization
import pandas as pd # ML, data science
import collections
from operator import attrgetter
from itertools import groupby

def getFreqsFromList(myList):
    data = {}
    # iterating over the list
    for item in myList:
        # checking the element in dictionary
        if item in data:
            # incrementing the counr
            data[item] += 1
        else:
            # initializing the count
            data[item] = 1
    return data

def graphPositiveFreqDoctor(covidPositiveDict):
    plt.bar(covidPositiveDict.keys(), covidPositiveDict.values(), color ='maroon',
                width = 0.4)
        
    plt.xlabel("Response")
    plt.ylabel("Frequency")
    plt.title("Covid frequency")
    plt.show()
    
def graphAnxietyDoctor(anxietyDict):

    fig1, ax1 = plt.subplots()
    ax1.pie(anxietyDict.values(), labels=anxietyDict.keys(), autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    
def graphLocationWithHospProtect(locationDict, hospProtectDict):
    # Numbers of pairs of bars you want
    N = len(locationDict)

    # Data on X-axis

    # Specify the values of blue bars (height)
    blue_bar = locationDict.values()
    # Specify the values of orange bars (height)
    orange_bar = hospProtectDict.values()

    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10,5))

    # Width of a bar 
    width = 0.3       

    # Plotting
    plt.bar(ind, blue_bar , width, label='Blue bar label')
    plt.bar(ind + width, orange_bar, width, label='Orange bar label')

    plt.xlabel('Here goes x-axis label')
    plt.ylabel('Here goes y-axis label')
    plt.title('Here goes title of the plot')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Xtick1', 'Xtick3', 'Xtick3'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')
    plt.show()
    
def graphFamilyFearWithLivStatus(famFearDict, liveStatusDict):
    # Numbers of pairs of bars you want
    N = len(famFearDict)

    # Data on X-axis

    # Specify the values of blue bars (height)
    blue_bar = famFearDict.values()
    # Specify the values of orange bars (height)
    orange_bar = liveStatusDict.values()

    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10,5))

    # Width of a bar 
    width = 0.3       

    # Plotting
    plt.bar(ind, blue_bar , width, label='Blue bar label')
    plt.bar(ind + width, orange_bar, width, label='Orange bar label')

    plt.xlabel('Here goes x-axis label')
    plt.ylabel('Here goes y-axis label')
    plt.title('Here goes title of the plot')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Xtick1', 'Xtick3', 'Xtick3'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')
    plt.show()
    
def graphMarriedWithFeelDizzy(marriedDict, dizzyDict):
    # Numbers of pairs of bars you want
    N = len(marriedDict)

    # Data on X-axis

    # Specify the values of blue bars (height)
    blue_bar = marriedDict.values()
    # Specify the values of orange bars (height)
    orange_bar = dizzyDict.values()

    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10,5))

    # Width of a bar 
    width = 0.3       

    # Plotting
    plt.bar(ind, blue_bar , width, label='Blue bar label')
    plt.bar(ind + width, orange_bar, width, label='Orange bar label')

    plt.xlabel('Here goes x-axis label')
    plt.ylabel('Here goes y-axis label')
    plt.title('Here goes title of the plot')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Xtick1', 'Xtick3', 'Xtick3'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')
    plt.show()
    
def graphAgeEducationHospProtect(ageDict, educationDict, hospProtectDict):
    # Numbers of pairs of bars you want
    N = len(ageDict)

    # Data on X-axis

    # Specify the values of blue bars (height)
    blue_bar = ageDict.values()
    # Specify the values of orange bars (height)
    orange_bar = educationDict.values()
     # Specify the values of red bars (height)
    red_bar = hospProtectDict.values()

    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10,5))

    # Width of a bar 
    width = 0.2       

    # Plotting
    plt.bar(ind, blue_bar , width, label='Blue bar label')
    plt.bar(ind + width, orange_bar, width, label='Orange bar label')
    plt.bar(ind + width + width, red_bar, width, label='Red bar label')

    plt.xlabel('Here goes x-axis label')
    plt.ylabel('Here goes y-axis label')
    plt.title('Here goes title of the plot')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Xtick1', 'Xtick3', 'Xtick3'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')
    plt.show()
    

    


def set_up_healthcare():
    
    hospitalWorkerList = []
    
    with open('data/healthcare_workers.csv', newline='', encoding="latin-1") as csvfile:
        
        reader = csv.DictReader(csvfile)

        for row in reader:
            
            ageRow = row['Please indicate your age']
            genderRow = row['Gender']
            indianTerritoryRow = row['Please indicate which Indian State/Union territory you are currently residing in ']
            educationRow = row['Educational qualification']
            maritalStatusRow = row['Marital status']
            covidPositiveRow = row['Are you currently COVID-19 positive? ']
            knowSomeoneCovidRow = row['Do you know any family member(s) or friend(s) who has/have tested positive for COVID-19?']
            anxietyDisorderRow = row['Have you ever been diagnosed with any anxiety disorder by a health worker like a psychiatrist/psychologist/counselor before?']
            adequateHospitalProtectionRow = row['The hospital has provided me with adequate personal protective equipment']
            livingStatusRow = row["During the lockdown period, indicate who you are living with:"]
            familyFearRow = row['My family expresses fear towards my work.']
            feelDizzyRow = row["I felt dizzy, lightheaded, or faint, when I read or listened to news about the coronavirus."]
            
            
            myHopsitalWorker = HealthcareWorker(age=ageRow, gender=genderRow, indianTerritory=indianTerritoryRow, education=educationRow, maritalStatus=maritalStatusRow, covidPositive=covidPositiveRow,
                                               knowSomeoneCovid=knowSomeoneCovidRow,anxietyDisorder=anxietyDisorderRow, 
                                               adequateHospitalProtection=adequateHospitalProtectionRow, familyFear=familyFearRow, livingStatus=livingStatusRow, feelDizzy=feelDizzyRow)
            
            hospitalWorkerList.append(myHopsitalWorker)
            
        
        # covidList = [HealthcareWorker.covidPositive for HealthcareWorker in hospitalWorkerList]
        covidList = map(attrgetter('covidPositive'), hospitalWorkerList)
        covidFreq = getFreqsFromList(covidList)
        graphPositiveFreqDoctor(covidFreq)
        
        anxietyList = map(attrgetter('anxietyDisorder'), hospitalWorkerList)
        anxietyFreq = getFreqsFromList(anxietyList)
        graphAnxietyDoctor(anxietyFreq)
        
        locList = map(attrgetter('indianTerritory'), hospitalWorkerList)
        locFreq = getFreqsFromList(locList)
        hospFreqList = map(attrgetter('adequateHospitalProtection'), hospitalWorkerList)
        hospFreqFreq = getFreqsFromList(hospFreqList) 
        graphLocationWithHospProtect(locFreq, hospFreqFreq)
        
        famFearList = map(attrgetter('familyFear'), hospitalWorkerList)
        famFearFreq = getFreqsFromList(famFearList)
        liveStatusList = map(attrgetter('livingStatus'), hospitalWorkerList)
        liveStatusListFreq = getFreqsFromList(liveStatusList) 
        graphFamilyFearWithLivStatus(famFearFreq, liveStatusListFreq)
        
        marriedList = map(attrgetter('maritalStatus'), hospitalWorkerList)
        marriedFreq = getFreqsFromList(marriedList)
        dizzyList = map(attrgetter('feelDizzy'), hospitalWorkerList)
        dizzyFreq = getFreqsFromList(dizzyList) 
        graphFamilyFearWithLivStatus(marriedFreq, dizzyFreq)
        
        ageList = map(attrgetter('age'), hospitalWorkerList)
        ageFreq = getFreqsFromList(ageList)
        educationList = map(attrgetter('education'), hospitalWorkerList)
        educationFreq = getFreqsFromList(educationList) 
        graphFamilyFearWithLivStatus(ageFreq, educationFreq, hospFreqFreq)
        
        print(str(hospitalWorkerList))
            
    
#take out folllowing count
class HealthcareWorker:
  def __init__(self, age, gender, indianTerritory, education,  maritalStatus, covidPositive, knowSomeoneCovid, 
               livingStatus, anxietyDisorder, familyFear, adequateHospitalProtection, feelDizzy):
    self.age = age
    self.gender = gender
    self.indianTerritory = indianTerritory
    self.education = education
    self.maritalStatus = maritalStatus
    self.covidPositive = covidPositive
    self.knowSomeoneCovid = knowSomeoneCovid
    self.livingStatus = livingStatus
    self.anxietyDisorder = anxietyDisorder
    self.familyFear = familyFear
    self.adequateHospitalProtection = adequateHospitalProtection
    self.feelDizzy = feelDizzy
    
if __name__ == "__main__":
    set_up_healthcare()
    print("All the text files have been filled with data")