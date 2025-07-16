with cte as (
    select t.request_at, count(t.id) as total_req
    from 
    users u1
    join trips t on t.client_id = u1.users_id
    join users u2 on t.driver_id = u2.users_id
    where u1.banned = 'No' and u2.banned = 'No' and t.request_at between "2013-10-01" and "2013-10-03"
    group by t.request_at
), cte1 as (
    select t.request_at, count(t.id) as banned_req
    from 
    users u1
    join trips t on t.client_id = u1.users_id
    join users u2 on t.driver_id = u2.users_id
    where u1.banned = 'No' and u2.banned = 'No' and t.status <> 'completed' and t.request_at between "2013-10-01" and "2013-10-03"
    group by t.request_at
)select cte.request_at as Day, round((coalesce(cte1.banned_req, 0) * 1.0 / cte.total_req), 2) as 'Cancellation Rate'
from
cte 
left join cte1 on cte.request_at = cte1.request_at