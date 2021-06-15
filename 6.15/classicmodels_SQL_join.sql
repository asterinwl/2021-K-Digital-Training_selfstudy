use classicmodels;
show tables;
select * from employees;
select	firstName from employees; #오류생길 시 위, 아래 공식도 확인하자.
select firstname, lastname from employees;
select firstname, lastname from employees where employees.employeeNumber>=1300;
select * from offices;
select city from offices where offices.officecode='1';
select city,phone from offices where offices.officecode='1';
select orders.orderNumber ,customers.country from orders 
left join customers on customers.customerNumber=orders.customerNumber;
select customers.customerNumber from customers left join
payments on customers.customerNumber=payments.customerNumber;
select orders.orderNumber,customers.country from orders inner join
customers on orders.customerNumber=customers.customerNumber where
customers.country='USA';
select customers.customerName, payments.checkNumber from customers
left join payments on customers.customerNumber=payments.customerNumber
where payments.paymentDate >= '2003-06-06';