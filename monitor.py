
from time import sleep
import sys

def vitals_alert(message):
  print(message)
  for i in range(6):
    print('\r* ', end='')
    sys.stdout.flush()
    sleep(1)
    print('\r *', end='')
    sys.stdout.flush()
    sleep(1)

def isTempOk(temperature):
  if temperature > 102 or temperature < 95:
    vitals_alert('Temperature critical!') 
    return False 
  return True
def isPulserateOk(pulseRate):
  if pulseRate < 60 or pulseRate > 100:
    vitals_alert('Pulse Rate is out of range!')
    return False
  return True
def isSpo2Ok(spo2):
  if spo2 < 90:
    vitals_alert('Oxygen Saturation out of range!')
    return False
  return True

def vitals_ok(temperature, pulseRate, spo2):
  return isTempOk(temperature) and isPulserateOk(pulseRate) and isSpo2Ok(spo2)

#for loop and print duplications removed