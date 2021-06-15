USE classicmodels;
SELECT customerNumber FROM classicmodels.customers;
SELECT count(productCode) FROM classicmodels.products;
select productname,productline from classicmodels.products;
SELECT sum(amount), count(checkNumber)actorcustomers FROM classicmodels.payments;
SELECT * FROM classicmodels.customers;
SELECT count(*) FROM classicmodels.customers;
SELECT count(*) FROM classicmodels.customers where country='USA';
SELECT * FROM classicmodels.orders;
SELECT * FROM classicmodels.orderdetails;
SELECT distinct orderNumber from classicmodels.orderdetails;
select * from classicmodels.orders where orderDate between '2003-01-06' and '2003-01-18';

select * from classicmodels.orders; #crtl+Enter을 쓰면 하나씩 나온다.
select productCode from products;

select customerNumber from classicmodels.customers where country in ('USA','Canada');
select customerNumber from classicmodels.customers where country not in ('USA','UK');
select count(customerNumber) from classicmodels.customers where country is null;

select employeeNumber from employees where reportsTo is null;