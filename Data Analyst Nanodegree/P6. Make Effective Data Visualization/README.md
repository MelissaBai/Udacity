#Prosper Loan Dataset
##Summary:
In this visualization, I illustrated the relationship between monthly disposable income and acceessibility of getting loans as well as bad loan ratio. Based on my two charts, higher monthly disposable income is easier to get loans, and also has a lower bad loan ratio.

##Design:
<p> I first calculated MonthlyDisposableIncome = StatedMonthlyIncome - MonthlyLoanPayment, and divided it into several groups: Less than 100, 100-1000, 1000-2000, 2000-3000, and more than 3000. Meanwhile, I also aggregated loan status to two categories: bad and good. Bad loans including status in defaulted, chargedoff, cancelled and all past dues, rest are good loans.
First chart is a bar chart of bad loan and good loan count for different monthly disposable income groups. From the chart we know that higher monthly disposable income is easier to get loans, as the bar height is taller as the disposable income increases.
Second chart is a bar chart of bad loan rate for different monthly disposable income group. We get to know that lower monthly disposable income groups (<=2000) have higher bad loan rate that’s around 10%, higher monthly disposable income groups have lower bad loan rate, which is around 5%.</p>
##Feedback:
###Feedback1:
Legend is not at the right place, y axis values are not readable, plot is too small.
###Feedback2:
Monthly disposable income groups are not ordered, they need to be either ascending or descending.
###Feedback3:
Your bad loan ratio is breakdown by category, not time series. Using line chart makes it look like x-axis is continuous or time serial, using a bar plot is better.

I have incorporate all these feedback in my index_2.html visualization.


##Resources:
*http://dimplejs.org/examples_viewer.html?id=bars_vertical_grouped
*Udacity Video
