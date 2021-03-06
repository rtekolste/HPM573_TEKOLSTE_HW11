import Parameters as P
import MarkovClasses as MarkovCls
import Support

print("Problem 3")


cohort = MarkovCls.Cohort(
        id=0,
    therapy=P.Therapies.NONE)

simOutputs = cohort.simulate()


cohort2 =  MarkovCls.Cohort(
        id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs2 = cohort2.simulate()

Support.print_comparative_outcomes(simOutputs, simOutputs2)
print("Done")
