import csv
import random

def is_holiday(month, day):
    # Public holidays
    if (month, day) in [(1, 1), (12, 25), (12, 26)]:
        return True
    # School holidays (rough estimates)
    if (3, 25) <= (month, day) <= (4, 15):
        return True
    if (7, 20) <= (month, day) <= (9, 5):
        return True
    if (10, 25) <= (month, day) <= (11, 5):
        return True
    if (12, 20) <= (month, day) <= (1, 5):
        return True
    return False

def get_temperature(month):
    # Rough seasonal temperatures for the UK
    if month in [12, 1, 2]:
        return random.randint(0, 10)  # Winter
    elif month in [3, 4]:
        return random.randint(5, 15)  # Spring
    elif month in [5, 6, 7, 8, 9]:
        return random.randint(10, 25)  # Summer
    else:
        return random.randint(5, 15)  # Autumn

def get_number_of_guides(temperature, holiday):
    if 20 <= temperature <= 30:
        guides = random.randint(14, 18)
        if holiday:
            guides += random.randint(0, 4)  # up to 22
    elif temperature > 30:
        guides = random.randint(10, 14)
    else:
        guides = random.randint(8, 14)
    return guides

def main():
    start_year = 2023

    with open("river_tour_data.csv", "w", newline='') as csvfile:
        fieldnames = ["Date", "Temperature", "Holiday", "Number of river tour guides"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for month in range(1, 13):
            for day in range(1, 32):
                if month in [4, 6, 9, 11] and day > 30:
                    continue
                if month == 2 and day > 28:  # This doesn't account for leap years. Adjust if needed.
                    continue

                temperature = get_temperature(month)
                holiday = is_holiday(month, day)
                
                writer.writerow({
                    "Date": f"{start_year}-{month:02d}-{day:02d}",
                    "Temperature": temperature,
                    "Holiday": holiday,
                    "Number of river tour guides": get_number_of_guides(temperature, holiday)
                })

if __name__ == "__main__":
    main()
