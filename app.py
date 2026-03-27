import streamlit as st
import base64

# ---------- 背景 ----------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        img = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
    }}

    /* 白カード */
    .card {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        color: black;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        max-width: 600px;
        margin: auto;
    }}

    .title {{
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg("prism-logo.png")

# ---------- 状態 ----------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "scores" not in st.session_state:
    st.session_state.scores = {
        "舞台":0,"音響":0,"照明":0,"映像":0,"衣装":0,
        "小道具":0,"制作":0,"Web":0,"役者":0
    }

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
    # （省略OK：他の質問そのまま）
]

# ---------- UI ----------
st.markdown('<div class="title">🎭 セクション適性診断</div>', unsafe_allow_html=True)

q_index = st.session_state.q_index

# 進捗バー
progress = (q_index) / len(questions)
st.progress(progress)

# ---------- 質問 ----------
if q_index < len(questions):
    q, choices = questions[q_index]

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader(f"Q{q_index+1}. {q}")

    answer = st.radio("", list(choices.keys()), key=q_index)

    if st.button("次へ"):
        for sec in choices[answer]:
            st.session_state.scores[sec] += 1
        st.session_state.q_index += 1
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- 結果 ----------
else:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🎉 診断結果")

    sorted_scores = sorted(
        st.session_state.scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top1, top2 = sorted_scores[0][0], sorted_scores[1][0]

    st.markdown(f"## あなたは **{top1} & {top2} タイプ！**")

    st.markdown(f"""
    **{descriptions[top1]}**  
    ＋  
    **{descriptions[top2]}**

    👉 この2セクションで輝けるタイプです！
    """)

    if st.button("もう一度診断する"):
        st.session_state.q_index = 0
        st.session_state.scores = {k:0 for k in st.session_state.scores}
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
