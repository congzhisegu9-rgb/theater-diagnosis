import streamlit as st
import base64

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

    /* 👇 ここが重要：中央パネル化 */
    .block-container {{
        max-width: 700px;
        margin: 60px auto;
        padding: 40px;
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }}

    /* ボタン全幅 */
    .stButton > button {{
        width: 100% !important;
        height: 55px;
        border-radius: 12px;
        font-size: 16px;
        margin: 6px 0;
        transition: 0.2s;
    }}

    .stButton > button:hover {{
        transform: scale(1.02);
    }}

    header, footer {{
        visibility: hidden;
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

# ---------- データ ----------
descriptions = {
    "舞台": "ものづくりが好きで、形にする達成感を大事にするタイプ！",
    "音響": "音にこだわり、空間を演出するセンスの持ち主！",
    "照明": "光で世界観を作る、演出の魔法使いタイプ！",
    "映像": "クリエイティブに表現するのが得意なタイプ！",
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
        "デザイン": ["映像", "Web"],
        "人と関わる": ["役者", "制作"]
    }),
    ("得意なことは？", {
        "細かい作業": ["衣装", "小道具"],
        "音や光": ["音響", "照明"],
        "企画": ["制作"],
        "表現": ["役者"]
    }),
]

# ---------- UI ----------
q_index = st.session_state.q_index

st.markdown("## 🎭 セクション適性診断")

if q_index < len(questions):
    q, choices = questions[q_index]

    st.caption(f"{q_index+1} / {len(questions)} 問")
    st.markdown(f"### Q{q_index+1}. {q}")

    for choice, secs in choices.items():
        if st.button(choice, key=f"{q_index}_{choice}"):
            st.session_state.history.append(secs)
            for sec in secs:
                st.session_state.scores[sec] += 1
            st.session_state.q_index += 1
            st.rerun()

    if q_index > 0:
        if st.button("← 戻る"):
            last_secs = st.session_state.history.pop()
            for sec in last_secs:
                st.session_state.scores[sec] -= 1
            st.session_state.q_index -= 1
            st.rerun()

    st.progress((q_index + 1) / len(questions))

else:
    st.markdown("## 🎉 診断結果")

    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
    top1, top2 = sorted_scores[0][0], sorted_scores[1][0]

    st.markdown(f"### {top1} & {top2} タイプ！")

    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.7); padding:20px; border-radius:15px;">
    <b>{top1}</b>：{descriptions[top1]}<br><br>
    <b>{top2}</b>：{descriptions[top2]}
    </div>
    """, unsafe_allow_html=True)

    if st.button("もう一度"):
        st.session_state.q_index = 0
        st.session_state.scores = {k:0 for k in st.session_state.scores}
        st.session_state.history = []
        st.rerun()
