import streamlit as st
from scraper import summarize

# Page config
st.set_page_config(page_title="Website Scraper", page_icon="🌐")

# Title
st.title("🌐 Web Scraper")
st.markdown("Enter a website URL and get a clean AI-powered summary for extracted content.")

# Input
url = st.text_input("🔗 Enter Website URL")

# Button
if st.button("Extract"):
    if url:
        with st.spinner("Fetching and summarizing..."):
            try:
                summary = summarize(url)
                st.success("Summary generated!")

                # Output box (scrollable)
                st.markdown("### 📄 Extracted Content")
                st.markdown(summary)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a URL.")