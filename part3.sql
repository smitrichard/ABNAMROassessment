-- extract multiple values from column “LanguageHaveWorkedWith“
SELECT Country, t2.value
FROM [Assessment].[dbo].[surveytable] t1
CROSS APPLY STRING_SPLIT(t1.[LanguageHaveWorkedWith], ';') t2;


-- find top 3 programming languages
SELECT TOP 3 LanguageHaveWorkedWith, COUNT(LanguageHaveWorkedWith) as LanguageHaveWorkedWithCount
FROM(
	SELECT Country, t2.value AS LanguageHaveWorkedWith
	FROM [Assessment].[dbo].[surveytable] t1
	CROSS APPLY STRING_SPLIT(t1.[LanguageHaveWorkedWith], ';') t2
	) src
Group by LanguageHaveWorkedWith
ORDER BY [LanguageHaveWorkedWithCount] DESC;

-- create a pivot to show count of these languages by country (let’s say they are: C++, Python and HTML/CSS)
SELECT Country,  [Javascript], [HTML/CSS], [Python]
FROM(
  	SELECT Country, t2.value AS LanguageHaveWorkedWith
	FROM [Assessment].[dbo].[surveytable] t1
	CROSS APPLY STRING_SPLIT(t1.[LanguageHaveWorkedWith], ';') t2
	) AS SourceTable 
PIVOT(
  	COUNT(LanguageHaveWorkedWith)  
  	FOR LanguageHaveWorkedWith IN ([Javascript], [HTML/CSS], [Python])  
	) AS PivotTable;
