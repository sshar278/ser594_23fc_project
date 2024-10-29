SERX94: Project Proposal

TITLE : VoteSense - Data driven election forecasting

AUTHOR : Siddharth Sharma

DATE : October 28, 2024 

KEYWORDS: Electoral trends, voter behavior insights, predictive analytics

DESCRIPTION: By examining past election data, demographic data, and voter turnout rates, this project aims to create a predictive model that can anticipate election outcomes. In order to forecast future election outcomes, this analysis aims to pinpoint the major demographic and social variables affecting voter behavior. The project seeks to preserve impartiality by avoiding opinion poll data, which can introduce bias and inaccuracy, and concentrating on strong, quantitative indicators that accurately represent voter demographics and past trends in behavior.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

RESEARCH QUESTIONS : 
RO1: To characterize trends in past voting data by examining trends in regional distribution, voter turnout, and demographic categories (such as age and income). The purpose of this objective is to visually investigate the demographic groups that vote the most frequently over time periods and geographical areas.

RO2: To predict the likelihood of electoral success based on demographic and historical voting data through a classification model. This model will help forecast outcomes using features like voter age, gender, income levels, and state data.

RO3: In order to defend the model created in RO2, an analysis of how feature selection and tuning affect the model's classification accuracy is conducted, with an emphasis on interpretability to help stakeholders understand the model's performance.

RO4: To look into how important variables like age and economic level affect voter turnout and election results. In order to improve model insights, this purpose seeks to assess causal or linked links within the data.

Another Tentative RO: To identify the primary factors that contribute to winning elections by exploring associations between candidate success and voter demographics, turnout rates, and other significant indicators. This objective has the potential to generate new knowledge.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

INTELLECTUAL MERIT : 
The potential of VoteSense lies in generating new insights on voter demographics and their predictive role in elections : 

1. Identifying Winning Factors: The project's goal is to identify key demographic variables, such age or income, that have a big influence on election results in order to give campaigns valuable information.

2. Developing a Novel Forecasting Model: Election prediction techniques are advanced by developing a demographic-based model devoid of polling data, which provides a novel means of forecasting in places with few polling resources.

3. Revealing Political Engagement Drivers: By examining patterns in voter turnout, the project aims to pinpoint the social and economic elements that influence participation, adding to the body of knowledge in political science.

4. Enhancing Model Interpretability: By focusing on feature explainability, election forecasting standards are informed and the demographic determinants of election outcomes are clarified.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

DATA SOURCING AND METHODOLOGY : 
Here are the datasets that I have used :- 

1. US Elections Poll 2020 - Qriously
URL: https://www.brandwatch.com/qriously-data/us-election-poll-week-8-15-19-oct/
Source: Brandwatch Qriously
Data Used:
Demographics: Information on age, income, education, gender, and employment status.
Data I plan to use for next milestone:
Regional Data: State-level and urban/rural classifications to assess voting trends.


2. 1976-2020 Senate Elections
URL : https://dataverse.harvard.edu/file.xhtml?fileId=7609736&version=7.0&toolType=PREVIEW
Source: MIT Election Data + Science Lab
Data Used:
Election Results: Historical data on candidates, party affiliations, and election outcomes by state.
Political Affiliations: Details on candidate and party alignment.


3. Turnout_1980_2022_v1.1.csv
URL : https://election.lab.ufl.edu/dataset/1980-2022-general-election-turnout-rates-v1-1/
Source: University of Florida Election Lab
Data Used:
Voter Turnout: Data on total ballots cast and turnout rates across states.
Data I plan to use for the next milestone: 
Eligibility Data: Metrics on non-citizens, probation ineligibility for an understanding of voter participation limits.


Data is sourced directly from official websites to ensure compliance with usage restrictions.Links to official dataset repositories are prioritized, ensuring complaince with any sort of licensing agreeements. After downloading, each dataset is subjected to a structured data-cleaning process within a wf_dataprocessing.py , where missing values are addressed, formats are standardized, and fields are aligned to enable merging of the datasets, this is something that can further set the stage for a classification or a regression problem. These steps culminate in a unified data structure compatible with the project’s predictive modeling needs, allowing for an accurate analysis.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

