import decimal
import math

getcontext().rounding=ROUND_HALF_DOWN

def clean():
    print('\n'*80)

def max_interval(p,t):
'''
Returns the maximum interval which p* lies with relative error at most 10^-4
'''
    if type(t)== int:
        if p>=0:
            return ((1-10**(-t))*p,(1+10**(-t))*p)
