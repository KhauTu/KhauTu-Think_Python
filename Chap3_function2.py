# void function

def final_amt(p,r,n,t):
    a = p * (1 + r/n) ** (n*t)
    return a
toInvest = float(input("How much do you want to invest?"))
fnl = final_amt(toInvest,0.08,12,5)
print("At the end of the period you'll have", fnl)

def final_amt_v2(principalAmount, nominalPercentagerate,numTimesPerYear, years):
    a = principalAmount * (1 + nominalPercentageRate / numTimesPerYear) ** (numTimesPerYear*years)
    return a
def final_amt_v3(amt, rate, compounded, years):
    a = amt * (1 + rate/compounded) ** (componded*years)
    return a