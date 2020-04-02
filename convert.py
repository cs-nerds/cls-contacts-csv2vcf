#!/usr/bin/env python3

"""
Script that dumps contacts from a csv file into a vcf (VCARD).
VCARDS are easier to use when importing contacts in mobile.
"""

from __future__ import annotations

__author__ = "James (Lemayian) Nakolah"
__version__ = "0.0.20200402"
__runtime__ = "Python=>3.7.0"

import csv
from jinja2 import Environment, FileSystemLoader

class ConConverter:
    """
    Contacts Converter:
        Converts contacts from csv files to vcf.
    """
    def __init__(self: ConConverter, csv_file: str, vcf_file: str) -> None:
        self.__in = csv_file
        self.__out = vcf_file
        self.__data = self.__read_csv_data()
    
    def __read_csv_data(self: ConConverter) -> list:
        """
        Read a cleaned csv file into a dictionary.
        """
        with open(self.__in, mode='r') as infile:
            data = [{header: value for header,value in row.items()}
                    for row in csv.DictReader(infile, skipinitialspace=True)]
            return data
    
    def write_vcf_data(self: ConConverter) -> None:
        """
        Write the contacts data to a vcf (VCARD) file.
        """
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('contact_template.vcf.j2')
        output_from_parsed_template = template.render(contacts=self.__data)
        with open(self.__out, mode='w') as outfile:
            outfile.write(output_from_parsed_template)


if __name__ == "__main__":
    contact_converter = ConConverter('cs_nerds_clean.csv', 'cs_nerds_contacts.vcf')
    contact_converter.write_vcf_data()