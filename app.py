import streamlit as st
import base64

st.set_page_config(layout="wide")

# ===== 背景 =====
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("prism-logo.jpg")

# ===== CSS =====
st.markdown(f"""
<style>

/* 背景 */
.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
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

.block-container {{
    padding-top: 0rem;
}}

/* ===== タイトル ===== */
.title {{
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: white;
    margin-top: 40px;
    margin-bottom: 60px;
}}

/* ===== ★ここが本質（内側をカード化） ===== */
div[data-testid="stRadio"] > div {{
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(15px);

    border-radius: 30px;
    padding: 40px;

    width: 420px;
    margin: 0 auto;

    border: 1px solid rgba(255,255,255,0.5);
    box-shadow: 0 10px 40px rgba(0,0,0,0.25);
}}

/* 質問 */
div[data-testid="stRadio"] label {{
    font-size: 22px !important;
    font-weight: bold;
    color: #222 !important;
    margin-bottom: 20px;
}}

/* 選択肢 */
div[data-testid="stRadio"] div[role="radiogroup"] label {{
    font-size: 18px;
    color: #222 !important;
    padding: 10px 0;
}}

div[data-testid="stRadio"] div[role="radiogroup"] label:hover {{
    background: rgba(255,255,255,0.3);
    border-radius: 10px;
    transform: translateX(5px);
}}

</style>
""", unsafe_allow_html=True)

# ===== タイトル =====
st.markdown('<div class="title">🎭 セクション適性診断</div>', unsafe_allow_html=True)

# ===== 質問 =====
choice = st.radio(
    "Q1. どんな作業が好き？",
    ["体を動かす","機械いじり","デザイン","裏方で支える"],
    index=None
)
