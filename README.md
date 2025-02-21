import streamlit as st

# Function to calculate PHQ-9 score
def calculate_score(responses):
    return sum(responses)

# Set Streamlit Page Config
st.set_page_config(page_title="Depression Screening Quiz", layout="centered")

# Custom CSS for Background & Styling
st.markdown(
    """
    <style>
        body {
            background-color: #D6EAF8;  /* Light pastel blue */
        }
        .stApp {
            background-color: #D6EAF8; /* Background for full page */
        }
        .stForm {
            background-color: #FFFFFF; /* White form box */
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.1);
        }
        .stButton button {
            background-color: #2874A6 !important;  /* Dark blue submit button */
            color: white !important;
            font-size: 18px !important;
            border-radius: 10px !important;
        }
        .stButton button:hover {
            background-color: #1B4F72 !important; /* Slightly darker on hover */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Instructions
st.markdown("<h1 style='text-align: center; color: #154360;'>🧠 Depression Screening Quiz (PHQ-9)</h1>", unsafe_allow_html=True)
st.write("**Answer all 10 questions to assess depression severity.**")

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

options = ["Not at all ", "Several days ", "More than half the days ", "Nearly every day "]

responses = {}

# Streamlit Form for Better UI
with st.form("quiz_form"):
    st.markdown("<div class='stForm'>", unsafe_allow_html=True)  # Open Styled Form
    for i, q in enumerate(questions):
        responses[q] = st.radio(q, options, key=f"q{i}", index=None)  # No pre-selected option
    st.markdown("</div>", unsafe_allow_html=True)  # Close Styled Form
    
    # Submit Button
    submitted = st.form_submit_button("Submit Quiz")

# Show results after submission
if submitted:
    # Ensure all questions are answered
    if None in responses.values():
        st.error("❌ Please answer all 10 questions before submitting.")
        st.stop()

    # Convert responses to numeric scores
    numeric_responses = [int(res.split("(")[1][0]) for res in responses.values()]
    total_score = calculate_score(numeric_responses)

    st.subheader(f"🔍 Your Depression Severity Score: {total_score}")

    if total_score <= 4:
        st.success("✅ Minimal or No Depression 😊")
    elif total_score <= 9:
        st.info("🟡 Mild Depression - Consider lifestyle changes.")
    elif total_score <= 14:
        st.warning("🟠 Moderate Depression - Seeking help is advisable.")
    elif total_score <= 19:
        st.error("🔴 Moderately Severe Depression - Professional help recommended.")
    else:
        st.error("🚨 Severe Depression - Please seek immediate professional support.")

    # Next Step Suggestion
    if total_score >= 10:
        st.write("💡 **Next Step:** Try our AI-based **Facial Expression Analysis** for deeper insights!")

  
