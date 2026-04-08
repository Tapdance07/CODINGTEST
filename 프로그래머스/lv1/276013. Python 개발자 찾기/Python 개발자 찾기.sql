SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
where SKILL_1 in ('Python') or SKILL_2 in ('Python') or SKILL_3 in ('Python')
order by ID asc;