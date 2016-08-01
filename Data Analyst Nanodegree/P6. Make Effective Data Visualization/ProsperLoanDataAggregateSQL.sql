
DEFINE INLINE TABLE range_status
SELECT
	CASE
  	WHEN MonthlyDisposable <= 100 THEN "Less than 100"
    WHEN MonthlyDisposable BETWEEN 100 AND 1000 THEN "100-1000"
    WHEN MonthlyDisposable BETWEEN 1001 AND 2000 THEN "1000-2000"
    WHEN MonthlyDisposable BETWEEN 2001 AND 3000 THEN "2000-3000"
    WHEN MonthlyDisposable >3000 THEN "More than 3000"
    ELSE 'None'
  END AS MonthlyDisposableRange,
  CASE
  	WHEN LoanStatus LIKE 'Past Due%' THEN 'Bad'
    WHEN LoanStatus LIKE 'ChargedOff' THEN 'Bad'
    WHEN LoanStatus LIKE 'Defaulted' THEN 'Bad'
    WHEN LoanStatus LIKE 'Cancelled' THEN 'Bad'
    ELSE 'Good'
  	END AS LoanStatusGroup
FROM (
SELECT
	LoanKey,
	(StatedMonthlyIncome - MonthlyLoanPayment) AS MonthlyDisposable,
  LoanStatus,
  ListingCategory_numeric
FROM ProsperLoanData );

//DEFINE INLINE TABLE group_counts
SELECT
	MonthlyDisposableRange,
  LoanStatusGroup,
  COUNT(*) AS counts
FROM range_status
GROUP BY 1,2
ORDER BY MonthlyDisposableRange


//100-1000, 0.086
//1000-2000, 0.1005
//2000-3000, 0.085
//>3000, 0.05
