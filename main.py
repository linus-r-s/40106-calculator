'''
Calculate frequency or resistor value for 40106 CMOS schmitt trigger oscillator.
'''

from math import log

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
  return 1/(f*c*log(vp(vdd)*(vdd-vn(vdd))/vn(vdd)*(vdd-vp(vdd))))

print(r(2, '1u', 9))