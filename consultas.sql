SELECT T0."Name" FROM "@O_GROUPING_BRANDS"  T0 WHERE T0."Code" = $["@BUD1"."U_Code_GroupingBrands"]


SELECT T0."CardName"
FROM OCRD T0  WHERE  T0."CardCode"= $["@ROOT_LT1"."U_CardCode"]

SELECT T0."ItmsGrpNam"
FROM OITB T0 WHERE T0."ItmsGrpCod"=$["@ROOT_OLT"."Code"]

## CONSULTA TIEMPOS LOGISTICOS  "TiemposLogisticos"
SELECT T1."Name" AS "Marca", T0."U_CardCode" AS "NIT", T0."U_CardName" AS "Proveedor",  T0."U_Origin",
CASE
WHEN  T0."U_Modality"='01'
THEN 'Courrier'
WHEN  T0."U_Modality"='02'
THEN 'Ordinario'
ELSE 'Virtual' 
END AS  "U_Modality",
CASE 
WHEN T0."U_Via" ='01'
THEN 'AEREO'
WHEN T0."U_Via" ='02'
THEN 'MARITIMO'
WHEN T0."U_Via" ='03'
THEN 'N/A'
END AS"U_Via", T0."U_FactoryDelivery", T0."U_LogisticsOperation"
FROM "SBOLINCE"."@ROOT_LT1"  T0
INNER JOIN "SBOLINCE"."@ROOT_OLT"  T1 ON T0."Code"= T1."Code" ORDER BY  T1."Name" ASC, T0."U_CardCode" ASC