"""This page is for searching and viewing the list of awesome resources"""
import streamlit as st
import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
from webpage.web_food_predict import *

def write():
    #위 구문 안쓰면 오류임

    st.title('식사 맛있게 하시고'')
    st.title('따뜻한 시간 보내세요~')
    input_data = st.text_area("식사 전의 기분을 입력하세요!")

    # 여기서 input_data를 감정분석 프로그램에 넘겨주고 그 인수를 받아와야 한다. - 해결!

    Push_listen_button = st.button("AI 음식 추천")
    if Push_listen_button:
        result,link = predict(input_data)
        st.success(result)
        from PIL import Image
        st.image(link, width=700)  # 400잡으면 전체 400축소됨.

    st.image('https://cdn.pixabay.com/photo/2018/04/20/18/13/tablecloth-3336687__340.jpg', width=700)


    st.write(
    """
    
    """



    )


if __name__ == "__main__":
    write()