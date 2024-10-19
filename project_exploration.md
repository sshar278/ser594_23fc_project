#### File to document all progress, findings, and challenges faced. Essential to explain the choices made in data processing and visualization.

### Note : The generated merged_data.db can be viewed using the sqlite db browser. This contains all the cleaned and processed data. Also run the core.py file in order to view each and every result

SERX94: Exploratory Data Munging and Visualization

TITLE : Exploring Election Data : Munging and Visual Insights

AUTHOR : Siddharth Sharma

DATE : 21 Oct, 2024

BASIC QUESTIONS : 

Dataset #1 : US Elections Poll 2020 - Qriously.csv

Dataset Author : Brandwatch qriously
Dataset Construction Date: 15 - 19 October, 2020
Dataset Record Count: 3523 rows, 21 columns

Dataset Field Meanings: 
Headline vote share: The candidate supported by the voter (e.g., Joe Biden, Donald Trump).
NCHS Urban_rural: Indicates if the voter resides in an urban, suburban, or rural area.
Start time: Date and time when the survey response was recorded.
How old are you?: Age range of the respondent (e.g., 55-64, 65+).
Are you: Gender of the respondent.
Highest degree completed: Education level attained by the respondent.
Current employment status: The respondent’s employment situation (e.g., working full-time, retired).
Yearly household income: Household income range from the previous year.
State: U.S. state where the respondent resides.
Region: The geographic region (e.g., Northeast, Midwest) of the respondent.
Kind of work: The industry or type of work the respondent does (e.g., industrial, healthcare).
Race/Ethnicity: The race or ethnicity of the respondent.

Dataset File Hash : ae4c7a6bc9597384a255f3f12d9fd909
URL(s) : https://www.brandwatch.com/qriously-data/us-election-poll-week-8-15-19-oct/
https://public.graphext.com/dbdadf87a5c21695/index.html?section=data 



Dataset #2 : 1976-2020-senate.csv

Dataset Author : MIT Election Data + Science Lab
Dataset Construction Date: 27 November, 2023
Dataset Record Count: 3629 rows, 19 columns

Dataset Field Meanings: 
year: The election year (e.g., 1976).
state: The name of the U.S. state where the election took place (e.g., ARIZONA).
state_po: The two-letter postal abbreviation of the state (e.g., AZ).
state_fips: Federal Information Processing Standard code for the state (numeric code to identify U.S. states).
state_cen: Census code for the state, often used for administrative purposes.
state_ic: Another internal code that may relate to state identification for official purposes.
office: The type of political office being contested (e.g., US SENATE).
district: The district where the election took place (for statewide races, this may be listed as “statewide”).
stage: The stage of the election (e.g., general election or primary, indicated by "gen").
special: Indicates if the election was a special election (TRUE/FALSE).
candidate: The name of the candidate running for office (e.g., SAM STEIGER).
party_detailed: The detailed political party of the candidate (e.g., REPUBLICAN, INDEPENDENT).
writein: Indicates if the candidate was a write-in candidate (TRUE/FALSE).
mode: The mode of the election (e.g., "total" indicating total votes counted).
candidatevotes: The total number of votes the candidate received.
totalvotes: The total number of votes cast in the election for that particular office.
unofficial: Whether the results are official or unofficial (TRUE/FALSE).
version: The version of the dataset or data update (e.g., 20210114).
party_simplified: The simplified party affiliation (e.g., REPUBLICAN, OTHER).

Dataset File Hash : 8bcb59d61b53a216b2ab4fa368efb4cd
URL : https://dataverse.harvard.edu/file.xhtml?fileId=7609736&version=7.0&toolType=PREVIEW



Dataset #3 : Turnout_1980_2022_v1.1.csv

Dataset Author: Micheal Mcdonald, University of Florida Election Lab
Dataset Construction Date: January 15, 2024
Dataset Record Count: 1144 rows, 15 columns

