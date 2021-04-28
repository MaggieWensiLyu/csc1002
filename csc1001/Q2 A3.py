class Polynomial():
    def __init__(self):
        self.poly = 1
        self.derivative = 0
    def setPoly(self,poly):
        if poly.count("-") != 0:        # check whether there is an '-' operator
            lis = list(poly)
            pos = lis.index("-")
            lis.insert(pos,"+")
            poly = "".join(lis)         #change the '-' operaiton into addition
        self.poly = poly
    def getderivative(self):
        return self.derivative
    def calDerivative(self,para):
        monomials = self.poly.split("+")  # all the monomials are cheated as a*x^b forms
        derivatives = []
        for monomial in monomials:       #remove the empty space in the monomial
            new = list(monomial)
            if " " in new:
             new.remove(" ")
             monomial = ''.join(new)
            firstPara = monomial.count(para)    # find the first parameter a 
            if firstPara == 0 :
                b = 0
            else:
                if monomial.count("^") == 0:
                    b = 1
                else:
                    b = float(monomial[monomial.index("^") + 1: ])
            secondPara = monomial.count("*")    #find the second parameter b
            if secondPara == 0:
                a = 1
            else:
                a = float(monomial[ : monomial.index("*")]) 
            first = b * a              #calculation
            if first == int(first):
                first = int(first)
            second  = b -1 
            if second == int(second):
                second = int(second)
            if second == 0 :          
                der = str(first)
            elif second  == 1:
                der = str(first) + para
            else:
               der = str(first) + para + "^" + str(second) 
            if first > 0:
             derivatives.append( "+" + der)
            elif first < 0:
             derivatives.append(der)
        if len(derivatives) > 0:                 # the result can not be empty
         self.derivative = "".join(derivatives)
         if self.derivative[0] == "+" or self.derivative[0] == "-":  #remove the first sign
             self.derivative = self.derivative[1:]
        else:
         self.derivative = 0
        
a = Polynomial()

poly = input("please input a polynomial:")
para = input("please input the parameter:")

a.setPoly(poly)
a.calDerivative(para)
print(a.getderivative())
        
