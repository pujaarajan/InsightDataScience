#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Functions to read and write H1B data"""

import logging
import csv
from collections import Counter, OrderedDict

__author__ = "Pujaa Rajan"
__email__ = "pujaa.rajan@gmail.com"


def read_h1b_data(args):
    """
    Read H1B data and count the number of certified applications for the input column group
    @param args:
    @return Dictionary of H1B data where the keys are the input column and the values are the counts. This dictionary is
    sorted by decreasing frequency and then alphabetically:
    """
    log = logging.getLogger('H1B_data_analysis.data.read_h1b_data')
    log.info('Beginning to read H1B data from {args.input_file}')

    try:
        certified_count = Counter()

        with open(args.input_file, newline='') as input_file:
            log.info('Opened H1B data input file')
            reader = csv.DictReader(input_file, delimiter=args.delimiter, quoting=csv.QUOTE_MINIMAL, skipinitialspace=True,
                                    escapechar='\\')
            for line in reader:
                if line[args.status_column] == 'CERTIFIED':
                    group_certified = line[args.input_column]
                    # Increase count by one for each person in the column group who was certified
                    certified_count[group_certified] += 1
        log.info('Finished reading in H1B data input file')
        log.info('Sorting the list firstÒ by decreasing frequency and then alphabetically')
        sorted_counts = OrderedDict(sorted(certified_count.items(), key=lambda item: (-item[1], item[0])))
        log.info('Finished counting certified H1B applications')
        return sorted_counts
    except Exception as error:
        log.error(
            'Error when reading H1B data and counting the number of certified applications for the input column group!'
            '\n{error}\nQuitting now.')
        quit()


def write_h1b_data(args, top_certified, total_certified):
    """
    Write the H1B data analysis to output files
    @param args:
    @param top_certified:
    @param total_certified:
    @return Nothing is returned. You can find the H1B data analysis is in the output files.:
    """

    try:
        log = logging.getLogger('H1B_data_analysis.data.write_h1b_data')
        log.info('Beginning to write H1B data output file to {args.output_file}')
        with open(args.output_file, 'w', newline='') as output_file:
            log.info('Opened H1B data output file')
            fieldnames = [args.output_column, 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter=args.delimiter, skipinitialspace=True)
            writer.writeheader()
            for key, value in top_certified:
                writer.writerow({args.output_column: key, 'NUMBER_CERTIFIED_APPLICATIONS': value,
                                 'PERCENTAGE': '{:.1%}'.format(value / total_certified)})
        log.info('Finished writing H1B data output file to {args.output_file}')
    except Exception as error:
        log.error(
            'Error when writing the H1B data analysis to output files!\n{error}\nQuitting now.')
        quit()
