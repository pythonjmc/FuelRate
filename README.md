# IMPORTANT!!!!
This system should only be used for recreational purposes. Not to be used in real life.

# FuelRate
Calculate whether or not you will have enough fuel to reach your destination.

# Sources
Game: RFS Real Flight Simulator

channel: https://discord.com/channels/665183274452254740/724543543422484521/791602762650484736

server: https://discord.gg/zn4srrWzvk

# How doest it work
This system allows you to know if you will have enough fuel in stock to reach your destination by applying the following formula: a-bx

where  

       a = Your fuel rate at the time of this calculation
       
       b = The remaining flight time in seconds
       
       c = Your current fuel rate (cruising altitude)

If you get a negative number on exit, this means that you will be short of that number of kg of fuel.
Otherwise, if you get a positive number, it will show the rate you have left on arrival.

**Exemple**

I do a flight from Seoul to Hong-Kong and i got: 

-1h15 left

- 37500kgs of fuel rate

- a fuel flow of 1.80 kgs/s

1h15 = 3609 secondes

calcul: 37500 - 3609 * 1.80 = 31003.8

This result means that I will be able to reach my destination with this fuel rate and that at the end of the journey I will have 31003.8 kilograms of fuel.
