import json
import csv
import random

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
            
            print(hospitalWorkerList)
            
    
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