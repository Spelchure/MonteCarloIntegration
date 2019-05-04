# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:01:10 2019

Monte carlo integration for anatically unsolvable functions.
"""

import random
import matplotlib.pyplot as plot

#Requirements of Monte Carlo Integration
#1.Non-linear function to integrate
#2.Limits(A,B)
#3.RNG



class Termocouple:
   _TERMOMINDEGREE = -200
   _TERMOMAXDEGREE = -170 
   
#ITS-90 TABLE  FOR TYPE J TERMOCOUPLE
   _termocoupleTable = {
           _TERMOMINDEGREE:-7.990,
           -199:-7.980, -198:-7.912, -197:-7.934,
           -196:-7.955, -195:-7.976, -195:-7.996,
           -194:-8.017, -193:-8.037, -192:-8.057,
           -191:-8.076, -190:-7.659, -189:-7.683,
           -188:-7.707, -187:-7.731, -186:-7.755,
           -185:-7.778, -184:-7.801, -183:-7.824,
           -182:-7.846, -181:-7.868, -180:-7.403,
           -179:-7.429, -178:-7.456, -177:-7.482, 
           -176:-7.508, -175:-7.534, -174:-7.559,
           -173:-7.585, -172:-7.610, -171:-7.634,
           _TERMOMAXDEGREE:-7.123
}
   
   def Termocouple(self):
       None
       
       
   @staticmethod
   def getTermoMinDegree():
       return Termocouple._TERMOMINDEGREE
   
   @staticmethod
   def getTermoMaxDegree():
       return Termocouple._TERMOMAXDEGREE
   
#Simple non-linear function
#Returns mV using Termocouple conversion table
#Parameters: degree in santigrat.
   def convertMV(self,degree):
        if degree < self._TERMOMINDEGREE or degree > self._TERMOMAXDEGREE:
            raise ValueError("Degree value must be between {0},{1}".format(self._TERMOMINDEGREE,
                             self._TERMOMAXDEGREE))
        return self._termocoupleTable[degree]
   def MonteCarlo(self,N=1000):
       a = self._TERMOMINDEGREE
       b = self._TERMOMAXDEGREE
       integral = 0
       rands = {}
       answer = []
       
       def fillRands():
           for i in range(N):
               rands[i] = random.randrange(a,b)

       for i in range(N):
           fillRands()
           integral = 0
           for i in range(N):
               integral += self.convertMV(rands[i])
               
           answer.append((b-a)/float(N)*integral)
         
       return answer
      
def main():
    tCouple = Termocouple()
    ans = tCouple.MonteCarlo()
    

    plot.title("Histogram of Distrubition Areas")
    plot.hist(ans, bins=50,ec='black',color='red')
    
    
    
if __name__ == '__main__':
    main()
