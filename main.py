import streamlit as st
import os
import base64
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="Ayushi's Portfolio", page_icon="🌟", layout="wide")

# --- Function to load local image ---
def get_base64_image(image_path):
    """Converts a local image file to a base64 string."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None # Return None if file is not found

# --- Image loading ---
image_path = "assets/Profile1.jpg" # The path to your image
base64_image = get_base64_image(image_path)

# Set the final image source
if base64_image:
    # If image loaded, use the base64 data
    image_src = f"data:image/jpg;base64,{base64_image}"
else:
    # Fallback placeholder if image is not found
    image_src = "https://placehold.co/300x300/f0f0f0/3a506b?text=Your+Photo"
    # Show a warning in the app console (or terminal)
    print("Warning: 'assets/Profile.jpg' not found. Using placeholder.")


# --- CSS STYLING ---
st.markdown(
    """
    <style>
        body {
            overflow: hidden; /* Prevents scrolling on this page */
        }
        
        .stApp {
            background-color: #3a506b; /* Kept your background color */
            height: 100vh;
            display: flex;
            flex-direction: column;
        }

        /* This new container safely centers your content */
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            width: 100%;
            height: 100%; /* Take up all available space */
            padding-top: 5vh; /* Add some space at the top */
        }

        /* All your other styles are preserved as you liked them */
        .profile-container {
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            margin-bottom: 20px;
        }
        .profile-circle {
            width: 300px;
            height: 300px;
            border-radius: 50%;
            border: 2px solid #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        .profile-img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover; /* Changed from 'cover' to 'contain' */
        }
        .title {
            color: white;
            font-size: 50px;
            font-weight: bold;
            text-align: center;
        }
        .subtitle1 {
            color: white;
            font-size: 25px;
            font-weight: normal;
            text-align: center;
        }
        .subtitle2 {
            color: white;
            font-size: 20px;
            font-weight: normal;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- START OF THE MAIN CONTAINER ---
# We wrap all your content in this new safe container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Profile Image with Circular Frame
st.markdown(f"""
    <div class='profile-container'>
        <div class='profile-circle'>
            <img src='{image_src}' class='profile-img'>
        </div>
    </div>
""", unsafe_allow_html=True)


# Typing Animation
components.html(
    """
    <div style="text-align: center;">
        <span class="dynamic-text"></span>
    </div>

    <script>
        const texts = ["Hi, I'm Ayushi !", "i_like_to_code.py" , "I am addicted to coffee ☕ !!"];
        let index = 0;
        let charIndex = 0;
        let isDeleting = false;

        function typeEffect() {
            let currentText = texts[index];
            let displayedText = currentText.substring(0, charIndex);
            
            // Find the element once
            const dynamicTextElement = document.querySelector(".dynamic-text");
            if (dynamicTextElement) {
                dynamicTextElement.textContent = displayedText;
            }

            if (!isDeleting && charIndex < currentText.length) {
                charIndex++;
                setTimeout(typeEffect, 100);
            } else if (isDeleting && charIndex > 0) {
                charIndex--;
                setTimeout(typeEffect, 50);
            } else {
                isDeleting = !isDeleting;
                if (!isDeleting) index = (index + 1) % texts.length;
                setTimeout(typeEffect, 1000);
            }
        }

        // Run the script after the element is definitely in the DOM
        if (document.readyState === 'loading') {
            document.addEventListener("DOMContentLoaded", typeEffect);
        } else {
            typeEffect(); // DOM is already loaded
        }
    </script>

    <style>
        .dynamic-text {
            border-right: 2px solid white;
            padding-right: 5px;
            font-weight: bold;
            color: white;
            font-size: 50px;
            display: inline-block;
            text-align: center;
            min-height: 1.2em; /* Prevents layout shift */
        }
    </style>
    """,
    height=100
)

# Subtitles
st.markdown(
    """
    <div class='subtitle1'>Creative Developer | ML Engineer | Data Enthusiast</div>
    <div class='subtitle2'>Machine Learning Engineer based in New York City, passionate about building intelligent systems and turning data into actionable insights.</div>
    """,
    unsafe_allow_html=True
)

# Custom CSS for buttons
st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            padding: 8px;
            font-size: 16px;
            background-color: #5bc0be; /* Green background */
            color: white;
            border: none;
        }
        .stButton>button:hover {
            background-color: #1c2541; /* Darker Green on Hover */
        }
        .stDownloadButton>button {
            width: 100%;
            border-radius: 10px;
            padding: 8px;
            font-size: 16px;
            background-color: #5bc0be; /* Green background */
            color: white;
            border: none;
        }
        .stDownloadButton>button:hover {
            background-color: #1c2541; /* Darker Green on Hover */
        }
        /* Style for disabled button */
        .stButton>button:disabled,
        .stDownloadButton>button:disabled {
            background-color: #a0a0a0;
            color: #d0d0d0;
            cursor: not-allowed;
        }
    </style>
""", unsafe_allow_html=True)

# Add some vertical space before buttons
st.markdown("<br>", unsafe_allow_html=True)

# --- UPDATED: Resume Loading Logic ---
resume_path = "assets/Resume_AyushiPatel.pdf"
resume_data = None
try:
    with open(resume_path, "rb") as file:
        resume_data = file.read()
except FileNotFoundError:
    print(f"Warning: Resume file not found at {resume_path}")

# Create columns with reduced spacing
col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="small") 

with col1:
    if resume_data:
        st.download_button(
            label="Download CV",
            data=resume_data,
            file_name="Resume_AyushiPatel.pdf", # The name users will see
            mime="application/octet-stream" # <-- This is the change
        )
    else:
        # Show a disabled button if the file wasn't found
        st.download_button(
            label="Resume Missing",
            data=b"",
            disabled=True
        )

with col2:
    if st.button("See my work"):
        st.switch_page("pages/portfolio.py")

with col3:
    if st.button("About"):
        st.switch_page("pages/about.py")

with col4:
    if st.button("Let's Connect"):
        st.switch_page("pages/contact.py")

# --- END OF THE MAIN CONTAINER ---
st.markdown('</div>', unsafe_allow_html=True)