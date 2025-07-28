Simulates the performace of a given portfolio over the last year in real time.

**What does this simulation do?**
1. Gives the option of 3 different portfolios of 5 stocks each with varying amounts of shares.
2. Plots a visual pie chart representing your preset portfolio and its current valuation.
3. Plots a visual graph of the portfolio valuation thoughout the last.

**How does it do it?**
It plots the pie chart and performance metrics using 2 useful python modules: 
1. Matplotlib, a comprehensive library for creating static, animated, and interactive visualizations. In my case to visualise the pie chart and graph.
2. Pandas, a software library for data manipulation and analysis. In my case to organize timestamps.

**General Rundown.***
The program starts by asking the user for its portfolio choice, then fetches the portfolio data for that choice. It evaluates the current valuation and stock pricing data for the pie chart. Then initialises subsplots for the pie chart and graph to exist and sets general appearences. It then sets up the pie chart to be drawn. Nextly, initialises the timestamps and list of all 365 portfolio valuations using both python modules discussed earlier, and sets up the performance graph to be drawn. Plots and tightens both of them at the end to get the visual representation you see.

