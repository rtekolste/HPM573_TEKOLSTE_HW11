import numpy as np
import Parameters as P
import InputData as Data

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
first_stroke =  - np.log(1-(15/1000))
print("Annual Rate of First Stroke =", first_stroke)
print("")

print("Part 3")
print("Annual Rates")
print("Transition to Stroke = 15/1000 = .015")

post_stroke = .9*first_stroke
print("Transition to Post-Stroke =", post_stroke)
stroke_death = .1*first_stroke
print("Transition to Stroke Death =", stroke_death)
print("")

print("Part 4")
recurrent_stroke = - np.log(1-(17/100))/5
print("Recurrent Stroke =", recurrent_stroke )
print("")

print("Part 5")
second_stroke_survive=.8*recurrent_stroke
print("Transition from Post-Stroke to Stroke =", second_stroke_survive)
second_stroke_die = .2*recurrent_stroke
print("Transition from Post Stroke to Death", second_stroke_die)
print("")

print("Part 6")
print("Therefore expected stay time is 7/365ths of a year")
print("Therefore Lambda = 365/7 = 52")

print("")
print("Problem 2")

RATE_MATRIX = [
    [None, post_stroke, 0, stroke_death, background_mort],
    [0, None, 52, 0, 0],
    [0, second_stroke_survive*(1-background_mort), None, second_stroke_die*(1-background_mort), background_mort],
    [0, 0, 0, None, 0],
    [0, 0, 0, 0, None],
]

print("Rate Matrix No Treatment", RATE_MATRIX)

RATE_MATRIX_ANTI_COAG = [
    [None, post_stroke, 0, stroke_death, background_mort],
    [0, None, 52, 0, 0],
    [0, second_stroke_survive*(1-background_mort)*0.75, None, second_stroke_die*(1-background_mort)*0.75, background_mort*1.05],
    [0, 0, 0, None, 0],
    [0, 0, 0, 0, None],
]
print("Rate Matrix Anticoagulation", RATE_MATRIX_ANTI_COAG)
