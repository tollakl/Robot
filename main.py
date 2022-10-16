import random as r
import oppgaver as opp


def main():

    sensordata = []
    for i in range(20):
        sensordata.append((opp.data_collector()))

    print(sensordata)

    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    z = []
    for i in range(len(x)):
        z.append(x[i][i]*y[i][i])

    print(z)

if __name__ == '__main__':
    main()





