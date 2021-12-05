"""This page is for searching and viewing the list of awesome resources"""
import streamlit as st
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
from webpage.web_food_predict import *

def write():
    #위 구문 안쓰면 오류임

    input_data = st.text_area("식사 전의 기분을 입력하세요!")

    # 여기서 input_data를 감정분석 프로그램에 넘겨주고 그 인수를 받아와야 한다. - 해결!

    Push_listen_button = st.button("AI 음식 추천")
    if Push_listen_button:
        result,link = predict(input_data)
        st.success(result)


    from PIL import Image
    st.image('https://cdn.pixabay.com/photo/2016/08/20/13/06/toppokki-1607479_960_720.jpg', width=700, caption="Image example: Diary")  # 400잡으면 전체 400축소됨.

    st.write(
    """
    
    <AI FOOD의 이론적 배경>

    광운대 산업심리학과 이상희 교수팀 연구논문 '대학생들의 정서에 따른 컴포트 푸드의 차이:성차를 중심으로(2014)'
    
    행복할 때 찾는 음식은?
    남학생 1위 고기, 2위 술
    여학생 1위 치킨, 2위 피자, 스파게티
    
    즐거울 때 찾는 음식은?
    남학생 1위 술, 2위 치킨
    여학생 1위 치킨, 2위 아이스크림
    
    슬플 때 찾는 음식은? 
    남학생 1위 술, 2위 초콜릿
    여학생 1위 초콜릿, 2위 술 
    
    화날 때 찾는 음식은?
    남학생 1위 술, 2위 매운음식
    여학생 1위 매운음식, 2위 초콜릿
    
    c.f. 국민건강증진법 시행령 및 시행규칙 개정안 6월 30에 의거 청소년 대상 주류광고 불가입니다.
    만19세 이상의 제한적 배포가 어렵기에 주류광고는 제거하겠습니다.


    """



    )


if __name__ == "__main__":
    write()