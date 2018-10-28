#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#

#python3 ./src/h1b_counting.py --help

# Test Data

python3 ./src/h1b_counting.py --input_file ./input/h1b_input.csv --output_file ./output/top_10_occupations.txt --top_n 10 --input_column SOC_NAME --status_column CASE_STATUS --output_column TOP_OCCUPATIONS
python3 ./src/h1b_counting.py --input_file ./input/h1b_input.csv --output_file ./output/top_10_states.txt --top_n 10 --input_column WORKSITE_STATE --status_column CASE_STATUS --output_column TOP_STATES


# 2014 Input Data

#python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2014.csv --output_file ./output/top_10_occupations.txt --top_n 10 --input_column LCA_CASE_SOC_NAME --status_column STATUS --output_column TOP_OCCUPATIONS

#python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2014.csv --output_file ./output/top_10_states.txt --top_n 10 --input_column LCA_CASE_WORKLOC1_STATE --status_column STATUS --output_column TOP_STATES


# 2015 Input Data

#python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2015.csv --output_file ./output/top_10_occupations.txt --top_n 10 --input_column SOC_NAME --status_column CASE_STATUS --output_column TOP_OCCUPATIONS

#python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2015.csv --output_file ./output/top_10_states.txt --top_n 10 --input_column WORKSITE_STATE --status_column CASE_STATUS --output_column TOP_STATES

# 2016 Input Data

#python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2016.csv --output_file ./output/top_10_occupations.txt --top_n 10 --input_column SOC_NAME --status_column CASE_STATUS --output_column TOP_OCCUPATIONS

#python3 ./src/h1b_counting.py --input_file ./h1b_statistics/input/H1B_FY_2016.csv --output_file ./output/top_10_states.txt --top_n 10 --input_column WORKSITE_STATE --status_column CASE_STATUS --output_column TOP_STATES
