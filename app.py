import streamlit as st
import base64

# ---------- 背景 ----------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>

    html, body, .stApp {{
        height: 100%;
        margin: 0;
    }}

    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.4);
        z-index: -1;
    }}

    .block-container {{
        max-width: 720px;
        margin: 60px auto;
        padding: 40px 30px;
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(10px);
        border-radius: 20px;
    }}

    header, footer {{
        visibility: hidden;
    }}

    /* 選択肢 */
    .choice-btn > button {{
        width: 90%;
        margin: 10px auto;
        display: block;
        height: 60px;
        border-radius: 999px;
        border: none !important;
        background: transparent !important;
        font-size: 18px;
        text-align: center;
    }}

    .choice-btn.selected > button {{
        background: rgba(120,160,255,0.8) !important;
        color: white !important;
    }}

    /* 👇 ここが重要：ナビボタン制御 */
    .nav-left button {{
        width: 100%;
    }}

    .nav-right {{
        display: flex;
        justify-content: flex-end;
    }}

    .nav-right button {{
        width: 100%;
    }}

    </style>
    """, unsafe_allow_html=True)

set_bg("prism-logo.png")

# ---------- 状態 ----------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "scores" not in st.session_state:
    st.session_state.scores = {k:0 for k in ["舞台","音響","照明","映像","衣装","小道具","制作","Web","役者"]}

if "history" not in st.session_state:
    st.session_state.history = []

if "selected" not in st.session_state:
    st.session_state.selected = {}

# ---------- データ ----------
questions = [
    ("どんな作業が好き？", {
        "体を動かす": ["舞台", "小道具"],
        "機材いじり": ["音響", "照明"],
        "デザイン": ["映像", "Web"],
        "人と関わる": ["役者", "制作"]
    }),
]

# ---------- UI ----------
q_index = st.session_state.q_index

st.markdown("<h1 style='text-align:center;'>🎭 セクション適性診断</h1>", unsafe_allow_html=True)

if q_index < len(questions):
    q, choices = questions[q_index]

    st.markdown(f"<p style='text-align:center;'>{q_index+1} / {len(questions)} 問</p>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;'>Q{q_index+1}. {q}</h2>", unsafe_allow_html=True)

    for choice, secs in choices.items():

        selected_class = ""
        if st.session_state.selected.get(q_index) == choice:
            selected_class = "selected"

        st.markdown(f'<div class="choice-btn {selected_class}">', unsafe_allow_html=True)

        if st.button(choice, key=f"{q_index}_{choice}"):
            st.session_state.selected[q_index] = choice

        st.markdown("</div>", unsafe_allow_html=True)

    # 👇 ナビボタン（ここが本命修正）
    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('<div class="nav-left">', unsafe_allow_html=True)
        if q_index > 0:
            if st.button("← 戻る"):
                st.session_state.q_index -= 1
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="nav-right">', unsafe_allow_html=True)
        if st.button("次へ →"):
            st.session_state.q_index += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.progress((q_index + 1) / len(questions))
