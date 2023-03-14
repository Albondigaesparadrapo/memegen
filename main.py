import streamlit as st
import requests
import json

subreddit = st.text_input
if subreddit != "":    
    if st.button("Generate meme"):
        url = "https://meme-api.com/gimme/"+subreddit
        rspt = requests.get(url)
        data = json.loads(rspt.text)
        meme = data["url"]
        memetitle = data["title"]
        memeauthor = data["author"]
        st.header(memetitle)
        st.markdown("---")
        st.subheader("Submitted by "+memeauthor)
        st.markdown("![Our meme]("+meme+")")
