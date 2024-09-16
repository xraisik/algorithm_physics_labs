def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"The price of a meal is: ${dollars}\nTip percentage is: {percent * 100}%")
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars: str) -> float:
    dollars = dollars.replace("$", "")
    dollars_float = float(dollars)

    return dollars_float

def percent_to_float(percent: str) -> float:
    percent = percent.replace("%", "")
    percent = float(percent) / 100.

    return percent

if __name__ == "__main__":
    main()