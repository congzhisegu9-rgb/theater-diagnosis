st.markdown(f"""
<style>

/* ===== 全体 ===== */
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

/* Streamlitデフォルト非表示 */
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

/* ===== ボタン（選択肢） ===== */
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
