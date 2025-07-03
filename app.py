import streamlit as st
import time
from game_logic import Snake, get_winner

st.set_page_config(page_title="Snake Scrum Battle", layout="centered")

if "snakes" not in st.session_state:
    st.session_state.snakes = [Snake(f"Snake {i+1}") for i in range(6)]

st.title("🐍 Snake Scrum Battle 🐍")
st.image("assets/snake1.png,snake2.png,snake3.png,snake4.png,snake5.png,snake6.png,snake7.png", width=100)
st.write("Six snakes enter the battle... only one survives!")

if st.button("Start Game"):
    for _ in range(30):
        for snake in st.session_state.snakes:
            snake.move()
        winner = get_winner(st.session_state.snakes)
        if winner:
            st.success(f"🏆 Winner: {winner} 🏆")
           
            break
        time.sleep(0.3)
    else:
        st.warning("It's a draw! Everyone is tired.")

    st.subheader("Final Scores:")
    for s in st.session_state.snakes:
        st.write(f"{s.name}: {'Alive' if s.alive else 'Dead'} | Score: {s.score}")
