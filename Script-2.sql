--part 1
select title , genre  from books 
where genre='Fantasy'

select first_name, last_name ,city   from customers 
where city ='Tehran'


select title, genre  from books 
where genre in ('Romance','Novel')

select title, genre  from books 
where genre not in ('Romance','Novel')

select title , price, stock, genre   from books 
where price between 10 and 15
and stock >0
and genre ='Romance'

select first_name ,email  from customers 
where email ilike '%.org'
and first_name ilike 's%'

select first_name , city from customers 
where city is null 
-- = نمیتواند nullرا چک کند

select title from books
where title ilike '%love%'

select title from books
where LOWER(title) like '%love%'

select title from books
where title ~* 'love'


--part 2

select first_name ||' '||last_name as full_name from customers  

--select contcat(first_name ,' ',last_name) as full_name from customers 

select MAX(price)as most_expensive, MIN(price)as cheapest from books 

select SUM(quantity)as total, round(AVG(quantity),2)as average from order_items 

select title ,price, pages, price::numeric/pages as price_per_page from books
order by price_per_page desc limit 3
-- تقسیم دو intبرابر با قسمت صحیح است. برای اینکه خارج قسمت کامل باشد باید یکی از اعداد نامریک شود

select title, price from books 
where price > (select AVG(price) from books )

select title, pages  from books 
where pages =(select MAX(pages) from books )

select concat(first_name , ' ',last_name ) from customers 
where customer_id not in(select o.customer_id  from orders o  )

select concat(first_name , ' ',last_name ) from customers 
where customer_id not exists (select 1  from orders o where c.customer_id =o.customer_id )

-- اگر جواب زیر کوپری null باشد not in جوابی بر نمیگرداند


--part 3
select genre,count(title)as total_books from books 
group by genre 
order by total_books  desc 

select author_id ,count(title)as total_book from books 
group  by author_id 


select status, count(order_id )as total_order from orders 
group by status 

select AVG(price)as average from books 
group by genre 
having AVG(price)>13 
order by average asc

select order_id,SUM(quantity *unit_price )as total from order_items 
group by order_id 
having SUM(quantity *unit_price ) >30

-- بعد از گروپ شرط را با havingمیگذاریم







