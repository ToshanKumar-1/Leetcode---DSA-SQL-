with nami as (
    select *,
    Dense_rank() over (order by salary desc) as rnk
    from employee
)select 
case 
when count(*) = 0 then null
else max(salary)
end as SecondHighestSalary 
from nami
where rnk = 2