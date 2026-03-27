import streamlit as st
import base64

st.set_page_config(layout="wide")  # ←これ必須

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("prism-logo.jpg")

st.markdown(f"""
<style>

/* 背景 */
.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
}}

.stApp::before {{
    content:"";
    position:fixed;
    width:100%;
    height:100%;
    backdrop-filter: blur(6px);
    background: rgba(0,0,0,0.25);
    z-index:-1;
}}

/* 上の余白削除 */
.block-container {{
    padding-top: 0rem;
}}

/* カード化 */
div[data-testid="stRadio"] {{
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(12px);

    border-radius: 25px;
    padding: 40px;

    width: 500px;
    margin: 100px auto;

    border: 1px solid rgba(255,255,255,0.5);
    box-shadow: 0 10px 35px rgba(0,0,0,0.2);
}}

/* タイトル */
div[data-testid="stRadio"] > label:first-child {{
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 20px;
    display: block;
    color: #111;
}}

/* 選択肢 */
div[data-testid="stRadio"] label {{
    color: #111 !important;
    padding: 10px 5px;
}}

div[data-testid="stRadio"] label:hover {{
    background: rgba(255,255,255,0.3);
    border-radius: 10px;
    transform: translateX(5px);
}}

</style>
""", unsafe_allow_html=True)

choice = st.radio(
    "Q1. どんな作業が好き？",
    ["体を動かす","機械いじり","デザイン","裏方で支える"],
    index=None
)
