Health Bot
A Streamlit-based medical consultation application that provides General OPD services, medical advice, and symptom checking using a CSP (Constraint Satisfaction Problem) solver with heuristics (MRV, Degree, LCV, Value-Ordering).
Features

General OPD Mode: View doctor availability and specialties.
Medical Advice Mode: Get personalized medical advice and recommendations.
Symptom Checker Mode: Analyze symptoms and suggest possible conditions with confidence scores.

Prerequisites

Python 3.8 or higher
Git
Internet connection (for API calls)

Installation
Clone the Repository

Open your terminal or command prompt.
Run the following command to clone the repository:git clone https://github.com/fawad57/Health-Bot.git

Replace your-username with your GitHub username.
Navigate to the project directory:cd Health-Bot

Set Up a Virtual Environment

Create a virtual environment:python -m venv venv

Activate the virtual environment:
On Windows:.\venv\Scripts\Activate.ps1

On macOS/Linux:source venv/bin/activate

Install Dependencies

Install the required Python packages:pip install -r requirements.txt

Configure API Key

Ensure the encoded_api_key in src/config.py is set to a valid Google Generative AI API key (base64 encoded).
Decode and use it as per the decode_api_key function.

Running the Application

With the virtual environment activated, run the application:streamlit run src/app.py

Open your browser and go to http://localhost:8501 to use the app.

Usage

Select a mode from the dropdown (General OPD, Medical Advice, Symptom Checker).
Enter your query or symptoms in the input box and click "Send".
View the bot's response in the chat interface.

Project Structure
Health-Bot/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── src/
│ ├── config.py # API configuration
│ ├── data.py # Static data (doctors, symptoms)
│ ├── sentiment.py # Sentiment analysis
│ ├── csp_solver.py # CSP-based symptom checker
│ ├── utils.py # Utility functions
│ ├── chat.py # Chat logic
│ ├── app.py # Main entry point
│ └── streamlit_app.py # Streamlit UI
└── docs/
└── (optional docs)

Requirements
Create a requirements.txt file with the following content:
streamlit
google-generativeai
textblob

Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Please follow the guidelines in CONTRIBUTING.md (if added).
License
This project is licensed under the MIT License - see the LICENSE file for details.
Contact
For issues or questions, please open an issue on the GitHub repository or contact [fawadhuayun96@gmail.com].
