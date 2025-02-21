import streamlit as st

# Function to calculate PHQ-9 score
def calculate_score(responses):
    return sum(responses)

# Streamlit UI
st.title("🧠 Depression Screening Quiz (PHQ-9)")

st.write("Answer the following 10 questions to assess depression severity.")

# Questions and answer choices (PHQ-9 scale)
questions = [
    "1. Little interest or pleasure in doing things?",
    "2. Feeling down, depressed, or hopeless?",
    "3. Trouble falling or staying asleep, or sleeping too much?",
    "4. Feeling tired or having little energy?",
    "5. Poor appetite or overeating?",
    "6. Feeling bad about yourself, or that you are a failure?",
    "7. Trouble concentrating on things (e.g., reading or watching TV)?",
    "8. Moving or speaking so slowly that others notice? Or being fidgety/restless?",
    "9. Thoughts that you would be better off dead, or hurting yourself?",
    "10. Feeling nervous, anxious, or on edge?"
]

options = ["Not at all (0)", "Several days (1)", "More than half the days (2)", "Nearly every day (3)"]

# User responses
responses = []
for q in questions:
    response = st.radio(q, options, index=0)
    responses.append(int(response.split("(")[1][0]))  # Extract numeric value from response

# Calculate total score
total_score = calculate_score(responses)

# Show results when user submits
if st.button("Submit Quiz"):
    st.subheader("🔍 Your Depression Severity Score: " + str(total_score))
    
    if total_score <= 4:
        st.success("Minimal or No Depression 😊")
    elif total_score <= 9:
        st.info("Mild Depression 🟡 - Consider lifestyle changes.")
    elif total_score <= 14:
        st.warning("Moderate Depression 🟠 - Seeking help is advisable.")
    elif total_score <= 19:
        st.error("Moderately Severe Depression 🔴 - Professional help recommended.")
    else:
        st.error("Severe Depression 🚨 - Please seek immediate professional support.")

    # Next Step Suggestion
    if total_score >= 10:
        st.write("💡 **Next Step:** Try our AI-based **Facial Expression Analysis** for deeper insights!")

# Run the script with: streamlit run quiz_app.py
