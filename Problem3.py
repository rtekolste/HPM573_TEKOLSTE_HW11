import Parameters as P
import InputData as Data
import scr.MarkovClasses as SupportLibMarkov
import Problem2 as P2
import MarkovClasses as MarkovCls
import Support as SupportMarkov

print("Problem 3")


cohort = MarkovCls.Cohort(
        id=0,
    therapy=P.Therapies.NONE)

simOutputs = cohort.simulate()

cohort2 =  MarkovCls.Cohort(
        id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs2 = cohort2.simulate()

SupportMarkov.print_comparative_outcomes(simOutputs, simOutputs2)
