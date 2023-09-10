# Predicting Love Islander Winners

https://github.com/KwameTaylor/bachelorette-predictor --- HUGE INSPO
### Repository Table of Contents
- README
- Data
- Data Dictionary
- Jupyter Notebooks
    - Wrangling/prepr
    - Analysis
    -
- Python Files
    - Wranging/prep
    - Analysis

- Model
- Anything else?

### What Is Love Island?
A group of single people move to a luxury villa in the hope of finding love and the summer of their life. Throughout the series, there are shock twists and surprise announcements that will test the relationships between the islanders. To remain in their luxury paradise and stand a chance of winning the £50,000 prize, contestants must couple up and win the hearts of each other and the public, as they ultimately decide who stays on `Love Island' and who goes.

**SPOILERS:** This data contains finale results from all seasons of Love Island.

### Project Scope
The end goal of this project is to create a model that predicts which islanders are most likely to be finalists on Love Island based on data from all previous seasons.
- Data wrangling - obtain historical data of all Love Island contestants
- Data processing - prepare data for analysis
- Feature Selection/Feature Engineering - Select/create features for use in the model
- Data Analyis - Graphs and charts using Python packages to determine correlations and significant variables for modeling
- Data Visualiation - Use tableau to visualize hisorical data and present findings
- Data Model - Create a model that gives predictions as to who will winbe finalists(target variable) on love island when given data(predictor variables) on current contestants.


### Project Flow
Each bullet point below contains many various processes but this is the overview and the order in which you should view Jupyter notebooks for full detail and thought processes. The entire process and final product is consolidated into the notebook "Loveislandmodel".

- Data Wrangling
- Data Exploration
- Data Visualization in Tableau
- Data Preprocessing
- Data Modeling


### Challenges
Not a central source of complete data, so will have to manually gather some features.
Some features have a direct relationship with the target variable. Target variable = Finalist. Length of stay variable likely has a direct relationship with this.
Some features may be too correlated with eachother? 
Small dataset - Only been 9 seasons, so first version of model will havea sample size of 295. - This will increase over time and improve model accuracy.
Impossible to quantify subjective data on candidates that lead to success ie. personality/likeability
- this will be a shortcoming of this model

Model Goal:
- I will collect islanders physical data (gender, height, etc.)
- I will collect data about their time on the show (when they entered, how many couples they were in)
- using the above 2 categories of data, can I predict who will be finalists on the show each season?

Feature Engineering/good questions to analyze:
    -Does a males/females age relate to reaching finals?
    -Does day entered relate to reaching finals?
    -Height?
    -# of partners?
    -Hair color?
    -Eye color?
    -Race?
    -Hometown/region?
    -# of unique parters?
    -New feature - #partners//length of stay - loyalty score? Does loyalty score impact change to be finalst? Low loyalty score means VERY LOYAL, high loyalty score means NOT LOYAL

    Loyalty score - 1st place is on avg more loyal than 2nd, 2nd more loyal than 3rd, 3rd more loyal than 4th, 4th more loyal than avg of dumped islanders
        - for  all islanders, exclude islanders who are casa amor entries AND have 0 couples - this means they did not make it out of casa amor and will skew data
    


### How to Contribute

### Notebooks Contents
Part 1: Data Wrangling
1) Gather data
2) Format/structure data for exploration

Part 2: Exploratory Data Analysis
1) Analysis of features
2) Find patterns and anomalies
3) use this to understand HOW i  want  to process

Part 3: Data Processing
1) Add new features
2) Remove redundant/unusable features
3) Convert features into a form suitable for modeling
4) After data processing send the processed data off to:
     1- tableau visualization for in depth analysis andstory telling
     2- modeling - use that processed data to create a predictive model


Part 4: Data analysis/Tableau visualization
1) Analysis/Visuals to tell story of historical data

Part 5: Predictive Modeling


### Data  Science  Workflow
Ask an interesting question - Can we predict who will succeed on Love Island using contestant physical traits and circumstances?
Get the data - Data retreived, process  revealed in data wrangling
Explore the data - EDA completed in data exploration - look for anomalies/patterns
Model the data  
Communicate and visualize the results


### Upkeep:
Once  the  model  is complete, there is ongoing work that needs to be performed:

When a Love Island season is active:
1) Get data on current group of Islanders each week and put that into model to determine odds.
2) Track changing weekly odds throughout each season
3) Once final  4 couples are locked in, check how accurate my model was at consistently predicting finalists

When Love Island season NOT active:
1) Add data from new completed seasons into the pipeline to increase  available data to improve quality of model.
2) Look for ways to improve accuracy of model by adding/changing features or using a  different  type of model
