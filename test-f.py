import streamlit as st
import streamlit.components as components
media_url="https://www.instagram.com/p/C4YGDd0y5xC/"
components.v1.html(f'<blockquote class="instagram-media" data-instgrm-permalink="{media_url}" data-instgrm-version="13"></blockquote><script async src="//www.instagram.com/embed.js"></script>', width=400, height=400, scrolling=True)