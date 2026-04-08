SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM (
    SELECT CATEGORY, PRICE, PRODUCT_NAME,
           -- 카테고리별로 가격이 높은 순서대로 등수를 매깁니다.
           RANK() OVER (PARTITION BY CATEGORY ORDER BY PRICE DESC) as rk
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
) t
WHERE rk = 1 -- 1등(최고가)인 데이터만 골라냅니다.
ORDER BY MAX_PRICE DESC;