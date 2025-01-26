import streamlit as st
import google.generativeai as genai

api_key = "AIzaSyDVKcpobld-urla1N8hmCEeWNRO-WNo87k"
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

st.title("AI-Powered Travel Planner")
st.subheader("Plan your dream trip with a personalized travel itinerary")

st.header("Tell us about your trip")
destination = st.text_input("Destination", placeholder="e.g., Paris, Tokyo")
budget = st.selectbox("Budget", ["Low", "Moderate", "Luxury"])
trip_duration = st.number_input("Trip Duration (in days)", min_value=1, max_value=30, step=1)
purpose = st.text_input("Purpose", placeholder="e.g., romantic getaway, adventure, family trip")
preferences = st.text_area(
    "Preferences",
    placeholder="e.g., fine dining, cultural walks, hidden gems, no dietary restrictions",
)

def refine_inputs(destination, budget, trip_duration, purpose, preferences):
    if not destination or not budget or not trip_duration or not purpose:
        return "Please fill out all the fields for better refinement!"
    
    refinement_prompt = f"""
    Based on the following trip details:
    - Destination: {destination}
    - Budget: {budget}
    - Duration: {trip_duration} days
    - Purpose: {purpose}
    - Preferences: {preferences}

    Refine these preferences and ask any additional questions needed for planning.
    """

    response=model.generate_content(refinement_prompt)
    return response.text

def generate_itinerary(destination, budget, trip_duration, purpose, preferences):
    if not destination or not budget or not trip_duration or not purpose:
        return "Please provide all details to generate your itinerary!"
    
    itinerary_prompt = f"""
    Create a detailed day-by-day travel itinerary for:
    - Destination: {destination}
    - Budget: {budget}
    - Duration: {trip_duration} days
    - Purpose: {purpose}
    - Preferences: {preferences}

    Include morning, afternoon, and evening activities aligned with preferences.
    """
    response=model.generate_content(itinerary_prompt)
    return response.text

st.header("Refine your preferences")
if st.button("Refine Inputs"):
    with st.spinner("Refining your preferences..."):
        refined_output = refine_inputs(destination, budget, trip_duration, purpose, preferences)
        st.text_area("Refined Preferences", refined_output, height=150)

st.header("Generate your itinerary")
if st.button("Generate Itinerary"):
    with st.spinner("Generating your itinerary..."):
        itinerary = generate_itinerary(destination, budget, trip_duration, purpose, preferences)
        st.text_area("Your Personalized Itinerary", itinerary, height=400)

