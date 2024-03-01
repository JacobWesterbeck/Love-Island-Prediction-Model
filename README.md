# LOVE ISLANDS "TYPE ON PAPER"
*******************
## Predicting Success on Love Island

### Project Overview
Love Island is a popular reality TV show that draws in millions of viewers each week. At the end of each season, 4 couples are chosen as finalists, and one couple is ultimately chosen as the winner and most compatible couple. Contestants must manage to appeal to their fellow islanders as well the public to avoid being dumped and maintain their spot in the villa. I hypothesize that discernible patterns exist in contestants' behavior and physical attributes, influencing their likelihood of reaching the finale. To test this hypothesis, I will develop a dynamic model that considers numerous variables of each candidate across multiple Love Island seasons. Through this model, I aim to determine if finalists can be accurately predicted based on predefined criteria.

**SPOILERS:** This project contains finale results from Love Island UK.

### Objective

The objective of this project is to answer the following questions: 
1) Are there features that give candidates an advantage in reaching the finale of the show?
2) Using those features, can we accurately predict which candidates will reach the finale?

To answer these questions, we will create a dataset containing information about each contestant who has appeared on Love Island. Then we will analyze that data for patterns and trends to determine which variables might correlate with success on the show. Once we have selected which features give the strongest signal, we will build a statistical model trained on those features to predict which islanders are most likely reach the finale.

### Challenges
Not a central source of complete contestant data. I will have to gather and prepare the data myself.
Small sample size - Only 9 seasons of Love Island to date, so first version of model will have a sample size of 295 contestants. - This will increase over time and improve model accuracy.
Difficult to quantify subjective data on candidates that lead to success ie. personality/likeability - will not be included in this model
Other features that would have been useful:
    - sentiment analysis on what the public is saying by scraping social media or something
    - candidates Screen time - does more screen time lead to higher chance of being  a finalist? maybe screen time/ days in villa as a datapoint
    - Features that incorporate couples - is there an optimal height difference etc.

**********************


### Table of Contents

1) Data Wrangling (data_wrangling.ipynb)

2) Exploratory Data Analysis (EDA.ipynb)

3) Data Preprocessing (data_preprocessing.ipynb)

4) Predictive Modeling (modeling.ipynb)


************************

### Conclusions
**************
Project goal was achieved by using the Random Forest Classifier to predict which contestants will reach the finale on Love Island. The features chosen do give predictive power, affirming our hypothesis that there are physical features and behaviors that will improve a contestants chances of being successful on Love Island.

-- Larger sample size will help with accuracy - more seasons of love island will increase sample size and ompitmize the signals coming from datapoints
-- Adding more features with strong signals - ie candidate screen time 




*************************

### Things I learned/ Would do Differently Next time

- Set proper datatypes correctly earlier in project
- More detailed commit messages


*************************