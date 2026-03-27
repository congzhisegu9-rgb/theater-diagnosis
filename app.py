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

    /* ===== ローディング画面 ===== */
    .loading-screen {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;

        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;

        background: rgba(0,0,0,0.35);
        z-index: 9999;
    }}

    /* ===== 正三角形（上向き） ===== */
    .triangle {{
        position: relative;
        width: 150px;
        height: calc(150px * 0.866);
    }}

    .edge {{
        position: absolute;
        height: 4px;
        background: rgba(255,255,255,0.2);
        transform-origin: left center;
    }}

    /* 下辺 */
    .e1 {{
        width: 150px;
        top: 0;
        left: 0;
        transform: rotate(0deg);
        animation: glow1 1.8s infinite;
    }}

    /* 左辺 */
    .e2 {{
        width: 150px;
        top: 0;
        left: 0;
        transform: rotate(120deg);
        animation: glow2 1.8s infinite;
    }}

    /* 右辺 */
    .e3 {{
        width: 150px;
        top: 0;
        left: 0;
        transform: rotate(-120deg);
        animation: glow3 1.8s infinite;
    }}

    /* アニメーション */
    @keyframes glow1 {{
        0%,100% {{ background: rgba(255,255,255,0.2); }}
        20% {{ background: white; }}
    }}

    @keyframes glow2 {{
        0%,100% {{ background: rgba(255,255,255,0.2); }}
        50% {{ background: white; }}
    }}

    @keyframes glow3 {{
        0%,100% {{ background: rgba(255,255,255,0.2); }}
        80% {{ background: white; }}
    }}

    .loading-text {{
        margin-top: 28px;
        color: white;
        font-size: 22px;
        letter-spacing: 0.2em;
    }}

    /* ===== ここから元UI（そのまま） ===== */

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

    .title {{
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 2px;
        line-height: 1.05;
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

    .choice-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    .choice-wrapper .stButton {{
        width: 70%;
    }}

    div.stButton {{
        margin: 0 !important;
        padding: 0 !important;
    }}

    div.stButton > button {{
        width: 100%;
        height: 52px;

        display: flex !important;
        align-items: center;
        justify-content: center;

        background: transparent !important;
        border: none !important;
        box-shadow: none !important;

        font-size: 32px;
        font-weight: 800;
        color: #333;

        margin: 0 !important;
        padding: 0 !important;

        border-radius: 8px;

        letter-spacing: 0.05em;
        line-height: 1.0;

        transition: all 0.12s ease;
    }}

    div.stButton > button:hover {{
        background: rgba(0,0,0,0.06) !important;
        transform: scale(1.02);
    }}

    div.stButton.selected > button {{
        background: rgba(120,150,255,0.25) !important;
    }}

    div.stButton > button p {{
        width: 100%;
        text-align: center !important;
        margin: 0 !important;
        line-height: 1.0 !important;
    }}

    .stProgress > div > div {{
        background-color: #6c8cff;
    }}

    </style>
    """, unsafe_allow_html=True)


set_bg("prism-logo.png")

# ---------- ローディング ----------
if st.session_state.loading:

    st.markdown("""
    <div class="loading-screen">
        <div class="triangle">
            <div class="edge e1"></div>
            <div class="edge e2"></div>
            <div class="edge e3"></div>
        </div>
        <div class="loading-text">Loading...</div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2.5)

    st.session_state.loading = False
    st.rerun()