Dataset Field Meanings:
YEAR: The year of the election (e.g., 2022).
STATE: The name of the U.S. state (or "United States" for the whole country).
STATE_ABV: The two-letter postal abbreviation of the state (e.g., AZ for Arizona).
TOTAL_BALLOTS_COUNTED: The total number of ballots cast in the election.
VOTE_FOR_HIGHEST_OFFICE: Votes cast specifically for the highest office (this column is missing values in the image but usually refers to votes for positions like president or governor).
VAP: Voting Age Population – the total number of people of voting age in the state.
NONCITIZEN_PCT: The percentage of the population that are non-citizens and thus ineligible to vote.
INELIGIBLE_PRISON: The number of individuals in prison and ineligible to vote.
INELIGIBLE_PROBATION: The number of individuals on probation and ineligible to vote.
INELIGIBLE_PAROLE: The number of individuals on parole and ineligible to vote.
INELIGIBLE_FELONS_TOTAL: Total number of felons who are ineligible to vote.
ELIGIBLE_OVERSEAS: The number of eligible voters residing overseas.
VEP: Voting Eligible Population – the total number of people eligible to vote.
VEP_TURNOUT_RATE: The percentage of the Voting Eligible Population that actually voted.
VAP_TURNOUT_RATE: The percentage of the Voting Age Population that actually voted.

Dataset File Hash: c2464102ca377a1e591fe73d4de7cd21
URL : https://election.lab.ufl.edu/dataset/1980-2022-general-election-turnout-rates-v1-1/


All three of these datasets are made up of actual data from the real world, so we can use them to gain fresh perspectives on election trends, voter behavior, and turnout. Without having to worry about the constraints that are usually connected with synthetic data, we can utilize these datasets for our analysis with confidence. 


INTERPRETABLE RECORDS :

### Record 1 (df1_processed.csv)

Raw Data: 
  Age          State                Income      Ethnicity Education
0  55-64        Florida  $100,000 to $149,999     White     Some college, no degree
1    65+  Massachusetts    $25,000 to $49,999     White     Associate 's degree

Interpretation: These data provide information about respondents' age, income, ethnicity, and education from respondents living in various U.S. states.The first is a Florida native who is between the ages of 55 and 64, has a respectable income, and identifies as White. The second respondent is from Massachusetts, is older, and makes less money. Common variables are important elements in election studies. These records gather basic demographic information that aids in understanding the socioeconomic position and potential voting behavior of these individuals. The data is a legitimate component of the dataset since it is indicative of the overall variation in demographic features across various U.S. regions.

### Record 2 (df2_processed.csv)

Raw Data:
    State  Year  CandidateVotes  TotalVotes PartyAffiliation
0  Arizona  1976          321236      741210       REPUBLICAN
1  Arizona  1976            1565      741210            OTHER

Interpretation: Election results for Arizona's 1976 U.S. Senate contest are available in both records. The first candidate, a member of the Republican Party, garnered a sizable number of votes, whilst the second candidate, a member of a minor or independent party, received a very lesser number.These records serve as a standard for illustrating how major parties garner a greater share of the vote in comparison to smaller, less well-liked candidates. They also aid in the comprehension of the dynamics of electoral rivalry in past elections.

### Record 3 (df3_processed.csv)

Raw Data: 
 State            Year     TurnoutRate
0  United States  2022      45.91%
1        Alabama  2022      37.31%

Interpretation: These records, one of which focuses exclusively on Alabama and the other on the national turnout for the 2022 elections, contain statistics on voter turnout rates.Alabama has a lower turnout rate than the national average, which is somewhat higher. These records aid in demonstrating the various ways that various circumstances might affect voter participation. They make sense for shedding light on variations in voter turnout by region.


