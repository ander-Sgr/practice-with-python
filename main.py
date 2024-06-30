import sys
from typing import List
from argparse import ArgumentParser, Namespace
import requests
import logging
from Person import Person
from handle_file import *


def parse_args(args: List) -> Namespace:
    parser = ArgumentParser(description="Our first program")
    parser.add_argument('-c', '--count', type=int)
    parser.add_argument('-v', '--verbosity', action='store_true')
    return parser.parse_args(args)


def config_level_logging(verbosity: bool) -> None:
    log_level = logging.WARNING
    if verbosity:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format='%(levelname )s - %(message)s')
    filter_urllib3 = logging.getLogger('urllib3')
    filter_urllib3.setLevel(logging.WARNING)


def get_random_users(count_users: int) -> List:
    logging.debug(f"Getting %d random users", count_users)
    endpoint = f"https://random-data-api.com/api/v2/users?size={count_users}"
    response = requests.get(endpoint, headers={'Accept': 'application/json'})
    logging.info("Code response: %s", response.status_code)
    if response.ok:
        return response.json()
    logging.warning("Error getting random users")
    return RuntimeError("Unable to get response from server")


def load_data_from_json(json_data: str) -> List[Person]:
    logging.debug("Creating object Person")
    persons = []
    for user in json_data:
        person = Person(
            user['last_name'],
            user['first_name'],
            user['address']['country'],
            user['address']['state']
        )
        persons.append(person)
    return persons


def main(args: List):
    parsed_args = parse_args(args)
    logging.debug("Initializing main function")
    config_level_logging(parsed_args.verbosity)
    response_data = get_random_users(parsed_args.count)
    data = load_data_from_json(response_data)
    processed_data = {}
    for person in data:
        logging.warning("%s %s", person.get_full_name(), person.get_location())
        attributes = person.get_attributes()
        country = attributes['country']
        state = attributes['state']
        if country not in processed_data:
            processed_data[country] = []
        if state not in processed_data[country]:
            processed_data[country].append(state)
    create_folder(processed_data)


if __name__ == '__main__':
    main(sys.argv[1:])
