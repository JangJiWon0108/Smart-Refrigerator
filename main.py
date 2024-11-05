# 라이브러리
import streamlit as st
from langchain_core.output_parsers import StrOutputParser


# 모듈
import chat
import date

# 사이드바 메뉴
pass

# 메뉴 리스트
pass

# 챗봇
input_itemlist="돼지고기, 양파"

llm=chat.f_import_llm()
prompt=chat.f_import_prompt()
chain=prompt | llm | StrOutputParser()

llm_answer=chain.invoke({"question":input_itemlist})

st.write(llm_answer)


