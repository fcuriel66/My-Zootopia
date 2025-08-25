import json

def load_data(file_path):
    """
    load data from json file
    :param file_path:
    :return:
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


#animals_data = load_data("animals_data.json")
#print(animals_data[5]["locations"])

def print_animals(animals_data):
    """
    Extract and prints animal characteristics in desired format
    stated in CODIO
    :param animals_data:
    :return:
    """
    for animal in animals_data:
        print(f"Name: {animal["name"]}")    # Filtered directly as directory
        print(f"Diet: {animal["characteristics"]["diet"]}") # Filtered by directory
                                                            # hierarchy, 1st characteristics
                                                            # and then diet.
        print(f"Location: {animal["locations"][0]}") # Just the first location (0 elem)
        if "type" in animal["characteristics"]: # Print type only if it exist in fox registry
            print(f"Type: {animal["characteristics"]["type"]}")
        else:
            print()
            continue
        print()

def main():
    animals_data = load_data("animals_data.json")
    print_animals(animals_data)

if __name__ == "__main__":
    main()

