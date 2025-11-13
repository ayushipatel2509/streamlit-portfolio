import streamlit as st
import base64
import time

# ---- PAGE SETUP ----
st.set_page_config(page_title="About Me", page_icon="💁‍♀️", layout="wide")

# ---- LOAD BASE664 IMAGE ----
def get_base64_image(image_path):
    """Converts a local image file to a base64 string."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

# --- Image loading ---
# Update this path to your actual "about" image in the assets folder
image_path = "assets/about-img-removebg-preview-Picsart-BackgroundRemover.jpg" 
base64_image = get_base64_image(image_path)

# Set the final image source
if base64_image:
    image_src = f"data:image/png;base64,{base64_image}"
else:
    # Fallback placeholder if image is not found
    image_src = "https://placehold.co/450x450/f0f0f0/3a506b?text=Your+Photo"
    print(f"Warning: '{image_path}' not found. Using placeholder.")


# ---- CUSTOM STYLING ----
st.markdown("""
    <style>
        /* --- Hide Streamlit UI --- */
        header[data-testid="stHeader"],
        footer[data-testid="stFooter"],
        .stSidebar {
            display: none !important;
        }

        /* --- Page Background --- */
        html, body, [class*="stApp"], .main {
            background-color: #3a506b !important;
            color: #ffffff !important;
        }

        /* --- Container Layout --- */
        .block-container {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 95vh;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        /* --- Animations --- */
        .image-container {
            opacity: 0;
            transform: translateX(100px);
            animation: slideInImage 1.8s ease-in-out forwards;
        }
        @keyframes slideInImage {
            0% { opacity: 0; transform: translateX(100px) scale(0.95); }
            50% { opacity: 0.5; transform: translateX(20px) scale(1.02); }
            100% { opacity: 1; transform: translateX(0) scale(1); }
        }

        .text-container {
            opacity: 0;
            transform: translateX(-100px);
            animation: slideInText 1.8s ease-in-out forwards;
            animation-delay: 1.2s;
        }
        @keyframes slideInText {
            0% { opacity: 0; transform: translateX(-100px); }
            50% { opacity: 0.5; transform: translateX(-20px); }
            100% { opacity: 1; transform: translateX(0); }
        }

        /* --- Text Styling --- */
        .about-title {
            font-size: 80px !important;
            font-weight: bold;
            margin-bottom: -10px;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            letter-spacing: 1px;
        }

        .about-description {
            font-size: 20px;
            color: #f0f0f0;
            line-height: 1.6;
            font-family: 'Inter', sans-serif;
        }

        .profile-img {
            width: 100%;
            max-width: 450px;
            height: auto;
            border-radius: 1rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        }

        /* --- Button Styling (Mint Glow Theme) --- */
        .stButton > button {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            padding: 0.75rem 1.5rem !important;
            border-radius: 12px !important;
            border: none !important;
            width: 100% !important;
            cursor: pointer !important;

            background: linear-gradient(90deg, #5bc0be 0%, #6fffe9 100%) !important;
            color: #0b132b !important;
            box-shadow: 0px 6px 18px rgba(91,192,190,0.22) !important;
            transition: transform 0.22s ease, box-shadow 0.22s ease, background 0.3s ease !important;
        }
        .stButton > button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0px 10px 28px rgba(91,192,190,0.36) !important;
            background: linear-gradient(90deg, #6fffe9 0%, #5bc0be 100%) !important;
        }
        .stButton > button:active {
            transform: translateY(0px) !important;
            box-shadow: 0px 4px 10px rgba(91,192,190,0.18) !important;
        }

        /* --- Responsive --- */
        @media screen and (max-width: 900px) {
            .about-title { font-size: 60px !important; }
            .about-description { font-size: 18px; }
            .block-container {
                flex-direction: column-reverse;
                text-align: center;
            }
            .profile-img {
                max-width: 300px;
                margin-bottom: 1.5rem;
            }
        }

        button:focus {
            outline: 3px solid rgba(91,192,190,0.25) !important;
            outline-offset: 2px !important;
        }
    </style>
""", unsafe_allow_html=True)


# ---- LAYOUT: COLUMNS ----
col1, col2 = st.columns([3, 5], gap="large")

# ---- IMAGE COLUMN ----
with col2:
    st.markdown(f"""
        <div class='image-container'>
            <img src='{image_src}' class='profile-img'>
        </div>
    """, unsafe_allow_html=True)


# ---- TEXT COLUMN ----
time.sleep(0.8) # Changed back to 0.8s per your code
with col1:
    st.markdown("<div class='text-container'>", unsafe_allow_html=True)
    st.markdown("<p class='about-title'>about.</p>", unsafe_allow_html=True)
    st.markdown("""
        <p class='about-description'>
        With a passion for machine learning,<br>
        I love transforming raw data into actionable insights.<br>
        My interests lie in predictive analytics, recommendation systems, and AI-driven automation. 
        <br><br>
        When I’m not coding, you’ll find me exploring nature, working on personal projects, 
        or perfecting my skincare routine. 
        </p>
    """, unsafe_allow_html=True)

    # ---- NAVIGATION BUTTONS ----
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Use columns for buttons
    b_col1, b_col2, b_col3 = st.columns([2, 2, 1]) # <-- WIDENED COLUMNS
    with b_col1:
        if st.button("See my work", use_container_width=True): # <-- ADDED USE_CONTAINER_WIDTH
            st.switch_page("pages/portfolio.py")
    with b_col2:
        if st.button("Home", use_container_width=True): # <-- ADDED USE_CONTAINER_WIDTH
            st.switch_page("main.py") # Navigate back to home

    st.markdown("</div>", unsafe_allow_html=True)