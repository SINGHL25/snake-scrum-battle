import streamlit as st
import time
from game_logic import Snake, create_board, get_winner

st.set_page_config(page_title="Snake Scrum Battle", layout="centered")
st.title("🐍 Snake Scrum Battle - Kingdom Showdown")
st.markdown("Let 6 custom snakes from different kingdoms battle for survival in 15 seconds!")

# Step 1: Input form
if "snakes_created" not in st.session_state:
    st.session_state.snakes_created = False

if not st.session_state.snakes_created:
    with st.form("snake_form"):
        names, kingdoms = [], []
        emojis = ["🐍", "🐢", "🐉", "🦎", "🦂", "🦕"]
        for i in range(6):
            name = st.text_input(f"Snake {i+1} Name", value=f"Snake{i+1}")
            kingdom = st.text_input(f"Snake {i+1} Kingdom", value=f"Kingdom{i+1}")
            names.append(name)
            kingdoms.append(kingdom)
        if st.form_submit_button("Let the Battle Begin!"):
            st.session_state.snakes = [Snake(names[i], emojis[i], kingdoms[i]) for i in range(6)]
            st.session_state.snakes_created = True
            st.session_state.running = True
            st.rerun()

# Step 2: Game logic (15-second loop)
if st.session_state.get("running", False):
    game_placeholder = st.empty()
    status_placeholder = st.empty()

    start_time = time.time()
    while time.time() - start_time < 15:
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
            status_placeholder.success(f"🏆 🎈 ⚡ Winner: {winner.name} from {winner.kingdom} {winner.emoji} | Score: {winner.score}")
            st.session_state.running = False
            break
        time.sleep(0.5)

    else:
        status_placeholder.info("⏱️ Time's up! No single winner.")
        st.session_state.running = False

# Step 3: Reset
if st.button("Reset Game"):
    st.session_state.clear()
    st.rerun()


