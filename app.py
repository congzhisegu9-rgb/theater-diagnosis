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

# ===== CSS（完成版）=====
st.markdown(f"""
<style>

/* ===== 背景 ===== */
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
    backdrop-filter: blur(8px); /* ぼかし */
    background: rgba(0,0,0,0.35); /* 暗さ */
    z-index:-1;
}}

/* ===== フォント ===== */
html, body, [class*="css"] {{
    font-family: "Helvetica Neue", "Noto Sans JP", sans-serif;
}}

/* ===== ガラスカード ===== */
.glass {{
    background: linear-gradient(
        rgba(255,255,255,0.45),
        rgba(255,255,255,0.25)
    ); /* ←方法A */

    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);

    border-radius: 20px;
    padding: 35px;
    max-width: 720px;
    margin: 30px auto;

    border: 1px solid rgba(255,255,255,0.4);
    box-shadow: 0 6px 25px rgba(0,0,0,0.2);

    animation: fadeIn 0.6s ease;
    text-align: center;
}}

/* ===== テキスト（方法B） ===== */
.glass h1, .glass h2, .glass h3 {{
    color: #111;
    text-shadow: 0 1px 3px rgba(255,255,255,0.6);
}}

.glass h1 {{
    font-weight: 600;
}}

.glass h3 {{
    margin-bottom: 20px;
}}

/* ===== 選択肢 ===== */
div[data-testid="stRadio"] {{
    margin-top: 15px;
}}

div[data-testid="stRadio"] label {{
    background: rgba(255,255,255,0.5);
    margin: 8px 0;
    padding: 12px 14px;
    border-radius: 12px;
    transition: 0.2s;
    color: black !important;
}}

div[data-testid="stRadio"] label:hover {{
    background: rgba(255,255,255,0.75);
    transform: translateX(6px);
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
    st.markdown('<div class="glass"><h2>Loading...</h2></div>', unsafe_allow_html=True)
    bar = st.progress(0)
    for i in range(101):
        time.sleep(0.01)
        bar.progress(i)
    st.session_state.started = True
    st.rerun()

# ===== タイトル =====
st.markdown("""
<div class="glass">
<h1>セクション適性診断</h1>
</div>
""", unsafe_allow_html=True)

# ===== 進捗 =====
st.progress(st.session_state.q_index / len(QUESTIONS))

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
    <h2>
    あなたは<br><br>
    <b>{top1}セクションタイプ</b><br><br>
    ＆<br><br>
    <b>{top2}セクションタイプ</b>
    </h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("もう一度"):
        st.session_state.q_index = 0
        for k in st.session_state.scores:
            st.session_state.scores[k] = 0
        st.session_state.started = False
        st.rerun()
