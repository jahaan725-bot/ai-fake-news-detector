import streamlit as st
from src.predict import predict_news

st.set_page_config(
    page_title="AI Fake News Detector",
    page_icon="📰"
)

st.title("📰 AI Fake News Detector")

st.write("Paste a news article below and check its credibility.")

article = st.text_area(
    "Enter News Article",
    height=250
)

if st.button("Analyze News"):

    if article.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = predict_news(article)

        st.subheader("Result")

        st.success(
            f"Prediction: {result['prediction']}"
        )

        st.metric(
            "Credibility Score",
            f"{result['credibility_score']}%"
        )

        st.write("Reason:")
        st.write(result["reason"])
