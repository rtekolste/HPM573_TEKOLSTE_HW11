import Parameters as P
import MarkovClasses as MarkovCls

print("Problem 3")


cohort = MarkovCls.Cohort(
        id=0,
    therapy=P.Therapies.NONE)

#simOutputs = cohort.simulate()
print(P.ParametersFixed._prob_matrix)

cohort2 =  MarkovCls.Cohort(
        id=1,
    therapy=P.Therapies.ANTICOAG)
