year = int(input("Enter your birth year: "))

if year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiac = [
        "Rat)",
        "Ox",
        "Tiger",
        "Rabbit",
        "Dragon",
        "Snake",
        "Horse",
        "Goat",
        "Monkey",
        "Rooster",
        "Dog",
        "Pig"
    ]

    sign = zodiac[(year - 1900) % 12]

    print("Your Chinese Zodiac Sign is :", sign)