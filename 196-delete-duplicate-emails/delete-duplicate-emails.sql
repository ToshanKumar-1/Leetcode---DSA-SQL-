with luffy as (
    select id, email, 
    row_number() over (partition by email order by id) as rnk
    from person
)delete from person where id in (
    select id from luffy
    where rnk > 1
)