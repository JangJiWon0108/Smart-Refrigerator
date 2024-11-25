import streamlit as st
import json
from datetime import datetime

def item_list_show():
    with open('marked_items.txt', 'r') as f:
        # 각 줄을 읽고 딕셔너리 형태로 복원하여 리스트에 저장
        marked_items_list = []
        for line in f.readlines():
            name, dates_str, color = line.strip().split(' | ')  # '|'로 구분된 항목들
            
            # 날짜 문자열을 datetime.date 객체로 변환
            dates = [datetime.strptime(date_str.strip(), '%Y-%m-%d').date() for date_str in dates_str.split(', ')]
            
            # 딕셔너리 형태로 복원하여 리스트에 추가
            marked_items_list.append({'name': name, 'dates': dates, 'color': color})

    if len(marked_items_list) > 0:
        for item in marked_items_list:
            st.write(f"**{item['name']}** - {item['dates'][0]} ~ {item['dates'][-1]}")
    else:
        st.info("등록된 품목이 없습니다.")
