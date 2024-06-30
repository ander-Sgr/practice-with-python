import os

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
                    pass


def add_user_to_state_file(country: str, state: str, full_name: str) -> None:
    output_dir = 'output'
    state_file = os.path.join(output_dir, country, f"{state}.txt")
    if os.path.exists(state_file):
        with open(state_file, 'a') as f:
            f.write(f"{full_name}\n")
    else:
        logging.error(f"El archivo para {state} en {country} no existe.")
