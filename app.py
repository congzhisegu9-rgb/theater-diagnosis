# ===== 質問 =====
if st.session_state.q_index < len(QUESTIONS):
    q = QUESTIONS[st.session_state.q_index]

    # 👇 これが超重要
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(
            f"<h3>Q{st.session_state.q_index+1}. {q['question']}</h3>",
            unsafe_allow_html=True
        )

        # 👇 これもカード内に入る
        choice = st.radio("", [c["text"] for c in q["choices"]])

        # 👇 ボタンも中
        if st.button("次へ", use_container_width=True):
            for c in q["choices"]:
                if c["text"] == choice:
                    for sec, pt in c["scores"].items():
                        st.session_state.scores[sec] += pt

            st.session_state.q_index += 1
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
