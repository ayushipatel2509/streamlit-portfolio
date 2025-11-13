import streamlit as st
import ssl
import smtplib

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Contact Me", page_icon="📩", layout="wide")

# ---- CUSTOM STYLING ----
st.markdown("""
    <style>
        /* --- Hide Streamlit UI --- */
        header[data-testid="stHeader"],
        footer[data-testid="stFooter"],
        .stSidebar {
            display: none !important;
        }

        /* --- Page Body Styling --- */
        html, body, [class*="stApp"] {
            background-color: #3a506b !important;
            color: #ffffff !important;
        }
        .main {
            background-color: #3a506b !important;
            color: #ffffff !important;
        }

        /* --- Text Styling --- */
        .contact-title {
            font-size: 36px !important;
            font-weight: 700 !important;
            margin-top: 30px !important;
            color: #ffcc70 !important;
            letter-spacing: 1px !important;
        }
        .contact-info {
            margin-top: 10px !important;
            color: #f0f0f0 !important;
            font-size: 18px !important;
        }
        label, .stTextInput label, .stTextArea label {
            color: #ffffff !important;
        }

        /* ======= Robust selectors for the form submit button =======
           We include multiple selectors because Streamlit versions render
           the submit button in slightly different wrappers.
           ======= */

        /* direct button inside the form */
        form button[type="submit"],
        /* st.form wrapper typically has data-testid="stForm" */
        div[data-testid="stForm"] button,
        div[data-testid="stForm"] .stButton > button,
        /* generic stButton wrapper (covers many streamlit versions) */
        .stButton > button,
        /* final fallback: any button inside main form area */
        [role="main"] form button,
        /* target last button (usually submit) */
        form button:last-of-type
        {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1.05rem !important;
            padding: 0.75rem 1.25rem !important;
            border-radius: 12px !important;
            border: none !important;
            width: 100% !important;
            max-width: 100% !important;
            cursor: pointer !important;
            
            /* Mint gradient + subtle shadow */
            background: linear-gradient(90deg, #5bc0be 0%, #6fffe9 100%) !important;
            color: #061220 !important;
            box-shadow: 0px 6px 18px rgba(91,192,190,0.22) !important;
            transition: transform 0.22s ease, box-shadow 0.22s ease !important;
        }

        /* hover + active - same wide selector set */
        form button[type="submit"]:hover,
        div[data-testid="stForm"] button:hover,
        .stButton > button:hover,
        [role="main"] form button:hover,
        form button:last-of-type:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0px 10px 28px rgba(91,192,190,0.36) !important;
            background: linear-gradient(90deg, #6fffe9 0%, #5bc0be 100%) !important;
        }
        form button[type="submit"]:active,
        div[data-testid="stForm"] button:active,
        .stButton > button:active,
        [role="main"] form button:active,
        form button:last-of-type:active {
            transform: translateY(0px) !important;
            box-shadow: 0px 4px 10px rgba(91,192,190,0.18) !important;
        }

        /* --- Navigation Buttons (not inside form) --- */
        .stButton:not(div[data-testid="stForm"] .stButton) > button,
        .stButton.stButton > button {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            padding: 0.6rem 1.2rem !important;
            border-radius: 10px !important;
            border: none !important;
            background-color: #5bc0be !important;
            color: #ffffff !important;
            transition: all 0.25s ease !important;
        }
        .stButton:not(div[data-testid="stForm"] .stButton) > button:hover {
            background-color: #4a607c !important;
            color: #ffffff !important;
        }

        /* small accessibility tweak: focus styles */
        button:focus {
            outline: 3px solid rgba(91,192,190,0.25) !important;
            outline-offset: 2px !important;
        }
    </style>
""", unsafe_allow_html=True)


# ---- CONTACT HEADER ----
st.markdown("<div class='contact-title'>CONTACT</div>", unsafe_allow_html=True)
st.markdown("""
    <p class='contact-info'><strong>I’ve got just what you need. <span style='color: #00bfff;'>Let's talk.</span></strong></p>
    <p class='contact-info'>📧 ayup25092@gmail.com</p>
    <p class='contact-info'>📍 New York City, USA</p>
""", unsafe_allow_html=True)

# ---- CONTACT FORM ----
with st.form("contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
    with col2:
        email = st.text_input("Email")

    subject = st.text_input("Subject")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Submit")
    if submitted:
        sender_email = "ayup25092@gmail.com"  
        receiver_email = "ayup25092@gmail.com"  
        
        # --- YOUR APP PASSWORD ---
        password = "pied ylcr yvag jvpn"  

        # Format Email
        email_message = f"""\
Subject: New Contact Form Submission from {name}

Name: {name}
Email: {email}
Subject: {subject}
Message: {message}
"""

        try:
            # Send Email
            context = ssl.create_default_context()
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, email_message)

            st.success("✅ Your message was sent successfully!")

        except Exception as e:
            # --- Simplified Error Message ---
            st.error(f"❌ An error occurred. Please try again later or email me directly.")

# ---- NAVIGATION FOOTER ----
st.markdown("<br><br><hr>", unsafe_allow_html=True)

nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 5])
with nav_col1:
    if st.button("Home", use_container_width=True):
        st.switch_page("main.py")
with nav_col2:
    if st.button("Portfolio", use_container_width=True):
        st.switch_page("pages/portfolio.py")