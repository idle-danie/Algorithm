SELECT P.PRODUCT_CODE, (P.PRICE * SUM(S.SALES_AMOUNT)) AS SALES
FROM PRODUCT P JOIN OFFLINE_SALE S
ON P.PRODUCT_ID = S.PRODUCT_ID
GROUP BY P.PRODUCT_ID
ORDER BY SALES DESC, P.PRODUCT_CODE
