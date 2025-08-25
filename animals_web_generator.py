import json

def load_data(file_path):
    """
    load data from json file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html(file_name):
    """
       read a html file
    """
    with open(file_name, "r") as handle:
        html_text = handle.read()
        return html_text


def write_html(html_text, file_name):
    """
    write an html file
    """
    with open(file_name, "w") as handle:
        handle.write(html_text)


def generate_string(animals_data):
    output = ""     # define empty string
    for animal in animals_data:
        # append info to each string of info
        output += f"Name: {animal["name"]}\n"
        output += f"Diet: {animal["characteristics"]["diet"]}\n"
        output += f"Location: {animal["locations"][0]}\n"
        # add data of type value only if it exist in orig. data
        if "type" in animal["characteristics"]:
            output += f"Type: {animal["characteristics"]["type"]}\n"
        else:
            continue
    return output


def main():
    animals_data = load_data("animals_data.json")
    animals_string = generate_string(animals_data)
    html_template = read_html("animals_template.html")
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_string)
    write_html(new_html,"animals_data.html")

if __name__ == "__main__":
    main()
