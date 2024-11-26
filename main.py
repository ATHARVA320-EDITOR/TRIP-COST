def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if "Charlotte" == city:
        return 180
    if "Chicago" == city:
        return 210
    if "Denver" == city:
        return 250
    if "Houston" == city:
        return 300
    if "Los Angeles" == city:
        return 500
def rental_car_cost(days):
    if days >= 7:
        return 40*days - 50
    if days >= 7:
        return 40*days - 20
    else:
        return 40*days
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print("Cost of car rent:", rental_car_cost(6))
print("Cost of plane ride:", plane_ride_cost("Los Angeles"))
print("Cost of hotel:", hotel_cost(7))
print("Total cost of the trip is", trip_cost("Los Angeles", 7, 500))
print(trip_cost("Chicago", 6500))
    
    
    