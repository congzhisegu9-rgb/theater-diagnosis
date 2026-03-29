import streamlit as st
import base64
import time

st.set_page_config(
page_title="セクション適性診断"
)
import base64
import time



# ---------- 初回ローディング ----------
if "loading" not in st.session_state:
st.session_state.loading = True
if "result_loading" not in st.session_state:
st.session_state.result_loading = False
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
       left: 50%;
       transform: translateX(-50%);
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
　　.loading-text {{
       margin-top: 25px;
       color: white;
       font-size: 48px;  /* 文字サイズを大きくする */
       letter-spacing: 0.2em;
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
           spin 0.8s linear 3,
           finish 1.1s ease forwards 2.4s;
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

   /* ===== 全辺同時フェード発光 ===== */
   @keyframes finish {{
       0% {{
           stroke-dashoffset: 0;
           stroke: rgba(255,255,255,0.4);
       }}
       100% {{
           stroke-dashoffset: 0;
           stroke: white;
       }}
   }}

   .loading-text {{
       margin-top: 25px;
       color: white;
       font-size: 22px;
       letter-spacing: 0.2em;
   }}

   </style>
   """, unsafe_allow_html=True)


set_bg("prism-logo.png")

# ---------- ローディング ----------
if st.session_state.loading:

st.markdown("""
   <div class="loading-screen">
       <svg class="triangle-svg" viewBox="0 0 100 86.6">
           <path d="M50 0 L100 86.6 L0 86.6 Z" />
       </svg>
       <div class="loading-text">劇工舎プリズム</div>
   </div>
   """, unsafe_allow_html=True)

time.sleep(3.5)

st.session_state.loading = False
st.rerun()

# ===== 以下にあなたの元コードをそのまま貼る =====
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
   /* ===== タイトル ===== */


   .title {{
       text-align: center;
       font-size: 42px;
       font-weight: 700;
       margin-bottom: 2px;
       line-height: 1.05;
   }}

   .fade {{
       animation: fadeIn 0.7s cubic-bezier(0.22, 1, 0.36, 1);
   }}

   @keyframes fadeIn {{
       from {{
           opacity: 0;
           transform: translateY(20px);
       }}
       to {{
           opacity: 1;
           transform: translateY(0);
       }}
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
       line-height: 1.1;
   }}

   
   /* ===== 中央寄せ ===== */
   .choice-wrapper {{
   display: flex;
   flex-direction: column;
   align-items: center;
   justify-content: center;
   gap: 10px;
}}

.choice-wrapper .stButton {{
   width: 100%;
   margin-right: 0 10px;
}}


   div.stButton {{
       margin: 0 !important;
       padding: 0 !important;
       width: 100% !important;
   }}

   div.stButton > button {{
       width: 100%;
       height: 52px;  /* ← 少し戻して押しやすく */

       display: flex !important;
       align-items: center;
       justify-content: center;

       background: transparent !important;
       border: none !important;
       box-shadow: none !important;

       font-size: 32px;   /* ← ここが最大強化ポイント */
       font-weight: 800;  /* ← 超太字 */
       color: #333;

       margin: 0 !important;
       padding: 0 !important;

       border-radius: 8px;

       letter-spacing: 0.05em;
       line-height: 1.0;

       transition: all 0.12s ease;
   }}

   /* ホバー */
   div.stButton > button:hover {{
       background: rgba(0,0,0,0.06) !important;
       transform: scale(1.02);
   }}
/* クリックした瞬間 */
div.stButton > button:active {{
   transform: scale(0.96);
}}
   div.stButton.selected > button {{
       background: rgba(120,150,255,0.25) !important;
   }}

   /* テキスト中央 */
   div.stButton > button p {{
       width: 100%;
       text-align: center !important;
       margin: 0 !important;
       line-height: 1.0 !important;
   }}

   /* ===== 進捗 ===== */
   .stProgress > div > div {{
   background: linear-gradient(90deg, #6c8cff, #9db3ff);
   border-radius: 10px;
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
"制作": "柔軟で素早い対応、頼りになる縁の下の力持ちタイプ！",
"Web": "デジタルで魅せる発信力のあるタイプ！",
"役者": "感情を武器に、世界を作る表現者タイプ！"
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

# ===== 結果直前ローディング =====
if q_index >= len(questions) and not st.session_state.result_loading:
st.session_state.result_loading = True

st.markdown("""
   <div class="loading-screen">
       <svg class="triangle-svg" viewBox="0 0 100 86.6">
           <path d="M50 0 L100 86.6 L0 86.6 Z" />
       </svg>
       <div class="loading-text">診断中...</div>
   </div>
   """, unsafe_allow_html=True)

time.sleep(3.5)
st.rerun()
if q_index < len(questions):
st.markdown(f"""
   <div class="title">セクション適性診断</div>
   <div class="subtitle">{q_index+1} / {len(questions)} 問</div>
   """, unsafe_allow_html=True)
else:
st.markdown("""
   <div class="title">セクション適性診断</div>
   """, unsafe_allow_html=True)


if q_index < len(questions):
q, choices = questions[q_index]

st.markdown(f'<div class="question fade">Q{q_index+1}. {q}</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,2,1])

with col2:

st.markdown('<div class="choice-wrapper fade">', unsafe_allow_html=True)

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

time.sleep(0.2)
st.session_state.q_index += 1
st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

if q_index > 0:
if st.button("← 戻る"):
last_secs = st.session_state.history.pop()
for sec in last_secs:
st.session_state.scores[sec] -= 1

st.session_state.q_index -= 1
st.rerun()

st.progress((q_index + 1) / len(questions))

else:
st.markdown('<div class="title">🎉 診断結果</div>', unsafe_allow_html=True)

sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
top1, top2 = sorted_scores[0][0], sorted_scores[1][0]

st.markdown(f"""
   <div style="background:rgba(255,255,255,0.85); padding:20px; border-radius:12px; text-align:center;">
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
st.session_state.result_loading = False
st.rerun()
