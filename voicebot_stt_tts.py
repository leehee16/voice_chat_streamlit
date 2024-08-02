import streamlit as st

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
            쏼라쏼라
            '''
        )
        st.markdown("")

#실행
if __name__ == "__main__" :
    print(__name__)
    main()