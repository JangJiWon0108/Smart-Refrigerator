# import streamlit as st
# import calendar
# from datetime import date

# # Streamlit 앱 제목
# st.title("유통기한 날짜 선택 캘린더")

# # 오늘 날짜 가져오기
# today = date.today()  # 오늘 날짜를 date 객체로 가져오기

# # 날짜 선택 입력 위젯
# selected_date = st.date_input("날짜를 선택하세요", today)

# # 선택된 날짜의 연도, 월을 분리
# selected_year = selected_date.year
# selected_month = selected_date.month

# # 선택한 연도와 월의 달력 생성
# cal = calendar.monthcalendar(selected_year, selected_month)

# # 달력을 위한 리스트 초기화
# calendar_display = []

# # 각 주를 순회하며 날짜를 리스트에 추가
# for week in cal:
#     week_display = []
#     for day in week:
#         if day == 0:
#             week_display.append(f"<td style='width: 50px; height: 50px; padding: 10px;'></td>")  # 빈 날은 비워둠
#         else:
#             # 오늘 날짜와 선택된 날짜를 기준으로 배경색을 설정
#             day_date = date(selected_year, selected_month, day)
#             if today <= day_date <= selected_date:  # 오늘부터 선택한 날짜까지
#                 week_display.append(f"<td style='width: 50px; height: 50px; background-color: red; color: white; text-align: center; vertical-align: middle; padding: 10px;'>{day}</td>")
#             else:
#                 week_display.append(f"<td style='width: 50px; height: 50px; text-align: center; vertical-align: middle; padding: 10px;'>{day}</td>")
#     calendar_display.append(week_display)

# # 캘린더 출력
# st.write(f"### {selected_year}년 {selected_month}월")

# # Streamlit의 st.markdown()을 사용하여 HTML을 포함한 캘린더 출력
# st.markdown("<table style='border-collapse: collapse; text-align: center;'>", unsafe_allow_html=True)
# for week in calendar_display:
#     st.markdown("<tr>" + "".join(week) + "</tr>", unsafe_allow_html=True)
# st.markdown("</table>", unsafe_allow_html=True)

# # 선택한 날짜 표시
# st.success(f"선택한 날짜: {selected_date}")


# import streamlit as st
# import calendar
# from datetime import datetime, date, timedelta
# import plotly.graph_objects as go
# import random

# # 최소 10가지 색상 목록 정의
# def get_color(index):
#     colors = [
#         '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF',
#         '#33FFF9', '#FF8C33', '#8C33FF', '#33FF8C', '#FF3333'
#     ]
#     return colors[index % len(colors)]

# # 달력 렌더링 함수 정의
# def render_calendar(year, month, marked_items=None):
#     # Calendar 모듈로 월간 달력 데이터 가져오기
#     cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
#     month_days = list(cal.itermonthdays(year, month))
    
#     # 날짜 데이터를 2차원 리스트로 변환 (7일씩 나눔)
#     weeks = [month_days[i:i + 7] for i in range(0, len(month_days), 7)]
    
#     # 빈 칸을 채우기 위해 첫 주와 마지막 주 처리
#     if len(weeks[0]) < 7:
#         weeks[0] = [''] * (7 - len(weeks[0])) + weeks[0]
#     if len(weeks[-1]) < 7:
#         weeks[-1] = weeks[-1] + [''] * (7 - len(weeks[-1]))
    
#     # 셀 데이터 생성 (날짜가 없는 셀은 공백 처리)
#     cell_values = []
#     for week in weeks:
#         week_values = []
#         for day in week:
#             if day == '' or day == 0:
#                 week_values.append('')
#             else:
#                 cell_content = f"<b>{day}</b>"
#                 if marked_items:
#                     for item in marked_items:
#                         if date(year, month, day) in item['dates']:
#                             cell_content += f"<br><span style='color:{item['color']};'>{item['name']}</span>"
#                 week_values.append(cell_content)
#         cell_values.append(week_values)
    
#     # 셀 데이터 플랫화
#     cell_values_flat = []
#     for week in cell_values:
#         cell_values_flat.append([f"{day}" for day in week])
    
