'''
This script is created to determine whether there is a relationship 
between GDP and the age that developers of a country first start coding.

*make sure to set the localPath variable before running the code
*and put the data files in this path
'''

# imports
import pandas as pd
import seaborn as sns
import scipy.stats as stats
    
# settings
localPath = 'C:/RICHARD/ABN assessment/'   #path where data files are stored
surveyFile = 'survey_results_public.csv'
surveyPath = localPath + surveyFile
gdpFile = 'tec00001_spreadsheet.xlsx'
gdpPath = localPath + gdpFile

# read data
try:
  dfSurvey = pd.read_csv(surveyPath
                       ,delimiter=',')

  dfGdp = pd.read_excel(gdpPath
                      ,sheet_name='Sheet 3'
                      ,header=8
                      ,skipfooter=7
                      ,usecols='A,X')
except IOError:
  print('Could not load the data!')
else:
  print('Data loaded succesfully!')
  
  # clean and transform data
  dfSurveyPart3 = dfSurvey[['ResponseId'
                            ,'Country'
                            ,'LanguageHaveWorkedWith']]
  dfSurvey = dfSurvey[['Country'
                       ,'Age1stCode']]
  dfSurvey['Age1stCode'] = dfSurvey['Age1stCode'].astype('category')
  dfSurvey['Country'] = dfSurvey['Country'].replace('United Kingdom of Great Britain and Northern Ireland', 'United Kingdom')
  
  dfGdp.dropna(inplace=True)
  dfGdp.rename(columns={'TIME': 'Country', '2021': 'Gdp_2021'}, inplace=True)
  dfGdp['Gdp_2021'] = dfGdp['Gdp_2021'].replace(':', None)
  dfGdp['Gdp_2021'] = dfGdp['Gdp_2021'].astype('int64')
  dfGdp['Country'] = dfGdp['Country'].str.replace(r'\(.*\)','')
  dfGdp['Country'] = dfGdp['Country'].str.strip()
  
  # merge data
  dfJoined = pd.merge(dfSurvey, dfGdp, how='left', on='Country')
  dfJoined.dropna(inplace=True)
  
  # plot data
  sns.boxplot(x='Age1stCode', y='Gdp_2021', data=dfJoined, order=['Younger than 5 years'
                                                                  ,'5 - 10 years'
                                                                  ,'11 - 17 years'
                                                                  ,'18 - 24 years' 
                                                                  ,'25 - 34 years'
                                                                  ,'35 - 44 years'
                                                                  ,'45 - 54 years'
                                                                  ,'55 - 64 years'
                                                                  ,'Older than 64 years'])
  
  # create df to investigate groups
  dfCheckGroups =  dfJoined.groupby('Age1stCode').describe()
  
  # ANOVA analysis
  fvalue, pvalue = stats.f_oneway(dfJoined['Gdp_2021'][dfJoined['Age1stCode'] == 'Younger than 5 years'],
                                  dfJoined['Gdp_2021'][dfJoined['Age1stCode'] == '5 - 10 years'],
                                  dfJoined['Gdp_2021'][dfJoined['Age1stCode'] == '11 - 17 years'],
                                  dfJoined['Gdp_2021'][dfJoined['Age1stCode'] == '18 - 24 years'],
                                  dfJoined['Gdp_2021'][dfJoined['Age1stCode'] == '25 - 34 years'],
                                  dfJoined['Gdp_2021'][dfJoined['Age1stCode'] == '35 - 44 years'],
                                  dfJoined['Gdp_2021'][dfJoined['Age1stCode'] == '45 - 54 years'],
                                  dfJoined['Gdp_2021'][dfJoined['Age1stCode'] == '55 - 64 years'],
                                  dfJoined['Gdp_2021'][dfJoined['Age1stCode'] == 'Older than 64 years'])
  print(f'F-value = {fvalue}, p-value = {pvalue}')
  print(['no significant differences between groups!' if pvalue < 0.05 else 'there are significant differences between groups!'])

 

