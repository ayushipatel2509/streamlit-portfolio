import streamlit as st
import base64

# ---- PAGE CONFIG ----
st.set_page_config(page_title="My Portfolio", page_icon="👩‍💻", layout="wide")

# ---- LOAD BASE64 IMAGE ----
def get_base64_image(image_path):
    """Converts a local image file to a base64 string."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

# ---- STYLING ----
st.markdown("""
    <style>
        /* --- Hide Streamlit UI --- */
        header[data-testid="stHeader"],
        footer[data-testid="stFooter"],
        .stSidebar {
            display: none;
        }

        /* --- Page Body Styling --- */
        .stApp {
            background-color: #3a506b;
            color: #ffffff;
        }
        .main {
            background-color: #3a506b;
            color: #ffffff;
        }
        
        /* --- General Text Styling --- */
        h1, h3, p, .stMarkdown {
            color: #ffffff;
        }
        
        /* --- Main Container --- */
        .block-container {
            padding: 2rem 3rem 3rem 3rem;
            max-width: 1200px;
        }
        
        /* --- NEW: Project Title Style --- */
        /* This separates the title from the card */
        .project-title {
            font-size: 1.75rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 1.5rem; /* <-- Adds space between title and card */
        }

        /* --- Project Card Styling --- */
        .project-card {
            background-color: #4a607c; /* A lighter blue-gray */
            border-radius: 10px;
            padding: 1.5rem;
            height: 100%;
            display: flex;
            flex-direction: column;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.3);
        }
        
        /* Removed h3 from here, as it's now in .project-title */
        
        .project-card .stImage img {
            border-radius: 5px;
            width: 100%;
            object-fit: cover;
            height: 250px; 
            margin-bottom: 0.5rem; 
        }
        
        .project-card p {
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 0.75rem;
        }
        
        .project-card .links {
            margin-top: auto; 
            padding-top: 1rem;
        }
        
        .project-card a {
            color: #8be9fd; 
            font-weight: bold;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        .project-card a:hover {
            color: #ffcc70; 
        }
        
        /* --- Navigation Button Styling --- */
        .stButton > button {
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            padding: 0.6rem 1.2rem;
            border-radius: 10px; /* <-- Matches your home page */
            
            /* --- The Fix --- */
            background-color: #5bc0be; /* <-- The mint background color */
            color: #ffffff !important; /* <-- White text */
            border: none; /* <-- No border */
            
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #4a607c; /* <-- Darker hover (like your cards) */
            color: #ffffff !important; 
            border: none;
        }
        
    </style>
""", unsafe_allow_html=True)


# ---- HELPER FUNCTION TO DISPLAY A PROJECT ----
def display_project(project):
    """Creates a formatted project title and card."""
    
    # --- 1. Display the Project Title ---
    # This is now separate from the card
    st.markdown(f"""
    <h3 class="project-title">{project['title']}</h3>
    """, unsafe_allow_html=True)

    # --- 2. Display the Project Card ---
    st.markdown(f"""
    <div class="project-card">
    """, unsafe_allow_html=True)
    
    # --- Image Gallery ---
    # Place native Streamlit columns INSIDE the card
    img_col1, img_col2, img_col3 = st.columns(3, gap="small")
    
    image_paths = project.get('image_paths', [])
    
    with img_col1:
        image_b64 = get_base64_image(image_paths[0] if len(image_paths) > 0 else None)
        if image_b64:
            st.image(f"data:image/png;base64,{image_b64}")
        else:
            st.image("https://placehold.co/300x250/4a607c/ffffff?text=Img+1")
            
    with img_col2:
        image_b64 = get_base64_image(image_paths[1] if len(image_paths) > 1 else None)
        if image_b64:
            st.image(f"data:image/png;base64,{image_b64}")
        else:
            st.image("https://placehold.co/300x250/4a607c/ffffff?text=Img+2")
            
    with img_col3:
        image_b64 = get_base64_image(image_paths[2] if len(image_paths) > 2 else None)
        if image_b64:
            st.image(f"data:image/png;base64,{image_b64}")
        else:
            st.image("https://placehold.co/300x250/4a607c/ffffff?text=Img+3")

    # --- Details ---
    # Add the rest of the card's HTML content
    st.markdown(f"""
        <p style="margin-top: 1.5rem;"><strong>Description:</strong> {project['description']}</p>
        <p><strong>Tools:</strong> {project['tools']}</p>
        
    </div>
    """, unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<h1 style='text-align: center; font-size: 3rem; margin-bottom: 0.5rem;'> My Portfolio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #f0f0f0;'>Welcome! Here's a showcase of my few projects.</p>", unsafe_allow_html=True)
st.markdown("---")
# REMOVED the <br><br><br> spacer to reduce space


# ---- PROJECTS DATA ----
# Define all your projects here in a clean list
project_list = [
    {
        "title": "Hill Climb Racing : GAME AUTOMATION",
        "image_paths": [ 
            "assets/hc1.jpg", 
            "assets/hc2.jpg", 
            "assets/hc3.jpg"  
        ],
        "description": "This system aims at developing an application, for gesture recognition. The camera or webcam connected to the system can be used to recognize the human hand gesture. Based on the analysis made by the application done on recognizing the human Hand Gestures, the operations on the Game will be performed with the game's default gaming controls.",
        "tools": "Developed in Python. Python libraries used:Open CV, mediapipe. PyWin for windows web application. Open CV mostly stretches towards real-time vision applications and takes advantage of MMX (Multimedia Extension) and SSE (Streaming SIMD Extensions) instructions when available. "
    },
    {
        "title": "Bioacoustics Ecoststem Health Score Assessment",
        "image_paths": [ 
            "assets/b1.png", 
            "assets/b2.png", 
            "assets/b3.png"  
        ],
        "description": "AI-driven Bioacoustic Ecosystem Health Assessment System that autonomously analyzes environmental sound data to generate a quantifiable Ecosystem Health Score and provide real-time alerts for the detection of rare and endangered species.",
        "tools": "Python 3.8+,PyTorch , TensorFlow (for CNN), Scikit-learn, XGBoost, Pandas, NumPy, Librosa, SciPy , Flask , Streamlit, Plotly (for visualizations), PostgreSQL for storing results and metadata. Version Control: Git / GitHub."
    },
    {
        "title": "STOCK TRACKER : Stock Merket Portfolio Management",
        "image_paths": [ 
            "assets/s1.jpg", 
            "assets/s2.jpg", 
            "assets/s3.jpg"  
        ],
        "description": "The Stock Market Portfolio Management Tracker is a predictive analytics system that leverages machine learning to analyze historical data and forecast future price trends.Key features include tools for trend identification, risk assessment, factor analysis, and a specialized SIP and Lumpsum calculator to help users plan investments systematically.Built using Python and ReactJS, the application automates data collection and analysis to overcome the inefficiencies of manual processing and improve scalability.This system is designed to assist investors, traders, and financial researchers in making informed decisions by visualizing complex market patterns and correlations.",
        "tools": "The project primarily utilizes Python, ReactJS, a versatile programming language widely used in data analysis and machine learning. We leverage popular Python libraries such as Pandas and NumPy for data manipulation. To gather historical stock market data, we utilize financial data providers or stock market databases. This may involve accessing APIs (Application Programming Interfaces) that provide access to real-time or historical stock price information. TradingView Widgets. "
    },
    {
        "title": "Tunexa: Emotion Based Music PLayer",
        "image_paths": [ 
            "assets/t1.jpg", 
            "assets/t2.jpg", 
            "assets/t3.jpg"  
        ],
        "description": "The proposed system detects the emotions of an individual through facial expressions and plays the music according to the mood detected. The expressions of the face could be happy, sad, angry, neutral, etc. The emotions on the face can be detected and captured through a webcam or an inbuilt camera. The emotions of an individual from the captured image could be detected using Fisherface Algorithm. Once the emotion is recognized, the system suggests a playlist for that emoon and plays the music automatically.",
        "tools": " Streamlit,scikit-learn, Keras,PyTorch,NumPy, pandas, Matplotlib, WebRTC "
    }
]

# ---- DISPLAY PROJECTS (One per row) ----
# Removed the large spacer from here

# --- Project 1 ---
display_project(project_list[0]) 
st.markdown("<br><br><br>", unsafe_allow_html=True) # Spacer

# --- Project 2 ---
display_project(project_list[1]) 
st.markdown("<br><br><br>", unsafe_allow_html=True) # Spacer

# --- Project 3 ---
display_project(project_list[2]) 
st.markdown("<br><br><br>", unsafe_allow_html=True) # Spacer

# --- Project 4 ---
display_project(project_list[3]) 


# ---- NAVIGATION FOOTER ----
st.markdown("<br><br><hr>", unsafe_allow_html=True)

nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 5])
with nav_col1:
    if st.button("Home", use_container_width=True):
        st.switch_page("main.py")
with nav_col2:
    if st.button("Contact", use_container_width=True):
        st.switch_page("pages/contact.py")