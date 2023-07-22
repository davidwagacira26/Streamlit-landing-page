import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Project Music", page_icon="::musical_note::", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---LOAD ASSETS--
lottie_coding = load_lottieurl("https://lottie.host/09e7c6d3-77d8-4e17-b815-12c9c2162783/adAhhd0YWr.json")

# ---HEADER SECTION---
with st.container():
    st.subheader("Hi, I'm David :blush:")
    st.title("Spotify Curator From Kenya")
    st.write("###")
    st.write(
        """
       "Project Music is one of the upcoming music platform based in Kenya which
       was started on May 2020 by David, holding a total of over 7500 
       total Spotify followers. Its main is to make artist's
       music to be heard and making their talent and passion for music recognized.
       If interested to submit your music for a review, the links are below.
        """
    )

    st.write("[Groover Link >](https://groover.co/band/signup/referral/influencer/2989/?utm_source=widget&utm_medium=widget_banner&utm_campaign=0.kenyan-hits&widget_id=2989)")
    st.write("[Submithub Link >](https://www.submithub.com/to/project-music)")

# ---ABOUT SECTION---
with st.container():
    st.write("---")

    left_column, right_column = st.columns(2)
    left_column.header("Playlists")

    # Corrected placement of the text
    left_column.write("Here are some of the playlists curated by Project Music.")

    left_column.write("###")
    playlist_links = [
        "[1.Sol Generation](https://open.spotify.com/playlist/3wXSFmXCk2GsT4qEuJ3ZfY?si=63b3d4f1e35f4fac)",
        "[2.Nostalgic Memories](https://open.spotify.com/playlist/5rJVxgesjLqWkGsBnl2RgK?si=0722721306564170)",
        "[3.Kenyan Hits](https://open.spotify.com/playlist/5GOwcAxcNIU2l6MoesmbBX?si=7d0348e124594991)",
        "[4.Rap Rewind](https://open.spotify.com/playlist/0WIijLnD4AE6Z3oRxelgi9?si=71623b5ee32e4a6f)",
        "[5.Afro Vibes](https://open.spotify.com/playlist/4JHj4zwzUMnu2VdvmijWGt?si=f76603eda9c64977)",
        "[6.R&B Pulse](https://open.spotify.com/playlist/2dk65hHvatH8Gzju02sA3V?si=d68b8469ee33491f)",
        "[7.00s and 10s](https://open.spotify.com/playlist/5FyrhALzoQ9YkIpcg1iW1a?si=969b50457ac94e52)",
        "[8.Rap Daily](https://open.spotify.com/playlist/3QAJE0PvNBAAvac94ic4Xk?si=3fda828547c64af6)",
        "[9.Pop Daily](https://open.spotify.com/playlist/3ZsTKr69pZkvDqeXqLnomy?si=e15b829b70044f6e)",
        "[10.UK Drill](https://open.spotify.com/playlist/2EautQVyDw0lU12crIyXAU?si=8e5bf0b7a3ec439b)",
        "[11.Hits Alert](https://open.spotify.com/playlist/0UyK8I4ZC3X2uEqZUNs7o8?si=427f786aab9b44b9)",
        "[12.EDM Party](https://open.spotify.com/playlist/6STy61hWywyHS2tKIEXuI7?si=0114b964cff24780)"
    ]

    for link in playlist_links:
        left_column.markdown(link)

    with right_column:
        st_lottie(lottie_coding, height=300, key="Spotify")

        # ---GALLERY---
        with st.container():
            st.write("---")
            st.header("Top Playlists")
            st.write("##")
            image_column, text_column = st.columns((1, 2))

            with image_column:
                st.image("https://projectmusicke.files.wordpress.com/2022/08/20220808_094248_0000_1_900x900.png")

            with text_column:
                st.subheader("Kenyan Hits")
                st.write(
                    """
                   Fresh tunes from Kenya right now.
                    """
                )

            # Additional image and text
            image_column2, text_column2 = st.columns((1, 2))

            with image_column2:
                # Assuming the link is an image link
                st.image("https://afrikalyrics.com/assets/artistes/sol-generation.jpg")

            with text_column2:
                st.subheader("Sol Generation")
                st.write(
                    """
                   Top Hits from the Sol Generation Group.
                    """
                )
        # ---CONTACT---
    with st.container():
        st.header("Contact")
        with st.form(key='contact_form'):
            st.text_input(label="Name")
            st.text_input(label="Email")
            st.text_area(label="Message")
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.success("Thank you for your message. We will get back to you shortly.")
