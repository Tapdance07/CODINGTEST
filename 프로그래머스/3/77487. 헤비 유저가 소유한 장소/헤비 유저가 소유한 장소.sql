with havy_user as (
select HOST_ID
FROM PLACES
GROUP By HOST_ID
having count(ID) >=2 )

select ID,	NAME,	HOST_ID
FROM PLACES 
where HOST_ID in(select HOST_ID FROM havy_user)
order by ID