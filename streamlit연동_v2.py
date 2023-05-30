import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import altair as alt
import webbrowser

# 추가 데코
#https://extras.streamlit.app/Color%20ya%20Headers

conn = pymysql.connect(host='127.0.0.1', port = 3306, user = 'root', password='root1234',db = 'shoppingdb', charset= 'utf8') # 내 서버 ip 주소와 연결

cur = conn.cursor()

customers_data = pd.read_csv("customers.csv", sep=",")
orders_data = pd.read_csv("orders.csv", sep=",")
products_data = pd.read_csv("products.csv", sep=",")
sales_data = pd.read_csv("sales.csv", sep=",")
sales_products_data = pd.read_csv("sales_products.csv", sep=",")

st.set_page_config(page_title="Customer Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )


st.title('🇦🇺 Customer Dashboard')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["✅My shop","🙋‍♀️🙋‍♂️Customer","🛒🛍️Items", "👍Recommendation", "🔗correaltion"])



with tab1:
    st.markdown("### DashBoard")

    # 쇼핑몰 전체 지표
    cur.execute('SELECT count(customer_id) FROM customers')
    result1 = cur.fetchone()
    total_users = '{:,}'.format(result1[0])

    cur.execute('SELECT count(product_id) FROM products')
    result2 = cur.fetchone()
    total_products = '{:,}'.format(result2[0])

    cur.execute('select avg(delivery_period) from orders')
    result3 = cur.fetchone()

    import decimal

    decimal_value = decimal.Decimal(result3[0])
    average_delivery_period = round(float(decimal_value),1)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total number of users", total_users)
    col2.metric("Total number of products", total_products)
    col3.metric("Average delivery period", average_delivery_period)

    # 전체 판매량 추이

    st.subheader('Sales 2021')
    sales = pd.DataFrame(orders_data['order_date'].value_counts(ascending=True))
    st.bar_chart(sales)

    ## 상품 타입별 판매량 추이

    st.subheader('Monthly Sales')
    cur.execute('''SELECT COUNT(order_month) FROM orders GROUP BY order_month
                    ORDER BY 
                    CASE
                        WHEN order_month = 'JAN' THEN 1
                        WHEN order_month = 'FEB' THEN 2
                        WHEN order_month = 'MAR' THEN 3
                        WHEN order_month = 'APR' THEN 4
                        WHEN order_month = 'MAY' THEN 5
                        WHEN order_month = 'JUN' THEN 6
                        WHEN order_month = 'JUL' THEN 7
                        WHEN order_month = 'AUG' THEN 8
                        WHEN order_month = 'SEP' THEN 9
                        WHEN order_month = 'OCT' THEN 10
                        ELSE 11 -- 기타 월에 대한 순서를 지정하고 싶은 경우
                    END''')
    result4 = cur.fetchall()

    monlty_sales = pd.DataFrame(result4, index=('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT'))
    #monlty_sales = monlty_sales.reindex(index=('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT'))
    st.bar_chart(monlty_sales)


    #monlty_sales = pd.DataFrame(result4,index= ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT'))
    #st.dataframe(monlty_sales)
    #st.bar_chart(monlty_sales)
# vip_customers_show = pd.DataFrame(vip_customers,
#     index=('1st','2nd','3rd'),                                    
#     columns=('customer_id','customer_name','gender','age','city','Total_payment($)'))
#     st.dataframe(vip_customers_show, use_container_width=True)

    # query = "SELECT sales_id, order_id, s.product_id, product_type, product_name, size, color, price_per_unit, s.quantity, total_price FROM sales as s LEFT JOIN products as p ON s.product_id = p.product_ID"
    # sales_products = pd.read_sql_query(query, conn)

    # chart_data = pd.DataFrame(sales_products_data['sales_id'].value_counts(),
    # columns=['Shirt', 'Jacket', 'Trousers'])
    # st.line_chart(chart_data)

    # chart_data = pd.DataFrame({
    #     'month' = ['JAN', 'FEB', 'MAR', 'APR', 'MAY, 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'] ),
    #     'second column' = result4
    # })

    # chart_data = chart_data(columns={'month':'index'}).set_index('index')

    # order_date_list = sales_products_data['order_date'].to_list()
    # order_date_list

    # sales_by_items = pd.DataFrame({
    #     "ItmeType": ['Shirt', 'Jacket', 'Trousers'],
    #     "Sales":  [i for i in ],
    #     "Date": [count(sales)]
    # })
    
    # line_chart = alt.Chart(sales_by_items).mark_line().encode(
    #         y=  alt.Y('Price ($)', title='Sales'),
    #         x=  alt.X('month(order_date)', title='Month')
    #     ).properties(
    #         height=400, width=700,
    #         title="Monthly Sales by Itmes"
    #     ).configure_title(
    #         fontSize=25
    #     )
    
    # st.altair_chart(line_chart, use_container_width=True)


