#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Functions to analyze H1B data

Currently, the following data analysis functions are supported:
1. Extract the top N number of certified H1B applications for the input column group
2. Counting the total number of certified H1B applications in the H1B data input file

"""

import logging
from collections import Counter, OrderedDict

__author__ = "Pujaa Rajan"
__email__ = "pujaa.rajan@gmail.com"


def count_top_certified(args, certified_count):
    """
    Extract the top N number of certified H1B applications for the input column group
    @param certified_count:Ò
    @param arguments:
    @return the top N number of certified H1B applications for the input column group sorted by decreasing frequency and
    then alphabetically:
    """
    log = logging.getLogger('H1B_data_analysis.analysis.count_top_certified')
    log.info(f'Counting the top N number of certified H1B applications for the input column group')
    try:
        return Counter(certified_count).most_common(args.top_n)
    except Exception as error:
        log.error(
            f'Error when extracting the top N number of certified H1B applications for the input column group!\n{error}'
            f'\nQuitting now.')
        quit()


def count_total_certified(certified_count):
    """
    Count the total number of certified H1B applications in the H1B data input file
    @param certified_count:
    @return the total number of certified H1B applications in the H1B data input file as an integer:
    """
    log = logging.getLogger('H1B_data_analysis.analysis.count_total_certified')
    log.info(f'Counting the total number of certified H1B applications in the H1B data input file')

    try:
        return sum(certified_count.values())
    except Exception as error:
        log.error(
            f'Error when counting the total number of certified H1B applications in the H1B data input file!\n{error}\n'
            f'Quitting now.')
        quit()
