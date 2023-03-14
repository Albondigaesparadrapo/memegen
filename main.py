import streamlit as st
import requests
import json

if st.button("Generate meme"):
    url = "https://meme-api.com/gimme/memes"
    rspt = requests.get(url)
    data = json.loads(rspt.text)
    meme = data["url"]
    memetitle = data["title"]
    memeauthor = data["author"]
    st.header(memetitle)
    st.markdown("---")
    st.subheader("Submitted by "+memeauthor)
    st.markdown("![Our meme]("+meme+")")
