# 라이브러리
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from streamlit_option_menu import option_menu

# 모듈
import chat
import date
import itemlist
import time
import json

# 함수
def stream_data():
    for word in llm_answer.split(" "):
        yield word + " "
        time.sleep(0.06) 

with open('marked_items.txt', 'r') as f:
        # 각 줄을 읽고 딕셔너리 형태로 복원하여 리스트에 저장
        marked_items_list = []
        for line in f.readlines():
            name, dates, color = line.strip().split(' | ')  # '|'로 구분된 항목들
            marked_items_list.append({'name': name})

# 페이지 설정
st.set_page_config(page_title="스마트 냉장고", page_icon="🤖", layout="centered")

# 사이드바 메뉴
with st.sidebar:
    selected = option_menu("Menu", ["유통기한 입력", "물품 리스트", "레시피 추천 챗봇"], 
         icons=["building", 'book', "mortarboard"], menu_icon="robot", default_index=0)


# 유통기한 입력
if selected=="유통기한 입력":
    date.calendar_main()

# 물품 리스트
elif selected=="물품 리스트":
    itemlist.item_list_show()

# 레시피 추천 챗봇
elif selected=="레시피 추천 챗봇":
    title_col1, title_col2, title_col3 = st.columns([0.7, 1, 1])

    # 첫 번째 열에 이미지 추가
    with title_col1:
        st.image("robot_image.png")

    # 두 번째 열에 제목 추가
    with title_col2:
        st.markdown(
            """
            <h1 style='color: black;'>레봇</h1>
            """, 
            unsafe_allow_html=True
        )
        st.markdown("<h5>안녕😁</h5>", unsafe_allow_html=True)
        st.markdown("<h6>나는 레봇이야🌈</h6>", unsafe_allow_html=True)
    
    if 'flag' not in st.session_state:
        st.session_state.flag=False

    if 'message_list' not in st.session_state:
        st.session_state.message_list = []

    for message in st.session_state.message_list:
        with st.chat_message(message["role"]):
            st.write(message["content"])    

    # 초기-냉장고에 있는 재료 기반
    if st.session_state.flag==False:
        # 초기 사용자 질문
        with st.chat_message("user"):
            user_init_message="현재 냉장고에 있는 물품으로 레시피를 하나 추천해줘❗"
            st.write(user_init_message) # user_question에 입력한 텍스트 저장
            st.session_state.message_list.append({"role":"user", "content":user_init_message})

        # 답변 생성 중이라는 ui 출력
        with st.spinner("답변을 생성하는 중입니다."):
            # LLM 모델 답변을 페이지에 띄움
            llm=chat.f_import_llm()
            prompt=chat.f_import_prompt_init()
            chain=prompt | llm | StrOutputParser()
            llm_answer=chain.invoke({"question":marked_items_list})

        with st.chat_message("ai"):
            ai_message=st.write_stream(stream_data)
            st.session_state.message_list.append({"role":"ai", "content":ai_message})

        # flag 반전
        st.session_state.flag=True

    if user_question := st.chat_input(placeholder="레시피를 추천해 드릴게요😁"):
        # 사용자가 입력한 채팅을 페이지에 띄움
        with st.chat_message("user"):
            st.write(user_question) # user_question에 입력한 텍스트 저장
            st.session_state.message_list.append({"role":"user", "content":user_question})

        # 답변 생성 중이라는 ui 출력
        with st.spinner("답변을 생성하는 중입니다."):
            # LLM 모델 답변을 페이지에 띄움

            llm=chat.f_import_llm()
            prompt=chat.f_import_prompt_no_init()
            chain=prompt | llm | StrOutputParser()
            llm_answer=chain.invoke({"question":user_question})

        with st.chat_message("ai"):
            ai_message=st.write_stream(stream_data)
            st.session_state.message_list.append({"role":"ai", "content":ai_message})
    