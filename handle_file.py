import os
from typing import List

from Person import Person


def create_folder(data: dict[str, str]) -> None:
    output_dir = 'output'

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for country, states in data.items():
        country_dir = os.path.join(output_dir, country)
        if not os.path.exists(country_dir):
            os.mkdir(country_dir)
        for state in states:
            state_file = os.path.join(country_dir, f"{state}.txt")
            if not os.path.exists(state_file):
                with open(state_file, 'w') as f:
                    f.write(f"Información sobre {state}\n")
