def main():
    start_miles = float(input("\nEnter the first odometer reading (miles): "))
    end_miles = float(input("\nEnter the second odometer reading (miles): "))
    amount_gallons = float(input("\nEnter the amount of fuel used (gallons): "))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    lp100k = lp100k_from_mpg(mpg)

    print(f"\n{mpg:.1f} miles per gallon")
    print(f"\n{lp100k:.2f} liters per 100 kilometers\n")


def miles_per_gallon(start, end, gallons):

    mpg = abs(end - start) / gallons

    return mpg


def lp100k_from_mpg(mpg):

    lp100k = 235.215 / mpg

    return lp100k

main()