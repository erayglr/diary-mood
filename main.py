import streamlit as st
import plotly.express as px
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path

st.title("Diary Tone")
st.subheader("Positivity")

allFiles = glob.glob("diary/*.txt")

analyzer = SentimentIntensityAnalyzer()
positiveDatas = []
negativeDatas = []

for files in allFiles:
    with open(files, "r") as file:
        days = file.read()
    scores = analyzer.polarity_scores(days)
    positiveDatas.append(scores["pos"])
    negativeDatas.append(scores["neg"])

allFiles = [Path(file).stem.replace("2023-10-", "Oct") for file in allFiles]

figure = px.line(x=allFiles, y=positiveDatas, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")

figure2 = px.line(x=allFiles, y=negativeDatas, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure2)