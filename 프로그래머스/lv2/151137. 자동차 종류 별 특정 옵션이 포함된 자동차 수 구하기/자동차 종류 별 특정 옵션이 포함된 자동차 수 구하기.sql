SELECT CAR_TYPE, count(CAR_ID) CARS
FROM 
(SELECT CAR_ID, CAR_TYPE
     from CAR_RENTAL_COMPANY_CAR
     where OPTIONS REGEXP '통풍시트|열선시트|가죽시트') as q
group by CAR_TYPE
order by CAR_TYPE asc;