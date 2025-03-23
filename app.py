import streamlit as st
import pickle
import pandas as pd
import time
import matplotlib.pyplot as plt
import os

# Page configuration
st.set_page_config(
    page_title="IPL Data Analysis & Prediction",
    page_icon="🏏",
    layout="wide"
)

# CSS styles (your existing styles here)
st.markdown(
    """
    <style>
    .stButton > button {
        width: 100%;
        text-align: center;
        display: block;
        margin-bottom: 10px;
        background-color: #1b0b61;
        font-family: monospace;
    }
     .github-button {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #022e15;
        color: #d3f5c6; /* Yellow text */
        font-family: monospace;
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        margin-bottom: 10px;
        border: 2px solid #d3f5c6; /* Border to prevent shifting */
    }
    .github-button:hover {
        background-color: yellow; /* Yellow background */
        color: #022e15; /* Deep Red text */
        border: 2px solid #022e15; /* Deep Red border */
    }
    a.github-button:visited, a.github-button:active {
        color: yellow !important;
        text-decoration: none !important;
    }
    a.github-button:hover {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define Teams
teams = [
    "Royal Challengers Bangalore", "Kings XI Punjab", "Mumbai Indians", "Kolkata Knight Riders",
    "Rajasthan Royals", "Chennai Super Kings", "Sunrisers Hyderabad", "Delhi Capitals",
    "Lucknow Super Giants", "Gujarat Titans"
]

# Define Indian Cities
cities = [
    "Bangalore", "Chandigarh", "Delhi", "Mumbai", "Kolkata", "Jaipur", "Hyderabad", "Chennai",
    "Ahmedabad", "Cuttack", "Nagpur", "Dharamsala", "Visakhapatnam", "Pune", "Raipur", "Ranchi",
    "Bengaluru", "Indore", "Navi Mumbai", "Lucknow", "Guwahati"
]

# Load Model
pipe = pickle.load(open('ipl.pkl', 'rb'))

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'

st.sidebar.title("Welcome to IPL Dataverse:")
# Sidebar Navigation
st.sidebar.image("ipl_logo.JPG", use_container_width=True)
st.sidebar.write("Navigation Guide:")

# Navigation buttons
if st.sidebar.button("Predict the Winner!"):
    st.session_state['current_page'] = 'prediction'

if st.sidebar.button("IPL Seasonal Trends"):
    st.session_state['current_page'] = 'seasonal_trends'

if st.sidebar.button("Seasonal Detailed Analysis"):
    st.session_state['current_page'] = 'seasonal_detailed'

if st.sidebar.button("Cap Winners"):
    st.session_state['current_page'] = 'cap_winners'

if st.sidebar.button("Bowler Statistics"):
    st.session_state['current_page'] = 'bowler_stats'

if st.sidebar.button("Batsman Statistics"):
    st.session_state['current_page'] = 'batsman_stats'

# Handle different pages based on session state
if st.session_state['current_page'] == 'prediction':
    st.title("🏏 IPL Win Probability Predictor")

    st.write("""
    This model predicts the probability of an IPL team winning a match based on various factors like:
    - Batting & Bowling Teams
    - Match Venue (City)
    - Target Score
    - Current Score, Overs, and Wickets
    - Required Run Rate & Current Run Rate
    
    The model is trained to provide balanced probabilities, avoiding extreme predictions.
    """)

    col1, col2 = st.columns(2)

    with col1:
        batting_team = st.selectbox('Select the Batting Team', sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select the Bowling Team', sorted(teams))

    selected_city = st.selectbox('Select the Match City', sorted(cities))
    target = st.number_input('Target Score', min_value=1, step=1, format="%d")

    col3, col4, col5 = st.columns(3)

    with col3:
        score = st.number_input('Current Score', min_value=0, step=1, format="%d")
    with col4:
        overs = st.number_input('Overs Completed', min_value=0, max_value=20, step=1, format="%d")
    with col5:
        wickets = st.number_input('Wickets Lost', min_value=0, max_value=10, step=1, format="%d")

    if st.button('🔮 Predict Probability'):
        with st.spinner('Calculating...⏳'):
            time.sleep(2)  # Simulate Processing Time

        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_remaining = 10 - wickets
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets_remaining],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        st.success("✅ Prediction Complete!")
        st.header(f"🏆 {batting_team} - {round(win * 100)}% Win Probability")
        st.header(f"⚡ {bowling_team} - {round(loss * 100)}% Win Probability")

        # Generate Pie Chart for Win Probability
        fig, ax = plt.subplots()
        labels = [f"{batting_team} Win", f"{bowling_team} Win"]
        sizes = [win * 100, loss * 100]
        colors = ["#4CAF50", "#FF5733"]
        explode = (0.1, 0)  # Slightly separate the winning team slice
        ax.pie(
            sizes, labels=labels, autopct="%1.1f%%", colors=colors,
            explode=explode, startangle=140, shadow=True, textprops={'fontsize': 14}
        )
        ax.axis("equal")  # Ensures pie chart is a circle

        # Show Pie Chart in Streamlit
        st.pyplot(fig)

elif st.session_state['current_page'] == 'seasonal_trends':
    st.title("📊 IPL Seasonwise Analysis")

    st.subheader("Average Runs per match")
    st.image("avg_runs_per_match.png", use_container_width=True)

    st.subheader("Targets 200 plus")
    st.image("targets_200_plus.png", use_container_width=True)

    st.subheader("Average Score per team in the seasons")
    st.image("avg_score_team_season.png", use_container_width=True)

    st.subheader("Number of matches played per season")
    st.image("num_of_match_per_season.png", use_container_width=True)
    
    st.subheader("Number of times a target of 200+ was scored")
    st.image("targets_200_plus.png", use_container_width=True)

elif st.session_state['current_page'] == 'seasonal_detailed':
    st.title("📊 Welcome to IPL Seasonal Analysis")
    st.write("""
    Over the past 17 years, IPL has provided some of the most thrilling moments in cricket history. 
    We have analyzed an extensive amount of historical data to bring these trends and insights to you. 
    Explore the various statistics across different seasons and uncover the hidden patterns of IPL.
    """)
    
    # Read available seasons from the folder
    seasons = [f"{year}" for year in range(2008, 2025)]  # IPL seasons from 2008 to 2024
    selected_season = st.selectbox("Select IPL Season", seasons)
    
    # Define categories for analysis
    categories = [
        "Average Score", "Matches Per Stadium", "Top Players",
        "Toss Decisions", "Total Runs", "Win Margins", "Wins By Team"
    ]
    
    selected_category = st.selectbox("Select Analysis Category", categories)
    
    # Convert category name to filename format
    category_filename = selected_category.lower().replace(" ", "_")
    image_path = f"ipl_season_plots/{selected_season}_{category_filename}.png"
    
    # Display analysis and image
    st.subheader(f"IPL {selected_season} - {selected_category} Analysis")
    st.write("""
    Below is a detailed visualization of how teams performed in the selected category for this season.
    These insights help us understand how the game evolved and how different factors played a role in team success.
    """)
    
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.warning("No visualization available for this selection.")
    
    st.write("""
    Stay tuned for more updates and deep dives into IPL's historical trends!
    """)

elif st.session_state['current_page'] == 'cap_winners':
    st.title("🏆 IPL Cap Winners - Orange & Purple Cap")
    st.write("""
    The **Orange Cap** is awarded to the highest run-scorer in a season, while the **Purple Cap** is given to the leading wicket-taker.
    These prestigious caps represent excellence in batting and bowling performances throughout the tournament.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🟠 Orange Cap Winner")
        st.image("orange_cap.png", use_container_width=True, caption="Highest Run Scorer of the Season")
    with col2:
        st.subheader("🟣 Purple Cap Winner")
        st.image("purple_cap.png", use_container_width=True, caption="Highest Wicket-Taker of the Season")
    
    st.header("Detailed Analysis")
    st.subheader("🟠 Orange Cap Winner")
    st.image("orange_cap.png", use_container_width=True, caption="Highest Run Scorer of the Season")
    
     # Orange Cap Data Table
    st.subheader("📊 Orange Cap Winners Over the Years")
    orange_cap_data = {
        "Season": ["2007/08", "2009", "2009/10", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020/21", "2021", "2022", "2023", "2024"],
        "Player": ["SE Marsh", "ML Hayden", "SR Tendulkar", "CH Gayle", "CH Gayle", "MEK Hussey", "RV Uthappa", "DA Warner", "V Kohli", "DA Warner", "KS Williamson", "DA Warner", "KL Rahul", "RD Gaikwad", "JC Buttler", "Shubman Gill", "V Kohli"],
        "Runs": [616, 572, 618, 608, 733, 733, 660, 562, 973, 641, 735, 692, 676, 635, 863, 890, 741],
        "Matches": [11, 12, 15, 12, 14, 17, 16, 14, 16, 14, 17, 12, 14, 16, 17, 17, 15],
        "Batting Avg": [68.44, 57.20, 47.54, 67.56, 61.08, 56.38, 44.00, 46.83, 81.08, 58.27, 52.50, 69.20, 48.29, 45.36, 57.53, 59.33, 61.75],
        "Strike Rate": [136.28, 139.85, 126.38, 177.78, 155.30, 126.38, 136.08, 152.72, 148.55, 138.74, 140.80, 139.52, 127.31, 133.97, 144.80, 152.92, 149.09]
    }
    
    orange_cap_df = pd.DataFrame(orange_cap_data)
    st.table(orange_cap_df)

    st.subheader("🟣 Purple Cap Winner")
    st.image("purple_cap.png", use_container_width=True, caption="Highest Wicket-Taker of the Season")
   
     # Purple Cap Data Table
    st.subheader("📊 Purple Cap Winners Over the Years")
    purple_cap_data = {
        "Season": ["2007/08", "2009", "2009/10", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020/21", "2021", "2022", "2023", "2024"],
        "Bowler": ["Sohail Tanvir", "RP Singh", "PP Ojha", "SL Malinga", "M Morkel", "DJ Bravo", "MM Sharma", "DJ Bravo", "B Kumar", "B Kumar", "AJ Tye", "Imran Tahir", "K Rabada", "HV Patel", "YS Chahal", "Mohammed Shami", "HV Patel"],
        "Wickets": [22, 23, 21, 28, 25, 32, 23, 26, 23, 26, 24, 26, 32, 32, 27, 28, 24],
        "Matches": [11, 16, 16, 16, 16, 18, 16, 16, 17, 14, 14, 17, 17, 15, 17, 17, 14],
        "Economy": [6.23, 6.75, 7.32, 5.94, 7.19, 7.73, 8.46, 8.19, 7.29, 7.11, 7.80, 6.80, 8.19, 7.66, 7.50, 7.92, 9.18],
        "Bowling Avg": [12.50, 18.70, 20.90, 14.04, 18.64, 15.78, 19.87, 17.00, 21.87, 14.77, 19.12, 16.92, 17.66, 14.41, 19.85, 19.00, 20.21]
    }
    purple_cap_df = pd.DataFrame(purple_cap_data)
    st.table(purple_cap_df)

elif st.session_state['current_page'] == 'bowler_stats':
    st.title("🎯 Top Bowler Stats in IPL")
    st.write("This is the bowling statistics for the last 5 IPL seasons and the first-ever IPL season.")

    # Read available seasons from bowler_stat.txt
    with open("bowler_stat.txt", "r") as file:
        data = file.read()
    
    # Extract available seasons
    seasons = [line.split('- ')[1].split(' ')[0] for line in data.splitlines() if "Top 10 Bowlers" in line]
    selected_season = st.selectbox("Select Season", seasons)
    
    # Display statistics for the selected season
    if selected_season:
        st.subheader(f"Top 10 Bowlers - {selected_season}")
        stats_start = data.find(f"Top 10 Bowlers - {selected_season}")
        stats_end = data.find("=", stats_start + 10)
        stats_text = data[stats_start:stats_end]
        st.text(stats_text)
        
        # Match and read the respective .csv file containing additional data
        season_file = f"bowler_stat_{selected_season}.csv"
        if os.path.exists(season_file):
            extra_df = pd.read_csv(season_file)
            st.subheader(f"Detailed Statistics:")
            st.table(extra_df)
        else:
            st.warning("No additional data available for this season.")
        
        # Show corresponding plot
        image_path = f"bowler_stat{selected_season}.png"
        st.subheader(f"IPL {selected_season}: Bowling Leaders and Their Impact")
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.warning("No visualization available for this season.")

        image_path = f"logo_footer.jpg"
        st.image(image_path, use_container_width=True)

elif st.session_state['current_page'] == 'batsman_stats':
    st.title("🎯 Top Batsman Stats in IPL")
    st.write("## Experienced batsmen stats for all the seasons of IPL.")
    st.image("exp_batsman_runstrikerate.png", use_container_width=True)

    st.write("## Top Individual Scores of all the seasons of IPL.")
    st.image("highest_individual_batter.png", use_container_width=True)

else:
    # Home page - this is what shows when no button is clicked
    st.markdown(
        "<h1 style='text-align: center; color: yellow;'>🏏 IPL Data Analysis & Prediction</h1>",
        unsafe_allow_html=True
    )

    # Insert IPL logo
    st.image("ipl_body.png", use_container_width=True)
    st.write(
        """
        The **Indian Premier League (IPL)**, founded in 2008 by the BCCI, is the most-watched 
        T20 cricket league globally. It features top players from around the world and has transformed 
        cricket with its electrifying matches and record-breaking performances.
        
        The IPL consists of **10 teams** representing various cities in India. The current teams are:
        - 🏆 Kolkata Knight Riders (KKR) -2024 Winner
        - 🔵 Mumbai Indians (MI)
        - 🔴 Royal Challengers Bangalore (RCB)
        - 🟡 Chennai Super Kings (CSK)
        - 🟠 Sunrisers Hyderabad (SRH)
        - 🔴 Punjab Kings (PBKS)
        - 🟡 Gujarat Titans (GT)
        - 🟢 Lucknow Super Giants (LSG)
        - 🟠 Rajasthan Royals (RR)
        - 🔵 Delhi Capitals (DC)

        Our platform provides **in-depth analysis** of all IPL seasons (2008-2024), 
        including match trends, player statistics, team performances, and a **prediction model** 
        for the 2025 season.
        """
    )

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <h3>Developed by:</h3>
        👨‍💻 <a href="https://github.com/Anurag-ghosh-12" target="_blank" style="text-decoration: none; color: white;">Anurag Ghosh</a>  <br>
        👨‍💻 <a href="https://github.com/Uttam-Mahata" target="_blank" style="text-decoration: none; color: white;">Uttam Mahata</a>  <br>
        👩‍💻 <a href="https://github.com/Suchana4Hazra" target="_blank" style="text-decoration: none; color: white;">Suchana Hazra</a>  <br>
        👨‍💻 <a href="https://github.com/Sidhupaji-2004" target="_blank" style="text-decoration: none; color: white;">Siddharth Sen</a>  <br>
        <br>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<a class="github-button" href="https://github.com/Anurag-ghosh-12/ipl" target="_blank">GitHub Repository</a>',
    unsafe_allow_html=True,
)
st.markdown("---")
st.markdown("IPL Dataverse | ©Gradient Geeks | Created with Streamlit 👑")