# Insight Data Engineering Fellows Assignment
# H1B Data Analysis

## Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run](README.md#Run)
4. [Input Data](README.md#input-data)
5. [Output Data](README.md#output-data)
6. [Tests](README.md#tests)
7. [Future Work](README.md#future-work)
8. [Questions?](README.md#questions?)

## Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

The problem I am trying to solve is:
1. To create a mechanism to analyze past years data, specifically calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.
2. To reuse the mechanism to analyze data for the year 2019 without needing to change the code.

You can read more about my solution here in [Approach](README.md#approach).

Requirements:
2. The README.md should include Problem, Approach, and Run sections.
4. Project follows specified directory structure.
1. The code is modular and reusable for future.
3. The code scales for a large amount of data.
5. Code is clean, well-tested, well-documented, and well-commented.
6. The output should only have 10 lines, even when there are ties in the count.
7. The output should have less than 10 lines if there are fewer than 10 groups of data.

## Approach

While each of these steps are in their respective files noted below, the functions are called in this order in h1b_counting.py. i did this because it makes the code more modular, and easy to add to. Using this structure, if someone wanted to add the capability to read in additional data sets, they can add it to the data.py file. Or if they wanted to add more analyses, then they can add it to analysis.py. Here are the steps of my approach:

**1. Set up logging and parse input arguments. See [utilities.py](https://github.com/pujaarajan/InsightDataScience/blob/master/src/analysis.py).**

First, I set up useful utilities, including logging and an argument parser, for analyzing H1B data. It is my personal preference to log every step. You see the logging printed to the console and printed to the H1B_data_analysis.log in the main project directory.

The required and optional input arguments are listed below followed by their rationale.

| Input Parameter | Description | Example | Required? | Default |
| --- | --- | --- | --- | --- |
| --input_file | Input file full path | ./h1b_input.csv | Yes | N/A |
| --output_file | Output file full path | ./top_10_occupations.csv | Yes | N/A |
| --input_column | Return the top n categories (e.g. occupations, states) with the most certified visa applications | ./top_10_occupations.csv | Yes |  N/A |
| --status_column | Input file status column to count number certified | STATUS or CASE_STATUS | Yes |  N/A |
| --output_column | Input file column to group by and analyze | LCA_CASE_SOC_NAME | Yes |  N/A |
| --top_n | Output file column header name | 100 | No |  10 |
| --delimiter | Delimiter of the input and output file used when reading and writing files | , | No | ; |

I added this because I don't believe it is good practice to hardcode integer values. With this additional argument, we can return any number of results. If you don't specify a value, then it defaults to 10.
e.  -  In the future, if we want to read and write using different delimiters, we could add an additional parameter for this. I added this as an optional input argument in case future H1B data files use a different delimiter.

The column name inputs, top_n, and delimiter options allow the code to be reusable and used year after year even with different file formats. For example, status is not hardcoded. This column is crucial for the analysis because we need this column to know if a person was certified or not. This column was also named differently in the 2014 and the 2015 data sets. Based on that pattern, I extracted the name using regex to just grab the column that says status in it anywhere. All the columns are user inputs because column names can change year to year. There's evidence of this in the provided sample input files in the google drive above. I considered using regex to search for the correct column, but having these be user inputs, ensures the right column is selected.

**2. Read input data and count the number of certified applications for the input column group. See [data.py](README_GIVEN.md#data.py)**

I created a dictionary of H1B data where the keys are the input column and the values are the counts. This dictionary is sorted by decreasing frequency and then alphabetically.

**3. Perform data analysis. See [analysis.py](https://github.com/pujaarajan/InsightDataScience/blob/master/src/analysis.py).**

Currently, the following data analysis functions are supported:
1. count_top_certified - Extract the top N number of certified H1B applications for the input column group
2. count_total_certified - Counting the total number of certified H1B applications in the H1B data input file

**4. Write data. See [data.py](https://github.com/pujaarajan/InsightDataScience/blob/master/src/data.py).**

Write the H1B data analysis to output files.

## Run

1. Clone Github repo. `git clone https://github.com/pujaarajan/h1b_statistics.git`
2. Change directory to project folder. `cd h1b_statistics`
3. Run the help command to understand the input arguments: `python3 ./src/h1b_counting.py --help`
4. Run this command after replacing variables. See below for example commands: `python3 ./src/h1b_counting.py --input_file <var> --output_file <var> --top_n <var> --input_column <var> --status_column <var> --output_column <var>`

### Example Run Command using the data in the input folder
```shell
python3 ./src/h1b_counting.py --input_file ./input/h1b_input.csv --output_file ./output/top_10_states.txt --input_column WORKSITE_STATE --status_column CASE_STATUS --output_column TOP_STATES
./src/h1b_counting.py --input_file ./input/h1b_input.csv --output_file ./output/top_10_occupations.txt --input_column SOC_NAME --status_column CASE_STATUS --output_column TOP_OCCUPATIONS
```

### Run Commands for 2014 Input Data
```shell
python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2014.csv --output_file ./output/top_10_occupations.txt --input_column LCA_CASE_SOC_NAME --status_column STATUS --output_column TOP_OCCUPATIONS
python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2014.csv --output_file ./output/top_10_states.txt --input_column LCA_CASE_WORKLOC1_STATE --status_column STATUS --output_column TOP_STATES
```

### Run Commands for 2015 Input Data
```shell
python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2015.csv --output_file ./output/top_10_occupations.txt --input_column SOC_NAME --status_column CASE_STATUS --output_column TOP_OCCUPATIONS
python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2015.csv --output_file ./output/top_10_states.txt --input_column WORKSITE_STATE --status_column CASE_STATUS --output_column TOP_STATES
```

### Run Commands for 2016 Input Data
```shell
python3 ./src/h1b_counting.py --input_file ./input/H1B_FY_2016.csv --output_file ./output/top_10_occupations.txt --input_column SOC_NAME --status_column CASE_STATUS --output_column TOP_OCCUPATIONS
python3 ./src/h1b_counting.py --input_file ./h1b_statistics/input/H1B_FY_2016.csv --output_file ./output/top_10_states.txt --input_column WORKSITE_STATE --status_column CASE_STATUS --output_column TOP_STATES
```

## Input Data

Raw data could be found [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension). I used the converted the Excel files into a semicolon separated (";") format and placed them into this Google drive [folder](https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf?usp=sharing). I tested your code on the files provided on the Google drive an

I also created 6 extra test data files you will see in the insight_testsuite. Each year of data can have different columns, so I made sure to test that my program could handle that in my test data. It's for this reason, column names are required as inputs to the program.

## Output Data

My program currently creates 2 output files:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications

Each line of the `top_10_occupations.txt` file contains fields in this order:
1. __`TOP_OCCUPATIONS`__: Occupation name associated with an application's Standard Occupational Classification (SOC) code
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for that occupation. An application is considered certified if it has a case status of `Certified`
3. __`PERCENTAGE`__: % of applications that have been certified for that occupation compared to total number of certified applications regardless of occupation. 

Each line of the `top_10_states.txt` file contains these fields in this order:
1. __`TOP_STATES`__: State where the work will take place
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for work in that state. An application is considered certified if it has a case status of `Certified`
3. __`PERCENTAGE`__: % of applications that have been certified in that state compared to total number of certified applications regardless of state.

Each line holds one record and each field on each line is separated by a semicolon (;) by default, but you can change the delimiter used for reading and writing using the optional delimiter input argument.
Percentages are rounded off to 1 decimal place. For instance, 1.05% should be rounded to 1.1% and 1.04% should be rounded to 1.0%. Also, 1% should be represented by 1.0%
The records in both files are sorted by __`NUMBER_CERTIFIED_APPLICATIONS`__ field, and in case of a tie, alphabetically by __`TOP_XXXXX`__. 
There, however, should not be more than 10 lines in each file. In case of ties, only list the top 10 based on the sorting instructions given above. This is tested by test_1.
Depending on the input, there may be fewer than 10 lines in each file. This is tested by test_2.

## Tests

I created 4 tests to test a variety of cases described below. I found a bug in run_tests.sh. See run_tests.sh lines 65-67.

1. test_1 - Given
2. your_own_test_1 - Tests if # output rows < 10 when # input data rows < 10
3. your_own_test_2 - Tests what happens if the input file only has a header row with no data
4. your_own_test_3 - Tests what happens if input file is empty

I also manually tested the code using the H1B_FY_2014.csv, H1B_FY_2015.csv, and H1B_FY_2016.csv from the Google Drive. See Run section for commands.

## Future Work

If I had more time, then I would work on the following:

1. Add a debug mode. I currently log everything on all runs which makes the console output lengthy, and sometimes hard to follow. 
2. I would log the number of lines in each file that's read in and sample outputs in the console to help debug.
3. I would create multiple run options so that you can run multiple analysis (e.g. occupations, states) at the same time.

## Questions

Contact Pujaa Rajan and pujaa.rajan@gmail.com. 
