(select u.name as results
from 
movies m
join
movierating mr on m.movie_id = mr.movie_id
join
users u on mr.user_id = u.user_id
group by u.name
order by count(mr.rating) desc, u.name asc
limit 1)
union all
(select m.title
from 
movies m
join
movierating mr on m.movie_id = mr.movie_id
join
users u on mr.user_id = u.user_id
where mr.created_at >='2020-02-01' and mr.created_at <= '2020-02-29'
group by mr.movie_id
order by avg(mr.rating) desc, m.title asc
limit 1)