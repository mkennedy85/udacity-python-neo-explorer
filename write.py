"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output
    row corresponds to the information in a single close approach from the
    `results` stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
    saved.
    """
    fieldnames = {
                'datetime_utc': 'String date object as UTC',
                'distance_au': 'Distance',
                'velocity_km_s': 'Velocity in km/s',
                'designation': 'Designation',
                'name': 'Name',
                'diameter_km': 'Diameter in km',
                'potentially_hazardous': 'Potentially hazardous',
            }

    with open(filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames.keys())
        writer.writeheader()
        for result in results:
            cad_object = result.serialize()
            row = {
                'datetime_utc': cad_object['datetime_utc'],
                'distance_au': cad_object['distance_au'],
                'velocity_km_s': cad_object['velocity_km_s'],
                'designation': cad_object['neo']['designation'],
                'name': (cad_object['neo']['name'] if cad_object['neo']['name']
                         else 'None'),
                'diameter_km': cad_object['neo']['diameter_km'],
                'potentially_hazardous': ('True' if cad_object['neo']
                                          ['potentially_hazardous']
                                          else 'False'),
            }
            writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is
    a list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
    saved.
    """
    results_output = []
    for result in results:
        results_output.append(result.serialize())

    with open(filename, 'w') as outfile:
        json.dump(results_output, outfile, indent=2)
