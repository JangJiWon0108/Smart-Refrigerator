import streamlit as st
import calendar
from datetime import date

# Streamlit 앱 제목
st.title("유통기한 날짜 선택 캘린더")

# 오늘 날짜 가져오기
today = date.today()  # 오늘 날짜를 date 객체로 가져오기

# 날짜 선택 입력 위젯
selected_date = st.date_input("날짜를 선택하세요", today)

# 선택된 날짜의 연도, 월을 분리
selected_year = selected_date.year
selected_month = selected_date.month

# 선택한 연도와 월의 달력 생성
cal = calendar.monthcalendar(selected_year, selected_month)

# 달력을 위한 리스트 초기화
calendar_display = []

# 각 주를 순회하며 날짜를 리스트에 추가
for week in cal:
    week_display = []
    for day in week:
        if day == 0:
            week_display.append(f"<td style='width: 50px; height: 50px; padding: 10px;'></td>")  # 빈 날은 비워둠
        else:
            # 오늘 날짜와 선택된 날짜를 기준으로 배경색을 설정
            day_date = date(selected_year, selected_month, day)
            if today <= day_date <= selected_date:  # 오늘부터 선택한 날짜까지
                week_display.append(f"<td style='width: 50px; height: 50px; background-color: red; color: white; text-align: center; vertical-align: middle; padding: 10px;'>{day}</td>")
            else:
                week_display.append(f"<td style='width: 50px; height: 50px; text-align: center; vertical-align: middle; padding: 10px;'>{day}</td>")
    calendar_display.append(week_display)

# 캘린더 출력
st.write(f"### {selected_year}년 {selected_month}월")

# Streamlit의 st.markdown()을 사용하여 HTML을 포함한 캘린더 출력
st.markdown("<table style='border-collapse: collapse; text-align: center;'>", unsafe_allow_html=True)
for week in calendar_display:
    st.markdown("<tr>" + "".join(week) + "</tr>", unsafe_allow_html=True)
st.markdown("</table>", unsafe_allow_html=True)

# 선택한 날짜 표시
st.success(f"선택한 날짜: {selected_date}")
