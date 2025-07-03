import streamlit as st
import time
from game_logic import Snake, create_board, get_winner

st.set_page_config(page_title="Snake Scrum Battle", layout="centered")

if "snakes" not in st.session_state:
    st.session_state.snakes = [
        Snake("Alice", "🐍"),
        Snake("Bob", "🐢"),
        Snake("Clara", "🐉"),
        Snake("Danny", "🦎"),
        Snake("Eva", "🦂"),
        Snake("Felix", "🦕"),
    ]

if "running" not in st.session_state:
    st.session_state.running = False

st.title("🐍 Snake Scrum Battle - Dynamic Emoji Edition")
st.markdown("Let 6 brave snakes fight to the end. One winner survives! 🏆")

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
        html_board = "<div style='font-size:30px; line-height:30px;'>"
        for row in board:
            html_board += "".join(cell or "⬜" for cell in row) + "<br>"
        html_board += "</div>"
        game_placeholder.markdown(html_board, unsafe_allow_html=True)

        winner = get_winner(st.session_state.snakes)
        if winner:
            status_placeholder.success(f"🏆 Winner: {winner.name} {winner.emoji} with score {winner.score}")
            st.session_state.running = False
            break
        time.sleep(0.5)

    else:
        status_placeholder.info("Game over. No single winner.")
        st.session_state.running = False

if st.button("Reset Game"):
    st.session_state.snakes = [
        Snake("Alice", "🐍"),
        Snake("Bob", "🐢"),
        Snake("Clara", "🐉"),
        Snake("Danny", "🦎"),
        Snake("Eva", "🦂"),
        Snake("Felix", "🦕"),
    ]
    st.session_state.running = False
    st.rerun()
