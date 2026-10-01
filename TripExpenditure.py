def hotelCost(nights):
    return 140* nights
def planeRideCost(city):
    if "Charlotte"== city:
        return 182
    elif "tampa" == city:
        return 220
    elif "pittsburgh" == city:
        return 222
    elif "Los angeles" == city:
        return 475

def rentalCarCost(days):
    if days>= 7:
        return 40 * days - 50
    elif days>=3:
        return 40 * days - 20
    else:
        return 40 * days


def tripCost(city, days, spendingMoney):
    return rentalCarCost(days) + hotelCost(days) + planeRideCost(city) + spendingMoney
print ("cost of car rental", rentalCarCost(5))
print ("cost of plane ride"), planeRideCost("Los angeles")
print ("cost of hotel room", hotelCost(7))
print("total cost of the trip :", tripCost("Los angeles", 7, 500))
print (tripCost("tampa", 6, 500))
