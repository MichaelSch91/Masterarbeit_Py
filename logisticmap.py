import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

def logistischeAbbildungRechner(x,r):
    #print(r*x*(1-x))
    return r*x*(1-x)

#mit Startwert s
def logistischeAbbildung(i,r,s):
    x=s
    list = []
    for j in range(i):
        list.append(logistischeAbbildungRechner(x,r))
        x = list[-1]
    return list

#mit Startwert s und Nachkommastellen n
def logistischeAbbildungNachkommastellen(i,r,s,n):
    x=s
    list = []
    for j in range(i):
        list.append(round(logistischeAbbildungRechner(x,r),n))
        x = list[-1]
    return list

#ohne Startwert s aber mit step um die Startwerte hochzuzählen
def logistischeAbbildung_s_counting(i,r,start_step):
    s=0.01
    list = []
    while s < 0.99:
        x=s
        for j in range(i):
            list.append(logistischeAbbildungRechner(x,r))
            x = list[-1]
        s+=start_step
        #print("s = ", s)
    return list

def save_histogram(list,r,start_step):
    #plt.plot(range(i),list)
    plt.hist(list,100, weights=np.ones(len(list)) / len(list))
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.title("Histogramm für r = {} \n Variation der Startwerte in Schritten von {}".format(round(r,2), start_step))
    #plt.xlim([9950, 10000])
    plt.ylim([0, 0.1])
    plt.xlabel('x-Wertebereich')
    plt.ylabel('Prozentualer Anteil')
    plt.savefig('plots\histogram_r_{}_start_{}.png'.format(round(r,2),start_step))
    plt.clf()
    #plt.show()

def logistischeAbbildung_counting_parameter_r_print(i,start_step,r_step,r_start):
    r = r_start
    while r <= 4.0:
        save_histogram(logistischeAbbildung(i, r, start_step),r,start_step)
        r += r_step

# Beginnen bei r = 4.0 und Wert schrittweise verringern bis r_stop
def logistischeAbbildung_decreasing_parameter_r_print(i,start_step,r_step,r_stop):
    r = 4.0
    while r >= r_stop:
        save_histogram(logistischeAbbildung(i, r, start_step),r,start_step)
        r -= r_step

# i = iterationen, s =startwert
if __name__ == "__main__":
    i = 100000
    r = r_start = r_stop = 3.9
    s = 0.1
    start_step = 0.01
    r_step = 0.01

    """
    list = logistischeAbbildung(i, r, start_step)
    print(len(list))
    print_histogram(list, r, start_step)
    """

    #print(logistischeAbbildung_s_counting(i, r, start_step))

    logistischeAbbildung_decreasing_parameter_r_print(i,start_step,r_step,r_stop)
    #print(list)
    """
    plt.plot(range(i),list)
    plt.scatter(range(i),list,color="red")
    plt.xlim([9950, 10000])
    plt.ylim([0, 1])
    plt.title("Generation mit r = {} und Startwert x_0 = {}".format(r,s))
    plt.xlabel("Generation")
    plt.ylabel('Population')
    plt.show()
    """


