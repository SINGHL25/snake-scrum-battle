import streamlit as st
import random
import time

st.set_page_config(page_title="Snake Scrum Battle", layout="wide")
st.title("🐍 Snake Scrum Battle Arena")

snake_names = ["ViperX", "CobraKai", "Fangzilla", "Venomatrix", "Serpento", "SlitherKing", "Pythonara"]
players = st.multiselect("Select Snakes (Players)", snake_names, default=snake_names[:6])

start_btn = st.button("Start Battle")

if start_btn and players:
    st.subheader("Battle Started!")
    leaderboard = {p: 0 for p in players}
    with st.empty():
        for i in range(30):
            attacker = random.choice(players)
            target = random.choice([p for p in players if p != attacker])
            leaderboard[attacker] += 1
            st.markdown(f"**{attacker}** engulfed **{target}**!")
            time.sleep(0.3)
        winner = max(leaderboard, key=leaderboard.get)
        st.success(f"🏆 Winner is **{winner}**! They host tomorrow's scrum! 🎤")
        st.balloons()
