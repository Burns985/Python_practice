import json
import csv
import time
import math
import threading


class Driver:
    def __init__(self, name, latitude, longitude, max_orders=1):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.max_orders = max_orders
        self.orders = []  # A list to track the driver's current orders


class Restaurant:
    def __init__(self, name, address, latitude, longitude, drivers, menu):
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.drivers = [Driver(f"{name}_driver{i + 1}", latitude, longitude) for i in range(drivers)]
        self.menu = menu


class RestaurantList:
    def __init__(self):
        self.restaurants = {}

    def add_restaurant(self, restaurant):
        self.restaurants[restaurant.name] = restaurant


class Util:
    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2):
        R = 3958.8  # Radius of Earth in miles

        # Convert latitude and longitude from degrees to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # Haversine formula
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c  # Distance in miles
        return distance

    @staticmethod
    def deliver_order(driver, order):
        restaurant_name = order.restaurant_name
        food = order.food
        order_time = order.order_time

        # Calculate distance from driver to restaurant
        distance_to_restaurant = Util.calculate_distance(driver.latitude, driver.longitude,
                                                         main.restaurant_list.restaurants[restaurant_name].latitude,
                                                         main.restaurant_list.restaurants[restaurant_name].longitude)

        # Calculate delivery time and return time in seconds
        delivery_time = int(distance_to_restaurant * 3600)  # 1 mile per second
        return_time = delivery_time

        # Simulate delivery
        time.sleep(delivery_time)
        print(f"[{time.strftime('%H:%M:%S')}] {driver.name} picked up {food} from {restaurant_name}!")

        # Simulate return to restaurant
        time.sleep(return_time)
        print(f"[{time.strftime('%H:%M:%S')}] {driver.name} completed delivery of {food} to {restaurant_name}!")


class Order:
    def __init__(self, order_time, restaurant_name, food):
        self.order_time = order_time
        self.restaurant_name = restaurant_name
        self.food = food


class Main:
    def __init__(self):
        self.restaurant_list = RestaurantList()

    def load_restaurants(self, filename):
        # Load restaurant information from JSON file
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for restaurant_data in data['data']:
                    restaurant = Restaurant(
                        restaurant_data['name'],
                        restaurant_data['address'],
                        restaurant_data['latitude'],
                        restaurant_data['longitude'],
                        restaurant_data['drivers'],
                        restaurant_data['menu']
                    )
                    self.restaurant_list.add_restaurant(restaurant)
        except FileNotFoundError:
            print("Restaurant file not found. Exiting.")
            exit(1)
        except json.JSONDecodeError:
            print("Invalid JSON format in restaurant file. Exiting.")
            exit(1)

    def load_schedule(self, filename):
        # Load schedule information from CSV file
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                schedule = [line for line in reader]
                # Strip leading and trailing whitespace from restaurant names
                schedule = [(order_time, restaurant_name.strip(), food) for order_time, restaurant_name, food in
                            schedule]
        except FileNotFoundError:
            print("Schedule file not found. Exiting.")
            exit(1)
        return schedule

    def start_program(self, schedule, latitude, longitude):
        drivers = []

        print("Starting execution of program...")

        for order_info in schedule:
            order_time, restaurant_name, food = order_info
            order_time = int(order_time)

            # Find an available driver for the order
            driver = self.find_available_driver(restaurant_name)

            # If no available driver, wait for one to become available
            while driver is None:
                time.sleep(1)
                driver = self.find_available_driver(restaurant_name)

            # Add the order to the driver's orders list
            driver.orders.append(Order(order_time, restaurant_name, food))

            # Start a thread to handle the order delivery
            order_thread = threading.Thread(
                target=Util.deliver_order,
                args=(driver, driver.orders[-1])  # Get the most recent order for the driver
            )
            drivers.append(order_thread)
            order_thread.start()

        for driver in drivers:
            driver.join()

        print("All orders complete!")

    def find_available_driver(self, restaurant_name):
        # Find an available driver for the given restaurant
        restaurant = self.restaurant_list.restaurants[restaurant_name]
        for driver in restaurant.drivers:
            if len(driver.orders) < driver.max_orders:
                return driver
        return None


if __name__ == "__main__":
    main = Main()

    # Get input filenames
    restaurants_file = input("What is the name of the file containing the restaurant information? ")
    schedule_file = input("What is the name of the file containing the schedule information? ")

    # Get user's current location
    latitude = float(input("What is the latitude? "))
    longitude = float(input("What is the longitude? "))

    main.load_restaurants(restaurants_file)
    schedule = main.load_schedule(schedule_file)
    main.start_program(schedule, latitude, longitude)
