SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM (SELECT * FROM APPOINTMENT WHERE MONTH(APNT_YMD) = 5) AS APPOINTMENT_MAY
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD