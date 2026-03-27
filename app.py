import streamlit as st
import base64

# ---------- 背景画像設定 ----------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        img = base64.b64encode(f.read()).decode()
    bg_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

set_bg("prism-logo.png")  # 画像ファイル名

# ---------- セクション ----------
sections = [
    "舞台", "音響", "照明", "映像", "衣装",
    "小道具", "制作", "Web", "役者"
]

scores = {s: 0 for s in sections}

# ---------- セクション説明 ----------
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

# ---------- 質問 ----------
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
st.title("🎭 セクション適性診断")

answers = []

for i, (q, choices) in enumerate(questions):
    ans = st.radio(f"Q{i+1}. {q}", list(choices.keys()), key=i)
    answers.append((ans, choices))

if st.button("診断する"):
    # スコア計算
    for ans, choices in answers:
        for sec in choices[ans]:
            scores[sec] += 1

    # 上位2つ取得
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top1, top2 = sorted_scores[0][0], sorted_scores[1][0]

    # 結果表示
    st.markdown("## 🎉 診断結果")

    st.markdown(
        f"### あなたは **{top1} & {top2} セクションタイプ！**"
    )

    st.markdown(
        f"""
        あなたは  
        **{descriptions[top1]}**  
        ＋  
        **{descriptions[top2]}**

        そんなあなたは、この2セクションで大活躍間違いなし！🔥
        """
    )
