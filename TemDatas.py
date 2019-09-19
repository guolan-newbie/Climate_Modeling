import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.pyplot import *

file1 = 'SURREY WHITE ROCK 1987.csv'
file2 = 'OTTAWA 2006.csv'

def surrey_white_rock():
    with open(file1,encoding='utf-8',errors='ignore') as f:
        reader = csv.reader(f)
        head_row = next(reader)

        #for index,name in enumerate(head_row):
        #    print(index,name)

        max_temps = []
        min_temps = []
        dates = []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                max_temp = float(row[5])
                min_temp = float(row[7])
            except ValueError:
                print(current_date,'N/A')
            else:
                dates.append(current_date)
                max_temps.append(max_temp)
                min_temps.append(min_temp)

        fig = plt.figure(dpi=300,figsize=(10,6))
        plt.plot(dates,max_temps,c='red',alpha=0.8,label='daily max temperature')
        plt.plot(dates,min_temps,c='blue',alpha=0.8,label='daily min temperature')
        plt.fill_between(dates,max_temps,min_temps,facecolor='yellow',alpha=0.3)

        plt.title('Temperatures of SURREY WHITE ROCK in 1987')
        plt.xlabel('Date',fontsize='12')
        fig.autofmt_xdate()
        plt.ylabel('T', fontsize='12')
        plt.tick_params(axis='both',which='major',labelsize=12)

        plt.legend(loc=2)

        ylim(-15, 35)

        plt.show()

def ottawa_quarter():
    with open(file2,encoding='utf-8',errors='ignore') as f:
        reader = csv.reader(f)
        head_row = next(reader)

        #for index,name in enumerate(head_row):
        #    print(index,name)

        mean_temps_3, mean_temps_6, mean_temps_9, mean_temps_12= [],[],[],[]
        dates_3, dates_6, dates_9, dates_12 = [],[],[],[]
        for i,row in enumerate(reader):
            if (i-2)%12 == 0:
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_3.append(current_date)
                    mean_temps_3.append(mean_temp)
            elif (i-5)%12 == 0:
                try:
                    mean_temp = float(row[7])
                    current_date = datetime.strptime(row[0], '%Y-%m')
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_6.append(current_date)
                    mean_temps_6.append(mean_temp)
            elif (i-8)%12 == 0:
                try:
                    mean_temp = float(row[7])
                    current_date = datetime.strptime(row[0], '%Y-%m')
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_9.append(current_date)
                    mean_temps_9.append(mean_temp)
            elif (i-11)%12 == 0:
                try:
                    mean_temp = float(row[7])
                    current_date = datetime.strptime(row[0], '%Y-%m')
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_12.append(current_date)
                    mean_temps_12.append(mean_temp)
        fig = plt.figure(dpi=300,figsize=(10,6))
        plt.plot(dates_3,mean_temps_3,c='green',alpha=0.8, label='mean T in Mar')
        plt.plot(dates_6,mean_temps_6, c='red', alpha=0.8, label='mean T in Jun')
        plt.plot(dates_9,mean_temps_9, c='yellow', alpha=0.8, label='mean T in Sept')
        plt.plot(dates_12,mean_temps_12, c='blue', alpha=0.8, label='mean T in Dec')

        plt.title('Mean temperatures of OTTAWA before 2006')
        plt.xlabel('Date',fontsize='12')
        fig.autofmt_xdate()
        plt.ylabel('T', fontsize='12')
        plt.tick_params(axis='both',which='major',labelsize=12)

        plt.legend(loc=2)

        ylim(-25, 35)

        plt.show()

def ottawa_months():
    with open(file2,encoding='utf-8',errors='ignore') as f:
        reader = csv.reader(f)
        head_row = next(reader)

        #for index,name in enumerate(head_row):
        #    print(index,name)

        mean_temps_2000, mean_temps_2001, mean_temps_2002, mean_temps_2003= [],[],[],[]
        mean_temps_2004, mean_temps_2005, mean_temps_2006 = [], [], [],
        dates_2000, dates_2001, dates_2002, dates_2003 = [],[],[],[]
        dates_2004, dates_2005, dates_2006 = [],[],[]
        for i,row in enumerate(reader):
            if i>=1332 and i<1344:
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_2000.append(current_date)
                    mean_temps_2000.append(mean_temp)
            elif i>=(1332+12) and i<(1344+12):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_2001.append(current_date)
                    mean_temps_2001.append(mean_temp)
            elif i>=(1332+12*2) and i<(1344+12*2):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_2002.append(current_date)
                    mean_temps_2002.append(mean_temp)
            elif i>=(1332+12*3) and i<(1344+12*3):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_2003.append(current_date)
                    mean_temps_2003.append(mean_temp)
            elif i>=(1332+12*4) and i<(1344+12*4):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_2004.append(current_date)
                    mean_temps_2004.append(mean_temp)
            elif i>=(1332+12*5) and i<(1344+12*5):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_2005.append(current_date)
                    mean_temps_2005.append(mean_temp)
            elif i>=(1332+12*6) and i<(1344+12*6):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_2006.append(current_date)
                    mean_temps_2006.append(mean_temp)


        fig = plt.figure(dpi=300,figsize=(10,6))
        plt.plot(mean_temps_2000,alpha=0.8, label='mean T in 2000')
        plt.plot(mean_temps_2001,alpha=0.8, label='mean T in 2001')
        plt.plot(mean_temps_2002,alpha=0.8, label='mean T in 2002')
        plt.plot(mean_temps_2003,alpha=0.8, label='mean T in 2003')
        plt.plot(mean_temps_2004, alpha=0.8, label='mean T in 2004')
        plt.plot(mean_temps_2005, alpha=0.8, label='mean T in 2005')
        plt.plot(mean_temps_2006, alpha=0.8, label='mean T in 2006')

        plt.title('Mean temperatures of OTTAWA before 2006')
        plt.xlabel('Date',fontsize='12')
        fig.autofmt_xdate()
        plt.ylabel('T', fontsize='12')
        plt.tick_params(axis='both',which='major',labelsize=12)

        plt.legend(loc=2)

        ylim(-25, 35)

        plt.show()

ottawa_months()
