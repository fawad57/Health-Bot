import google.generativeai as genai
from sentiment import detect_sentiment
from utils import format_doctor_data, filter_doctors_by_specialty
from data import DOCTOR_DATA

# Initialize LLM (to be configured in main app)
convo = None

def initialize_chat(config):
    """Initialize the chat with API configuration."""
    global convo
    # Access the decode_api_key function and encoded_api_key from the config dictionary
    decode_api_key = config["decode_api_key"]
    encoded_api_key = config["encoded_api_key"]
    genai.configure(api_key=decode_api_key(encoded_api_key))
    convo = genai.GenerativeModel(model_name="gemini-1.5-pro").start_chat()

def chat_interface(mode, user_input):
    """Handle chat interactions based on the selected mode."""
    if mode == "General OPD":
        response, sentiment_msg = handle_general_opd(user_input)
        return response, sentiment_msg
    elif mode == "Medical Advice":
        return medical_consultance(user_input, mode)
    elif mode == "Symptom Checker":
        from csp_solver import check_symptoms
        from data import symptom_conditions
        return check_symptoms(user_input, symptom_conditions), ""
    else:
        return "Please select a valid mode.", ""

def handle_general_opd(user_input):
    """Process General OPD queries with sentiment analysis."""
    sentiment, sentiment_message = detect_sentiment(user_input)
    if user_input.lower() == "list all doctors":
        response = format_doctor_data()
    elif "specialist" in user_input.lower():
        specialty = user_input.split("specialist in ")[-1].strip()
        response = filter_doctors_by_specialty(specialty)
    else:
        response = "Sorry, I couldn't understand your query. Please ask about doctors or specialties."
    return response, sentiment_message if sentiment in ["negative", "positive"] else ""

def medical_consultance(script, mode):
    """Provide medical consultations based on user input with sentiment analysis."""
    # Detect sentiment
    sentiment, sentiment_message = detect_sentiment(script)

    if mode == "General OPD":
        prompt = f"""
            - Provide General OPD services, including doctor availability and specialties.
            - Use the following data for answers:
              {DOCTOR_DATA}.
            - Answer queries clearly without suggesting medicines or diets.
            - Keep the output simple and easy to understand by the user.
            - Do not reply with useless information such as "I'm sorry, but I cannot provide medical advice."
            User Input: {script}
            """
    elif mode == "Medical Advice":
        # Adjust prompt based on sentiment
        if sentiment == "negative":
            script = f"{script} (Note: User might be feeling negative, provide empathetic response)"
        prompt = f"""
            - Act as a doctor providing personalized advice.
            - Recommend medicines and diet plans based on symptoms or conditions.
            - If it asks any General OPD question, reply "KINDLY CHOOSE 'General OPD' mode as this is not my work."
            User Input: {script}
            """
    else:
        return "Invalid mode for medical consultation.", ""

    try:
        response = convo.send_message(prompt)
        return response.text, sentiment_message
    except Exception as e:
        return f"Error Occurred: {e}", ""