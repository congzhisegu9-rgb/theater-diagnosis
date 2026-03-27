import streamlit as st
import base64
import time

# ===== 初期化 =====
if "started" not in st.session_state:
    st.session_state.started = False

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "scores" not in st.session_state:
    st.session_state.scores = {
        "舞台":0,"音響":0,"照明":0,"映像":0,
        "衣装":0,"小道具":0,"制作":0,"Web":0,"役者":0
    }

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
    background: rgba(0,0,0,0.3);
    z-index:-1;
}}

/* カード */
.q-card {{
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(12px);

    border-radius: 25px;
    padding: 35px;
    max-width: 650px;
    margin: 60px auto;

    border: 1px solid rgba(255,255,255,0.4);
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
}}

/* タイトル */
.q-card h3 {{
    text-align: left;
    color: #111;
    margin-bottom: 20px;
    font-size: 22px;
}}

/* 👇ここが核心：radioを完全にカードに溶かす */
div[data-testid="stRadio"] {{
    background: transparent !important;
    padding: 0 !important;
    box-shadow: none !important;
}}

/* 選択肢 */
div[data-testid="stRadio"] label {{
    color: #111 !important;
    padding: 10px 5px;
    border-radius: 10px;
    transition: 0.2s;
}}

div[data-testid="stRadio"] label:hover {{
    background: rgba(255,255,255,0.2);
    transform: translateX(5px);
}}

</style>
""", unsafe_allow_html=True)

# ===== データ =====
QUESTIONS = [
    {
        "question": "どんな作業が好き？",
        "choices": [
            {"text": "体を動かす","scores":{"舞台":2,"役者":2}},
            {"text": "機械いじり","scores":{"音響":2,"照明":2}},
            {"text": "デザイン","scores":{"衣装":2,"映像":1}},
            {"text": "裏方で支える","scores":{"制作":2}},
        ]
    }
]

# ===== 質問 =====
q = QUESTIONS[st.session_state.q_index]

st.markdown('<div class="q-card">', unsafe_allow_html=True)

st.markdown(f"<h3>Q{st.session_state.q_index+1}. {q['question']}</h3>", unsafe_allow_html=True)

choice = st.radio(
    "",
    [c["text"] for c in q["choices"]],
    index=None
)

st.markdown('</div>', unsafe_allow_html=True)

# ===== 動作 =====
if choice is not None:
    for c in q["choices"]:
        if c["text"] == choice:
            for sec, pt in c["scores"].items():
                st.session_state.scores[sec] += pt

    st.session_state.q_index += 1
    st.rerun()
