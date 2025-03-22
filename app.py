import streamlit as st
import pickle
import pandas as pd
import time
import matplotlib.pyplot as plt

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

# Sidebar Navigation
st.sidebar.title("🏏 IPL Win Predictor")
menu = st.sidebar.radio("Navigation", ["Prediction Page", "Season Data"])

# General Info & Prediction Page
if menu == "Prediction Page":
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

# Season Data Section
elif menu == "Season Data":
    st.title("📊 IPL Season Analysis")

    st.subheader("Average Runs per match")
    st.image("avg_runs_per_match.png", use_container_width=True)

    st.subheader("Targets 200 plus")
    st.image("targets_200_plus.png", use_container_width=True)

    st.subheader("Average Score per team in the seasons")
    st.image("avg_score_team_season.png", use_container_width=True)

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### Developed by:")
st.sidebar.markdown("👨‍💻 Anurag Ghosh  \n👨‍💻 Uttam Mahata  \n👩‍💻 Suchana Hazra  \n👨‍💻 Siddhart Sen")
st.sidebar.markdown("[GitHub Repository](https://github.com/Anurag-ghosh-12/ipl)")
