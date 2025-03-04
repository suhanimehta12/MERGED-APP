# -*- coding: utf-8 -*-
"""merged_app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QpKhGD2d_fzcUl_DXJOHep8bEyz1Q8ga
"""

!pip install streamlit

!pip install streamlit scikit-learn pandas numpy
!npm install -g localtunnel

!wget -q -O - https://loca.lt/mytunnelpassword

# Commented out IPython magic to ensure Python compatibility.
# %%writefile fullapp.py
# import streamlit as st
# 
# 
# st.set_page_config(page_title="employee retention and recruitment model", layout="wide")
# 
# 
# st.title("employee retention and recruitment model")
# 
# app_choice = st.radio("Select an Application:", ["employee retention", "employee recruitment"])
# 
# 
# if app_choice == "employee retention":
#     st.page_link("https://blank-app-ztexj6vr8xi.streamlit.app/", label="EMPLOYEE RETENTION APPLICATION")
# 
# 
# elif app_choice == "employee recruitment":
#     st.page_link("https://blank-app-r88p17uu5ea.streamlit.app/", label="EMPLOYEE RECRUITMENT APPLICATION")
#

!streamlit run fullapp.py &>/dev/null &


!npx localtunnel --port 8501

# Commented out IPython magic to ensure Python compatibility.
# %%writefile try.py
# import streamlit as st
# 
# st.page_link("try.py", label="Home", icon="🏠")
# #st.page_link("fullapp.py", label="Page 1", icon="1️⃣")
# #st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
# st.page_link("http://www.google.com", label="Google", icon="🌎")
# 
#

!streamlit run try.py &>/dev/null &


!npx localtunnel --port 8501