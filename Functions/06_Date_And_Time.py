def calculate_seconds(days, hours, minutes, seconds):
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
    return total_seconds

def main():
    days = int(input("Enter the number of days: "))
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    total_seconds = calculate_seconds(days, hours, minutes, seconds)

    print("Total Seconds:", total_seconds)

main()