with tab2:
    st.markdown("### Customer Dataset")
    st.write(customers_data)

    customers_gender = pd.DataFrame(customers_data['gender'].value_counts())
    customers_age = pd.DataFrame(customers_data['age'].value_counts())
    customers_city = pd.DataFrame(customers_data['city'].value_counts())

    left_col, middle_col, right_col = st.columns(3)
    with left_col:
        st.subheader('gender')
        left_col.bar_chart(customers_gender,use_container_width=True)
    with middle_col:
        st.subheader('age')
        middle_col.bar_chart(customers_age,use_container_width=True)
    with right_col:
        st.subheader('city')
        right_col.bar_chart(customers_city,use_container_width=True)

    st.markdown("### VIP Customers")
    cur.execute('''select c.customer_id, customer_name, gender, age, city, sum(o.payment) as `Total_payment($)`
                    from customers c
                    left join orders o on c.customer_id = o.customer_id 
                    group by c.customer_id
                    order by sum(o.payment) desc
                    limit 3
                    ''')
    vip_customers = cur.fetchall()
    
    vip_customers_show = pd.DataFrame(vip_customers,
    index=('1st','2nd','3rd'),                                    
    columns=('customer_id','customer_name','gender','age','city','Total_payment($)'))
    st.dataframe(vip_customers_show, use_container_width=True)
    

    # top3 고객 구매 정보
    st.markdown("### Purchase volume by VIP customer")
    cur.execute('''select count(product_id) as `Total order quantity`
                    from sales_products sp
                    left join orders o on sp.order_id = o.order_id
                    where customer_id = 664
                    ''')
    vip_customer1 = cur.fetchall()
    vip_customers_show1 = pd.DataFrame(vip_customer1)
    vip_customer_val1 = vip_customers_show1[0].values

    cur.execute('''select count(product_id) as `Total order quantity`
                    from sales_products sp
                    left join orders o on sp.order_id = o.order_id
                    where customer_id = 566
                    ''')
    vip_customer2 = cur.fetchall()
    vip_customers_show2 = pd.DataFrame(vip_customer2)
    vip_customer_val2 = vip_customers_show2[0].values

    cur.execute('''select count(product_id) as `Total order quantity`
                    from sales_products sp
                    left join orders o on sp.order_id = o.order_id
                    where customer_id = 282
                    ''')
    vip_customer3 = cur.fetchall()
    vip_customers_show3 = pd.DataFrame(vip_customer3)
    vip_customer_val3 = vip_customers_show3[0].values

    from PIL import Image
    left_col3, middle_col3, right_col3 = st.columns(3)
    with left_col3:
        image1 = Image.open('woman1.png')
        st.image(image1, caption=None, width=190, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    with middle_col3:
        image2 = Image.open('man2.png')
        st.image(image2, caption=None, width=190, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    with right_col3:
        image3 = Image.open('woman3.png')
        st.image(image3, caption=None, width=190, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    col1, col2, col3 = st.columns(3)
    col1.metric(vip_customers_show['customer_name'][0], vip_customer_val1)
    col2.metric(vip_customers_show['customer_name'][1], vip_customer_val2)
    col3.metric(vip_customers_show['customer_name'][2], vip_customer_val3)

with tab3:

    # top3 상품 정보
    st.markdown("### Best 3 Items")
    col1, col2, col3 = st.columns(3)
    col1.metric('✨TOP1✨ Total sales', 24)
    col2.metric('✨TOP1✨Total sales', 24)
    col3.metric('✨TOP2✨Total sales', 23)

    cur.execute('''select product_id,product_type,product_name,size,color,price_per_unit
                    from sales_products
                    where product_id = 579
                    limit 1
                    ''')
    top1_item = cur.fetchone() 
    top1_item_show1 = pd.DataFrame(top1_item,
    index=('product_id','product_type','product_name','size','color','price_per_unit')                                    
    )                      

    cur.execute('''select product_id,product_type,product_name,size,color,price_per_unit
                    from sales_products
                    where product_id = 78
                    limit 1
                    ''')
    top2_item = cur.fetchone() 
    top2_item_show2 = pd.DataFrame(top2_item,
    index=('product_id','product_type','product_name','size','color','price_per_unit')                                    
    ) 

    cur.execute('''select product_id,product_type,product_name,size,color,price_per_unit
                    from sales_products
                    where product_id = 472
                    limit 1
                    ''')
    top3_item = cur.fetchone() 
    top3_item_show3 = pd.DataFrame(top3_item,
    index=('product_id','product_type','product_name','size','color','price_per_unit')                                    
    ) 
    from PIL import Image
    left_col4, middle_col4, right_col4 = st.columns(3)
    with left_col4:
        st.image('https://cdn.shopify.com/s/files/1/0282/3965/9061/products/astra-bomber-jacket-kelly-green-jacket-the-frankie-shop-934712.jpg?v=1638997993',width=190) #이미지에서 우클릭 이미지 주소복사
        st.dataframe(top1_item_show1)
    with middle_col4:
        st.image('https://cdn-img.prettylittlething.com/3/b/1/0/3b10c53f7384a29d430b0c7a5c0550c60a47377b_clx9442_2.jpg?imwidth=300',width=190) #이미지에서 우클릭 이미지 주소복사
        st.dataframe(top2_item_show2)
    with right_col4:
        st.image('https://lillyluimages.s3.amazonaws.com/product-images/530-1000/padded-cropped-puffer-jacket-green-ariadne-lily-lulu-fashion-15.jpg',width=190) #이미지에서 우클릭 이미지 주소복사
        st.dataframe(top3_item_show3)

    #월별 인기 상품 조회(특정기간 아이템 트렌드 분석)
    
    cur.execute('''select DISTINCT month(order_date) as order_month
                    from sales_products
                    order by order_month
                        ''')
    result5 = cur.fetchall()
    month_items = pd.DataFrame(result5)
    month_options = month_items[0].tolist()
    month = st.selectbox(
        'Which month would you like to see?', month_options, 0)
    # month_items = month_items[month_items[0]==month]

    st.write('You selected:', month)

    # cur.execute('''select DISTINCT product_type
    #                 from sales_products
    #                 order by product_type
    #                     ''')
    # result6 = cur.fetchall()
    # items_type = pd.DataFrame(result6)
    # type_options = items_type[0].tolist()
    # type = st.multiselect(
    #     'What items would you like to see?', type_options, ['Shirt']
    #      )

    # st.write('You selected:', type)

    # 월 선택 후 상품 type 별 인기 상품 조회
    montly_hot = pd.read_csv('sales_products.csv')
    columns = montly_hot.columns

    shirt_tab, jacket_tab, trousers_tab = st.tabs(['Shirt','Jacket','Trousers'
])
    with shirt_tab:
        # query1 = '''SELECT product_id, COUNT(product_id) as Sales
        # FROM sales_products
        # WHERE MONTH(order_date) = %s and product_type = 'Shirt'
        # GROUP BY product_id
        # ORDER BY COUNT(product_id) DESC
        # LIMIT 5 
        # '''
        
        # cur.execute(query1, (month,))

        # result6 = cur.fetchall()        
        # columns = [column[0] for column in cur.description]
        # shirt_val = pd.DataFrame(result6, columns=columns)


        query2 = '''SELECT sp.product_id, p.product_name, p.size, p.color, sp.price_per_unit, COUNT(sp.product_id) as sales
                FROM sales_products sp
                JOIN products p ON sp.product_id = p.product_id
                WHERE MONTH(sp.order_date) = %s and sp.product_type = 'Shirt'
                GROUP BY sp.product_id, p.product_name, p.size, p.color, sp.price_per_unit
                ORDER BY COUNT(sp.product_id) DESC
                LIMIT 5
                    '''

        cur.execute(query2, (month,))

        result7 = cur.fetchall()        
        columns = [column[0] for column in cur.description]
        shirt_val2 = pd.DataFrame(result7, index = ('1st','2nd','3rd','4th','5th'), columns=columns)
        st.dataframe(shirt_val2, use_container_width=True)
    
    with jacket_tab:
        query3 = '''SELECT sp.product_id, p.product_name, p.size, p.color, sp.price_per_unit, COUNT(sp.product_id) as sales
                FROM sales_products sp
                JOIN products p ON sp.product_id = p.product_id
                WHERE MONTH(sp.order_date) = %s and sp.product_type = 'Jacket'
                GROUP BY sp.product_id, p.product_name, p.size, p.color, sp.price_per_unit
                ORDER BY COUNT(sp.product_id) DESC
                LIMIT 5
                    '''

        cur.execute(query3, (month,))

        result8 = cur.fetchall()        
        columns = [column[0] for column in cur.description]
        jacket_val = pd.DataFrame(result8, index = ('1st','2nd','3rd','4th','5th'), columns=columns)
        st.dataframe(jacket_val, use_container_width=True)

    with trousers_tab:
        query4 = '''SELECT sp.product_id, p.product_name, p.size, p.color, sp.price_per_unit, COUNT(sp.product_id) as sales
                FROM sales_products sp
                JOIN products p ON sp.product_id = p.product_id
                WHERE MONTH(sp.order_date) = %s and sp.product_type = 'Trousers'
                GROUP BY sp.product_id, p.product_name, p.size, p.color, sp.price_per_unit
                ORDER BY COUNT(sp.product_id) DESC
                LIMIT 5
                    '''

        cur.execute(query4, (month,))

        result9 = cur.fetchall()        
        columns = [column[0] for column in cur.description]
        trousers_val = pd.DataFrame(result9, index = ('1st','2nd','3rd','4th','5th'), columns=columns)
        st.dataframe(trousers_val, use_container_width=True)

with tab4:
    st.markdown("### Item Recommendation")

    # 상품 type 선택
    cur.execute('''select DISTINCT product_type
                    from sales_products
                    order by product_type
                        ''')
    type_result = cur.fetchall()
    items_type = pd.DataFrame(type_result)
    type_options = items_type[0].tolist()
    type = st.selectbox(
        'What items would you like to see?', type_options, 0
         )

    st.write('You selected:', type)

    # 상품 size 선택
    cur.execute('''SELECT DISTINCT size
                    FROM sales_products
                    ORDER BY
                    CASE
                        WHEN size = 'XS' THEN 1
                        WHEN size = 'S' THEN 2
                        WHEN size = 'M' THEN 3
                        WHEN size = 'L' THEN 4
                        WHEN size = 'XL' THEN 5
                        ELSE 6 -- 기타 사이즈에 대한 순서를 지정하고 싶은 경우
                    END
                        ''')
    size_result = cur.fetchall()
    items_size = pd.DataFrame(size_result)
    size_options = items_size[0].tolist()
    size = st.selectbox(
        'What size of item would you like to see?', size_options, 0)

    st.write('You selected:', size)

    # 상품 color 선택
    cur.execute('''SELECT DISTINCT color
                    FROM sales_products
                    ORDER BY
                    CASE
                        WHEN color = 'red' THEN 1
                        WHEN color = 'orange' THEN 2
                        WHEN color = 'yellow' THEN 3
                        WHEN color = 'green' THEN 4
                        WHEN color = 'blue' THEN 5
                        WHEN color = 'indigo' THEN 6
                        WHEN color = 'violet' THEN 7
                        ELSE 8 -- 기타 색상에 대한 순서를 지정하고 싶은 경우
                    END
                        ''')
    color_result = cur.fetchall()
    items_color = pd.DataFrame(color_result)
    color_options = items_color[0].tolist()
    color = st.selectbox(
        'What color of item would you like to see?', color_options, 0)

    st.write('You selected:', color)

    st.text('                                ')
    st.markdown('#### Check out the results below 👇')

    # DataFrame 생성    
    cur.execute('''select product_id, product_type, product_name, size, color, age, price_per_unit
                    from sales_products sp
                    left join customers_orders co on sp.order_id = co.order_id
                    order by age
                        ''')
    reco_result = cur.fetchall()

    reco_items = pd.DataFrame(reco_result, columns=['product_id', 'product_type', 'product_name', 'size', 'color', 'age', 'price_per_unit'])

    # reco_selection = reco_items.query('''
    #     product_type == @type
    #     and size == @size
    #     and color == @color
    # ''')

    # st.dataframe(reco_selection)

    reco_selection = reco_items.query(
        f"product_type == '{type}' and size == '{size}' and color == '{color}'"
    )

    st.dataframe(reco_selection.head(5), use_container_width=True)

    if "search_input_enter_pressed" not in st.session_state:
        st.session_state.search_input_enter_pressed = False

    item_search = st.text_input('Search the item!')

    if item_search:
        if st.button('Search') or (st.session_state.search_input_enter_pressed and st.session_state.search_input == item_search):
            search_query = f"https://www.google.com/search?q={item_search}"
            webbrowser.open_new_tab(search_query)

        if st.session_state.search_input_enter_pressed:
            st.session_state.search_input_enter_pressed = False
            st.session_state.search_input = item_search


    st.text('                                ')
    st.markdown('#### Select the customer age group and product price!')
    st.markdown('##### (you can see more detailed results!😉)')
    st.text('                                ')
    
    # 고객 연령대 선택(구간bar)
    age_values = st.slider(
        'What age would you like to see?',
        0, 80, (25, 45))
    st.write('Values:', age_values)  
  

    # 상품 가격 선택(구간bar)
    price_values = st.slider(
        'What price of item would you like to see?',
        90, 119, (95, 105))
    st.write('Values:', price_values)

    start_button = st.button(
    "filter apply 📊 ")#"버튼에 표시될 내용"

    # button이 눌리는 경우 start_button의 값이 true로 바뀌게 된다.
    # 이를 이용해서 if문으로 버튼이 눌렸을 때를 구현 
    
    if start_button:
    #slider input으로 받은 값에 해당하는 값을 기준으로 데이터를 필터링합니다.
    # age_filter= reco_selection[(reco_selection['age']>= age_values[0]) & (reco_selection['age'] <= age_values[1])]
    # price_filter = reco_selection[(reco_selection['age']>= age_values[0]) & (reco_selection['age'] <= age_values[1])]
        st.success("Filter Applied!👏👏👏")
        age_price_filter = reco_selection[
            (reco_selection['age']>= age_values[0]) & (reco_selection['age'] <= age_values[1])
            &(reco_selection['price_per_unit']>= price_values[0]) & (reco_selection['price_per_unit']<= price_values[1])]
        st.subheader("How about recommend this Item to your customers?")
        st.table(age_price_filter)



# if "search_input_enter_pressed" not in st.session_state:
#     st.session_state.search_input_enter_pressed = False

# item_search = st.text_input('Search the item!')

# if item_search:
#     if st.button('Search') or (st.session_state.search_input_enter_pressed and st.session_state.search_input == item_search):
#         search_query = f"https://www.google.com/search?q={item_search}"
#         webbrowser.open_new_tab(search_query)

#     if st.session_state.search_input_enter_pressed:
#         st.session_state.search_input_enter_pressed = False
#         st.session_state.search_input = item_search

with tab5:
    st.markdown("### Correaltion")

    # cust_order = pd.merge(left=customers_data, right=orders_data, 
    #                   left_index=True, right_index=True) # merging
    # cop_data = pd.merge(left=cust_order, right=products_data, 
    #                 left_index=True, right_index=True) # merging
    # cop_data["sales"] = cop_data["price"] * cop_data["quantity"] # let's make a sales data
                        

    # sns.set_style("whitegrid") # set the seaborn style
    # # let's make a correlation matrix for `cop_data`
    # fig = plt.figure(dpi=100, figsize=(24, 18)) # figure the size
    # sns.heatmap(cop_data.corr(), annot=True, cmap="Blues") # create a heatmap
    # plt.title("COP (Customer, Order, Product) Data Correlation", weight="bold", fontsize=30, fontname="fantasy", pad=75) # title
    # plt.xticks(weight="bold", fontsize=15) # x-ticks
    # plt.yticks(weight="bold", fontsize=15); # y-ticks


    # 데이터 로드
    customers_data = pd.read_csv("customers.csv")
    orders_data = pd.read_csv("orders.csv")
    products_data = pd.read_csv("products.csv")
    sales_products_data = pd.read_csv("sales_products.csv", sep=",")

    # 데이터 병합
    cust_order = pd.merge(left=customers_data, right=orders_data, left_on="customer_id", right_on="customer_id")
    cop_data = pd.merge(left=cust_order, right=sales_products_data, left_on="order_id", right_on="order_id")
    cop_data["sales"] = cop_data["price_per_unit"] * cop_data["quantity"]
    numeric_cols = cop_data.select_dtypes(include=np.number)
    correlation = numeric_cols.corr()

    # Heatmap 생성
    fig = plt.figure(dpi=100, figsize=(24, 18))
    sns.heatmap(correlation, annot=True, cmap="Blues")
    plt.title("COP(Customer, Order, Product) Data Correlation", weight="bold", fontsize=30, fontname="fantasy", pad=75)
    plt.xticks(weight="bold", fontsize=15)
    plt.yticks(weight="bold", fontsize=15)

    # Streamlit에서 표시
    st.pyplot(fig)