BACKGROUND DOMAIN KNOWLEDGE : When attempting to predict elections outcomes, political analysts and policymakers can benefit from using election forecasting. Forecasting helps predict how different voter groups will act in an election by examining a variety of criteria, such as demographic trends, past election results, and election turnout rate. These predictions are now more accurate than ever thanks to recent developments in data science and predictive analytics, which also provide insights into voter tendencies that can affect policy and campaign tactics. 
Firstly, my project includes exploring demographic data. Numerous characteristics, including age, gender, household income and level of education, frequently impact the behavior of voters. For example, younger voters prefer to support candidates who are more progressive, but older voters are more inclined to support conservative policies. According to a Pew Research Center study from 2023, these demographic factors have a significant impact on voter preferences, particularly across US regions. I will be using demographic data from datasets such as the US Elections Poll 2020 in my study. This assist in determining which demographic groupings have the greatest influence on the results of elections in various geographic areas.
Turnout numbers for elections will also be a crucial component of my analysis. One of the most important variables in deciding the outcome of an election is voter turnout, which is the percentage of eligible voters who actually cast a ballot. Election results can be significantly impacted by lower voter turnout, particularly among younger voters and members of minority groups. Disparities in voter turnout by age, gender, and race continue to be major obstacles to attaining fair participation in elections, according to research by CIRCLE (2022). We can evaluate the relationship between election outcomes and variations in turnout rates among various states and demographic categories by utilizing voter turnout data.
Initially in my project proposal, I was also planning to include to latest opinion polls data but I was concerned that doing so may introduce potential bias and unreliability in our data since polls usually have margin of error.
In summary, the VoteSense project integrates data from several sources, such as voter participation, demographics, and turnout rate, in an effort to create a comprehensive model for election forecasting. This can offer deeper insights into how many factors—from age and income to turnout rates and candidate popularity—affect election outcomes by utilizing these data points. As demonstrated by FiveThirtyEight (2024), recent developments in data science coupled with the growing accessibility of election-related data allow for the creation of increasingly precise models to forecast future election outcomes.

References :  
Pew Research Center. (2023, July 12). Voting patterns in the 2022 elections. Pew Research Center. Retrieved from https://www.pewresearch.org/politics/2023/07/12/voting-patterns-in-the-2022-elections/
Erikson, R. S., & Wlezien, C. (2020). Forecasting the 2020 Presidential Election: Leading Economic Indicators, Polls, and the Vote. PS: Political Science & Politics, 54(1), 55-58. DOI: 10.1017/S1049096520001481
CIRCLE. (2022). Youth turnout by race and gender reveals major inequities. Tufts University. Retrieved from https://circle.tufts.edu/latest-research/2022-youth-turnout-race-and-gender-reveals-major-inequities
FiveThirtyEight. (2024). Election forecasting and polling insights. Retrieved from https://fivethirtyeight.com


DATASET GENERALITY : The dataset is highly reflective of real-world electoral behavior, supported by both its statistical features and logical alignment. Quantitative variables like age, income, and voter turnout present realistic distributions. For instance, the age range of 21 to 70 years, with a median of 59.5, accurately represents voting demographics, where older individuals typically have higher turnout. The income range from $37,499.5 to $124,999.5 aligns with middle-class incomes, historically tied to political participation. Turnout rates, from 25.07% to 79.21%, capture the variability of voter engagement across states.The qualitative variables, such as ethnicity and education, further enhance the dataset’s real-world representativeness. Ethnicity data, with five categories where White is the most frequent (1174) and Asian the least (49), reflects actual demographic distributions in U.S. elections. This diversity mirrors the true voting population. Additionally, the correlation matrix shows realistic relationships, such as weak or moderate correlations between income and turnout, reflecting the complex factors that shape voter participation.This combination of representative statistics and correlations ensures that the dataset offers a well-rounded view of real-world voting patterns, making it suitable for deriving insights that are applicable to real-world election scenarios.


## Data Transformations
### Transformation N
**Description:** TODO

**Soundness Justification:** TODO

(duplicate above as many times as needed; remove this line when done)


## Visualizations
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)