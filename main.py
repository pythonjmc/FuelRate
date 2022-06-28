#Request data from the user: Remaining time (hours and minutes); remaining fuel rate, current fuel flow.
TimeRemainingHour = int(input("Enter the number of hours remaining without minutes,  if there is no hours please tap 'enter': "))

TimeRemainingMinutes = float(input("Enter the number of minutes remaining as a decimal number with a zero in front: 26 mins = 0.26: "))

FuelRate = int(input("Enter the current remaining fuel rate: "))

FuelFlow = float(input("Enter the current oil flow rate."))


#Converting time in second 
HoursInSeconds = int(TimeRemainingHour * 3600) + float(TimeRemainingMinutes * 60)

#Calcul
if TimeRemainingHour == True:
    calcul = FuelRate - HoursInSeconds*FuelFlow
    print(calcul)
    if calcul > 0:
        print("You have enough fuel fuel to reach your destination.")
    elif calcul < 0:
        print("You will not have enough fuel to reach your destination, create a route to the nearest airport.")
else:
    calcul = int(TimeRemainingMinutes) - int(FuelRate) * float(FuelFlow)
