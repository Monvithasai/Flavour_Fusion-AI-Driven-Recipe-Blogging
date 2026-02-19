# Flavour_Fusion-AI-Driven-Recipe-Blogging

🍽 Flavour Fusion:AI Driven Recipe Blogging


Flavour Fusion is a Generative AI-powered web application that automatically creates structured recipe blog posts based on user input. The system integrates Google Gemini 2.5 Flash to generate high-quality, engaging culinary content.

Developed as part of the Google Cloud Generative AI Internship Program.

🚀 Features
👉AI-powered recipe blog generation

👉Custom word count selection

👉Structured blog format (Ingredients, Instructions, Tips)

👉Interactive Streamlit user interface

👉Fun programmer joke displayed during generation

👉Secure API key management using .env file

🛠 Tech Stack

👉Python

👉Streamlit

👉Google Generative AI (Gemini 2.5 Flash)

👉python-dotenv

👉dotenv

📂 Project Structure
FlavourFusion/

│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── ProjectInitialization and Planning/
├── Data Collection and Preprocessing/
├── Model Development/
├── Project Documentation/
│
└── outputs/


👉Install Dependencies

pip install -r requirements.txt

👉Create a .env File

Create a file named .env and add:

GOOGLE_API_KEY=your_api_key_here

👉Run the Application

streamlit run app.py

The app will open in your browser at:

http://localhost:8501

🧠 How It Works

User enters a recipe topic and desired word count.

The backend formats a structured prompt.

The prompt is sent to Gemini 2.5 Flash via Google Generative AI API.

The model generates a structured recipe blog.

The content is displayed on the Streamlit interface.

🤖 Model Used

Gemini 2.5 Flash

Large Language Model (LLM)

Transformer-based architecture

Hosted on Google Cloud

Optimized for fast text generation

🎥 Demo Video

https://drive.google.com/file/d/1bcaL1b9OWpdhG25Xg1R9m4GqgkzsetNR/view?usp=sharing


