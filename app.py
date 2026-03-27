import streamlit as st
import base64
import time

# ===== ページ設定（重要）=====
st.set_page_config(layout="wide")

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

/* 背景 */
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

/* 背景を少し暗く＋ぼかし */
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

/* ===== 質問カード（radio全体をカード化） ===== */
div[data-testid="stRadio"] {{
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(12px);

    border-radius: 25px;
    padding: 40px;

    width: 520px;
    margin: 150px auto;

    border: 1px solid rgba(255,255,255,0.5);
    box-shadow: 0 10px 35px rgba(0,0,0,0.2);
}}

/* 質問タイトル */
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
    display: flex;
    align-items: center;
}}

div[data-testid="stRadio"] label:hover {{
    background: rgba(255,255,255,0.3);
    border-radius: 10px;
    transform: translateX(5px);
}}

/* ===== タイトル ===== */
.title {{
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: white;
    margin-top: 40px;
}}

/* ===== 結果カード ===== */
.result-card {{
    background: rgba(255,255,255,0.85);
    padding: 40px;
    border-radius: 20px;
    width: 600px;
    margin: 120px auto;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}}

</style>
""", unsafe_allow_html=True)

# ===== データ =====
QUESTIONS = [
    {
        "question": "Q1. どんな作業が好き？",
        "choices": [
            {"text": "体を動かす","scores":{"舞台":2,"役者":2}},
            {"text": "機械いじり","scores":{"音響":2,"照明":2}},
            {"text": "デザイン","scores":{"衣装":2,"映像":1}},
            {"text": "裏方で支える","scores":{"制作":2}},
        ]
    },
    {
        "question": "Q2. 得意なことは？",
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
    st.markdown('<div class="title">セクション適性診断</div>', unsafe_allow_html=True)

    bar = st.progress(0)
    for i in range(101):
        time.sleep(0.01)
        bar.progress(i)

    st.session_state.started = True
    st.rerun()

# ===== タイトル =====
st.markdown('<div class="title">🎭 セクション適性診断</div>', unsafe_allow_html=True)

# ===== 質問 =====
if st.session_state.q_index < len(QUESTIONS):

    q = QUESTIONS[st.session_state.q_index]

    choice = st.radio(
        q["question"],  # ←ここ重要
        [c["text"] for c in q["choices"]],
        index=None,
        key=st.session_state.q_index
    )

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

    top1 = sorted_scores[0][0]
    top2 = sorted_scores[1][0]

    st.markdown(f"""
    <div class="result-card">
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
