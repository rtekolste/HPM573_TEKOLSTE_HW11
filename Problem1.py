import numpy as np

print("Problem 1")
print("")
print("Part 1")

print("Background death = Total Mortality - Stroke Mortality")
print("Total Mortality = 1,800/100,000")
print("Stroke Mortality = 36.2/100,000")

background_mort = - np.log(1-(1763.8/100000))
print("Background Mortality =", background_mort)

print("")
print("Part 2")
print("Annual Rate of First Stroke = 15/1000")
print("")
print("Part 3")
print("Annual Rates")
print("Transition to Stroke = 15/1000 = .015")
print("Transition to Post-Stroke = .9*15/1000 = .0135")
print("Transition to Stroke Death = .1*15/1000 = .0015")
print("")

print("Part 4")
print("Rate of No Stroke/5 Years = . 83")
print(".83 = R(no stroke)^5")
print("R(no stroke) = .83^(1/5) = .968")
print("Recurrent Stroke = .0312")
print("")

print("Part 5")
print("Transition from Post-Stroke to Stroke = .0312*.8 =.02496")
print("Transition from Post Stroke to Death = .0312*.2 =.00624")
print("")

print("Part 6")
print("Therefore expected stay time is 7/365ths of a year")
print("Therefore Lambda = 365/7")

