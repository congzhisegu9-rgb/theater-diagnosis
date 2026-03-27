import streamlit as st
import base64
import time

# ---------- 初回ローディング ----------
if "loading" not in st.session_state:
    st.session_state.loading = True

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
    .loading {{
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        color: white;
        font-size: 28px;
        font-weight: bold;
    }}

    .spinner {{
        border: 6px solid rgba(255,255,255,0.2);
        border-top: 6px solid white;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        animation: spin 1s linear infinite;
        margin-bottom: 20px;
    }}

    @keyframes spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}

    </style>
    """, unsafe_allow_html=True)


set_bg("prism-logo.png")

# ---------- ローディング表示 ----------
if st.session_state.loading:

    st.markdown("""
    <div class="loading">
        <div class="spinner"></div>
        Loading...
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)  # ← 表示時間（調整OK）

    st.session_state.loading = False
    st.rerun()

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

st.markdown(f"## 🎭 セクション適性診断")

if q_index < len(questions):
    q, choices = questions[q_index]

    st.markdown(f"### Q{q_index+1}. {q}")

    for choice, secs in choices.items():
        if st.button(choice):

            st.session_state.history.append(secs)
            for sec in secs:
                st.session_state.scores[sec] += 1

            st.session_state.q_index += 1
            st.rerun()

else:
    st.markdown("## 🎉 診断結果")

    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
    top1, top2 = sorted_scores[0][0], sorted_scores[1][0]

    st.markdown(f"### {top1} & {top2} タイプ！")

    st.markdown(f"{descriptions[top1]}\n\n{descriptions[top2]}")
