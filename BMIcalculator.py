# BMI calculator 
''' 
Here are the general BMI categories:

Underweight: BMI less than 18.5
Normal weight: BMI between 18.5 and 24.9
Overweight: BMI between 25 and 29.9
Obesity:
Class I: BMI between 30 and 34.9
Class II: BMI between 35 and 39.9
Class III (Severe obesity): BMI of 40 or higher
'''

def bmi():
    ''' BMI calculator function  '''
    while True: 
        name = input('Enter your name : ') 
        weight = int(input('Enter your weight (in kg) : ' ))  
        heightincm = int(input('Enter your height (in cm) : ' ))         
        heightinm = heightincm/100
        # bmi formula (for kilograms and m)
        bmi = weight/(heightinm*heightinm)
        if bmi<18.5 and bmi>0:
            print(name,'You have underweight')
            break
        elif bmi>18.5 and bmi<24.9:
            print(name,'you have normal weight ')
            break
        elif bmi>25 and bmi<29.9:
            print(name,'You have overweight')
            break
        elif bmi>30 and bmi<34.9:
            print(name,'You have obesity')
            break
        elif bmi>35 and bmi<39.9:
            print(name,'You have high obesity')
            break
        elif bmi>40:
            print(name,"You have severe obesity")
            break
        elif bmi<0:
            print('You give invalid data Try again')
            continue
bmi()
