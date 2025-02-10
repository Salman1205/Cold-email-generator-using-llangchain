## 🚀 Overview
The **Cold Email Generator** is a powerful AI-driven tool that automates the process of crafting personalized cold emails based on job descriptions. This project utilizes **LangChain**, **Streamlit**, and **Chromadb** to analyze job postings, extract relevant skills, and generate professional emails with links to your portfolio.

## 📌 Features
- Extracts job descriptions from URLs.
- Uses AI to analyze required skills.
- Matches skills with your portfolio links.
- Generates customized cold emails instantly.
- User-friendly interface with **Streamlit**.

## 🛠️ Technologies Used
- **Python** 🐍
- **LangChain** (for AI-based job extraction and email generation)
- **Streamlit** (for the frontend UI)
- **Chromadb** (for vector storage of portfolio data)
- **Pandas** (for data manipulation)
- **UUID** (for unique document identification)

## 📂 Project Structure
```
Cold-Email-Generator-Langchain/
│── app/
│   ├── main.py         # Streamlit app
│   ├── portfolio.py    # Portfolio handling (CSV-based)
│   ├── chains.py       # AI model interaction
│   ├── utils.py        # Helper functions
│── resource/
│   ├── my_portfolio.csv  # CSV file with portfolio data
│── requirements.txt           # Project requirements
│── README.md           # Project documentation
```

## 🔧 Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Salman1205/Cold-Email-Generator-llangchain.git
cd Cold-Email-Generator-llangchain
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Streamlit App**
```bash
streamlit run app/main.py
```

## 📜 How It Works
1. Enter a **job URL** in the Streamlit UI.
2. The app scrapes the job description.
3. AI extracts **required skills**.
4. Portfolio links are retrieved from **Chromadb**.
5. A personalized email is generated.
6. The email is displayed in the UI for copying.

## 🤝 Contributing
Feel free to fork the repository, create a branch, and submit a pull request!

## 🛡️ License
This project is licensed under the **MIT License**.

---

🚀 **Developed by [Salman1205](https://github.com/Salman1205)**



write it in this format for my linkeding keep it short:
Music Recommendation System
Music Recommendation System
A project that suggests similar songs by extracting and analyzing audio features using a neural network model, with additional features such as song lyrics display and a web interface.

Functionality:
>Extracts MFCC (Mel-frequency cepstral coefficients) features from audio files and stores them in a MongoDB database.
>Trains a neural network model with the extracted features and evaluates its performance.
>Utilizes Apache Kafka for efficient data streaming and processing during feature extraction and model training.
>Built a website using Flask to interact with the recommendation system, allowing users to query for similar songs.
>Implements speech recognition and NLP to print song lyrics on the website, enhancing user experience.
