import streamlit as st
import os
# 각 기능별 파일을 exec(open(...))으로 실행하는 구조
# Streamlit 공식 multipage 구조를 쓰면 더 안전하지만, 요청대로 기존 방식 유지

st.set_page_config(page_title="반려견 케어 통합 서비스", layout="wide")
st.sidebar.title("🐾 분리불안 반려견 케어")

page = st.sidebar.radio(
    "이동할 기능을 선택하세요",
    ("불안 행동 실시간 알림","맞춤형 강아지 챗봇", "실시간 사진 스트리밍",  "분리불안 리포트")
)


if page == "불안 행동 실시간 알림":
    st.header("불안 행동 실시간 알림")
    exec(open(os.path.join(os.path.dirname(__file__), "inform.py")).read())
elif page == "맞춤형 강아지 챗봇":
    st.header("맞춤형 강아지 챗봇")
    exec(open(os.path.join(os.path.dirname(__file__), "index.py")).read())
elif page == "실시간 사진 스트리밍":
    st.header("실시간 사진 스트리밍")
    exec(open(os.path.join(os.path.dirname(__file__), "video.py")).read())

elif page == "분리불안 리포트":
    st.header("분리불안 리포트")
    exec(open(os.path.join(os.path.dirname(__file__), "report.py")).read())
