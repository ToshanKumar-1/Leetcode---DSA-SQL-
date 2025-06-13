with cte1 as (
    select visited_on, sum(amount) as amt
    from customer
    group by visited_on
),cte2 as (
    select visited_on,
    sum(amt) over (
        order by visited_on
        rows between 6 preceding and current row
    ) as 'amount',
    cast((avg(amt*1.00) over (
        order by visited_on
        rows between 6 preceding and current row
    )) as decimal(10, 2)) as average_amount,
    row_number() over (
        order by visited_on 
    ) as rnk
    from cte1
)
select visited_on, amount, average_amount from cte2
where rnk >= 7