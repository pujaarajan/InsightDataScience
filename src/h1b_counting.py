#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main file for analyzing H1B data"""

import utilities
import logging
import data
import analysis
import os

__author__ = "Pujaa Rajan"
__email__ = "pujaa.rajan@gmail.com"

if __name__ == '__main__':
    utilities.logger()
    log = logging.getLogger('H1B_data_analysis.main')

    log.info('Beginning to run H1B data analysis code')
    input_args = utilities.parse_arguments()

    h1b_data = data.read_h1b_data(input_args)

    top_certified = analysis.count_top_certified(input_args, h1b_data)
    total_certified = analysis.count_total_certified(h1b_data)

    data.write_h1b_data(input_args, top_certified, total_certified)

    log.info('Finished running H1B data analysis code')
    #log.info(f'See log file here: {os.getcwd()}/H1B_data_analysis.log')
    log.info("Exiting")
