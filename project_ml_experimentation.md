#### SERX94: Experimentation

**Title** : VoteSense : Data-Driven Election Forecasting


**Author** : Siddharth Sharma


**Date** : 25th November, 2024


## Explainable Records
From the predictions for the ActualPartyAffiliation computed in the predictions.csv file present in evaluation, I have selected the following two records and explained why the predicted output is correct in terms of the domain knowledge. 

### Record 1
**Raw Data:**  
State: Kentucky
Year: 2010
Candidate Votes: 755,706
Total Votes: 1,356,096
Ethnicity: White(majority in this context, encoded as 4 in the predictions.csv file)
Education: High School Graduate(encoded as 2 in the predictions.csv file)
Turnout Rate: 0.445
Income: $124,999.5
Predicted Party Affiliation: Republican

**Prediction Explanation:** 
**Actual Party Affliliation for this record** : Republican
Given Kentucky's moderate turnout rate (44.5%), high income ($124,999.5), and preponderance of high school graduates, the "Republican" projection for the state in 2010 makes sense. Consistent voting preferences in these areas are frequently reflected in the moderate turnout rate, which signifies consistent voter participation. Voting behavior may be influenced by the high income, which indicates a populace that is economically stable. This assumption is further supported by the educational profile of many Kentucky voters who live in suburban and rural areas. All of these elements work together to make the model's results plausible given Kentucky's 2010 socioeconomic and electoral circumstances.
**RO s satisfied** : 
RO1: This record demonstrates how regional characteristics and demographic trends, such as income, turnout rate, and education, influence voting patterns.
RO2: The classification model effectively predicts the likelihood of a Republican win using historical voting data and demographic features.
RO4: The record illustrates the importance of economic level (income) and turnout rate in determining election outcomes, contributing to a better understanding of causal relationships in voting behavior.

### Record 2
**Raw Data:** 
State: Arizona
Year: 2000
Candidate Votes: 108,926
Total Votes: 1,397,076
Ethnicity: White (majority in this context, encoded as 4)
Education: College Graduate(encoded as 4)
Turnout Rate: 0.4637
Income: $62,499.5
Predicted Party Affiliation: Other

**Prediction Explanation**
**Actual Party Affliliation for this record** : OTHER
In 2000, Arizona's slightly higher turnout percentage (46.37%), medium income ($62,499.5), and college-educated population all support the "Other" (third-party membership) prediction. Support for third-party candidates is consistent with a varied voter base, as indicated by the moderate turnout rate. The middle-class demographic may choose local or issue-based politicians over those from established party lines. Higher education also indicates a politically conscious populace that may take into account several platforms. Together, these elements support the model's prediction in the political climate of Arizona in 2000.
**RO s satisfied** : 
RO1: Highlights the significance of demographic diversity (income and education) and turnout rates in shaping regional voting trends.
RO2: Demonstrates the model's ability to predict third-party support using demographic and historical voting data.
RO4: Explores the relationship between education, income, and voter turnout, illustrating their combined influence on election outcomes.

## Interesting Features
### Feature A
**Feature:** TODO

**Justification:** TODO

### Feature B
**Feature:** TODO

**Justification:** TODO

## Experiments 
### Varying A
**Prediction Trend Seen:** TODO

### Varying B
**Prediction Trend Seen:** TODO

### Varying A and B together
**Prediction Trend Seen:** TODO


### Varying A and B inversely
**Prediction Trend Seen:** TODO

(duplicate above as many times as needed; remove this line when done)