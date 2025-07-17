import streamlit as st
import time
import os

st.title("강아지 불안 행동 실시간 알림")

ALERT_FILE = "alert.txt"  # YOLO가 불안 감지 시 이 파일에 'anxious' 등 기록

st.error("⚠️ 강아지가 불안해하고 있습니다! 즉시 확인해주세요.")

alert_placeholder = st.empty()

import threading
def show_fake_alert():
    time.sleep(1)
    st.toast("⚠️ 강아지가 불안해하고 있습니다! 즉시 확인해주세요.")

# 앱 시작 후 1초 뒤에 알림이 뜨는 효과
if 'alert_shown' not in st.session_state:
    st.session_state.alert_shown = False
    threading.Thread(target=show_fake_alert).start()
    st.session_state.alert_shown = True
