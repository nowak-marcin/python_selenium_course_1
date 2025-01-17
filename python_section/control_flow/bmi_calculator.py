print('witaj w programie BMI MNO CALCULATOR!!!')

weight = int(input('podaj swoją wagę w kg: '))
height = float(input('podaj swój wzrost w metrach: '))
bmi = round(weight / (height ** 2), 1)

if bmi <= 18.5:
    print(f'twój bmi wynosi {bmi}, co oznacza niedowage')
elif 18.5 < bmi <= 25:
    print(f'twój bmi wynosi {bmi}, co oznacza stan normalny')
elif 25 < bmi <= 30:
    print(f'twój bmi wynosi {bmi}, co oznacza nadwage')
else:
    print(f'twój bmi wynosi {bmi}, co oznacza otylosc')
