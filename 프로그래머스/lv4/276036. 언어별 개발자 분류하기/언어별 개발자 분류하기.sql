SELECT GRADE, ID, EMAIL
FROM (
    SELECT 
        CASE 
            -- A: Front End 스킬(전체 합과 비교)과 Python 스킬을 모두 가진 경우
            WHEN (SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End')) > 0 
                 AND (SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python')) > 0 THEN 'A'
            -- B: C# 스킬을 가진 경우 (위의 A 조건에 해당하지 않는 사람 중)
            WHEN (SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#')) > 0 THEN 'B'
            -- C: 그 외의 Front End 개발자 (A, B 조건에 해당하지 않는 사람 중)
            WHEN (SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End')) > 0 THEN 'C'
        END AS GRADE,
        ID,
        EMAIL
    FROM DEVELOPERS
) AS RESULT
WHERE GRADE IS NOT NULL
ORDER BY GRADE ASC, ID ASC;