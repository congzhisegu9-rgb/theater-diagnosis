import streamlit as st
import base64
import time

# ===== 初期化（←最重要：一番上に置く）=====
if "started" not in st.session_state:
    st.session_state.started = False

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "scores" not in st.session_state:
    st.session_state.scores = {
        "舞台":0,"音響":0,"照明":0,"映像":0,
        "衣装":0,"小道具":0,"制作":0,"Web":0,"役者":0
    }

# ===== 背景画像 =====
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("prism-logo.jpg")

# ===== CSS =====
st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
}}

.stApp::before {{
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
    z-index: -1;
}}

.card {{
    background: rgba(255,255,255,0.9);
    padding: 30px;
    border-radius: 20px;
    max-width: 650px;
    margin: 30px auto;
}}

.card h1, .card h2, .card h3 {{
    color: black;
    text-align: center;
}}

div[data-testid="stRadio"] label {{
    color: black !important;
}}

div[data-testid="stRadio"] label:hover {{
    background: rgba(0,0,0,0.1);
    border-radius: 10px;
}}

button:hover {{
    transform: scale(1.05);
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
    },
    {
        "question": "得意なことは？",
        "choices": [
            {"text": "人前で話す","scores":{"役者":3}},
            {"text": "PC作業","scores":{"Web":3,"映像":1}},
            {"text": "細かい作業","scores":{"小道具":2,"衣装":2}},
            {"text": "全体管理","scores":{"制作":3}},
        ]
    }
]

# ===== ローディング =====
if not st.session_state.started:
    st.markdown('<div class="card"><h2>読み込み中...</h2></div>', unsafe_allow_html=True)

    bar = st.progress(0)
    for i in range(101):
        time.sleep(0.01)
        bar.progress(i)

    st.session_state.started = True
    st.rerun()

# ===== タイトル（カード①）=====
st.markdown("""
<div class="card">
<h1>🎭 セクション適性診断</h1>
</div>
""", unsafe_allow_html=True)

# ===== 質問（カード②）=====
if st.session_state.q_index < len(QUESTIONS):
    q = QUESTIONS[st.session_state.q_index]

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(f"<h3>Q{st.session_state.q_index+1}. {q['question']}</h3>", unsafe_allow_html=True)

        choice = st.radio("", [c["text"] for c in q["choices"]])

        if st.button("次へ", use_container_width=True):
            for c in q["choices"]:
                if c["text"] == choice:
                    for sec, pt in c["scores"].items():
                        st.session_state.scores[sec] += pt

            st.session_state.q_index += 1
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# ===== 結果 =====
else:
    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)

    top1 = sorted_scores[0][0]
    top2 = sorted_scores[1][0]

    st.markdown(f"""
    <div class="card">
    <h2>
    あなたが向いているのは…<br><br>
    <b>{top1}</b> セクション、<b>{top2}</b> セクション
    </h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("もう一度"):
        st.session_state.q_index = 0
        for k in st.session_state.scores:
            st.session_state.scores[k] = 0
        st.session_state.started = False
        st.rerun()
