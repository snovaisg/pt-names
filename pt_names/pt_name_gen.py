"""
This module contains a function for generating random names in Portuguese.
"""
import csv
import random
from unidecode import unidecode
from typing import Optional

class Person:
    def __init__(self, first_name: str, last_name: str, gender: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = self.get_email()
        self.full_name = self.get_full_name()

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_email(self) -> str:
        # Replace spaces in the first name with dots, convert to lowercase, and remove special characters
        first_name = unidecode(self.first_name.replace(" ", ".").lower())
        # Convert last name to lowercase and remove special characters
        last_name = unidecode(self.last_name.replace(" ", ".").lower())
        return f"{first_name}.{last_name}@example.com"

def read_names_from_csv(file_name: str) -> dict:
    names = {"M": [], "F": []}

    with importlib.resources.open_text("pt_name_gen", file_name) as csvfile:
        csv_reader = csv.DictReader(csvfile)
    
        for row in csv_reader:
            name = row["name"]
            classification = row["classification"]
            names[classification].append(name)

    return names

def generate_name(gender: Optional[int] = None) -> str:
    """
    Generates a random name in Portuguese.

    Parameters:
        gender (int): The gender of the name to generate. 0 for male, 1 for female.

    Returns:
        Name: An object containing the generated name.
    """
    names = read_names_from_csv("first_names.csv")
    
    men_names = names["M"]
    women_names = names["F"]

    with importlib.resources.open_text("pt_name_gen", "last_names.csv") as csvfile:
        surnames = [row["last_name"] for row in csv.DictReader(csvfile)]

    try:
        if gender is None:
            gender = random.randint(0, 1)
        first_name = random.choices(men_names if gender == 0 else women_names, k=1)[0]
        last_name = random.choices(surnames, k=1)[0]
        return Person(first_name, last_name, gender)
    except ValueError:
        return "Invalid gender parameter. Please specify 0 for male or 1 for female."
    except IndexError:
        return "An error occurred while accessing the list of names or surnames."
    except Exception as e:
        return f"An error occurred: {e}"
