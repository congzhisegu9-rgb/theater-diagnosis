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

# ===== CSS（デザイン本体）=====
st.markdown(f"""
<style>

/* ===== 背景 ===== */
.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
}}

/* ===== 中央配置 ===== */
.main > div {{
    display: flex;
    justify-content: center;
}}

/* ===== ガラスカード ===== */
.glass {{
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    border-radius: 25px;
    padding: 40px 50px;

    width: 650px;
    margin-top: 80px;

    border: 1.5px solid rgba(255,255,255,0.6);

    box-shadow: 0 10px 40px rgba(0,0,0,0.2);

    animation: fadeIn 0.6s ease;
}}

/* ===== タイトル ===== */
.glass h3 {{
    text-align: left;
    font-size: 24px;
    color: #222;
    margin-bottom: 25px;
}}

/* ===== 選択肢 ===== */
div[data-testid="stRadio"] label {{
    background: transparent;
    padding: 12px 10px;
    margin: 10px 0;
    border-radius: 10px;
    color: #222 !important;
    font-size: 18px;
    transition: 0.2s;
}}

div[data-testid="stRadio"] label:hover {{
    background: rgba(255,255,255,0.3);
    transform: translateX(8px);
}}

/* ===== アニメーション ===== */
@keyframes fadeIn {{
    from {{opacity:0; transform: translateY(20px);}}
    to {{opacity:1; transform: translateY(0);}}
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
    st.markdown('<div class="glass"><h3>Loading...</h3></div>', unsafe_allow_html=True)
    bar = st.progress(0)
    for i in range(101):
        time.sleep(0.01)
        bar.progress(i)
    st.session_state.started = True
    st.rerun()

# ===== 質問 =====
if st.session_state.q_index < len(QUESTIONS):

    q = QUESTIONS[st.session_state.q_index]

    with st.container():
        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.markdown(f"<h3>Q{st.session_state.q_index+1}. {q['question']}</h3>", unsafe_allow_html=True)

        choice = st.radio(
            "",
            [c["text"] for c in q["choices"]],
            index=None,
            key=st.session_state.q_index
        )

        st.markdown('</div>', unsafe_allow_html=True)

    if choice is not None:
        time.sleep(0.2)

        for c in q["choices"]:
            if c["text"] == choice:
                for sec, pt in c["scores"].items():
                    st.session_state.scores[sec] += pt

        st.session_state.q_index += 1
        st.rerun()

# ===== 結果 =====
else:
    sorted_scores = sorted(
        st.session_state.scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top1, top2 = sorted_scores[0][0], sorted_scores[1][0]

    st.markdown(f"""
    <div class="glass">
    <h3>
    あなたは<br><br>
    <b>{top1}セクションタイプ</b><br><br>
    ＆<br><br>
    <b>{top2}セクションタイプ</b>
    </h3>
    </div>
    """, unsafe_allow_html=True)

    if st.button("もう一度"):
        st.session_state.q_index = 0
        for k in st.session_state.scores:
            st.session_state.scores[k] = 0
        st.session_state.started = False
        st.rerun()
