import streamlit as st
import base64
import time

# ===== ページ設定 =====
st.set_page_config(layout="wide")

# ===== 初期化 =====
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

# ===== 背景 =====
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("prism-logo.jpg")

# ===== CSS =====
st.markdown(f"""
<style>

/* ===== 背景 ===== */
.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

html, body, .stApp {{
    height: 100%;
}}

/* 少し暗く＋ぼかし */
.stApp::before {{
    content:"";
    position:fixed;
    width:100%;
    height:100%;
    backdrop-filter: blur(6px);
    background: rgba(0,0,0,0.25);
    z-index:-1;
}}

/* 上余白削除 */
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
    margin-bottom: 40px;
}}

/* ===== カード（ここが最重要） ===== */
div[data-testid="stRadio"] {{
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(15px);

    border-radius: 30px;
    padding: 40px 50px;

    width: 420px;              /* ←サイズ調整（これ重要） */
    margin: 0 auto;            /* ←完全中央 */

    border: 1px solid rgba(255,255,255,0.5);
    box-shadow: 0 10px 40px rgba(0,0,0,0.25);
}}

/* タイトル（質問） */
div[data-testid="stRadio"] > label:first-child {{
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 20px;
    display: block;
    color: #222;
}}

/* 選択肢 */
div[data-testid="stRadio"] label {{
    color: #222 !important;
    padding: 10px 0;
    display: flex;
    align-items: center;
}}

div[data-testid="stRadio"] label:hover {{
    background: rgba(255,255,255,0.3);
    border-radius: 10px;
    transform: translateX(5px);
}}

</style>
""", unsafe_allow_html=True)

# ===== タイトル =====
st.markdown('<div class="title">🎭 セクション適性診断</div>', unsafe_allow_html=True)

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
    q["question"],
    q["choices"],
    index=None
)

# ===== 動作 =====
if choice is not None:
    time.sleep(0.2)
    st.session_state.q_index += 1
    st.rerun()