#     # Plotly를 사용하여 달력 그리기
#     fig = go.Figure(
#         data=[
#             go.Table(
#                 header=dict(values=['S', 'M', 'T', 'W', 'T', 'F', 'S'],
#                             line_color='darkslategray',
#                             fill_color='lightskyblue',
#                             align='center',
#                             font=dict(color='black', size=14),
#                             height=30),
#                 cells=dict(values=list(zip(*cell_values_flat)),
#                            line_color='darkslategray',
#                            fill_color='white',
#                            align='left',  # 셀 왼쪽 위에 날짜 숫자를 표시하기 위해 정렬을 왼쪽으로 설정
#                            font=dict(color='black', size=14),
#                            height=80),  # 셀의 세로길이를 더 길게 설정
#                 columnwidth=[80] * 7
#             )
#         ]
#     )

#     fig.update_layout(margin=dict(l=5, r=5, t=20, b=20), height=600)
#     return fig

# # Streamlit 앱 제목 설정
# st.title('Streamlit 달력 예제')

# # 오늘의 날짜 가져오기
# today = datetime.today()

# def main():
#     # 상태 저장을 위해 세션 상태 사용
#     if 'year' not in st.session_state:
#         st.session_state.year = today.year
#     if 'month' not in st.session_state:
#         st.session_state.month = today.month
#     if 'marked_items' not in st.session_state:
#         st.session_state.marked_items = []

#     # 품목 입력
#     item = st.text_input('품목 입력')

#     # 일 수 선택 버튼 및 달력
#     selected_dates = st.date_input('시작 및 종료 날짜 선택', value=[today, today], min_value=datetime(today.year, 1, 1), max_value=datetime(today.year, 12, 31))

#     # 완료 버튼 생성
#     if st.button('완료'):
#         if len(selected_dates) == 2 and item:
#             start_date, end_date = selected_dates
#             marked_dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
#             # 최소 10가지 색상 중에서 선택
#             color = get_color(len(st.session_state.marked_items))
#             st.session_state.marked_items.append({'name': item, 'dates': marked_dates, 'color': color})

#     # 현재 연도와 월 표시 및 달을 넘기는 버튼
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col1:
#         if st.button('이전 달'):
#             if st.session_state.month == 1:
#                 st.session_state.month = 12
#                 st.session_state.year -= 1
#             else:
#                 st.session_state.month -= 1
#     with col2:
#         st.write(f"### {st.session_state.year}년 {st.session_state.month}월")
#     with col3:
#         if st.button('다음 달'):
#             if st.session_state.month == 12:
#                 st.session_state.month = 1
#                 st.session_state.year += 1
#             else:
#                 st.session_state.month += 1

#     # 달력 표시
#     calendar_fig = render_calendar(st.session_state.year, st.session_state.month, st.session_state.marked_items)
#     st.plotly_chart(calendar_fig)

# if __name__ == "__main__":
#     main()

from datetime import date, datetime, timedelta
import calendar
import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import json


# 최소 10가지 색상 목록 정의
def get_color(index):
    colors = [
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF',
        '#33FFF9', '#FF8C33', '#8C33FF', '#33FF8C', '#FF3333'
    ]
    return colors[index % len(colors)]

# 달력 렌더링 함수 정의
def render_calendar(year, month, marked_items=None):
    # Calendar 모듈로 월간 달력 데이터 가져오기
    cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
    month_days = list(cal.itermonthdays(year, month))

    # 날짜 데이터를 2차원 리스트로 변환 (7일씩 나눔)
    weeks = [month_days[i:i + 7] for i in range(0, len(month_days), 7)]

    # 빈 칸을 채우기 위해 첫 주와 마지막 주 처리
    if len(weeks[0]) < 7:
        weeks[0] = [''] * (7 - len(weeks[0])) + weeks[0]
    if len(weeks[-1]) < 7:
        weeks[-1] = weeks[-1] + [''] * (7 - len(weeks[-1]))

    # 셀 데이터 생성 (날짜가 없는 셀은 공백 처리)
    cell_values = []
    for week in weeks:
        week_values = []
        for day in week:
            if day == '' or day == 0:
                week_values.append('')
            else:
                cell_content = f"<b>{day}</b>"
                if marked_items:
                    for item in marked_items:
                        if date(year, month, day) in item['dates']:
                            cell_content += f"<br><span style='color:{item['color']};'>{item['name']}</span>"
                week_values.append(cell_content)
        cell_values.append(week_values)

    # 셀 데이터 플랫화
    cell_values_flat = []
    for week in cell_values:
        cell_values_flat.append([f"{day}" for day in week])

    # Plotly를 사용하여 달력 그리기
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(values=['S', 'M', 'T', 'W', 'T', 'F', 'S'],
                            line_color='darkslategray',
                            fill_color='lightskyblue',
                            align='center',
                            font=dict(color='black', size=14),
                            height=30),
                cells=dict(values=list(zip(*cell_values_flat)),
                            line_color='darkslategray',
                            fill_color='white',
                            align='left',
                            font=dict(color='black', size=14),
                            height=80),
                columnwidth=[80] * 7
            )
        ]
    )

    fig.update_layout(margin=dict(l=5, r=5, t=20, b=20), height=600)
    return fig



