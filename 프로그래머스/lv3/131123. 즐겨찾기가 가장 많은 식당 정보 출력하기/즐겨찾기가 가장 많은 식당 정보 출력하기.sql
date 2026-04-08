-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM (SELECT FOOD_TYPE, REST_ID,REST_NAME ,FAVORITES, RANK() over(partition BY FOOD_TYPE order by FAVORITES desc) as RNK
     from REST_INFO 
     ) as a
where RNK = 1
order by FOOD_TYPE desc;