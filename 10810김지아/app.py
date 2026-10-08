import streamlit as st
import streamlit.components.v1 as components
import os

# 1. 화면 전체를 넓게 사용하는 설정
st.set_page_config(
    page_title="나만의 입체 가상 공부방",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 여백 최적화 및 불필요한 기본 헤더 제거
st.markdown("""
    <style>
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. index.html 파일 로드
html_file_path = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # 950px 높이로 꽉 차게 렌더링
    components.html(html_code, height=950, scrolling=True)
else:
    st.error("같은 폴더 안에 index.html 파일이 없습니다.")