# 메인 함수
def calendar_main():
    # 오늘의 날짜 가져오기
    today = datetime.today()

    # 상태 저장을 위해 세션 상태 사용
    if 'year' not in st.session_state:
        st.session_state.year = today.year
    if 'month' not in st.session_state:
        st.session_state.month = today.month
    if 'marked_items' not in st.session_state:
        st.session_state.marked_items = []

    # 품목 입력
    item = st.text_input('품목 입력')

    # 일 수 선택 버튼 및 달력
    selected_dates = st.date_input('시작 및 종료 날짜 선택', value=[today, today], min_value=datetime(today.year, 1, 1), max_value=datetime(today.year, 12, 31))

    # 완료 버튼 생성
    if st.button('완료'):
        if len(selected_dates) == 2 and item:
            start_date, end_date = selected_dates
            marked_dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
            # 최소 10가지 색상 중에서 선택
            color = get_color(len(st.session_state.marked_items))
            st.session_state.marked_items.append({'name': item, 'dates': marked_dates, 'color': color})
            


    # 유통기한 경고 표시
    for item in st.session_state.marked_items:
        # 유통기한의 마지막 날짜 계산
        if item['dates']:
            expiry_date = max(item['dates'])
            remaining_days = (expiry_date - today.date()).days

            # 남은 유통기한이 3일 이하일 경우 경고 표시
            if remaining_days <= 3 and remaining_days >= 0:
                st.warning(f"{item['name']}의 유통기한이 {remaining_days}일 남았습니다!")

    # 품목 삭제 기능
    st.markdown("<h4>등록된 품목 목록</h4>", unsafe_allow_html=True)
    if len(st.session_state.marked_items) > 0:
        for i, item in enumerate(st.session_state.marked_items):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{item['name']}** - {item['dates'][0]} ~ {item['dates'][-1]}")
            with col2:
                if st.button(f"삭제 {i + 1}", key=f"delete_{i}"):
                    del st.session_state.marked_items[i]
                    st.experimental_rerun()  # 삭제 후 페이지 새로고침
                

    # 현재 연도와 월 표시 및 달을 넘기는 버튼
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button('◀️이전 달'):
            if st.session_state.month == 1:
                st.session_state.month = 12
                st.session_state.year -= 1
            else:
                st.session_state.month -= 1
    with col2:
        st.write(f"### {st.session_state.year}년 {st.session_state.month}월")
    with col3:
        if st.button('다음 달▶️'):
            if st.session_state.month == 12:
                st.session_state.month = 1
                st.session_state.year += 1
            else:
                st.session_state.month += 1

    # 달력 표시
    calendar_fig = render_calendar(st.session_state.year, st.session_state.month, st.session_state.marked_items)
    st.plotly_chart(calendar_fig)

    # 품목 저장
    marked_items_list = list(st.session_state.marked_items)
    with open('marked_items.txt', 'w') as f:
        for item in marked_items_list:
            # 날짜 리스트를 문자열로 변환 (YYYY-MM-DD 형식)
            dates_str = ', '.join([d.strftime('%Y-%m-%d') for d in item['dates']])
            
            # 딕셔너리를 문자열로 변환하여 저장
            f.write(f"{item['name']} | {dates_str} | {item['color']}\n")