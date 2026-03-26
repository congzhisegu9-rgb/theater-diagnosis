import streamlit as st

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

st.title("🎭 セクション適性診断")

answers = []

for i, q in enumerate(QUESTIONS):
    choice = st.radio(q["question"], [c["text"] for c in q["choices"]], key=i)
    answers.append(choice)

if st.button("診断する"):
    scores = {section: 0 for section in SECTIONS}

    for i, q in enumerate(QUESTIONS):
        selected_text = answers[i]
        for c in q["choices"]:
            if c["text"] == selected_text:
                for sec, pt in c["scores"].items():
                    scores[sec] += pt

    result = max(scores, key=scores.get)

    st.header(f"あなたにおすすめ 👉 {result}")
    st.write(scores)
