import streamlit as st

# Title and Introduction (Professional Look)
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")
st.title("🌱 Growth Mindset Challenge 🌱")
st.markdown("""
    **Welcome to the Growth Mindset App!** 💡  
    A growth mindset is the belief that abilities can be developed through dedication and hard work. Let's start exploring it together! 💪
    
    This app will help you set your learning goals, reflect on challenges, track your progress, and stay motivated. Let's begin!
""")

# Goal Setting Section (Interactive)
st.header("🎯 Set Your Learning Goals 📚")
goal = st.text_input("What is your growth goal for this week? 🗓️", placeholder="E.g., Improve coding skills, read a new book")
if goal:
    st.success(f"✅ Your goal for the week is: *{goal}*")

# Display a Reflection Prompt (User-Friendly)
st.header("📝 Reflection Time 🧠")
reflection = st.text_area("Reflect on a challenge you faced recently and what you learned from it: 🤔", 
                          placeholder="Write here...")
if reflection:
    st.write(f"💬 Your Reflection: *{reflection}*")

# Progress Tracker with Professional Look
st.header("📊 Track Your Progress 🏆")
st.write("**How far have you come in achieving your goal?** 📈")
progress = st.radio("Select your progress status:", 
                    ("No progress 🚫", "Some progress 📊", "Goal achieved ✅"))
if progress:
    st.success(f"💪 Your progress: *{progress}*")

# Show Motivational Quote (Professional & Inspiring)
st.header("🌟 Stay Motivated! 🌟")
st.write("Here's a motivational quote to keep you going: 💬")
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "Success is the sum of small efforts, repeated day in and day out. - Robert Collier"
]
st.markdown(f"**💬 {quotes[0]}**")

