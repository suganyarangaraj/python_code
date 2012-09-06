import csv
import os
import sys
import random
import datetime

from random import randint
from datetime import date, timedelta

def write_payments_tsv(tsv_path):

    user_id=[]
    tx_id=[]
    revenue=[i*5 for i in range(5)]
    tx_date=[]
    n=1000
    for i in range(1,n+1):
         user_id.append(i)
         tx_id.append('tx' + str(i))
         revenue.append(random.choice(revenue))   
         
    for i in range(0,30):
        tx_date.append(datetime.date.today() - datetime.timedelta(days=i))
    
    f=open(tsv_path,"w")
    for i in range(n):
        thedate=random.choice(tx_date)
        f.writelines((str(user_id[i]) + '\t' + str(tx_id[i]) + '\t' + str(revenue[i]) +'\t' + str(thedate) +'\n'))
    f.close()
    
def main():

    tsv_dir='./tsv'
    if not os.path.exists(tsv_dir):
        os.mkdir(tsv_dir, 0755)    
    tsv_path = os.path.join(tsv_dir, 'revenue_tx' + '.tsv')
    write_payments_tsv(tsv_path)

if __name__ == '__main__':
    sys.exit(main())
 
