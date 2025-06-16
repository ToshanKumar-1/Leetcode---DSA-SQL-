select c.category, count(a.account_id) as accounts_count
from(
    select "High Salary" as category
    union all
    select "Average Salary"
    union all
    select "Low Salary"
)as c
left join
accounts a
on (
(c.category = 'High Salary' and a.income > 50000) or
(c.category = "Average Salary" and a.income <= 50000 and a.income >= 20000) or
(c.category = "Low Salary" and a.income < 20000)
)
group by category
