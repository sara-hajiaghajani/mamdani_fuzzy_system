
from simpful import *
import matplotlib.pyplot as plot

# Create a fuzzy system object
FS = FuzzySystem()

# Define fuzzy sets and linguistic variables
# Employee_Experience
V1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=25, d=30), term="Non_Technical")
V2 = FuzzySet(function=Trapezoidal_MF(a=20, b=30, c=60, d=70), term="Technical")
V3 = FuzzySet(function=Trapezoidal_MF(a=55, b=70, c=100, d=100), term="Security_Analyst")
LV1 = LinguisticVariable([V1, V2, V3], concept="Employee Experience", universe_of_discourse=[0, 100])
FS.add_linguistic_variable("Employee_Experience", LV1)
LV1.plot()

# Security_Level
V4 = FuzzySet(function=Triangular_MF(a=0, b=0, c=20), term="Non")
V5 = FuzzySet(function=Triangular_MF(a=15, b=25, c=35), term="Low")
V6 = FuzzySet(function=Triangular_MF(a=26, b=50, c=80), term="Medium")
V7 = FuzzySet(function=Triangular_MF(a=70, b=100, c=100), term="High")
LV2 = LinguisticVariable([V4, V5, V6, V7], concept="Security Level", universe_of_discourse=[0, 100])
FS.add_linguistic_variable("Security_Level", LV2)
LV2.plot()

# Company_Policy
V8 = FuzzySet(function=Triangular_MF(a=0, b=0, c=40), term="Weak")
V9 = FuzzySet(function=Triangular_MF(a=25, b=50, c=75), term="Medium")
V10 = FuzzySet(function=Triangular_MF(a=60, b=100, c=100), term="Strong")
LV3 = LinguisticVariable([V8, V9, V10], concept="Company Policy", universe_of_discourse=[0, 100])
FS.add_linguistic_variable("Company_Policy", LV3)
LV3.plot()

# Phishing_Attack_Level
V11 = FuzzySet(function=Triangular_MF(a=9, b=9, c=30), term="Weak")
V12 = FuzzySet(function=Triangular_MF(a=20, b=50, c=75), term="Medium")
V13 = FuzzySet(function=Triangular_MF(a=57, b=100, c=100), term="Strong")
LV4 = LinguisticVariable([V11, V12, V13], concept="Phishing Attack Level", universe_of_discourse=[0, 100])
FS.add_linguistic_variable("Phishing_Attack_Level", LV4)
LV4.plot()

# Employee_Job_Satisfaction
V14 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=10, d=20), term="Weak")
V15 = FuzzySet(function=Trapezoidal_MF(a=25, b=65, c=100, d=100), term="Medium")
V16 = FuzzySet(function=Trapezoidal_MF(a=50, b=65, c=100, d=100), term="Strong")
LV5 = LinguisticVariable([V14, V15, V16],concept="Employee Job Satisfaction", universe_of_discourse=[0, 100])
FS.add_linguistic_variable("Employee_Job_Satisfaction", LV5)
LV5.plot()

# Procrastination
V17 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=20, d=35), term="Weak")
V18 = FuzzySet(function=Trapezoidal_MF(a=25, b=35, c=55, d=60), term="Medium")
V19 = FuzzySet(function=Trapezoidal_MF(a=50, b=70, c=100, d=110), term="Strong")
LV6 = LinguisticVariable([V17, V18, V19], concept="Procrastination", universe_of_discourse=[0, 110])
FS.add_linguistic_variable("Procrastination", LV6)
LV6.plot()

# Define output fuzzy sets and linguistic variable
# Employee_Susceptibility
V20 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=15, d=30), term="Low")
V21 = FuzzySet(function=Trapezoidal_MF(a=20, b=30, c=55, d=65), term="Medium")
V22 = FuzzySet(function=Trapezoidal_MF(a=55, b=75, c=100, d=110), term="High")
LV7 = LinguisticVariable([V20, V21, V22], concept="Employee Susceptibility", universe_of_discourse=[0, 110])
FS.add_linguistic_variable("Employee_Susceptibility", LV7)
LV7.plot()

# Define fuzzy rules

R1 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Non) AND (Company_Policy IS Medium) AND " \
     "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
     "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R2 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Strong) AND " \
     "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Medium) AND " \
     "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R3 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Strong) AND " \
     "(Phishing_Attack_Level IS Weak) THEN (Employee_Susceptibility IS Low)"
R4 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS High) AND (Company_Policy IS Weak) AND " \
     "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Medium) AND " \
     "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R5 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Non) AND (Company_Policy IS Medium) AND " \
     "(Phishing_Attack_Level IS Strong) AND (Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R6 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Strong) AND " \
     "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Medium) AND " \
     "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Medium)"
R7 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Non) AND (Company_Policy IS Weak) AND " \
     "(Phishing_Attack_Level IS Strong) THEN (Employee_Susceptibility IS High)"
R8 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Non) AND (Company_Policy IS Medium) AND " \
     "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
     "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Medium)"
