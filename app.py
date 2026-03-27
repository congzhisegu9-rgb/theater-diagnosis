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
        background-repeat: no-repeat;
    }}

    /* ===== 中央カード ===== */
    .block-container {{
        max-width: 600px;
        margin: 80px auto;
        padding: 60px 50px;

        background: rgba(255,255,255,0.92);
        border-radius: 16px;

        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        backdrop-filter: blur(6px);
    }}

    header, footer {{
        visibility: hidden;
    }}

    /* ===== タイトル ===== */
    .title {{
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 10px;
    }}

    .subtitle {{
        text-align: center;
        color: #888;
        margin-bottom: 30px;
    }}

    .question {{
        text-align: center;
        font-size: 22px;
        font-weight: 600;
        margin: 30px 0;
    }}

    /* ===== ボタン ===== */
    div.stButton {{
        width: 100%;
    }}

    div.stButton > button {{
        width: 100%;
        height: 50px;

        background: transparent !important;
        border: none !important;
        box-shadow: none !important;

        font-size: 18px;
        color: #333;

        text-align: center;

        margin: 12px 0;
        border-radius: 8px;

        transition: all 0.2s ease;
    }}

    div.stButton > button:hover {{
        background: rgba(0,0,0,0.05) !important;
    }}

    div.stButton.selected > button {{
        background: rgba(120,150,255,0.25) !important;
        font-weight: 600;
    }}

    /* ===== 進捗 ===== */
    .stProgress > div > div {{
        background-color: #6c8cff;
    }}

    </style>
    """, unsafe_allow_html=True)


set_bg("prism-logo.png")

# ---------- 状態 ----------
sections = ["舞台","音響","照明","映像","宣伝美術","衣装","小道具","制作","Web","役者"]

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "scores" not in st.session_state:
    st.session_state.scores = {k:0 for k in sections}

if "history" not in st.session_state:
    st.session_state.history = []

if "selected" not in st.session_state:
    st.session_state.selected = {}

# ---------- データ ----------
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
    ("得意なことは？", {
        "細かい作業": ["衣装", "小道具"],
        "音や光": ["音響", "照明"],
        "企画": ["制作"],
        "表現": ["役者"]
    }),
    ("好きな役割は？", {
        "裏で支える": ["制作", "小道具"],
        "技術を極める": ["音響", "照明"],
        "作品を彩る": ["衣装", "宣伝美術"],
        "前に出る": ["役者"]
    }),
    ("どっちが好き？", {
        "チームで動く": ["制作", "舞台"],
        "一人で集中": ["衣装", "映像"],
        "空間づくり": ["照明", "音響"],
        "表現する": ["役者", "宣伝美術"]
    }),
    ("こだわるポイントは？", {
        "見た目": ["衣装", "宣伝美術"],
        "音": ["音響"],
        "光": ["照明"],
        "動き": ["舞台", "役者"]
    }),
    ("作業スタイルは？", {
        "コツコツ": ["衣装", "小道具"],
        "直感": ["役者", "映像"],
        "計画的": ["制作"],
        "試行錯誤": ["照明", "音響"]
    }),
    ("楽しいと感じる瞬間は？", {
        "完成したとき": ["舞台", "小道具"],
        "演出がハマったとき": ["照明", "音響"],
        "表現が伝わったとき": ["役者", "映像"],
        "人に届いたとき": ["制作", "宣伝美術"]
    }),
    ("どんなことにワクワクする？", {
        "ものづくり": ["舞台", "小道具"],
        "演出": ["照明", "音響"],
        "デザイン": ["映像", "宣伝美術"],
        "コミュニケーション": ["制作", "役者"]
    }),
]


# ---------- UI ----------
q_index = st.session_state.q_index

# タイトル
st.markdown(f"""
<div class="title">🎭 セクション適性診断</div>
<div class="subtitle">{q_index+1} / {len(questions)} 問</div>
""", unsafe_allow_html=True)

# 質問表示
if q_index < len(questions):
    q, choices = questions[q_index]

    st.markdown(f'<div class="question">Q{q_index+1}. {q}</div>', unsafe_allow_html=True)

    for choice, secs in choices.items():

        selected_class = ""
        if st.session_state.selected.get(q_index) == choice:
            selected_class = "selected"

        st.markdown(f'<div class="stButton {selected_class}">', unsafe_allow_html=True)

        if st.button(choice, key=f"{q_index}_{choice}"):

            st.session_state.selected[q_index] = choice

            st.session_state.history.append(secs)
            for sec in secs:
                st.session_state.scores[sec] += 1

            st.session_state.q_index += 1
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # 戻るボタン
    if q_index > 0:
        if st.button("← 戻る"):
            last_secs = st.session_state.history.pop()
            for sec in last_secs:
                st.session_state.scores[sec] -= 1

            st.session_state.q_index -= 1
            st.rerun()

    st.progress((q_index + 1) / len(questions))

# ---------- 結果 ----------
else:
    st.markdown('<div class="title">🎉 診断結果</div>', unsafe_allow_html=True)

    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
    top1, top2 = sorted_scores[0][0], sorted_scores[1][0]

    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.85); padding:25px; border-radius:12px; text-align:center;">
    <h2>{top1} & {top2} タイプ！</h2>
    <p><b>{top1}</b><br>{descriptions[top1]}</p>
    <p><b>{top2}</b><br>{descriptions[top2]}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("もう一度"):
        st.session_state.q_index = 0
        st.session_state.scores = {k:0 for k in sections}
        st.session_state.history = []
        st.session_state.selected = {}
        st.rerun()
