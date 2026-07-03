import streamlit as st

from predictor import predict

st.set_page_config(
    page_title="Social Media Post Depression Detector",
    page_icon="🧠"
)

st.title("🧠 Social Media Post Depression Detector")

st.write(
    "Paste a social media post below."
)

text = st.text_area(
    "Post",
    height=220
)

if st.button("Predict"):

    if text.strip() == "":

        st.warning("Please enter some text.")

    else:

        with st.spinner("Analyzing..."):

            result = predict(text)

        st.success("Prediction Complete")

        st.subheader("Prediction")

        st.info(result["label"])

        st.subheader("Confidence")

        st.progress(result["confidence"]/100)

        st.write(f'{result["confidence"]}%')

        st.subheader("Reason")

        st.info(result["reason"])

st.caption(
    "⚠️ Disclaimer: This application is developed for educational and "
    "demonstration purposes only. It does not provide medical advice or "
    "clinical diagnosis."
)