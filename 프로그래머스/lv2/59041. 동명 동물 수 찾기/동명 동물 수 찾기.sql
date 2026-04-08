-- 코드를 입력하세요
SELECT NAME, count(NAME) COUNT
from ANIMAL_INS
GROUp By NAME
having COUNT >= 2
order by NAME asc;