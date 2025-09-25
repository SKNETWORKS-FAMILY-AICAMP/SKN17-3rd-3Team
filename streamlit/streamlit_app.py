import streamlit as st
import time
from rag import get_response

# 페이지의 제목과 아이콘을 설정합니다.
st.set_page_config(page_title="travelPT", page_icon="🤖")

# 페이지 제목을 중앙에 표시합니다.
st.markdown("<h1 style='text-align: center;'>도와줘 관광피티</h1>", unsafe_allow_html=True)
st.markdown("---")

# st.session_state에 'messages'가 없으면 초기화합니다.
# 이 세션 상태는 페이지가 다시 실행되어도 대화 기록을 유지하는 데 사용됩니다.
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 내용을 모두 보여줍니다.
# for-loop를 통해 st.session_state.messages에 저장된 모든 메시지를 반복하여 출력합니다.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("무엇이든 물어보세요!"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("답변을 생각하고 있어요..."):
        assistant_response, _ = get_response(prompt)
        
    message_placeholder = st.empty()
    full_response = ""

    for chunk in assistant_response.split():
        full_response += chunk + " "
        time.sleep(0.1)
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
        
    # 챗봇의 최종 답변을 대화 기록에 추가합니다.
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.rerun()
    