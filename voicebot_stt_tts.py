#스트림릿 임포트
import streamlit as st

# OpenAI 패키지 추가
import openai
import os
from dotenv import load_dotenv

# env 경로 지정
try:
    load_dotenv()
    print(".env 파일을 성공적으로 로드했습니다.")
except Exception as e:
    print(f".env 파일을 로드하는 중 오류가 발생했습니다: {e}")

# OpenAI API 키 설정하기
try:
    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key is None:
        raise ValueError("API 키가 환경 변수에서 로드되지 않았습니다.")
    print("API 키를 성공적으로 로드했습니다.")
except Exception as e:
    print(f"API 키를 로드하는 중 오류가 발생했습니다: {e}")

# OpenAI 클라이언트 설정하기
try:
    client = openai.OpenAI(api_key=api_key)
    print("OpenAI 클라이언트를 성공적으로 설정했습니다.")
except Exception as e:
    print(f"OpenAI 클라이언트를 설정하는 중 오류가 발생했습니다: {e}")

##### 메인 함수 #####
def main():
    # 페이지 타이틀 설정 / 탭 이름으로 뜸
    st.set_page_config(page_title="음성 챗봇 프로그램", layout="wide")

    # 제목 / 페이지 안쪽에 글자
    st.header("음성 챗봇 프로그램")

    # 구분선
    st.markdown("---")
    with st.expander(
        "음성 챗봇에 프로그램에 대하여", expanded=True):
        st.write(
            '''
            쏼라쏼라\n
            라쏼라쏼
            '''
        )
        st.markdown("")

    #contents, 길어서 변수 지정
    system_content = "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"

    # session state 초기화
    if "chat" not in st.session_state:
        st.session_state["chat"] = []

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": system_content}]

    if "check_reset" not in st.session_state:
        st.session_state["check_reset"] = False

    # 사이드바 생성
    with st.sidebar:

        # GPT모델 선택 라디오 버튼
        model = st.radio(label = "GPT모델", options=["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo"])
        st.markdown("---")

        # 리셋버튼
        if st.button(label= "초기화") :
             # 리셋 코드 
            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role": "system", "content": system_content}]
            st.session_state["check_reset"] = True
    
    # 기능 구현 공간 : 뷰포트에 왼쪽,오른쪽 아래에 공간만들기
    col1, col2 = st.columns(2)
    with col1:
        # 왼쪽 영역 작성
        st.subheader("질문하기")

    with col2:
        # 오른쪽 영역 작성
        st.subheader("질문/답변")

#실행
if __name__ == "__main__" :
    print(__name__)
    main()