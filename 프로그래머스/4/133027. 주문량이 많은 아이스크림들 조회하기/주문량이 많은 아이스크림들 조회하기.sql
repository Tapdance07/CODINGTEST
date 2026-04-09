with ice as(
    select *
    FROM FIRST_HALF 
    UNION ALL
    select * 
    FROM JULY
)
select FLAVOR
from ice
group by FLAVOR
order by sum(TOTAL_ORDER) desc
limit 3