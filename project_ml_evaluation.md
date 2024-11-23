#### SERX94: Machine Learning Evaluation

**Title** VoteSense : Data-Driven Election Forecasting.

**Author** : Siddharth Sharma

**Date** : 25th November, 2024

## Evaluation Metrics
## Metric 1
**Name:** Accuracy
**Choice Justification:** Accuracy calculates the proportion of accurate forecasts among all forecasts. When assessing the overall accuracy of predictions in a classification task, such as predicting party affiliation, this statistic is especially pertinent.
**Interpretation:** A brief summary of the model's overall performance is given by accuracy. For example, the Random Forest Classifier's accuracy of 76.45% means that around three-fourths of the samples were accurately predicted to be party affiliated.

### Metric 2
**Name:** F1 score (weighted)
**Choice Justification:** The F1 Score provides a single metric that assesses a model's capacity to accurately identify positive cases while reducing false positives and false negatives by striking a balance between precision and recall. To ensure equitable representation for unbalanced datasets, a weighted F1 Score averages the scores for each class according to their support.
**Interpretation** The Random Forest model's balanced performance across all classes is highlighted by its weighted F1 Score of 0.73. It considers both how well the model predicts the majority classes (like "OTHER") and how poorly it predicts the minority classes (like "LIBERTARIAN").Although for the random forest algorithm, I have also computed the precision and recall for each of the 4 political affiliations, still for applications where both false positives and false negatives have substantial ramifications, a higher F1 score denotes a better trade-off between precision and recall. It guarantees that forecasts in this project are accurate and consistent across political affiliations.


## Alternative Models
## Alternative 1 - The original random forest classifier model (so not exactly an alternate but just writing for continuity)
**Construction**:
To deal with imbalances between political affiliations (such as "OTHER" vs. "LIBERTARIAN"), a balanced Random Forest Classifier was developed. Features include Turnout Rate, Ethnicity, Education, Candidate Votes, Total Votes, Age, and Income.
Preprocessing: To guarantee model compatibility, I applied label encoders to categorical characteristics.
**Evaluation**:
With a weighted F1 Score of 0.73 and an accuracy of 76.45%, the Random Forest Classifier performed well overall, especially for majority classes like "OTHER" and "DEMOCRAT." It handled intricate relationships between parameters like age, income, and turnout rate with ease and offered insightful information about the significance of each feature. It had trouble with minority classes, such as "LIBERTARIAN," which had little data; as a result, the class received a low F1 Score of 0.13. Notwithstanding these difficulties, the model was the most dependable and solid choice for the project since it struck a compromise between interpretability and fairness.

## Alternative 2 - Fine tuned KNN model with k=3 neighbors
**Construction** : 
The k=3 KNN model was created as a localized substitute for Random Forest. To guarantee comparability, it made use of the same preprocessing pipeline (such as label encoding) and features (such as Turnout Rate, Education, Age, and Income). This KNN model makes predictions based on the three nearest neighbors, concentrating on local patterns while being more susceptible to noise and outliers than Random Forest, which uses ensemble decision trees and class weights.I utilized the Random Forest Classifier's preprocessing method and a lower k number to concentrate on local patterns.
**Evaluation and justification for value of k**:
64.35% accuracy
F1 Score Weighted: 0.6270
When analyzing particular demographic patterns, such as the correlation between voter behavior in particular states and socioeconomic parameters like age or income, it was able to capture local linkages in the data with effectiveness. However, because a smaller k makes the model more sensitive to individual outliers, noise in the data affected its performance. 

## Alternative 3 - Fine tuned KNN model with k=5 neighbors
**Construction** :
To balance local and global trends, this KNN model with 𝑘 = 5 increased the neighborhood size. By taking into account five neighbors, it decreased sensitivity to noise while retaining the same features and preprocessing as Random Forest and the 𝑘 = 3 KNN. This model employed a slightly wider neighborhood to smooth forecasts while maintaining a moderate focus on local patterns, in contrast to Random Forest, which averages across numerous decision trees.
**Justification for value of k** : Here I sought to use an intermediate k (=5) value to balance both local and wider patterns.
**Evaluation**:
Accuracy: 64.48%
Weighted F1 Score: 0.6303
With an accuracy of 64.48% and a weighted F1 Score of 0.6303, the KNN model with 𝑘 = 5 demonstrated a marginal improvement over the k=3 model. The model struck a balance between accounting for larger trends in the data and capturing local patterns by employing an intermediate k value. As a result, it was less sensitive to noise than 𝑘 = 3, which enhanced its generalizability.

## Alternative 4 - Fine tuned KNN model with k=7 neighbors
**Construction and justification for value of k** :
The neighborhood size was further expanded by the KNN model with 𝑘 = 7k=7 in order to capture more extensive patterns throughout the dataset. This version focused on generalization by including seven neighbors in predictions, while maintaining the same characteristics and preprocessing as the other models. This KNN model lessened the impact of noise at the expense of some local pattern sensitivity, whereas Random Forest prioritizes feature relevance through tree-based decisions.
**Evaluation**:
The KNN variation with k=7 performed the best among the options, achieving a weighted F1 Score of 0.6368 and an accuracy of 65.64%. In contrast to lesser k values, such as k = 3, a larger k number allowed the model to concentrate on more general patterns throughout the dataset, lessening the influence of noise and outliers. Generalization was enhanced by this method, particularly for majority classes.
In contrast to the Random Forest Classifier, which had a substantially greater accuracy and F1 Score, the model nevertheless performed poorly. Because KNN relied on distance metrics, it was less able to handle imbalances among political affiliations and was less effective for this high-dimensional dataset.

## Visualization
### Visual N
**Analysis:** I have not written the analysis for the visuals in this paper as it is not required for this milestone. However I have still generated them in the visuals folder for future use. 

## Best Model

**Model:** With a weighted F1 Score of 0.6368 and an accuracy of 65.64%, the KNN model with 𝑘 = 7 outperformed the other two KNN models. Compared to 𝑘 = 3 and k = 5, this approach reduced susceptibility to noise and outliers by capturing broader patterns by expanding the neighborhood size. It performed worse than the Random Forest Classifier, which had a much higher accuracy and F1 Score overall, even if it generalized better for majority classes.
