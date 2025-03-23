# BrainDead 🧠 2K25:

![BrainDead Logo](https://github.com/user-attachments/assets/db36aa27-72f8-4fd6-9de6-18f1c4b4c8f6)

# BrainDead 🧠: The Ultimate Data Analysis & Machine Learning Challenge

---

# Problem Statement 1: Statistics is All You Need: IPL Data Analysis and 2025 Winner Prediction – The Game Behind the Game!

#### <div align="right">🎯 Marks: 40</div>

#### 📌 Problem Statement:
Cricket is the most popular sport in India. There are various formats of this game and the most loved one is the Indian Premier League (IPL). This professional Twenty20 cricket league in India gets contested during March or April and May of every year by eight teams representing ten different cities on India. The league was founded by the Board of Control for Cricket in India (BCCI) in 2008. The IPL has an exclusive window in ICC Future Tours Programme. It is the most-attended cricket league in the world. Currently, it’s the 18th season of IPL.

You have to perform a comprehensive analysis of IPL data from its inception through to the most recent season in 2024, aimed at uncovering key **insights**, **trends**, and **patterns**. It should consists of **data collection**, **preprocessing**, and **exploratory data analysis (EDA)** to visualize metrics such as **win rates**, **player performance**, and **team statistics**. The analysis includes statistical insights to identify significant factors influencing match outcomes. You may use pandas and NumPy for data manipulation and matplotlib and seaborn for data visualization.

Also, try to develop an **ensemble model**, combining different classifier models (one such example is the ensembling of classifiers like **Random Forest** and **XGBoost**) for predicting the winner of the 2025 IPL season. It should explain the **model’s features**, **training**, **validation**, and **performance evaluation**. Additionally, you can explore experimenting with **neural networks**. The results section must present the model’s predictions for the 2025 season, and discussion regarding the potential strengths and limitations, and should provide insights into the predicted performance of teams and key players. The primary objective is to use historical IPL data to build a predictive model for future match prediction outcomes, demonstrating the application of advanced machine learning techniques to sports data.

#### 🔍 Analysis Goals:

##### 1️⃣ **Data Cleaning and Feature Engineering**
- Ensure that **no missing values or outliers** exist in the dataset.
- Handle potential issues that could **impact insights and predictions**.

##### 2️⃣ **Exploratory Data Analysis (EDA)**
Perform the following analyses based on the **IPL 2008-2024 Dataset**:

###### 🏏 **Team Performance:**
- **Plot Matches Played and Winning Percentages**
- **Plot Run Rate and Economy Rate (as a bowling side)**
- **Plot Highest and Lowest Scores**
- **Plot Total 4s and 6s**
- **Plot Average Powerplay and Death Overs Score**
- **Powerplay Analysis**

###### 👤 **Player Performance:**
- **Get the top 20 run-scorers**
- **Plot Batting Average vs Batting Strike Rate for the top 20 run-scorers**
- **Find Highest Average and Strike Rate for players with >50 matches**
- **Plot top wicket-takers**
- **Plot top highest individual scores**
- **Man of the Match Count Analysis**
- **Use K-Means Clustering to plot Batting Average vs Bowling Economy Rate for number of clusters = 3 (Batsman, Bowler, All Rounder)**
- **Identify Top 10 Batsmen in each run category**:
  - **Top 6’s scorer**
  - **Top 4’s scorer**
  - **Top 2’s scorer**
  - **Top 1’s scorer**

###### 📅 **Seasonal Analysis:**
- **Calculate average runs per match per season**
- **Identify targets of 200+ runs per season**
- **Find the average score of each team per season**
- **Analyze runs of Orange Cap Holders per season**
- **Track wickets of Purple Cap Holders per season**
- **Find top 10 bowlers per season**

##### 3️⃣ **Feature Extraction**:
- Extract key features from **`matches.csv`** dataset.
- Extract crucial insights from **`deliveries.csv`** dataset.

##### 4️⃣ **Winner Prediction Model**: Develop a **prediction model** based on the above analyses to predict the **winner of 2025 IPL.**.

---

#### 🛠 Tools for Analysis:
Participants may use the following tools:

- **MS Excel**
- **Tableau/Power BI**
- **Jupyter Notebook/Google Colab with Matplotlib**

#### 📂 Dataset Link:
The dataset consists of two separate CSV files: **matches** and **deliveries**. These files contain the information of each match summary and ball by ball details, respectively. [BrainDead IPL Complete Dataset (2008-2024)](https://github.com/jayantapaul/BrainDead-2K25/blob/77aa9fe4887b4a937358ea13156f90e24fbcfc89/Brain%20Dead%20IPL%20Dataset.zip)

#### 📊 Data Field Description of 'matches' file:

The **`matches.csv`** file consists of the match informations of **1095 face-offs** amongst the teams in all the IPL seasons in the last 17 years! 
-	**'id'**: Unique identifier for each match.
-	**'city'**: City where the match was played.
-	**'date'**: Date of the match.
-	**'player_of_match'**: Name of the player who was awarded "Player of the Match."
-	**'venue'**: Stadium or venue where the match was played.
-	**'neutral_venue'**: Binary indicator (0 or 1) indicating if the match was played on a neutral venue (1) or not (0).
-	**'team1'**: Name of the first team participating in the match.
-	**'team2'**: Name of the second team participating in the match.
-	**'toss_winner'**: Name of the team that won the toss.
-	**'toss_decision'**: Decision taken by the toss-winning team (either 'field' or 'bat').
-	**'winner'**: Name of the team that won the match.
-	**'result'**: The result of the match (e.g., 'runs', 'wickets', 'tie', etc.).
-	**'result_margin'**: The margin by which the winning team won the match (e.g., runs or wickets).
-	**'eliminator'**: Binary indicator (0 or 1) indicating if the match was decided by an eliminator (1) or not (0).
-	**'method'**: The method used to decide the match (e.g., Duckworth-Lewis, etc.).
-	**'umpire1'**: Name of the first on-field umpire.
-	**'umpire2'**: Name of the second on-field umpire.

#### 📊 Data Field Description of 'deliveries' file:

The **`deliveries.csv`** file consists of ball by ball informations of all the 1095 face-offs. The dataset consists of **14,26,312 delivery entries** and **17 attributes**.
-	**'match_id'**: Unique identifier for each match.
-	**'inning'**: The inning number of a match
-	**'batting_team'**: The name of the batting team
-	**'bowling_team'**: The name of the bowling team
-	**'over'**: The over number in the ongoing inning for the batting team
-	**'batter'**: The name of the batsman (at the striker end)
-	**'bowler'**: The name of the bowler
-	**'non_striker'**: The name of the batsman at the non-striker end
-	**'batsman_runs'**: Runs scored by the batsman (at the striker end)
-	**'extra_runs'**: Extra runs (if any) conceded by the bowler
-	**'total_runs'**: The total runs conceded by the bowler (including the runs scored by the batsman and the extra runs conceded)
-	**'extra_type'**: The type of extra runs conceded (wide, no-ball, bye, leg-bye, etc.)
-	**'is_wicket'**: A flag variable to indicate if there is a dismissal in a particular ball ('0' means 'no dismissal'; '1' means 'dismissal')
-	**'player_dismissal'**: The name of the player (batsman) who got dismissed
-	**'dismissal_kind'**: The type of dismissal (caught, bowled, run-out, LBW, stumping, obstructing the field, etc.)
-	**'fielder'**: The name of the fielder (may be bowler also) participated in the dismissal

#### 🔑 Key Details:
- **1 run** is given as an extra run to the batting team in case of wide and no-ball.
- The bowler has to bowl **one extra delivery** in case of wide and no-ball.
- The runs scored by the batsman in case of bye and leg-bye will not get counted in the batsman's individual run, rather, it will get added to the team total.
- The **'super over'** situation in case of a tie should not be considered in any evaluation. Those are just for tie-breaking purposes.
- In December 2018, the team changed its name from the **Delhi Daredevils** to the **Delhi Capitals**.
- **Sunrisers Hyderabad** replaced the **Deccan Chargers** in 2012 and debuted in 2013.

#### Important Formulae:

Batting Average = Total Runs Scored / Number of times out

Batting Strike Rate = (Total Runs / Total Balls Faced) * 100

Bowling Economy Rate = Total Runs Conceded / Total Overs Bowled

---
