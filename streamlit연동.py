import streamlit as st
import pymysql
import pandas as pd
#import pandas_bokeh
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px

conn = pymysql.connect(host='127.0.0.1', port = 3306, user = 'root', password='root1234',db = 'shoppingdb', charset= 'utf8') # 내 서버 ip 주소와 연결

cur = conn.cursor()

customers_data = pd.read_csv("customers.csv", sep=",")
orders_data = pd.read_csv("orders.csv", sep=",")
products_data = pd.read_csv("products.csv", sep=",")
sales_data = pd.read_csv("sales.csv", sep=",")

st.set_page_config(page_title="Customer Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )
#st.dataframe(df)

# st.sidebar.header("Please Filter Here: ")
# city = st.sidebar.multiselect(
#     "Select the Month",
#     options=df["City"]


st.title('🇦🇺 Customer Dashboard')

tab1, tab2, tab3 = st.tabs(["✅My shop","🙋‍♀️🙋‍♂️Customer","🛒🛍️Items"])

total_users = int(customers_data["customer_id"].count)
total_products = int(products_data["product_id"].count)
average_delivery_time = avg(

with tab1:
    st.markdown("### My shop DashBoard")
    st.write(customers_data)

    st.subheader('gender')
    customers_gender = pd.DataFrame(customers_data['gender'].value_counts())
    st.bar_chart(customers_gender)
    
    st.subheader('age')
    customers_age = pd.DataFrame(customers_data['age'].value_counts())
    st.bar_chart(customers_age)

    st.subheader('city')
    customers_city = pd.DataFrame(customers_data['city'].value_counts())
    st.bar_chart(customers_city)

with tab2:
    st.markdown("### Customer Dataset")
    st.write(customers_data)

    st.subheader('gender')
    customers_gender = pd.DataFrame(customers_data['gender'].value_counts())
    st.bar_chart(customers_gender)
    
    st.subheader('age')
    customers_age = pd.DataFrame(customers_data['age'].value_counts())
    st.bar_chart(customers_age)

    st.subheader('city')
    customers_city = pd.DataFrame(customers_data['city'].value_counts())
    st.bar_chart(customers_city)

with tab3:
    st.markdown("### Item Dataset")
    st.write(customer_data)

    st.subheader('gender')
    customers_gender = pd.DataFrame(customer_data['gender'].value_counts())
    st.bar_chart(customers_gender)
    
    st.subheader('age')
    customers_age = pd.DataFrame(customer_data['age'].value_counts())
    st.bar_chart(customers_age)

    st.subheader('city')
    customers_city = pd.DataFrame(customer_data['city'].value_counts())
    st.bar_chart(customers_city)

# # 전체 고객 성별 통계
# import matplotlib.pyplot as plt
# plt.rcParams["figure.figsize"] = (4,2)

# fig = plt.figure(figsize=(5,5))


# labels = ['Male', 'Non-binary', 'Polygender', 'Genderqueer', 'Genderfluid', 'Bigender', 'Female', 'Agender']
# points = [143, 131, 128, 127, 122, 120, 115, 114]

# plt.title('Customers gender')
# plt.pie(points, labels=labels, autopct='%.1f%%', counterclock=False, startangle=90)
# st.pyplot(fig)

# 전체 고객 연령 통계  
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=["a", "b", "c"])

# st.bar_chart(chart_data)


#orders_data =  pd.read_csv("orders.csv", sep=",")

# st.write(orders_data)

# month_options = orders_data['order_month'].unique().tolist()
# month = st.selectbox('Which month would you like to see?', month_options,0)
# orders_data = orders_data[orders_data['order_month']==month]

