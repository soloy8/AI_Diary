#-*-coding:utf-8-*-

#다층 페이지 구성을 위하여, 원본 폴더인 diary를 side바 기능만 남긴 main.py로 변경하고, src파일의 Home 파일에 diary를 이전함.

#AI감정분석으로 이전.
#import pandas as pd
#import numpy as np


#import구문.
import streamlit as st

#login용
import pandas as pd
import sqlite3

#sidebar용 page import

import awesome_streamlit as ast
#src import를 못해서 추가시킴.

#scr의 각 페이지 import
import pages.AI감정분석
import pages.AI뮤직
import pages.AI푸드
import pages.AI여행
import pages.달력
import pages.제작진행부분




#test part


#사이드바
#사이드바 PAGES 정의
PAGES = {
    "AI뮤직": pages.AI뮤직,
    "AI푸드": pages.AI푸드,
    "AI감정분석": pages.AI감정분석,
    "AI여행": pages.AI여행,
    "달력": pages.달력,
    "제작진행부분": pages.제작진행부분,

}

st.sidebar.header("어디로 갈까요...")
#임시중지 add_selectbox = st.sidebar.selectbox("왼쪽 사이드바 Select Box", ("일기장", "AI가 분석한 당신의 감정", "감정을 채워줄 노래"))
# 사이드바 분기
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]

#스피너 여기서 들어가서 한번 더 넣으면 이중임.
with st.spinner(f"Loading {selection} ..."):
    ast.shared.components.write_page(page)
st.sidebar.title("Diary_Sentiment_Analysis")
st.sidebar.write("인공지능(AI)  자연어처리(NLP)")
st.sidebar.write("감성분석(Sentiment-Analysis)")
st.sidebar.title("\nContribute")
st.sidebar.write(
"""
황보현 교수님 캡스톤디자인B \n
감동의 8조 (가나다순) \n
길지호 김소원 이상미 이지훈 정준엽\n
\n
모두의 노고에 진심으로 감사드립니다.\n
\n
""")


#사이드바 종료

#본문 ->src pages의 home 파일로 이전.

#st.balloons()
#풍선 상태요소.

# test data
###### 하단 login기능. 

import sqlite3

conn, cur = None, None
conn = sqlite3.connect('capstoneDB.db')
cur = conn.cursor()


def create_usertable():
    cur.execute('CREATE TABLE IF NOT EXISTS userTable(username TEXT,password TEXT)')


def add_userdata(username, password):
    cur.execute('INSERT INTO userTable(username,password) VALUES (?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    cur.execute('SELECT*FROM userTable WHERE username =? AND password=?', (username, password))
    data = cur.fetchall()
    return data


def view_all_users():
    cur.execute('SELECT*FROM userTable')
    data = cur.fetchall()
    return data


def main():
    # 공통실행
    st.title("simple login")

    # 선택실행
    menu = ["Home", "Login", "Signup"]
    choice = st.sidebar.selectbox("Menu", menu)

    ## home(작동확인)
    if choice == "Home":
        st.subheader("Home")


    ## Login
    # c.f. subheader9 미존재로 error
    elif choice == "Login":
        st.subheader("Login Section")
        username = st.sidebar.text_input("User Name")

        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.button("Login"):
            create_usertable()
            result = login_user(username, password)
            if result:
                st.success("Logged In as {}".format(username))
                task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])
                if task == "Add Post":
                    st.subheader("Add your Post")
                elif task == "Analytics":
                    st.subheader("Analytics")
                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result, columns=["Username", "Password"])
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")


    ##Sign_up
    # =
    elif choice == "Signup":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, new_password)
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")


## run
main()