-- 코드를 입력하세요
SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID IN (SELECT ANIMAL_ID
                   FROM ANIMAL_INS
                   WHERE SEX_UPON_INTAKE IN ('Intact Male', 'Intact Female'))
        and SEX_UPON_OUTCOME IN ('Neutered Male', 'Spayed Female')
order by ANIMAL_ID asc;