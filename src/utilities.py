#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Utilities for analyzing H1B data"""

import argparse
import logging

__author__ = "Pujaa Rajan"
__email__ = "pujaa.rajan@gmail.com"


def logger():
    """
    Create and format logger that logs to file and console
    @return None:
    """
    logger = logging.getLogger('H1B_data_analysis')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('H1B_data_analysis.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with the same log level
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info('Finished creating logger')


def parse_arguments():
    """
    Define and parse input arguments
    @return: Input arguments
    """
    log = logging.getLogger('H1B_data_analysis.utilities.parse_arguments')
    log.info("Beginning to parse input arguments")

    parser = argparse.ArgumentParser(
        description='Return the top 10 categories (e.g. occupations, states) with the most certified visa applications')

    parser.add_argument('--input_file', required=True, action="store", default=None, help='Input file full path')
    parser.add_argument('--output_file', required=True, action='store', default=None, help='Output file full path')
    parser.add_argument('--input_column', required=True, action="store", default=None,
                        help='Input file column to group by and analyze (e.g. LCA_CASE_SOC_NAME, LCA_CASE_WORKLOC1_STATE)')
    parser.add_argument('--status_column', required=True, action="store", default=None,
                        help='Input file status column to count number certified (e.g. STATUS, CASE_STATUS)')
    parser.add_argument('--output_column', required=True, action="store", default=None,
                        help='Output file column header name (e.g. TOP_STATES, TOP_OCCUPATIONS')
    parser.add_argument('--top_n', required=False, action='store', default=10, type=int,
                        help='Return the top n categories (e.g. occupations, states) with the most certified visa applications')
    parser.add_argument('--delimiter', required=False, action='store', default=';',
                        help='Delimiter of the input and output file (used when reading and writing files)')

    try:
        input_arguments = parser.parse_args()

        log.info('Reading input arguments')
        log.info('Input file:{input_arguments.input_file}')
        log.info('Output file: {input_arguments.output_file}')
        log.info('Top N rows: {input_arguments.top_n}')
        log.info('Input column: {input_arguments.input_column}')
        log.info('Status column: {input_arguments.status_column}')
        log.info('Output column: {input_arguments.output_column}')
        log.info('Finished reading input arguments')

        return input_arguments

    except Exception as error:
        log.exception('Error when parsing input arguments!\nQuitting now.')
        parser.error(str(error))
        log.error('Quitting')
        quit()
