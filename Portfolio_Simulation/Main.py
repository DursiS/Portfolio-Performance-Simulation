""" Outside Modules """
import matplotlib.pyplot as plt

""" Local Modules """
import Dataset
import Presets
import Timestamps


""" Initialises Portfolio Choice """
choice = Presets.get_choice()
portfolio = Presets.preset(choice)



""" Initialises Pricing Data """
total = Dataset.portfolio_total(portfolio)
stock_to_total = Dataset.stock_to_total(portfolio)



""" General Chart/Graph Settings """
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.patch.set_facecolor('#1e1e1e') #Background
axs[1].set_facecolor('#2c2c2c') # Plot Area
axs[1].spines['bottom'].set_color('white')
axs[1].spines['left'].set_color('white')
axs[1].tick_params(axis='x', colors='white')
axs[1].tick_params(axis='y', colors='white')



""" Portfolio Pie Chart Settings """
pricing_labels = Dataset.price_label(stock_to_total)
axs[0].pie(
stock_to_total.values(), 
labels=pricing_labels, 
autopct='%1.1f%%',
textprops={'color': 'white'}
)
axs[0].set_title(f"Portfolio Preset #{choice}", c='white')



""" Performance Graph Settings """
times = Timestamps.times()
values = Timestamps.portfolio_values(portfolio, times)
b_lim = int(min(values)) * 0.95
axs[1].plot(times, values, linewidth=0.6, c="green")
axs[1].set_ylim(bottom=b_lim)
axs[1].set_title("Performance over the year.", c='white')



""" Plots it """
plt.tight_layout()
plt.show()




