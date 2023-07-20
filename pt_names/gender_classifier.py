"""
# Usage
name_to_search = "Victor"
name_matcher = NameMatcher()
gender = name_matcher.find_name(name_to_search)

if gender is not None:
    print(f"Gender for the name '{name_to_search}' is: {gender}")
else:
    print(f"No matching name found")
"""

import csv
from typing import Optional, Dict
import importlib.resources
from pt_names import data_files

class GenderClassifier:
    """Class to find the gender of a given name by searching in a CSV file.
    """

    def __init__(self, file_name: str = "first_names.csv"):
        self.file_name = file_name
        self.name_data = self._load_name_data()

    def _load_name_data(self) -> Dict[str, str]:
        """
        Load name data from the CSV file into a dictionary.

        Returns:
            Dict[str, str]: A dictionary with names as keys and gender classification as values.
        """
        name_data = {}

        with importlib.resources.open_text(data_files, self.file_name) as csvfile:
            csv_reader = csv.DictReader(csvfile)

            for row in csv_reader:
                name = row["name"]
                classification = row["classification"]
                name_data[name] = classification

        return name_data
    
    def __call__(self, name : str) -> Optional[str]:
        """
        Find the gender of the given name in the CSV file.

        looks only at the first word passed in the name string.

        Args:
            name (str): The name to search for.

        Returns:
            Optional[str]: The gender of the name if found, otherwise None.
        """
        name = name.upper().split(" ")[0].strip()
        return self.name_data.get(name, None)