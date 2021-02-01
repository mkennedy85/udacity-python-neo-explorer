"""Extract data on near-Earth objects and close approaches from CSV and
JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth
    objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []

    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            neo = NearEarthObject(designation=row['pdes'],
                                  name=row['name'],
                                  diameter=row['diameter'],
                                  hazardous=row['pha'],)
            neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close
    approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []

    with open(cad_json_path) as infile:
        content = json.load(infile)
        data = content['data']
        fields = {}

        for key in content['fields']:
            fields[key] = content['fields'].index(key)

        for row in data:
            approach = CloseApproach(designation=row[fields['des']],
                                     time=row[fields['cd']],
                                     distance=row[fields['dist']],
                                     velocity=row[fields['v_rel']],)
            approaches.append(approach)
    return approaches
