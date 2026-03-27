import streamlit as st
import base64
import time

# ===== 初期化 =====
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

# ===== 背景 =====
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("prism-logo.png")

# ===== CSS =====
st.markdown(f"""
<style>

/* 背景 */
.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
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

/* 👇これが本質：radio全体をカード化 */
div[data-testid="stRadio"] {{
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(12px);

    border-radius: 25px;
    padding: 30px 40px;
    max-width: 650px;
    margin: 80px auto;

    border: 1px solid rgba(255,255,255,0.5);
    box-shadow: 0 10px 35px rgba(0,0,0,0.2);
}}

/* 質問タイトルを中に見せる */
div[data-testid="stRadio"] > label:first-child {{
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 15px;
    display: block;
    color: #111;
}}

/* 選択肢 */
div[data-testid="stRadio"] label {{
    color: #111 !important;
    padding: 10px 5px;
    display: flex;
    align-items: center;
}}

div[data-testid="stRadio"] label:hover {{
    background: rgba(255,255,255,0.25);
    border-radius: 10px;
    transform: translateX(5px);
}}

</style>
""", unsafe_allow_html=True)

# ===== データ =====
QUESTIONS = [
    {
        "question": "Q1. どんな作業が好き？",
        "choices": [
            "体を動かす",
            "機械いじり",
            "デザイン",
            "裏方で支える"
        ]
    }
]

# ===== 表示 =====
q = QUESTIONS[st.session_state.q_index]

choice = st.radio(
    q["question"],  # ←タイトルをここに入れるのが超重要
    q["choices"],
    index=None
)
