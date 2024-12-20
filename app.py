import streamlit as st
from newspaper import Article


def extract_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text


# Streamlit App
st.title("Article Summariser")

url_input = st.text_input("Enter the article URL:")

if url_input:
    try:
        article_text = extract_article(url_input)
        st.write(article_text)
    except Exception as e:
        st.error(f"Error extracting article: {e}")
