import numpy as np
import matplotlib.pyplot as plt
import statistics
import random
import csv
import os

import logisticmap

def plot(list1, list2, n1, n2, list):
    fig, host = plt.subplots(figsize=(8, 5), layout='constrained')
    #ax2 = host.twinx()
    #ax3 = host.twinx()
    host.set_xlim(0, 100)
    host.set_ylim(0, 1)
    #ax2.set_ylim(0, 100)
    #ax2.set_ylabel("Werte")


    host.plot(list1, color='green', label ="{} Nachkommastellen".format(n1))
    host.plot(list2, color='blue', label="{} Nachkommastellen".format(n2))
    host.plot(list, color='red', label="Abweichung (logisticmap {} Nachkommastellen - logisticmap {} Nachkommastellen)".format(n2,n1))
    # plt.xlim([9950, 10000])
    # plt.ylim([0, 1])
    #host.set_yscale('log')
    #ax2.set_title("Histogramm Floats \n Zahlenbereich 0 bis 1 in {} Klassen".format(100))
    host.set_xlabel("Generationen")
    host.set_ylabel('Werte')

    #plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    host.set_title("Logistische Abbildung mit r = {}".format(round(r, 2)))
    host.legend(loc="lower left")
    #ax2.legend(loc="lower left")
    #ax3.legend(loc="lower right")
    # plt.xlim([9950, 10000])
    #plt.ylim([0, 0.1])
    #plt.xlabel('x-Wertebereich')
    #plt.ylabel('Prozentualer Anteil')
    plt.show()

def random_list(iterations):
    list = []
    for x in range(iterations):
        list.append(abs(random.uniform(0,1) - random.uniform(0,1)))
    return list

def plot_abweichung(list):
    fig, host = plt.subplots(figsize=(8, 5), layout='constrained')
    #ax2 = host.twinx()
    #ax3 = host.twinx()
    host.set_xlim(0, 500)
    host.set_ylim(0, 1)
    host.plot(list, color='red', label="Abweichung (logisticmap {} Nachkommastellen - logisticmap {} Nachkommastellen)".format(n2,n1))
    host.set_xlabel("Generationen")
    host.set_ylabel('Abweichung')
    host.set_title("Logistische Abbildung mit r = {}".format(round(r, 2)))
    host.legend(loc="lower left")
    plt.show()

def evaluation_nachkommastellen_abweichungen(iterations,n1,n2):
    list1 = logisticmap.logistischeAbbildungNachkommastellen(iterations,r,s,n1)
    list2 = logisticmap.logistischeAbbildungNachkommastellen(iterations,r,s,n2)
    list = []
    for i in range(len(list1)):
        list.append(abs(list2[i] - list1[i]))
    return list

def iterations_until_delta_max(list ,delta_max):
    for i in range(len(list)):
        if list[i] > delta_max:
            return i
    return "error"

def print_interations_until_delta_max_from_different_n(n1,n2,delta_max):
    while n1 < 17:
        while n2 <= 17:
            print("n1 = {}, n2 = {}, delta_max = {} erreicht bei {}".format(n1,n2,delta_max,iterations_until_delta_max(evaluation_nachkommastellen_abweichungen(iterations,n1,n2),delta_max)))
            n2 += 1
        n1 += 1
        n2 = n1 + 1

def print_interations_until_delta_max_from_different_n_csv(n1,n2,delta_max):
    while n1 < 17:
        while n2 <= 17:
            print("{}, {}, {} , {}".format(delta_max,n1,n2,iterations_until_delta_max(evaluation_nachkommastellen_abweichungen(iterations,n1,n2),delta_max)))
            n2 += 1
        n1 += 1
        n2 = n1 + 1

#todo
def csv_to_list(filepath):
    with open(os.path.abspath(filepath)) as f:
        reader = csv.reader(f)
        data = list(reader)
    list = []
    for d in data:
        list.append(float(d[0]))
    return list

if __name__ == "__main__":
    # n1 =  Nachkommastellen für Berechnung; n2 = Nachkommastellen für Evaluation
    n1 = 1
    n2 = 2
    delta_max = 0.05

    iterations = 100000
    r = r_start = r_stop = 3.92
    s = 0.1
    start_step = 0.01
    r_step = 0.01

    #todo, falls nötig
    filepath_double = 'C:/Users/micha/source/repos/LogisticMap/double_precision.csv'
    filepath_long_double = 'C:/Users/micha/source/repos/LogisticMap/double_precision.csv'
    #print_interations_until_delta_max_from_different_n(n1,n2,delta_max)

    #print("List1 ",logisticmap.logistischeAbbildungNachkommastellen(iterations,r,s,n1)[0:500])




    """
    while delta_max <= 0.2:
        print_interations_until_delta_max_from_different_n_csv(n1, n2, delta_max)
        delta_max = round((delta_max + 0.05),2)
    

    list1 = logisticmap.logistischeAbbildungNachkommastellen(iterations,r,s,n1)
    list2 = logisticmap.logistischeAbbildungNachkommastellen(iterations,r,s,n2)
    list = []
    for i in range(len(list1)):
        list.append(abs(list2[i] - list1[i]))

    plot(list1, list2, n1, n2, list)

    #print("mittlere Abweichung: {}".format(statistics.mean(list)))

    #plot_abweichung(list)
    """

"""
    for y in range(20):
        list_random = random_list(i)
        print("mittlere Abweichung zufällige Listen: {}".format(statistics.mean(list_random)))
"""