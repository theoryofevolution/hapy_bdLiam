import streamlit as st
import pandas as pd
from datetime import datetime
import csv
import os

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday, Liam!",
    page_icon="🎉",
    layout="wide",  # Set the layout to wide
    initial_sidebar_state="collapsed"
)

# Set background color to yellow
page_bg_img = '''
<style>
body {
background-color: yellow;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and subtitle
st.title("🎉 Happy Birthday, Liam! 🎂")
st.subheader("Wishing you a day filled with love, joy, and celebration!")

# Current date and time
now = datetime.now()
st.write(f"Today is: {now.strftime('%A, %B %d, %Y')}")

# Birthday Message
st.write("""
***Hey Liam,***

***On this special day, We want to take a moment to let you know how amazing you are. May your birthday be as incredible as you are, filled with all the happiness and love you deserve. Here's to another year of fantastic adventures and wonderful memories.***

***Happy Birthday!***

***With love,***
***Yash, Mumble, Katherine, Nathan, Parnika, and the rest of the 99!***
""")

# Confetti effect
st.balloons()

# Embed audio file
st.markdown("### 🎶 Play this song before looking at anything Liam!")
audio_file = 'Coldplay - Yellow.mp3'
if os.path.exists(audio_file):
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')

# Create two columns
col1, col2, col3 = st.columns(3)

with col1:
    # Display images
    st.write("### Birthday Photos")
    image_files = [
        "IMG_3138.jpg", "IMG_3637.jpg", "IMG_4174.jpg", "IMG_5030.jpg",
        "IMG_5321.jpg", "IMG_5689.jpg", "IMG_7114.jpg", "IMG_7838.jpg", "IMG_7844.png",
        "20231206_154223.jpg", "20240129_100548.jpg"
    ]

    for image_file in image_files:
        if os.path.exists(image_file):
            st.image(image_file, use_column_width=True)

with col2:
    # Interactive component - Birthday wishes
    st.write("### Leave a Birthday Wish for Liam")
    name = st.text_input("Your Name")
    message = st.text_area("Your Birthday Wish")
    if st.button("Send Wish"):
        if name and message:
            with open('messages.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, message])
            st.success("Your message has been sent!")
with col3:
    # Display messages
    st.write("### Birthday Wishes from Friends")
    if st.button("Para Lima: Refresh Messages"):
        df = pd.read_csv('messages.csv')
        for index, row in df.iterrows():
            st.write(f"**{row['name']}**: {row['message']}")
