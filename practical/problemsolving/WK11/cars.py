# Practical 11 - Cars
# liusy088
#

def load_cars():
    """Load and return a list of cars data using dictionary."""
    cars = []
    try:
        with open("cars.txt") as in_file:
            for line in in_file:
                parts = line.strip().split()
                car = {
                    "make": parts[0],
                    "model": parts[1],
                    "year": int(parts[2]),
                    "doors": int(parts[3]),
                    "seats": int(parts[4]),
                    "kms": int(parts[5])
                }
                cars.append(car)
    except FileNotFoundError:
        pass
    return cars


def print_cars(cars):
    """Print the list of cars in a table format."""
    if not cars:
        print("No cars available.")
        return

    print(f"{'Make':<10} {'Model':<10} {'Year':>5} {'Doors':>6} {'Seats':>6} {'Kms':>8}")
    for car in cars:
        print(
            f"{car['make']:<10} {car['model']:<10} {car['year']:>5} {car['doors']:>6} {car['seats']:>6} {car['kms']:>8}")


def find_cars(cars, key, value):
    """Find and return a new list of cars with matching key value."""
    matched_cars = []
    for car in cars:
        if key in car:
            if car[key] == value:
                matched_cars.append(car)
    return matched_cars


def sort_cars(cars, key):
    """Sort cars in the list with key and return True if successful."""
    if not cars or key not in cars[0]:
        return False
    cars.sort(key = lambda car: car[key])
    return True


def main():
    """Main function to run at start."""
    cars = load_cars() # load car records from input file

    command = ''
    while command != 'quit':
        print() # Print an empty line.

        # Get user intput of the command to run.
        command = input("Command [print, find, sort, quit]: ")

        # Print command.
        if command == 'print':
            print_cars(cars)

        # Find command.
        elif command == 'find': 
            # Get user input of field and value for searching.
            field = input('Field: ')
            value = input('Value: ')

            # Convert the value to int if numeric.
            if value.isnumeric():
                value = int(value)
            
            # Find cars matching the field value and print.
            result = find_cars(cars, field.lower(), value)
            print_cars(result)

        # Sort command.
        elif command == 'sort':
            # Get user input of field to sort with.
            field = input('Sort by which field? ')

            # Sort the cars in key
            success = sort_cars(cars, field.lower())
            if success:
                print("Sorted the cars in:", field.capitalize())
            else:
                print("Cannot sort the cars with:", field)
        
    print("Good bye!")

# Start with running the main function.
main()
