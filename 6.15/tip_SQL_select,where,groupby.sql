use tip;
select total_bill from tip.tips where tip >=7;

SELECT total_bill, tip, smoker, time
FROM tips
LIMIT 5;

SELECT *, tip/total_bill as tip_rate
FROM tips
LIMIT 5;

SELECT *
FROM tips
WHERE time = 'Dinner'
LIMIT 5;

SELECT *
FROM tips
WHERE time = 'Dinner' AND tip > 5.00;

SELECT *
FROM tips
WHERE size >= 5 OR total_bill > 45;

SELECT sex, count(*)
FROM tips
GROUP BY sex;

SELECT day, AVG(tip), COUNT(*)
FROM tips
GROUP BY day;

SELECT day, AVG(tip), COUNT(*)
FROM tips
GROUP BY day
order BY day desc;

SELECT day, AVG(tip), COUNT(*)
FROM tips
GROUP BY day
order BY day asc;

SELECT smoker, day, COUNT(*), AVG(tip)
FROM tips
GROUP BY smoker, day;

SELECT smoker,total_bill,AVG(tip),count(*)
FROM tips
GROUP BY smoker, day order by smoker;


