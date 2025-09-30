# File: webapp.py

import streamlit as st
from problem_generator import TOPICS # Import our topics dictionary

# --- App Title and Description ---
st.title("Algebra I 'Do Now' Generator")
st.write("Select a topic from the dropdown menu and click 'Generate Problem' to get a new question.")

# --- UI Elements ---
# Create the dropdown menu for topic selection
selected_topic = st.selectbox("Select a Topic:", options=list(TOPICS.keys()))

# Create two columns for the buttons to appear side-by-side
col1, col2 = st.columns(2)

# --- Button Logic ---
# Generate Problem Button
if col1.button("Generate Problem"):
    # Get the corresponding generator function
    generator_func = TOPICS[selected_topic]
    # Generate and store the new problem/answer in the session state
    st.session_state.problem, st.session_state.answer = generator_func()

# Show Answer Button
if col2.button("Show Answer"):
    # This button doesn't need to do anything itself;
    # it just causes the app to rerun and display the answer below.
    pass

# --- Display Area ---
# Check if a problem has been generated and stored in the session state
if 'problem' in st.session_state:
    st.header("Problem:")
    st.subheader(st.session_state.problem) # Display the problem

    st.header("Answer:")
    # Use an expander to hide the answer until the user clicks on it
    with st.expander("Click to see the answer"):
        st.subheader(st.session_state.answer)