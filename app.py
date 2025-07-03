import streamlit as st
import time
from game_logic import Snake, create_board, get_winner

st.set_page_config(page_title="Snake Scrum Battle", layout="centered")

# Initialize snakes only once
if "snakes" not in st.session_state:
    st.session_state.snakes = [
        Snake("S1", "🐍"),
        Snake("S2", "🐢"),
        Snake("S3", "🐉"),
        Snake("S4", "🦎"),
        Snake("S5", "🦂"),
        Snake("S6", "🦕"),
    ]

if "running" not in st.session_state:
    st.session_state.running = False

st.title("🐍 Snake Scrum Battle - Dynamic Edition")
st.markdown("Let the 6 emoji snakes battle on a 10x10 board. One survivor wins! 🏆")

if st.button("Start Battle"):
    st.session_state.running = True

if st.session_state.running:
    game_placeholder = st.empty()
    status_placeholder = st.empty()

    for _ in range(50):
        for snake in st.session_state.snakes:
            snake.update_direction()
            snake.move(create_board(st.session_state.snakes))

        board = create_board(st.session_state.snakes)
        board_str = "\n".join(["".join(row) for row in board])
        game_placeholder.code(board_str)

        winner = get_winner(st.session_state.snakes)
        if winner:
            status_placeholder.success(f"🏆 Winner: {winner.name} {winner.emoji} with score {winner.score}")
            st.session_state.running = False
            break
        time.sleep(0.5)

    else:
        status_placeholder.info("Game over. No single winner.")
        st.session_state.running = False

# Reset button
if st.button("Reset Game"):
    st.session_state.snakes = [
        Snake("S1", "🐍"),
        Snake("S2", "🐢"),
        Snake("S3", "🐉"),
        Snake("S4", "🦎"),
        Snake("S5", "🦂"),
        Snake("S6", "🦕"),
    ]
    st.session_state.running = False
    st.experimental_rerun()
