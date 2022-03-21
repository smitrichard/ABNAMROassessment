# ABNAMROassessment

General

This file contains explanation to the assessment that has been given to me. Next to this file there are specific files for each of the parts of the assessment, they will be mentioned as I will elaborate on each specific part.
For the GDP data I decided to use Eurostat as data provider since a link to the data was provided in the assessment. In this file there were 3 sheets with different units of measure (euro per capita, million purchasing power standards and million euro). For this assessment i chose to use GDP in million euro.
Both data files have been downloaded and added to the repo.

Part 1

Question:
Determine whether there is a relationship between GDP and the age that developers of a country first start coding. Extract and create one or more tables to store the data necessary to perform this comparison. Use a visual plot to support your conclusion(s).

Solution:
For this question and the data included I noticed this would be a yearly analysis and that the data-files could potentially be different every year. Looking at the business needs i identyfied, I believe it would make most sense to provide a custom solution since this code would be ran only once (a year). 
Therefore I have provided a python script to perform the following steps:
-	Read both data files

i used the pandas library to load the data and made sure the rest of the script would not run in case of an error loading one of the files.
-	Transform the data

using the pandas library i transformed and cleaned the data to only include the information relevant to awnser the question.
- Checking the variables

in order to evaluate GDP by age groups i created a dataframe to store descriptive values by group.
-	Visualize the data

to visualize the data i used the seaborn library to create a boxplot of GDP by age group. i included the plot as a picture in the repo.
-	Scientific analysis*

using the scipy.stats library i performed an ANOVA test to compare GDP by age groups, no significant differences were found.

*Based on the visualization it was clear there is no relationship between GDP and age. Looking at the distribution of the age groups it was clear that it did not match the requirements for an ANOVA test(to look for significant differences between groups), however for the assignment I included the ANOVA test to showcase it.

Files:
-	part1.py
-	survey_results_public.csv
-	tec00001_spreadsheet.xlsx
-	boxplot_gdp-age.png

Part 2

Question:
Create a REST web service that exposes a single method to return both the GDP and youngest coding age range, using the table(s) defined in Part 1, when the ISO code of a country is supplied as input. Suggest at least 2 ways that the scalability of this service can be increased.

Solution:
For this question I used Visual Studio to build an REST web service with ASP.NET Core. In Visual Studio i created a new project and select: ASP.NET Core Web API. This automaticcaly comes with a pre defined weatherforecast API which needs to be changed to your specific requirements, which can be done by editing the Program.cs file.

To make it a custom solution i identified the following steps:
-	Configure endpoints

the endpoint: GET /ISOcountrycode should return the youngest age group and corresponding mean GDP value
-	Setup a connection to the data

This usually involves creating a connection string with the information of the database and authentication.

Files:
-	in Folder ABNpart2

Part 3

Question:
Load the survey results into a SQL table and write a pivot query to list the number of developers by country for the top 3 programming languages. As a random example, the output could look like:

Country	C++	Python	HTML/CSS

Afghanistan	1	0	23

…	…	…	…

Zimbabwe	0	12	34


Solution:
To answer this question I identified 3 main steps that need to be done:
1) I noticed that the way the relevant data about programming languages (column: “LanguageHaveWorkedWith”) is stored needed to be changed. Multiple values are stored in 1 column, I chose to transform the data so that each value was stored in a separate row.
2) After step 1 a query could be written to identify the top 3 most used programming languages.
3) With the top 3 programming languages known from step 2, i created a pivot table to provide the output needed from the main question. 

I created a SQL script that includes 3 queries for all the 3 steps mentioned. I also included a .bak file to restore the database i created locally for this part of the assessment. I manually imported the survey file into the database and stored is as 'surveytable'.

Files:
-	Part3.sql
-	assessment.zip

