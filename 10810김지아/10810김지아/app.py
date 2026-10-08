import streamlit as st
import streamlit.components.v1 as components
import os

# 1. 화면 가로 폭 꽉 차게 설정
st.set_page_config(
    page_title="3D Viewer",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 여백을 줄이고 여분의 스크롤을 방지하는 CSS 설정
st.markdown("""
    <style>
        /* 기본 여백 및 상하 패딩 제거 */
        html, body, [data-testid="stAppViewContainer"], .main {
            overflow: hidden !important;
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
            max-width: 100% !important;
        }
        
        /* 상단 헤더 및 하단 푸터 숨기기 */
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. 같은 폴더에 있는 HTML 파일 읽어오기
html_file_path = "index.html"  # 만약 HTML 파일명이 다르다면 이름만 수정해주세요 (예: "main.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # 4. 읽어온 HTML을 화면에 렌더링 (height 숫자로 전체 화면 높이 조절)
    # ※ 화면에서 스크롤이 생기거나 가려지면 height=600 숫자를 550, 500 등으로 살짝 조절해보세요.
    components.html(html_content, height=600, scrolling=False)
else:
    st.error(f"'{html_file_path}' 파일을 찾을 수 없습니다. app.py와 같은 폴더에 있는지 확인해 주세요!")