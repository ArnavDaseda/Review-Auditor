from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import os

st.set_page_config(page_title="Titan Review Auditor",page_icon="⚡")
st.title("⚡ AI Review Auditor")
st.write("Paste a customer review...")
review_text = st.text_area("customer_review:",height=150,
                           placeholder="paste review here...")
if st.button("Analyze Review"):
    try:
        llm = ChatGroq(
            temperature=0,
            groq_api_key= st.secrets.get("GROQ_API_KEY"),           
            model="llama-3.1-8b-instant",
        )

        template = """
        You are a ruthless business analyst.
        Analyze the following customer review for a hotel.
        Identitfy:
        1. The Sentiment(Positive/Negative)
        2. The Specific Complaint
        3. A Recommended Fix

        Review: {review_text}
        """
        prompt = ChatPromptTemplate.from_template(template)

        chain = prompt|llm
        with st.spinner("The Titan is analyzing..."):
            response=chain.invoke({"review_text":review_text})
            st.success("Analysis Complete")
            st.markdown(response.content)

    except Exception as e:
        st.error(f"System Failure:{e}")