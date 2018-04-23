
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50     # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1/52         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03     # annual discount rate

ADD_BACKGROUND_MORT = True  # if background mortality should be added

PSA_ON = False      # if probabilistic sensitivity analysis is on

# annual cost of each health state
HEALTH_COST = [
    0,     # Well
    5000,  # Stroke (one time cost)
    200,   # Post-Stroke
    0,     # Stroke Death      # Dead
    ]

ANNUAL_STATE_COST_ANTICOAG = [
    0,     # Well
    5000,  # Stroke (one time cost)
    750,   # Post-Stroke
    0,     # Stroke Death      # Dead
    ]

# annual health utility of each health state
#ANNUAL_STATE_UTILITY = [
#    1.0000,   # Well
#    0.8865,   # Stroke
#    0.9000,   # Post-Stroke
#    0.0000,   # Stroke Death
#    ]

HEALTH_UTILITY = [
    1,          #Well
    0.2,        #Stroke (average time = 1 week)
    0.9,        #Post Stroke
    0           #Death
]



# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.75
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05


NoTreatment_COST = 0
Anticoag_COST = 2000

ANNUAL_PROB_BACKGROUND_MORT= 1763.8/100,000
