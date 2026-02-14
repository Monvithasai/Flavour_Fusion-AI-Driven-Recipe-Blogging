import streamlit as st
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import random

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY"),
    http_options=types.HttpOptions(api_version='v1')
)

def get_joke():

    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache."
    ]
    return random.choice(jokes)

def recipe_generation(user_input, word_count):

    st.write("### Generating your recipe...")

    st.info(f"While I work on creating your blog, here's a little joke:\n\n**{get_joke()}**")

    # Accessing the stable gemini-2.5-flash model
    chat = client.chats.create(model="gemini-2.5-flash")


    prompt = f"Write a recipe based on the input topic: {user_input} and number of words: {word_count}. Ensure it has Ingredients, Instructions, and Tips sections."

    try:
        response = chat.send_message(prompt)
        st.success("Your recipe is ready!")
        return response.text
    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None

def main():

    st.title("RecepieMaster: AI-Powered Blog Generation")
    st.write("Hello! I'm RecepieMaster, your friendly robot. Let's create a fantastic recipe together!")


    topic = st.text_input("Topic", placeholder="e.g., malai kofta")
    word_count = st.number_input("Desired length (words)", min_value=50, max_value=2000, value=300)

    if st.button("Generate recipe"):
        if topic:
            result = recipe_generation(topic, word_count)
            if result:
                st.markdown("---")
                st.markdown(result)
        else:
            st.warning("Please enter a topic first.")

if __name__ == "__main__":
    main()
