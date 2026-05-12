"""
실습 3용 Streamlit 프론트엔드 (EC2 배포 대상).
터미널에서 `streamlit run app.py` 실행 시 요청 로그가 콘솔에 출력됩니다.
"""

import streamlit as st

st.set_page_config(page_title="OSS 실습 3", page_icon="🖥️")

st.title("오픈소스소프트웨어실습 · EC2 배포 데모")
st.markdown(
    "간단한 입력과 버튼으로 동작을 확인합니다. "
    "**브라우저에서 조작할 때** EC2 터미널에 Streamlit 로그가 함께 찍히는지 데모 영상에 담아 주세요."
)

name = st.text_input("이름을 입력하세요", placeholder="예: 홍길동")
message = st.text_area("메시지 (선택)", placeholder="짧은 문장을 적어도 됩니다.")

if st.button("실행"):
    if not name.strip():
        st.warning("이름을 한 글자 이상 입력해 주세요.")
        print("[demo] 실행 버튼: 이름 미입력")
    else:
        print(f"[demo] 실행 버튼: name={name.strip()!r}, message_len={len(message.strip())}")
        st.success(f"안녕하세요, **{name.strip()}** 님!")
        if message.strip():
            st.info(f"메시지: {message.strip()}")
        st.caption("버튼 클릭 시 서버에서 세션이 갱신되며, 터미널에 HTTP 요청 로그가 이어집니다.")

st.divider()
st.markdown(
    "이후 실습 4에서는 **FastAPI** 백엔드와 연동할 수 있도록 이 화면을 확장하면 됩니다."
)
