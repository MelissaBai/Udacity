Prosper Loan Dataset

Summary:
In this visualization, I illustrated the relationships between different monthly disposable income groups and bad loans, which include loan status in ‘defaulted’, ‘chargedoff’ and ‘all past dues’. In addition, the bad loan rate is calculated for each group.

Design:
Aggregated variables are taken from the prosper loan data sets. I first calculated MonthlyDisposableIncome = StatedMonthlyIncome - MonthlyLoanPayment, and aggregated the new variable into several groups: Less than 100, 100-1000, 1000-2000, 2000-3000, and more than 3000. Meanwhile, I also re-categorized loan status to three categories: bad, good and cancelled. Bad loans including status in defaulted, chargedoff and all past dues; cancelled is cancelled, and the rest are good loans. Meanwhile, I also calculated the bad loan ratios in each monthly disposable income group.

Feedback:
For my first visualization, there were some plot suggestions I received including y axis values not readable, plot too small, legend not at the right place. I incorporated these suggestions in my second version. I have also received suggestions to add a second plot about the bad loan ratio, and have the x-axis categories ordered: from less than 100 to more than 3000.
Meanwhile, I have also received suggestions about doing a statistic analysis to see if there is statistic significance between different groups in terms of bad loan ratio. However, I was not able to determine which analysis is best for the data.


Resources:
http://dimplejs.org/examples_viewer.html?id=bars_vertical_grouped
Udacity Video
