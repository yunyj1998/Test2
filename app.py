# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='YYJ Test', page_icon=':bar_chart:', layout='wide')

#Title
st.title("yyj test Portfolio dashboard")

image1 = Image.open("images/123.png").resize((1000, 600))

st.image(image1)

st.write(
    """
    ### Welcome to my portfolio site.
    **This site was created by a young man in his 20s who dreams of becoming a data analyst.**
    """
)

st.subheader('Portfolio contents')
st.write(
    """
   Table of Contents

1. About me
2. Why I learned to programme
3. technology stack
4. Project Portfolio Introduction
5. project code review
6. Introduction to GitHub and blogging
7. other work experience
8.The road ahead
9. other contacts
    """
)

st.subheader('Record your learning')
st.write(
    """
Institution name : **Yonsei It Academy**

kDigital Training
(Big data analysis course using Ai)

Learning period 28 December 2022 - 23 June 2023 Course

We learned Python, R language, SQL, Hadoop, Java, Linux, etc. but the core of our course was Python
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**GitHub: [MR yun ](https://github.com/yunyj1998)**', icon="💡")
with c2:
    st.info('**NAVER brog: [post](https://blog.naver.com/yunyj1998)**', icon="💻")
with c3:
    st.info('**Second job : [Video pd](https://www.notion.so/MR-_YUN-100d23b1a85b42d2b9e29262f02e9011?pvs=4)**', icon="🧠")