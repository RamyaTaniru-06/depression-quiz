import joblib
import pandas as pd

# Load the trained model
model = joblib.load("saved_model.pkl")
print("✅ Model loaded successfully!")

# Load the TF-IDF vectorizer
vectorizer = joblib.load("saved_vectorizer.pkl")
print("✅ Vectorizer loaded successfully!")

# Take user input
input_text = input("Enter a tweet/message: ")

# Vectorize input text
input_vectorized = vectorizer.transform([input_text])

# Convert to DataFrame to maintain feature names
feature_names = vectorizer.get_feature_names_out()
input_vectorized_df = pd.DataFrame(input_vectorized.toarray(), columns=feature_names)

# Predict
prediction = model.predict(input_vectorized_df)[0]

# Define severity levels & recommendations
severity_mapping = {
    "Normal": ("Low Depression Risk", "Maintain a healthy routine. Practice mindfulness."),
    "Depression": ("Moderate Depression Risk", "Engage in therapy or talk to someone you trust."),
    "Suicidal": ("High Depression Risk", "Seek immediate help from professionals or helplines."),
    "Anxiety": ("Moderate Anxiety", "Practice deep breathing and relaxation techniques."),
    "Bipolar": ("Mood Instability", "Monitor mood changes and maintain routine."),
    "Stress": ("High Stress Level", "Manage stress with exercise and meditation."),
    "Personality disorder": ("Personality Disorder", "Seek therapy for structured intervention.")
}

severity_level, recommendation = severity_mapping.get(prediction, ("Unknown", "No recommendation available."))

# Output prediction
print(f"\n📝 Prediction: {prediction}")
print(f"⚠️ Severity Level: {severity_level}")
print(f"💡 Recommendation: {recommendation}")
