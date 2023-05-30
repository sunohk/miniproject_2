show databases;
use shoppingdb;
select *
from orders;

-- select order_id, date_format(order_date,'%m') as order_month
-- from orders
-- -- group by month(order_date)
-- order by order_id asc;

-- 새로운 컬럼 추가
ALTER TABLE orders
ADD COLUMN order_month date;

-- 월 추출하여 새로운 컬럼에 업데이트

UPDATE orders
SET order_month = (SELECT DATE_FORMAT(order_date, '%m'));



-- UPDATE orders
-- SET order_month = DATE_FORMAT(order_date, '%m');

select *
from orders;

use shoppingdb;
select *
from products;

select product_type
from products
group by product_type;

select product_name,count(product_name)
from products
group by product_name;

# shirt type 종류, 수량
select product_name, count(product_name)
from products
where product_type = 'Shirt'
group by product_name;

##총 수량(12개 종류 * 35개씩)
select count(product_id)
from products
where product_type = 'Shirt';

# Jacket type 종류, 수량
select product_name, count(product_name)
from products
where product_type = 'Jacket'
group by product_name;

##총 수량(12개 종류 * 35개씩 총 420개)
select count(product_id)
from products
where product_type = 'Jacket';


# 'Trousers' type 종류, 수량
select product_name, count(product_name)
from products
where product_type = 'Trousers'
group by product_name;

##총 수량(12개 종류 * 35개씩)
select count(product_id)
from products
where product_type = 'Trousers';

select *
from orders;

# 배송기간 
select order_id,DATEDIFF(delivery_date,order_date) as delivery_time
from orders
order by delivery_time desc;

select avg(datediff(delivery_date,order_date)) as average_delivery_time
from orders;

-- 새로운 컬럼 추가
ALTER TABLE orders
ADD COLUMN order_month date;

-- 월 추출하여 새로운 컬럼에 업데이트

-- UPDATE orders
-- SET order_month = (SELECT DATE_FORMAT(order_date, '%m'))

UPDATE orders
SET delivery_period = datediff(delivery_date,order_date);

select *
from orders;


commit;

SELECT @@AUTOCOMMIT;



select order_month, count(order_month)
from orders
group by order_month
order by order_month;



select avg(delivery_period)
from orders;

SELECT count(customer_id) FROM customers;

select *
from customers;

select *
from orders;

select *
from sales;

select *
from products;

# sales-product table left join하여 새로 생성하기

SELECT sales_id, order_id, s.product_id, product_type, product_name, size, color, price_per_unit, s.quantity, total_price
FROM  sales as s
LEFT JOIN products as p ON s.product_id = p.product_ID;

CREATE TABLE sales_products (
  sales_id INT,
  order_id INT,
  product_id INT,
  product_type VARCHAR(50),
  product_name VARCHAR(50),
  size VARCHAR(50),
  color VARCHAR(50),
  price_per_unit INT,
  quantity INT,
  total_price INT
  
);

-- 두 테이블을 조인하여 결과를 새로운 테이블에 삽입
INSERT INTO sales_products
SELECT sales_id, order_id, s.product_id, product_type, product_name, size, color, price_per_unit, s.quantity, total_price
FROM  sales as s
LEFT JOIN products as p ON s.product_id = p.product_ID;


select *
from sales_products;

-- 새로운 컬럼 추가
ALTER TABLE sales_products
ADD COLUMN order_date date;

-- orders 테이블의 배송월 컬럼을 새로운 컬럼에 업데이트
UPDATE sales_products
JOIN orders ON sales_products.order_id = orders.order_id
SET sales_products.order_date = orders.order_date;

select order_month, count(order_month) from orders group by order_month order by order_month;

select c.customer_id, customer_name, gender, age, city, sum(o.payment) as `Total_payment($)`
from customers c
left join orders o on c.customer_id = o.customer_id 
group by c.customer_id
order by sum(o.payment) desc
limit 3;

select *
from orders
where customer_id = 664;

select *
from orders
where customer_id = 566;

select *
from orders
where customer_id = 282;

select *
from sales_products;

select product_id,product_type,product_name,size,color,price_per_unit,quantity,total_price, sp.order_date
from sales_products sp
left join orders o on sp.order_id = o.order_id
where customer_id = 282
order by product_type
;

select count(product_id) as `Total order quantity`
from sales_products sp
left join orders o on sp.order_id = o.order_id
where customer_id = 566
;

select product_id,sum(quantity) as `Total sales`
from sales_products
group by product_id
order by sum(quantity) desc
limit 3;

select *
from sales_products;

select *
from sales;

select product_id,product_type,product_name,size,color,price_per_unit
from sales_products
where product_id = 579
;

select product_id,sum(quantity)
from sales_products
where product_id = 579
group by product_id
;

select product_id,product_type,product_name,size,color,price_per_unit
from sales_products
where product_id = 78
;

select product_id,sum(quantity)
from sales_products
where product_id = 78
group by product_id
;

select product_id,product_type,product_name,size,color,price_per_unit
from sales_products
where product_id = 472
;

select product_id,sum(quantity)
from sales_products
where product_id = 472
group by product_id
;

select *
from orders;

select count(order_month) 
from orders 
group by order_month 
order by order_month;