import streamlit as st
import base64

# ===== 背景画像読み込み =====
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("prism-logo.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        z-index: -1;
    }}

    h1, h2, h3, p {{
        color: white;
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ===== データ =====
SECTIONS = ["舞台", "音響", "照明", "映像", "衣装", "小道具", "制作", "Web", "役者"]

QUESTIONS = [
    {
        "question": "どんな作業が好き？",
        "choices": [
            {"text": "体を動かす", "scores": {"舞台": 2, "役者": 2}},
            {"text": "機械いじり", "scores": {"音響": 2, "照明": 2}},
            {"text": "デザイン", "scores": {"衣装": 2, "映像": 1}},
            {"text": "裏方で支える", "scores": {"制作": 2}},
        ]
    },
    {
        "question": "得意なことは？",
        "choices": [
            {"text": "人前で話す", "scores": {"役者": 3}},
            {"text": "PC作業", "scores": {"Web": 3, "映像": 1}},
            {"text": "細かい作業", "scores": {"小道具": 2, "衣装": 2}},
            {"text": "全体管理", "scores": {"制作": 3}},
        ]
    }
]

# ===== 状態管理 =====
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.scores = {s: 0 for s in SECTIONS}

# ===== UI =====
st.image("prism-logo.jpg", width=200)
st.title("セクション適性診断")

# ===== 質問 =====
if st.session_state.q_index < len(QUESTIONS):
    q = QUESTIONS[st.session_state.q_index]

    st.subheader(f"Q{st.session_state.q_index+1}. {q['question']}")

    choice = st.radio("", [c["text"] for c in q["choices"]])

    if st.button("次へ", use_container_width=True):
        for c in q["choices"]:
            if c["text"] == choice:
                for sec, pt in c["scores"].items():
                    st.session_state.scores[sec] += pt

        st.session_state.q_index += 1
        st.rerun()

# ===== 結果 =====
else:
    result = max(st.session_state.scores, key=st.session_state.scores.get)

    st.header(f"あなたにおすすめ 👉 {result}")
    st.write(st.session_state.scores)

    if st.button("もう一度"):
        st.session_state.q_index = 0
        st.session_state.scores = {s: 0 for s in SECTIONS}
        st.rerun()
