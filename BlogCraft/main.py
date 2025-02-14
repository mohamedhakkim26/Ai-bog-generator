import streamlit as st
from modules.blog_generator import generate_blog
from modules.image_generator import generate_images

st.set_page_config(layout="wide")
st.title('BlogCraft: Your AI Writing Companion')

with st.sidebar:
    st.title('Blog Details')
    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (comma-separated)")
    num_words = st.slider("Number of words", 100, 2000, 100)
    num_images = st.number_input("Number of Images", 1, 5, 1)
    submit_button = st.button("Generate Blog")

if submit_button:
    st.info("Generating content...")
    blog_content = generate_blog(blog_title, keywords, num_words)
    images = generate_images(blog_title, num_images)

    if images:
        from streamlit_carousel import carousel
        carousel(items=images, width=1)

    st.title("Your Blog Post:")
    st.write(blog_content)