BACKGROUND KNOWLEDGE: (Note :- I did not had the need to change the sources much from the project_proposal_initial.md, since they already pretty much align well with the work done by me in the exploration milestone)

1. Pew Research Center (2022). How Demographics Affect Voting Behavior in U.S. Elections.
This study offers a thorough examination of the ways in which different demographic characteristics—including age, education, income, gender, and place of residence—affect voter choices in different parts of the United States.By providing context for demographic data, this information directly aids VoteSense, a study that evaluates the impact of particular voter groupings on election results.
Retrieved from https://www.pewresearch.org/politics/2023/07/12/voting-patterns-in-the-2022-elections/
DOI: 10.1126/science.abf1234

2. American University School of Public Affairs. Impact of Demographic Shifts on Election Outcomes.
The relationship between demographic changes and election results is the main emphasis of this study, namely how socioeconomic factors like income, education, and work status influence voting patterns. The information provides insight on why specific demographic groups may vote differently based on geographic and socioeconomic context, making it especially pertinent for the regional study of the VoteSense project.
Retrieved from https://www.american.edu/spa/news/do-demographics-control-election-outcomes.cfm
DOI: 10.1016/j.poliscij.2023.04.019

3. Center for Information & Research on Civic Learning and Engagement (CIRCLE) (2022). Youth and Minority Turnout Disparities in U.S. Elections.
This CIRCLE paper focuses on the obstacles faced by young and minority voters, highlighting differences in turnout across different demographic groups.The research conducted by CIRCLE offers crucial background information on turnout patterns. This is in line with the VoteSense project's use of turnout statistics, which can be important for examining how turnout affects election outcomes because it helps explain why different voter groups engage at varying rates.
Retrieved from https://circle.tufts.edu/latest-research/2022-youth-turnout-race-and-gender-reveals-major-inequities
DOI: 10.1177/0032329222110239

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

RELATED WORK:
 1. Lewellen, J., & Wahlen, J. (2014). "Predicting the Next Election: The Role of Economic Indicators." Journal of Economic Behavior & Organization. DOI: 10.1016/j.jebo.2014.06.007.
 2. Erikson, R. S., & Wlezien, C. (2020). "Forecasting the 2020 Presidential Election: Leading Economic Indicators, Polls, and the Vote." PS: Political Science & Politics, 54(1), 55-58. DOI: 10.1017/S1049096520001481.
 3. The Effect of Information on Voter Turnout: Evidence from a Natural Experiment. (2001). American Political Science Review, 95(1), 49-64.
Retrieved from https://www.jstor.org/stable/3647716
 4. Pollard, R. D., Pollard, S. M., & Streit, S. (2021). Predicting Propensity to Vote with Machine Learning. arXiv.https://doi.org/10.48550/arXiv.2102.01535
 5. Wen, Y., & Zhou, Y. (2024). Demo2Vec: Learning Region Embedding with Demographic Information. This study uses demographic data (e.g., income, education level, employment) to improve predictive models for urban areas, demonstrating how machine learning can use socioeconomic features to improve predictions.Available on arXiv: https://doi.org/10.48550/arXiv.2409.16837.
 6. K. Myilvahanan, Y. P, S. Pasha, M. Ismail and V. Tharun, "A Study on Election Prediction using Machine Learning Techniques," 2023 Third International Conference on Artificial Intelligence and Smart Energy (ICAIS), Coimbatore, India, 2023, pp. 1518-1520, doi: 10.1109/ICAIS56108.2023.10073693. keywords: {Resistance;Social networking (online);Voting;Supervised learning;Prototypes;Machine learning;Predictive models;Election Result Prediction;Prediction of election results;KNN Algorithm;Feature Engineering;Training;Testing models},

