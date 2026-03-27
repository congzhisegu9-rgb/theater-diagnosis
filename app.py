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
        background-repeat: no-repeat;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.3);
        z-index: -1;
    }}

    .main, .block-container {{
        background: transparent;
    }}

    .block-container {{
        padding-top: 20px;
    }}

    header, footer {{
        visibility: hidden;
    }}

    /* カード */
    .card {{
        background-color: rgba(255,255,255,0.95);
        padding: 35px;
        border-radius: 20px;
        color: black;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        max-width: 600px;
        margin: 40px auto;
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
    ("得意なことは？", {
        "細かい作業": ["衣装", "小道具"],
        "音や光": ["音響", "照明"],
        "企画": ["制作"],
        "表現": ["役者"]
    }),
    ("惹かれる役割は？", {
        "形を作る": ["舞台"],
        "雰囲気作り": ["照明", "音響"],
        "世界観": ["衣装", "映像"],
        "まとめ役": ["制作"]
    }),
    ("作業スタイルは？", {
        "コツコツ": ["衣装", "小道具"],
        "本番集中": ["音響", "照明", "役者"],
        "PC作業": ["Web", "映像"],
        "人と話す": ["制作"]
    }),
    ("興味あるのは？", {
        "DIY": ["舞台", "小道具"],
        "音楽": ["音響"],
        "光": ["照明"],
        "ファッション": ["衣装"]
    }),
    ("ワクワクする瞬間は？", {
        "完成": ["舞台"],
        "演出が決まる": ["音響", "照明"],
        "作品完成": ["映像", "衣装"],
        "反応": ["役者", "制作"]
    }),
    ("性格は？", {
        "職人": ["舞台", "小道具", "衣装"],
        "冷静": ["音響", "照明"],
        "クリエイティブ": ["映像", "Web"],
        "社交的": ["制作", "役者"]
    }),
    ("やってみたいのは？", {
        "セット作り": ["舞台"],
        "操作": ["音響", "照明"],
        "編集・制作": ["映像", "Web"],
        "演技": ["役者"]
    })
]

# ---------- UI ----------
q_index = st.session_state.q_index

if q_index < len(questions):
    q, choices = questions[q_index]

    st.markdown('<div class="card">', unsafe_allow_html=True)

    # タイトル（カード内＆見やすく）
    st.markdown("""
    <h2 style='text-align:center; margin-bottom:10px;'>
    🎭 セクション適性診断
    </h2>
    """, unsafe_allow_html=True)

    st.caption(f"{q_index+1} / {len(questions)} 問")

    st.subheader(f"Q{q_index+1}. {q}")

    answer = st.radio("", list(choices.keys()), key=q_index)

    if st.button("次へ"):
        for sec in choices[answer]:
            st.session_state.scores[sec] += 1
        st.session_state.q_index += 1
        st.rerun()

    st.progress((q_index + 1) / len(questions))

    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("## 🎉 診断結果")

    sorted_scores = sorted(
        st.session_state.scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top1, top2 = sorted_scores[0][0], sorted_scores[1][0]

    st.markdown(f"""
    <div style="text-align:center; font-size:24px; margin:20px 0;">
    あなたは<br>
    <span style="font-size:32px; font-weight:bold; color:#ff4b4b;">
    {top1} & {top2}
    </span><br>
    タイプ！
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:#f5f5f5; padding:20px; border-radius:15px; line-height:1.8;">
    <b>{top1}</b>：{descriptions[top1]}<br><br>
    <b>{top2}</b>：{descriptions[top2]}<br><br>
    👉 この2セクションで輝けるタイプです！
    </div>
    """, unsafe_allow_html=True)

    if st.button("もう一度診断する"):
        st.session_state.q_index = 0
        st.session_state.scores = {k:0 for k in st.session_state.scores}
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
