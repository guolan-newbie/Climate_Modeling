import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.pyplot import *

file1 = 'SURREY WHITE ROCK 1987.csv'
file2 = 'OTTAWA 2006.csv'
files = []
for i in range(1959,2029,10):
    f1 = 'C:\\Users\86183\Desktop\Modeling\Ottawa\\'+str(i)+'.csv'
    files.append(f1)

mean_temps_1959, mean_temps_1969, mean_temps_1979, mean_temps_1989 = [], [], [], []
mean_temps_1999, mean_temps_2009, mean_temps_2019 = [], [], [],
dates_1959, dates_1969, dates_1979, dates_1989 = [], [], [], []
dates_1999, dates_2009, dates_2019 = [], [], []

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

def ottawa_months2():
    with open(file2,encoding='utf-8',errors='ignore') as f:
        reader = csv.reader(f)
        head_row = next(reader)

        #for index,name in enumerate(head_row):
        #    print(index,name)

        mean_temps_1956, mean_temps_1966, mean_temps_1976, mean_temps_1986= [],[],[],[]
        mean_temps_1996, mean_temps_1946, mean_temps_2006 = [], [], [],
        dates_1946, dates_1956, dates_1966, dates_1976 = [],[],[],[]
        dates_1986, dates_1996, dates_2006 = [],[],[]
        for i,row in enumerate(reader):
            if i>=684 and i<696:
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_1946.append(current_date)
                    mean_temps_1946.append(mean_temp)
            elif i>=(684+120) and i<(696+120):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_1956.append(current_date)
                    mean_temps_1956.append(mean_temp)
            elif i>=(684+120*2) and i<(696+120*2):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_1966.append(current_date)
                    mean_temps_1966.append(mean_temp)
            elif i>=(684+120*3) and i<(696+120*3):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_1976.append(current_date)
                    mean_temps_1976.append(mean_temp)
            elif i>=(684+120*4) and i<(696+120*4):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_1986.append(current_date)
                    mean_temps_1986.append(mean_temp)
            elif i>=(684+120*5) and i<(696+120*5):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_1996.append(current_date)
                    mean_temps_1996.append(mean_temp)
            elif i>=(684+120*6) and i<(696+120*6):
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m')
                    mean_temp = float(row[7])
                except ValueError:
                    print(current_date,'N/A')
                else:
                    dates_2006.append(current_date)
                    mean_temps_2006.append(mean_temp)


        fig = plt.figure(dpi=300,figsize=(10,6))
        plt.plot(mean_temps_1946,alpha=0.8, label='mean T in 1946')
        plt.plot(mean_temps_1956,alpha=0.8, label='mean T in 1956')
        plt.plot(mean_temps_1966,alpha=0.8, label='mean T in 1966')
        plt.plot(mean_temps_1976,alpha=0.8, label='mean T in 1976')
        plt.plot(mean_temps_1986, alpha=0.8, label='mean T in 1986')
        plt.plot(mean_temps_1996, alpha=0.8, label='mean T in 1996')
        plt.plot(mean_temps_2006, alpha=0.8, label='mean T in 2006')

        plt.title('Mean temperatures of OTTAWA before 2006')
        plt.xlabel('Date',fontsize='12')
        fig.autofmt_xdate()
        plt.ylabel('T', fontsize='12')
        plt.tick_params(axis='both',which='major',labelsize=12)

        plt.legend(loc=2)

        ylim(-15, 25)

        plt.show()

def ottawa_daily():
    year = 1959

    for file in files:
        with open(file,encoding='utf-8',errors='ignore') as f:
            reader = csv.reader(f)
            head_row = next(reader)

            #for index,name in enumerate(head_row):
            #    print(index,name)

            for i,row in enumerate(reader):
                global mt1959, mt1969, mt1979, mt1989, mt1999, mt2009, mt2019
                if i>=24 and year == 1959:
                    try:
                        current_date = datetime.strptime(row[0], '%Y-%m-%d')
                        mean_temp = float(row[5])
                    except ValueError:
                        print(current_date,'N/A')
                    else:
                        mean_temps_1959.append(mean_temp)
                        dates_1959.append(current_date)

                if i>=24 and year == 1969:
                    try:
                        current_date = datetime.strptime(row[0], '%Y-%m-%d')
                        mean_temp = float(row[5])
                    except ValueError:
                        print(current_date,'N/A')
                    else:
                        mean_temps_1969.append(mean_temp)
                        dates_1969.append(current_date)

                if i>=24 and year == 1979:
                    try:
                        current_date = datetime.strptime(row[0], '%Y-%m-%d')
                        mean_temp = float(row[5])
                    except ValueError:
                        print(current_date,'N/A')
                    else:
                        mean_temps_1979.append(mean_temp)
                        dates_1979.append(current_date)

                if i>=24 and year == 1989:
                    try:
                        current_date = datetime.strptime(row[0], '%Y-%m-%d')
                        mean_temp = float(row[5])
                    except ValueError:
                        print(current_date,'N/A')
                    else:
                        mean_temps_1989.append(mean_temp)
                        dates_1989.append(current_date)

                if i>=24 and year == 1999:
                    try:
                        current_date = datetime.strptime(row[0], '%Y-%m-%d')
                        mean_temp = float(row[5])
                    except ValueError:
                        print(current_date,'N/A')
                    else:
                        mean_temps_1999.append(mean_temp)
                        dates_1999.append(current_date)

                if i>=24 and year == 2009:
                    try:
                        current_date = datetime.strptime(row[0], '%Y-%m-%d')
                        mean_temp = float(row[5])
                    except ValueError:
                        print(current_date,'N/A')
                    else:
                        mean_temps_2009.append(mean_temp)
                        dates_2009.append(current_date)

                if i>=24 and year == 2019:
                    try:
                        current_date = datetime.strptime(row[0], '%Y-%m-%d')
                        mean_temp = float(row[5])
                    except ValueError:
                        print(current_date,'N/A')
                    else:
                        mean_temps_2019.append(mean_temp)
                        dates_2019.append(current_date)
        year += 10

    fig = plt.figure(dpi=300,figsize=(10,6))
    plt.plot(mean_temps_1959,alpha=0.5, linewidth=0.8,label='mean T in 1959')
    plt.plot(mean_temps_1969, alpha=0.5, linewidth=0.8,label='mean T in 1969')
    plt.plot(mean_temps_1979, alpha=0.5, linewidth=0.8,label='mean T in 1979')
    plt.plot(mean_temps_1989, alpha=0.5, linewidth=0.8,label='mean T in 1989')
    plt.plot(mean_temps_1999, alpha=0.5, linewidth=0.8,label='mean T in 1999')
    plt.plot(mean_temps_2009, alpha=0.5, linewidth=0.8,label='mean T in 2009')
    plt.plot(mean_temps_2019, c='black',alpha=1, linewidth=2,label='mean T in 2019')

    plt.title('Max temperatures of OTTAWA before 2019')
    plt.xlabel('Date',fontsize='12')
    fig.autofmt_xdate()
    plt.ylabel('T', fontsize='12')
    plt.tick_params(axis='both',which='major',labelsize=12)

    plt.legend(loc=2)
    xlim(1,365)
    ylim(-20,35)

    plt.show()

ottawa_daily()