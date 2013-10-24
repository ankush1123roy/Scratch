""" Original Matlab code by Kiana changed by Ankush """

import random
import numpy 
from numpy import matrix as MA
def randd(lb, up, number):
    ind = []

# Generate 'number' values from the uniform distribution on the interval [lb,ub)

  up=up+1 # [lb,ub]
  if number>=up:
    prinf('number should be <= up+1')
    return

# queries = floor(a + (b-a).*rand(number,1));

  a,b=lb,up
  n=1
  ind = floor(a + (b-a).*rand(1,1))
  while n < number:
    r = floor(a + (b-a).*rand(1,1))
    if  isempty(find(ind==r))  %~any(ind==r):
        ind = [ind r]
        n=n+1

  return ind
