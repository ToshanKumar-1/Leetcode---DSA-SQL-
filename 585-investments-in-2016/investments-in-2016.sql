with cte1 as (
    select * from insurance
    where tiv_2015 in (select tiv_2015 from insurance group by tiv_2015 having count(*) > 1)
), cte2 as(
    select pid, lat, lon from insurance group by lat, lon having count(*) = 1 
)select round(sum(cte1.tiv_2016), 2) as tiv_2016
from cte1
join 
cte2 
on cte1.pid = cte2.pid