import base64
import os
import streamlit as st


def apply_theme(image_file="food.png"):
  img_layer = ""
  if image_file and os.path.exists(image_file):
    with open(image_file, "rb") as f:
      img = base64.b64encode(f.read()).decode()
    img_layer = (
        f'linear-gradient(rgba(255, 251, 235, 0.70), rgba(255, 251, 235,'
        f' 0.70)), url("data:image/png;base64,{img}") center 20px / 450px auto'
        ' no-repeat,'
    )

  st.markdown(
      f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400;600&display=swap');

    html, body, .stApp, .stApp * {{
        font-family: 'Pixelify Sans', monospace !important;
    }}

    .stApp {{
        background: linear-gradient(180deg, #FFF3C4 0%, #FFE0B5 55%, #FFD1DC 100%) fixed;
        image-rendering: pixelated;
    }}

    header[data-testid="stHeader"] {{
        background: transparent;
    }}

    .block-container {{
        background: {img_layer} #FFFBEB !important;
        border: 4px solid #8B5E3C;
        border-radius: 16px;
        box-shadow: 6px 6px 0 #C99A6B;
        max-width: 500px;
        margin-top: 2rem;
        padding: 2rem 1.5rem !important;
    }}

    /* Extra top margin specifically for mobile phones */
    @media (max-width: 768px) {{
        .block-container {{
            margin-top: 6rem !important;
        }}
    }}

    h1, h2, h3, p, label, span, li,
    div[data-testid="stMarkdownContainer"] * {{
        color: #5A3E2B !important;
    }}
    h1 {{ font-size: 2.2rem !important; }}

    .stCaption, div[data-testid="stCaptionContainer"] p {{
        color: #5A3E2B !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        text-shadow: 1px 1px 0px rgba(255, 255, 255, 0.9);
    }}

    /* Input wrappers with dark brown borders & pop-out shadow */
    .stTextInput, .stPassword {{
        background: #FFF8E1 !important;
        border: 3px solid #8B5E3C !important;
        border-radius: 10px !important;
        box-shadow: 3px 3px 0 #8B5E3C !important;
        padding: 2px 8px !important;
        margin-bottom: 10px;
    }}

    div[data-baseweb="input"] {{
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}

    div[data-baseweb="input"] input {{
        background-color: transparent !important;
        color: #5A3E2B !important;
        -webkit-text-fill-color: #5A3E2B !important;
        border: none !important;
        box-shadow: none !important;
    }}

    /* Clean Eye Icon for Password Visibility */
    .stPassword button {{
        background: transparent !important;
        border: none !important;
        font-size: 0 !important;
        color: transparent !important;
        text-shadow: none !important;
        position: relative;
    }}

    .stPassword button svg {{
        display: none !important;
    }}

    .stPassword button::after {{
        content: "👁️" !important;
        font-size: 18px !important;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        visibility: visible !important;
    }}

    /* Buttons */
    .stButton > button {{
        background: #FFD966 !important;
        color: #5A3E2B !important;
        border: 3px solid #8B5E3C !important;
        border-radius: 10px !important;
        box-shadow: 3px 3px 0 #8B5E3C !important;
    }}
    .stButton > button:hover {{
        background: #FFC93C !important;
    }}
    .stButton > button:active {{
        box-shadow: none !important;
        transform: translate(3px, 3px);
    }}

    /* Alert / output box */
    div[data-testid="stAlert"] {{
        background: #FFF8E1 !important;
        border: 3px solid #8B5E3C !important;
        border-radius: 10px !important;
        box-shadow: 3px 3px 0 #8B5E3C !important;
    }}
    div[data-testid="stAlert"] * {{
        color: #5A3E2B !important;
    }}
    </style>
    """,
      unsafe_allow_html=True,
  )