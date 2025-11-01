import os
from dotenv import load_dotenv
import google.generativeai as genai

# ✅ Load environment variables
load_dotenv()

# ✅ Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("⚠️ API key not found! Please put your key into a file named .env like:\nGEMINI_API_KEY=your_key_here")

# ✅ Configure Gemini API
genai.configure(api_key=api_key)

# ✅ Choose a valid model name (based on the docs)
model = genai.GenerativeModel("gemini-2.5-flash")  # this is a current model name per docs :contentReference[oaicite:2]{index=2}

print("🤖 RoyalChatbot is online! Type 'exit' to stop.\n")

# ✅ Simple chat loop
while True:
    user_input = input("You: ")
    if user_input in ["exit", "quit"]:
        print("👋 RoyalChatbot: Goodbye!")
        break

    # 🎯 Custom replies
    elif user_input in ["hi", "hello", "hey"]:
        print("RoyalChatbot: 👑 Hello there! I'm RoyalChatbot — how are you today?")
        continue
    elif "how are you" in user_input:
        print("RoyalChatbot: 😊 I'm feeling royal as always! What about you?")
        continue



    response = model.generate_content(user_input)
    print("RoyalChatbot:", response.text)
