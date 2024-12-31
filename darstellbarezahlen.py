import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

def gleitkommazahl_rechner(s,m,b,e):
    return (-1)**s*(m/(2**23))*b**(e-127)


"""
def darstellbare_zahl():
    print(r*x*(1-x))
    return r*x*(1-x)

def darstellbare_zahl(i,r,s):
    x=s
    list = []
    for j in range(i):
        list.append(logistischeAbbildungRechner(x,r))
        x = list[-1]
    return list
"""
def save_histogram(list):
    #plt.plot(range(i),list)
    plt.hist(list,100, weights=np.ones(len(list)) / len(list),histtype=u'step')
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    #plt.title("Histogramm für r = {} \n Variation der Startwerte in Schritten von {}".format(round(r,2), start_step))
    #plt.xlim([9950, 10000])
    plt.ylim([0, 0.1])
    #plt.xlabel('x-Wertebereich')
    #plt.ylabel('Prozentualer Anteil')
    plt.savefig('plots\histogram_r_{}_start_{}.png'.format(round(r,2),start_step))
    plt.clf()
    #plt.show()

def show_histogram(list):
    #plt.plot(range(i),list)
    plt.hist(list,1000,histtype=u'step')
    #plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    #plt.title("Histogramm für r = {} \n Variation der Startwerte in Schritten von {}".format(round(r,2), start_step))
    #plt.xlim([9950, 10000])
    #plt.ylim([0, 0.002])
    #plt.xlabel('x-Wertebereich')
    #plt.ylabel('Prozentualer Anteil')
    #plt.savefig('plots\histogram_r_{}_start_{}.png'.format(round(r,2),start_step))
    plt.show()
    #plt.clf()


# i = iterationen, s =startwert
if __name__ == "__main__":

    s = 0
    m = 0
    b = 2
    e = 121 # restliche Zahlen schon nach erstem Durchlauf erfasst (e > 121 ist sehr nah an 0.0)

    histogram_klassen = 100

    list = [0]*histogram_klassen
    list[0] = 121*2**23 # für e != 0 (hier bei e =121 und histogram_klassen =20 und histogram_klassen = 100)
    list_bereiche = [None]*histogram_klassen
    for i in range(histogram_klassen):
        list_bereiche[i] = (i+1)/histogram_klassen
    print(list_bereiche)

    while e <= 254:
        m = 0
        while m< 2**23:
            x = gleitkommazahl_rechner(s, m, b, e)

            """
            if x > 1:
                break
            """
            for i in range(len(list_bereiche)):
                if i == 0:
                    if x > 0 and x <= list_bereiche[i]:
                        list[i] += 1
                if x > list_bereiche[i-1] and x <= list_bereiche[i]:
                    list[i] += 1
            """
            if x > 0 and x < 0.05:
                list[0] += 1
            if x >= 0.05 and x < 0.1:
                list[1] += 1
            if x >= 0.1 and x < 0.15:
                list[2] += 1
            if x >= 0.15 and x < 0.2:
                list[3] += 1
            if x >= 0.2 and x < 0.25:
                list[4] += 1
            if x >= 0.25 and x < 0.3:
                list[5] += 1
            if x >= 0.3 and x < 0.35:
                list[6] += 1
            if x >= 0.35 and x < 0.4:
                list[7] += 1
            if x >= 0.4 and x < 0.45:
                list[8] += 1
            if x >= 0.45 and x < 0.5:
                list[9] += 1
            if x >= 0.5 and x < 0.55:
                list[10] += 1
            if x >= 0.55 and x < 0.6:
                list[11] += 1
            if x >= 0.6 and x < 0.65:
                list[12] += 1
            if x >= 0.65 and x < 0.7:
                list[13] += 1
            if x >= 0.7 and x < 0.75:
                list[14] += 1
            if x >= 0.75 and x < 0.8:
                list[15] += 1
            if x >= 0.8 and x < 0.85:
                list[16] += 1
            if x >= 0.85 and x < 0.9:
                list[17] += 1
            if x >= 0.9 and x < 0.95:
                list[18] += 1
            if x >= 0.95 and x < 1:
                list[19] += 1
            """
            m+=1
        print(e," ", list)
        e+=1


    #print(len(list))
    #show_histogram(list)


    plt.plot(list_bereiche,list)
    #plt.xlim([9950, 10000])
    #plt.ylim([0, 1])
    plt.yscale('log')
    plt.title("Histogramm Floats \n Zahlenbereich 0 bis 1 in {} Klassen".format(histogram_klassen))
    plt.xlabel("Wertebereich")
    plt.ylabel('Anzahl')
    plt.show()