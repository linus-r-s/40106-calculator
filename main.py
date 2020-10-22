'''
Calculate frequency or resistor value for 40106 CMOS schmitt trigger oscillator.
'''

from math import log
from bisect import bisect_left

# Easier conversion of large and small values
UNITS = {'k': 1000, 'M': 1000000, 'u': 0.000001, 'n': 0.000000001}


def vp(vdd):
  '''
  Calculate positive threshold of inverter based on vdd
  '''
  return (vdd/2) + vdd*.08

def vn(vdd):
  '''
  Calculate negative threshold of inverter based on vdd
  '''
  return (vdd/2) - vdd*.11

def parse_value(value):
  '''
  Convert values
  '''
  if type(value) == int:
    return value
  else:
    unit = value[-1]
    return float(value[:-1])*UNITS[unit]

def standard_value(r):
  values = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
  mult = 1
  while r >= 10:
    r = r / 10
    mult *= 10
  pos = bisect_left(values, r)
  if pos == 0:
    r = values[0]
  elif pos == len(values):
    r = values[-1]
  else:
    before = values[pos - 1]
    after = values[pos]
    if after - r < r - before:
      r = after
    else:
      r = before
  return int(r * mult)

print(standard_value(100012))


def f(r, c, vdd):
  '''
  Calculate frequency
  '''
  r = parse_value(r)
  c = parse_value(c)
  return 1/(r*c*log(vp(vdd)*(vdd-vn(vdd))/vn(vdd)*(vdd-vp(vdd))))


def r(f, c, vdd):
  '''
  Calculate resistance value
  '''
  f = parse_value(f)
  c = parse_value(c)
  r = 1/(f*c*log(vp(vdd)*(vdd-vn(vdd))/vn(vdd)*(vdd-vp(vdd))))
  return r

#print(r(2, '1u', 9))