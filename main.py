import streamlit as st
import requests
import json

sublist = (dadjokes,memes,wholesomememes,jokes,ihadastroke)
subreddit = st.multiselect("Your subreddit:",sublist)
if st.button("Generate meme"):
    if subreddit != "":    
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
