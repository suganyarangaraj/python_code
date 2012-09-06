import csv
import os
import sys
import random
import datetime

from random import randint
from datetime import date, timedelta

def write_payments_tsv(tsv_path):

    user_id=[]
    user_name=[]  
    year=[]
    age=[]
    gender=['male','male','female','female']
    created=[]  
    dateList=[]
    country=['us','uk','ind','aus','Bel','Fran','Italy','Ger','Indo','Bang','Sri','Bra','Gre','Swi']
    n=1000
    for i in range(1,n+1):
         user_id.append(i)
         user_name.append('name' + str(i))

    for i in range(n):
         year.append(random.randint(1952,1984))
         gender.append(random.choice(gender))
         country.append(random.choice(country))
   
    for j in range(len(year)):
       age.append(2012-year[j])

    for i in range(0,30):
        created.append(datetime.date.today() - datetime.timedelta(days=i))
    
    f=open(tsv_path,"w")
    for i in range(n):
        thedate=random.choice(created)
        f.writelines((str(user_id[i]) + '\t' + str(user_name[i]) + '\t' + str(year[i]) + '\t' + str(age[i]) + '\t' + str(gender[i]) + '\t' + str(country[i]) + '\t'+ str(thedate) +'\n'))       
    
    
def main():

    tsv_dir='./tsv'
    if not os.path.exists(tsv_dir):
        os.mkdir(tsv_dir, 0755)    
    tsv_path = os.path.join(tsv_dir, 'user' + '.tsv')
    write_payments_tsv(tsv_path)

if __name__ == '__main__':
    sys.exit(main())
 
