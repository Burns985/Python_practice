import calendar
import datetime


def print_day(date):
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    print(day_name[day])


def print_year(year):
    cal = calendar.TextCalendar()
    year_calendar = cal.formatyear(year)
    print(year_calendar)


def print_month(month, year):
    cal = calendar.TextCalendar()
    year_calendar = cal.formatmonth(year, month)
    print(year_calendar)


def get_valid_date_input():
    while True:
        date_input = input('Enter the date (e.g: 25 07 2023): ')
        try:
            datetime.datetime.strptime(date_input, '%d %m %Y')
            return date_input
        except ValueError:
            print("Invalid date format. Please enter the date in the format 'dd mm yyyy'.")


def get_valid_year_input():
    while True:
        year_input = input('Enter the year: ')
        if year_input.isdigit() and int(year_input) > 0:
            return int(year_input)
        else:
            print("Invalid year. Please enter a valid year (a positive integer).")


def get_valid_month_input():
    while True:
        month_input = input('Enter the month (1-12): ')
        if month_input.isdigit():
            month = int(month_input)
            if 1 <= month <= 12:
                return month
            else:
                print("Invalid month. Please enter a month between 1 and 12.")
        else:
            print("Invalid input. Please enter a valid month (a positive integer).")


def main():
    try:
        while True:
            print()
            choice = input("1. Print day of the week\n"
                           "2. Print calendar for a year\n"
                           "3. Print calendar for a month\n"
                           "4. Exit\n"
                           "Enter your choice: ")

            if choice == '1':
                date_input = get_valid_date_input()
                print_day(date_input)
            elif choice == '2':
                year_input = get_valid_year_input()
                print_year(year_input)
            elif choice == '3':
                month_input = get_valid_month_input()
                year_input = get_valid_year_input()
                print_month(month_input, year_input)
            elif choice == '4':
                print("Thank you for using our program!\n"
                      "Have a lovely rest of the day.\n"
                      "Exiting program...")
                break
            else:
                print("Invalid choice. Please select a valid option (1/2/3/4).")
    except KeyboardInterrupt:
        print("\n\nNice try buddy...")


if __name__ == "__main__":
    main()