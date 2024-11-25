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
**Feature:** Candidate Votes
**Justification:** Candidate votes, which indicate a candidate's total number of votes, are a key determinant of electoral success. It is essential for predicting results because, from a domain perspective, it captures past voting trends and regional party strength. This characteristic is essential to the model since it offers a robust, numerical indication of voter preferences.

### Feature B
**Feature:** Turnout Rate
**Justification:** The percentage of eligible voters who cast ballots in an election is known as the turnout rate. Since differences in turnout frequently correspond with voter participation and the popularity of politicians or policies, it is a crucial feature. The dynamics of electoral participation, which have a major influence on election outcomes and party success, are reflected in the turnout rate from a domain viewpoint. This feature provides more context for comprehending the predictions made by the model.


## Experiments 
Feature A: Candidate Votes, Feature B: Turnout Rate 
**Note** : For this task, I wrote a function experiment_with_features in wf_ml_evaluation.py, and for checking the trend, I took 4 varied test samples in order to discover the different trends by varying A and B

### Varying A 
**Prediction Trend Seen:** Changing While lower values tended toward minority parties like LIBERTARIAN or OTHER, CandidateVotes showed a strong association between higher vote counts and predictions for majority parties like DEMOCRAT or REPUBLICAN. Given that CandidateVotes represents candidate popularity, a crucial indicator of party identification, this is consistent with domain knowledge. The high relevance of this characteristic indicates how dependent the model is on it, yet other factors like TurnoutRate and area demography mitigate forecasts. For example, even moderate vote counts produced majority party projections in areas with high historical party dominance, illustrating the model's sophisticated management of contextual effects.

### Varying B
**Prediction Trend Seen:** In contrast to CandidateVotes, altering TurnoutRate alone showed more robust and dynamic forecast adjustments. In Sample 3, expectations supporting DEMOCRAT were linked to lower TurnoutRate values, while intermediate rates swung toward REPUBLICAN and higher rates returned to DEMOCRAT. As TurnoutRate rose, Sample 4's forecasts changed from LIBERTARIAN to OTHER. This suggests that TurnoutRate is a crucial aspect for assessing results since it records participation trends connected to demographic and geographic contexts.

### Varying A and B together
**Prediction Trend Seen:**  Interesting dynamics were brought to light by the combined influence of CandidateVotes and TurnoutRate when they were modified in a coordinated manner. As both traits grew for Sample 1, the predictions first changed from OTHER at lower values to LIBERTARIAN. Likewise, for Sample 3, LIBERTARIAN predictions were supported by intermediate correlations, while OTHER was restored by high results. These patterns highlight the significance of researching feature dependencies by indicating that the combined effect of CandidateVotes and TurnoutRate may increase or decrease their separate effects.

### Varying A and B inversely
**Prediction Trend Seen:** A complicated interplay between the features was revealed by inversely correlating CandidateVotes and TurnoutRate, where the impact of one feature frequently offset the decline of the other. With the exception of a few shifts to LIBERTARIAN when TurnoutRate was noticeably higher, Sample 1's forecasts mostly stayed OTHER. Predictions for Sample 4 changed from LIBERTARIAN to OTHER when CandidateVotes rose and TurnoutRate fell. These findings demonstrate how these features' inverse connection produces a balancing dynamic, implying that changes in one feature may be counteracted by thresholds of the other.

