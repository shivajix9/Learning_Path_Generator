import streamlit as st
from main import learning_path_chain
import re

st.title("📚 Learning Path Generator")

skill = st.text_input("Enter Skill")

if st.button("Generate Roadmap"):

    # Edge Case 1: Empty Input
    if not skill.strip():
        st.warning("Please enter a skill.")
        st.stop()

    # Edge Case 2: Only Numbers
    if skill.isdigit():
        st.error("Skill must contain text.")
        st.stop()

    # Edge Case 3: Very Long Input
    if len(skill) > 100:
        st.error("Skill name is too long.")
        st.stop()

    # Edge Case 4: Special Characters Only
    if not re.search(r"[A-Za-z]", skill):
        st.error("Please enter a valid skill.")
        st.stop()

    try:
        result = learning_path_chain.invoke(
            {"skill": skill}
        )

        st.subheader("Learning Stages")

        for stage in result.learning_stages:
            st.write(f"✅ {stage}")

        st.subheader("Key Topics")

        for topic in result.key_topics:
            st.write(f"📚 {topic}")

        st.subheader("Learning Goal Summary")

        st.info(result.learning_goal_summary)

    except Exception as e:
        st.error(f"Error generating roadmap: {e}")