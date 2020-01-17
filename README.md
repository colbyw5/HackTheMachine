### HackTheMachine Winning Submission

**Background**:The HackTheMachine Data Science Challenge was help September 7-9 in Brooklyn, NY.  The event brought together data science professionals and students from a variety of backgrounds, including private industry, academia and governemnt, to tackle a pressing issue in the Navy: fleet availability.  In other words, F-18s are not useful to National Security if they are unable to fly.  Our team (Team Jumbos) split the first-place $20,000 prize fund.

![](https://github.com/colbyw5/HackTheMachine/blob/master/event_info/Hack_NY_Vector_Final_LOGO.png)

**Data**: The Navy provided 7+ years of Maintenance Action Form (MAF) dataset, which contains a record of maintenance actions performed on the aircraft. It is a record of everything maintainers have done to the aircraft including: routine inspections, part removal and replacement, mission-related changes, and unscheduled maintenance, including unforeseen failures. The Memory Unit (MU) dataset is provided as well. The MU data is a time-stamped record of all failures or anomalies automatically reported by the aircraft’s avionics system, similar to an error log your auto mechanic might download from your car when the check engine light comes on.

**Challenge**: The main two challenges were 1) Identify the MU error codes associated with corrosion wiring issues, which is flagged in the MAF data and 2) train a predictive model to identify aircrafts with corrosion flags based on the MU error code sequences prior to repair.  The code and results presented in this repository focus on challenge 2, as this was the challenge I assumed.

**Methods**: The majority of the work was manipulating the two datasets to associate MU error codes with MAF actions.  Though an AWS instance was available to research teams, we quickly found the connectivity issues at the host site were prohibitive.  We thus did all data wrangling on local machines.  We first joined the MU and MAF datasets by aircraft, and filtered error codes within 30 days pre/post of repair.  When then created a dataset of unique MAF actions: each repair was a row with a T/F flag for wiring corrosion repair, and the features were the frequency of each error code pre and post repair.  

We then needed perform feature selection, as there were 900+ error codes.  The event organizers gave us a tip at the opening ceremony: MU error codes associated with corrosive wires usually stopped occuring after the repair.  Thus we calculated the % decrease in error code frequency for all MU codes after a wiring corosion repair, ignoring codes that occured during the maintencance window (these codes usually occurred as technicians were trying to recreated the issue).  We decided to use the 20 MU codes with the largest % decrease post wire corrosion repair.  

![Left: average % decrease in MU code frequency after wire corrosion repair; Right: frequency of MU code across all aircraft in test set](https://github.com/colbyw5/HackTheMachine/blob/master/presentation/mu_freq.png)

Next we split the data: 35 aircrafts to train an algorithm, 10 to test.  We trained fours models: logistic regression with L2 normialization, SVM with linear kernel, RandomForest and XGBoost.  Under normal circumstances we would use cross-validation to gridsearch the proper hyperparameters.  However, due to the condensed timeline, we made a few adjustments to each model's hyperparameters and observed model performance, focusing on model accuracy.  Once we found the most accurate model (see results below), we re-trained the model on all 45 aircrafts and submitted our results to our team's GitLab repository for evaluation.

**Results**:  Of the models trained, Random Forest acheived the highest accuracy (74.5%).  Below is a table of model metrics on the held-out test data and an ROC plot.  The organizers evaluated our algorithm on aircraft data not offered to participants, but we were not aware of the results.  

![Classifier Performance Metrics](https://github.com/colbyw5/HackTheMachine/blob/master/presentation/model_perf.png)

![ROC Curves for Classifiers](https://github.com/colbyw5/HackTheMachine/blob/master/presentation/ROC_curves.jpeg)

**Key Takeaways**: One of the main take aways we had from this exercise was data science takes time.  We had to accept that a 1.5 days was not enough time to take on all the challenges and that our results would not be as good as if we had a month to experiment.  Model accuracy could have been improved had we had time to explore more/less MU codes as features or if we had selected optimal hyperparameters.  More complex model stuctures (including neural networks) would have been considered if time permitted.  

Ultimately sacrificing complexity and best-practices for quick results was validated, as most teams had little to present because their work was not submitted by the deadline.  Our team took home 1st place, and we later were connected with the Maintenance Facility that generated the data to share our findings.

**Directory Structure**

- data
    - clean: Clean MU and MAF datasets generated by the clean notebook files
- code
    - clean: The notebook in this folder cleans the raw MU and MAF data, such as converting date columns to datetime objects and converting Yes/No columns to Boolean
    - predict: In this notebook we read in both clean datasets and created the dataset of MAF actions with associated 30-day MU code frequencies prior to repair.  We then trained four classifiers and tested on the 10 held out aircrafts.  Visualizations of model performance are generated as well
    - provided: This code was provided by event organizers to help attendees better understand the supplied data and sugest approaches to the challenges
    - archive: Previous code files no longer needed
- presentation: Slides presented to event organizers and attendees at the event conclusion, in addition to model performance visualizations and tables.
- event_info: event details and code notebook providing some exploratory analyses
