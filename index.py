
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os


# .env 파일에서 OPENAI_API_KEY 불러오기
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# 카카오톡 스타일 채팅방 UI 적용
st.markdown("""
    <style>
    .chat-container {
        height: 500px;
        overflow-y: auto;
        background: transparent;
        border-radius: 0;
        padding: 0 0 8px 0;
        margin-bottom: 0;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        box-shadow: none;
    }
    .user-msg {
        text-align: right;
        color: #1a73e8;
        margin: 4px 0;
        background: #e3f2fd;
        border-radius: 16px 16px 4px 16px;
        display: inline-block;
        padding: 8px 14px;
        max-width: 80%;
        float: right;
        clear: both;
    }
    .bot-msg {
        text-align: left;
        color: #222;
        margin: 4px 0;
        background: #fff;
        border-radius: 16px 16px 16px 4px;
        display: inline-block;
        padding: 8px 14px;
        max-width: 80%;
        float: left;
        clear: both;
    }
    </style>
""", unsafe_allow_html=True)

st.title("맞춤형 강아지 GPT 챗봇 🐶")

# 강아지 정보 입력
with st.form("dog_info_form"):
    st.write("강아지에 대한 정보를 자유롭게 입력해주세요!")
    dog_info = st.text_area("강아지 정보", "예: 이름, 나이, 견종, 성격, 건강 상태 등")
    submitted = st.form_submit_button("정보 저장 및 상담 시작")

if "dog_profile" not in st.session_state:
    st.session_state["dog_profile"] = ""

if submitted:
    st.session_state["dog_profile"] = dog_info
    st.success("강아지 정보가 저장되었습니다!")


# 챗봇 대화
def render_chat():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state["chat_history"]:
        if msg["role"] == "user":
            st.markdown(f"<div class='user-msg'>나: {msg['content']}</div>", unsafe_allow_html=True)
        elif msg["role"] == "assistant":
            st.markdown(f"<div class='bot-msg'>강아지 챗봇: {msg['content']}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state["dog_profile"]:
    st.write(f"**내 강아지 정보:** {st.session_state['dog_profile']}")

    # chat_history가 없으면 초기화
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # 채팅 메시지 영역 (항상 최신 메시지가 아래)
    chat_box = st.container()
    with chat_box:
        render_chat()

    # 입력창을 채팅창 아래에 배치
    with st.form("chat_input_form", clear_on_submit=True):
        user_input = st.text_input("", placeholder="메시지를 입력하세요...", key="chat_input")
        submitted = st.form_submit_button("전송")

    if submitted and user_input:
        # system 메시지는 항상 첫 번째로만 추가
        system_message = {"role": "system", "content": f"너는 반려견 전문가 챗봇이야. 사용자가 입력한 강아지 정보: {st.session_state['dog_profile']}를 참고해서 맞춤형 상담을 해줘."}
        messages = [system_message] + st.session_state["chat_history"] + [{"role": "user", "content": user_input}]

        answer = ""
        with st.spinner("답변 생성 중..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                stream=True
            )
            response_container = st.empty()
            for chunk in response:
                delta = chunk.choices[0].delta
                if hasattr(delta, "content") and delta.content:
                    answer += delta.content
                    response_container.markdown(f"<div class='bot-msg'>강아지 챗봇: {answer}▌</div>", unsafe_allow_html=True)
            response_container.markdown(f"<div class='bot-msg'>강아지 챗봇: {answer}</div>", unsafe_allow_html=True)

        st.session_state["chat_history"].append({"role": "user", "content": user_input})
        st.session_state["chat_history"].append({"role": "assistant", "content": answer})

        # 채팅창을 최신 메시지로 스크롤(자동 새로고침)
        st.rerun()
