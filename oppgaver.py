import random as r
import time as t
import calendar


#funksjon som genererer sensordata
def sensor():
    sensor = r.randint(1,10)
    return sensor

#funksjon som lager timstamp
def timestamp():
    GMTtid = t.gmtime()
    timestamp = calendar.timegm(GMTtid)
    return timestamp


## oppgave 1
def data_collector():
    tid = timestamp()
    sample = sensor()
    return tid, sample


##oppgave 2
def matrix_calc():
    x = [1,2,3]
    y = [1,2,3]

    z = x*y
    return z


