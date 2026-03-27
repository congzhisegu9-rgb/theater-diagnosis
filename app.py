import streamlit as st
import base64
import time

# ---------- 状態 ----------
if "loading" not in st.session_state:
    st.session_state.loading = True

if "result_loading_done" not in st.session_state:
    st.session_state.result_loading_done = False


# ---------- 背景 ----------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>

    html, body, .stApp {{
        margin: 0;
        padding: 0;
        height: 100%;
    }}

    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* ===== ローディング ===== */
    .loading-screen {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;

        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;

        z-index: 9999;
    }}

    .loading-screen::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0,0,0,0.45);
        z-index: -1;
    }}

    /* ===== 正三角形 ===== */
    .triangle-svg {{
        width: 180px;
        height: 156px;
    }}

    .triangle-svg path {{
        fill: none;
        stroke: rgba(255,255,255,0.25);
        stroke-width: 4;
        stroke-linecap: round;
        stroke-linejoin: round;

        stroke-dasharray: 300;
        stroke-dashoffset: 300;

        animation:
            spin 0.9s linear 3,
            finish 1.4s ease forwards 2.1s;
    }}

    /* ===== 時計回り ===== */
    @keyframes spin {{
        0% {{
            stroke-dashoffset: 300;
        }}
        100% {{
            stroke-dashoffset: 0;
        }}
    }}

    /* ===== 最後に全辺フェード発光 ===== */
    @keyframes finish {{
        0% {{
            stroke: rgba(255,255,255,0.4);
        }}
        100% {{
            stroke: white;
        }}
    }}

    .loading-text {{
        margin-top: 25px;
        color: white;
        font-size: 22px;
        letter-spacing: 0.2em;
    }}

    /* ===== 中央カード ===== */
    .block-container {{
        max-width: 600px;
        margin: 20px auto;
        padding: 28px;

        background: rgba(255,255,255,0.92);
        border-radius: 14px;

        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
        backdrop-filter: blur(6px);
    }}

    header, footer {{
        visibility: hidden;
    }}

    /* ===== タイトル ===== */
    .title {{
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 2px;
    }}

    .subtitle {{
        text-align: center;
        color: #888;
        margin-bottom: 6px;
        font-size: 14px;
    }}

    .question {{
        text-align: center;
        font-size: 30px;
        font-weight: 600;
        margin: 10px 0;
    }}

    .choice-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    .choice-wrapper .stButton {{
        width: 70%;
    }}

    div.stButton > button {{
        width: 100%;
        height: 52px;
        font-size: 32px;
        font-weight: 800;
        background: transparent !important;
        border: none !important;
    }}

    </style>
    """, unsafe_allow_html=True)


set_bg("prism-logo.png")


# ---------- ローディング関数（共通化） ----------
def show_loading():
    st.markdown("""
    <div class="loading-screen">
        <svg class="triangle-svg" viewBox="0 0 100 86.6">
            <path d="M50 0 L100 86.6 L0 86.6 Z" />
        </svg>
        <div class="loading-text">Loading...</div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(3.5)


# ---------- 初回ローディング ----------
if st.session_state.loading:
    show_loading()
    st.session_state.loading = False
    st.rerun()


# ---------- データ ----------
sections = ["舞台","音響","照明","映像","宣伝美術","衣装","小道具","制作","Web","役者"]

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "scores" not in st.session_state:
    st.session_state.scores = {k:0 for k in sections}

if "history" not in st.session_state:
    st.session_state.history = []

if "selected" not in st.session_state:
    st.session_state.selected = {}

descriptions = {
    "舞台": "ものづくりが好きで、形にする達成感を大事にするタイプ！",
    "音響": "音にこだわり、空間を演出するセンスの持ち主！",
    "照明": "光で世界観を作る、演出の魔法使いタイプ！",
    "映像": "クリエイティブに表現するのが得意なタイプ！",
    "宣伝美術": "デザインで作品の魅力を伝える広報センス抜群タイプ！",
    "衣装": "細部までこだわる美意識の高いタイプ！",
    "小道具": "職人肌で、リアルな世界を支えるタイプ！",
    "制作": "全体をまとめるリーダー気質タイプ！",
    "Web": "デジタルで魅せる発信力のあるタイプ！",
    "役者": "感情表現が豊かで、人前に立つのが得意なタイプ！"
}

questions = [
    ("どんな作業が好き？", {
        "体を動かす": ["舞台", "小道具"],
        "機材いじり": ["音響", "照明"],
        "デザイン": ["映像", "Web","宣伝美術"],
        "人と関わる": ["役者", "制作"]
    }),
]

# ---------- UI ----------
q_index = st.session_state.q_index

# ★ 結果直前ローディング
if q_index >= len(questions) and not st.session_state.result_loading_done:
    show_loading()
    st.session_state.result_loading_done = True
    st.rerun()


st.markdown(f"""
<div class="title">🎭 セクション適性診断</div>
<div class="subtitle">{q_index+1} / {len(questions)} 問</div>
""", unsafe_allow_html=True)


if q_index < len(questions):
    q, choices = questions[q_index]

    st.markdown(f'<div class="question">{q}</div>', unsafe_allow_html=True)

    for choice, secs in choices.items():
        if st.button(choice):
            for sec in secs:
                st.session_state.scores[sec] += 1
            st.session_state.q_index += 1
            st.rerun()

else:
    st.markdown('<div class="title">🎉 診断結果</div>', unsafe_allow_html=True)

    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
    top1, top2 = sorted_scores[0][0], sorted_scores[1][0]

    st.write(top1, top2)
