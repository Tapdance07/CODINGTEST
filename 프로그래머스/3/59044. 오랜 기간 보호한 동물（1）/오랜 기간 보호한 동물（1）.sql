-- 코드를 입력하세요
SELECT NAME , DATETIME
FROM ANIMAL_INS 
WHERE ANIMAL_ID NOT IN (select ANIMAL_ID
                       FROM ANIMAL_OUTS)
order by DATETIME asc
limit 3;