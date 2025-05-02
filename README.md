# 🩺 Health Bot

**Health Bot** is a Streamlit-based medical consultation application offering General OPD services, personalized medical advice, and symptom checking powered by a **Constraint Satisfaction Problem (CSP)** solver with heuristics like **MRV**, **Degree**, **LCV**, and **Value-Ordering**.

---

## ✨ Features

- **General OPD Mode:**  
  View doctor availability and specialties.

- **Medical Advice Mode:**  
  Get personalized medical advice and recommendations.

- **Symptom Checker Mode:**  
  Analyze symptoms and receive possible condition suggestions with confidence scores.

---

## 🧰 Prerequisites

- Python 3.8 or higher  
- Git  
- Internet connection (for API calls)

---

## 🚀 Installation

### 1. Clone the Repository
- Open your terminal or command prompt.
- Run the following command to clone the repository:

```bash
git clone https://github.com/fawad57/Health-Bot.git
cd Health-Bot
````

---

### 2. Set Up a Virtual Environment

#### On Windows:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure API Key

Ensure the `encoded_api_key` in `src/config.py` is set to a valid **Google Generative AI API key** (base64 encoded).
Use the `decode_api_key()` function to decode and use the key appropriately.

---

## 🏃‍♂️ Running the Application

With the virtual environment activated, run:

```bash
streamlit run src/app.py
```

Open your browser and navigate to:
[http://localhost:8501](http://localhost:8501)

---

## 💬 Usage

1. Select a mode from the dropdown (`General OPD`, `Medical Advice`, or `Symptom Checker`).
2. Enter your query or symptoms in the input box.
3. Click **Send**.
4. View the bot's response in the chat interface.

---

## 📁 Project Structure

```
Health-Bot/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── src/
│   ├── config.py         # API configuration
│   ├── data.py           # Static data (doctors, symptoms)
│   ├── sentiment.py      # Sentiment analysis
│   ├── csp_solver.py     # CSP-based symptom checker
│   ├── utils.py          # Utility functions
│   ├── chat.py           # Chat logic
│   ├── app.py            # Main entry point
│   └── streamlit_app.py  # Streamlit UI
└── docs/
    └── (optional docs)
```

---

## 📦 Requirements

Create a `requirements.txt` file with the following content:

```text
streamlit
google-generativeai
textblob
```

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository, make improvements, and submit a pull request.


---

## 📝 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for more details.

---

## 📬 Contact

For issues or suggestions, please [open an issue](https://github.com/your-username/Health-Bot/issues)
or contact: **[fawadhumayun96@gmail.com](mailto:fawadhumayun96@gmail.com)**

---