R9 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Non) AND (Company_Policy IS Weak) AND " \
     "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
     "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R10 = "IF (Employee_Experience IS Technical) AND (Security_Level IS High) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R11 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Non) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Weak) AND (Procrastination IS Strong)" \
      " THEN (Employee_Susceptibility IS High)"
R12 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Non) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R13 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Non) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R14 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Non) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R15 = "IF (Employee_Experience IS Technical) AND (Security_Level IS High) AND (Company_Policy IS Strong) AND " \
      "(Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R16 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Non) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R17 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Low) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R18 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS High) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Medium)"
R19 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Low) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Medium)"
R20 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Medium)"
R21 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Low) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R22 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Low) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Medium) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R23 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Medium) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Low)"
R24 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS High) AND " \
      "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R25 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Non) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R26 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Low) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R27 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R28 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Non) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R29 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS High) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Weak) THEN (Employee_Susceptibility IS Low)"
R30 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS High) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R31 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Medium) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R32 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Non) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R33 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Low) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R34 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Medium) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Low)"
R35 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Low) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R36 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS High) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R37 = "IF (Security_Level IS Non) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R38 = "IF (Security_Level IS Low) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R39 = "IF (Security_Level IS High) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Weak) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R40 = "IF (Security_Level IS Medium) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Medium)"
R41 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Non) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R42 = "IF (Security_Level IS Medium) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R43 = "IF (Employee_Experience IS Non_Technical) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R44 = "IF (Employee_Experience IS Technical) AND " \
      "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R45 = "IF (Employee_Experience IS Technical) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Medium)"
R46 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Non) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Strong) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R47 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS High) AND " \
      "(Phishing_Attack_Level IS Weak) THEN (Employee_Susceptibility IS Low)"
R48 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS High) AND (Company_Policy IS Strong) AND " \
      "(Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Low)"
R49 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Low) AND (Company_Policy IS Weak) AND " \
      "(Employee_Job_Satisfaction IS Weak) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R50 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Low) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Medium)"
R51 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Medium) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R52 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Strong) THEN (Employee_Susceptibility IS Low)"
R53 = "IF (Employee_Experience IS Technical) AND (Security_Level IS High) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Weak) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R54 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS High) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R55 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Low) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"
R56 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Medium)"
R57 = "IF (Employee_Experience IS Technical) AND (Security_Level IS High) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Low)"
R58 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS High)"
R59 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R60 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Low) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Strong) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R61 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Medium) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Strong) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R62 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS High) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R63 = "IF (Employee_Experience IS Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Weak) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Low)"
R64 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Medium) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Medium) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS High)"
R65 = "IF (Employee_Experience IS Non_Technical) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R66 = "IF (Employee_Experience IS Technical) AND (Security_Level IS High) AND (Company_Policy IS Strong) AND " \
      "(Phishing_Attack_Level IS Strong) AND (Employee_Job_Satisfaction IS Medium) AND " \
      "(Procrastination IS Medium) THEN (Employee_Susceptibility IS Medium)"
R67 = "IF (Employee_Experience IS Technical) AND (Security_Level IS High) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Weak) AND " \
      "(Procrastination IS Weak) THEN (Employee_Susceptibility IS Low)"
R68 = "IF (Employee_Experience IS Non_Technical) AND (Security_Level IS Non) AND (Company_Policy IS Medium) AND " \
      "(Phishing_Attack_Level IS Strong) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS High)"
R69 = "IF (Employee_Experience IS Security_Analyst) AND (Security_Level IS Non) AND (Company_Policy IS Weak) AND " \
      "(Phishing_Attack_Level IS Strong) AND " \
      "(Procrastination IS Strong) THEN (Employee_Susceptibility IS Medium)"


FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23,
              R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44,
              R45, R46, R47, R48, R49, R50, R51, R52, R53, R54, R55, R56, R57, R58, R59, R60, R61, R62, R63, R64, R65,
              R66, R67, R68, R69])

# Get Input
val1 = input("Enter your value between [0,100] for Employee_Experience: ")
val1 = float(val1)
val2 = input("Enter your value between [0,100] for Security_Level: ")
val2 = float(val2)
val3 = input("Enter your value between [0,100] for Company_Policy: ")
val3 = float(val3)
val4 = input("Enter your value between [0,100] for Phishing_Attack_Leve: ")
val4 = float(val4)
val5 = input("Enter your value between [0,110] for Employee_Job_Satisfaction: ")
val5 = float(val5)
val6 = input("Enter your value between [0,110] for Procrastination: ")
val6 = float(val6)

# Set antecedents values
FS.set_variable("Employee_Experience", val1)
FS.set_variable("Security_Level", val2)
FS.set_variable("Company_Policy", val3)
FS.set_variable("Phishing_Attack_Level", val4)
FS.set_variable("Employee_Job_Satisfaction", val5)
FS.set_variable("Procrastination", val6)

# Perform Mamdani inference and print output
print(FS.Mamdani_inference(["Employee_Susceptibility"]))
