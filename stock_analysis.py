import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

ticks = ['AAPL', 'MSFT', 'AMZN', 'TSLA', 'GOOG', 'NVDA']


stdev_dict = {}
stock_data_dict = {}
stock_return_dict = {}
stdev_dict = {}

for tick in ticks:
    stock_data_dict[tick] = yf.download(tick,
                                        start='2011-01-01',
                                        end='2025-10-04')['Close']
    stock_return_dict[tick] = stock_data_dict[tick].pct_change().round(
        4).dropna()


# after the execution of this for loop, the data is now stored in the dictionaries and we will not need to get data everytime we want to use it. we can simply call the specific element of the dictionary


def scatter_plot_function(the_return_dict_of_all_stocs_will_go_here):
    # this simply means that in for a specific tick, returns is the name given by us for the the items that are stored under that tick
    for tick, returns in the_return_dict_of_all_stocs_will_go_here.items():
        plt.scatter(returns.index, returns, s=0.3, color="blue")
        plt.title(f"Daily Returns of {tick}")
        plt.xlabel('Date')
        plt.ylabel('Returns')
        # plt.axhline(0, color='black', linewidth=0.3)
        # plt.axvline(0, color='black', linewidth=0.3)
        plt.grid(True, linestyle="--", alpha=0.3)
        plt.legend()
        plt.show()


def histogram_plot_function(the_return_dict_of_all_stocs_will_go_here):
    for tick, returns in the_return_dict_of_all_stocs_will_go_here.items():
        returns.plot(title=f"the histogram plot of returns of {tick}",
                     kind='hist',
                     bins=100,
                     color='red',
                     edgecolor='black')
        plt.xlabel('Returns')
        plt.ylabel('Frequency')
        plt.xlim(-0.3, 0.3)
        plt.legend()
        plt.show()


def standard_deviation_function(the_return_dict_of_all_stocs_will_go_here):
    for tick, returns in the_return_dict_of_all_stocs_will_go_here.items():
        stdev = np.std(returns)
        stdev_dict[tick] = float(stdev)
    print(stdev_dict)


def covariance_plot_function(the_return_dict_of_all_stocs_will_go_here):
    for tick1, returns1 in the_return_dict_of_all_stocs_will_go_here.items():
        for tick2, returns2 in the_return_dict_of_all_stocs_will_go_here.items():
            plt.scatter(returns1, returns2, s=0.3, color="green")
            plt.title(f"The covariance between {tick1} and {tick2}")
            plt.xlabel(f"Returns of {tick1} per trading day")
            plt.ylabel(f"Returns of {tick2} per trading day")
            plt.axhline(0, color='black', linewidth=0.2)
            plt.axvline(0, color='black', linewidth=0.2)
            plt.grid(True, linestyle="--", alpha=0.3)
            plt.figaspect(12)
            plt.legend()
            plt.show()


def linear_regg_model_for_covariance(covariance_plot_results):
    correlation_dict = {}
    for tick1, returns1 in covariance_plot_results.items():
        for tick2, returns2 in covariance_plot_results.items():
            if tick1 != tick2:
                slope, intercept, r, p, std_err = stats.linregress(
                    returns1, returns2)
                # Calculate the regression line
                regression_line = slope * returns1 + intercept
                plt.scatter(returns1, returns2, s=0.3, color="green")
                # Plot the regression line
                plt.plot(returns1, regression_line, color='red')
                plt.title(f"Linear Regression between {tick1} and {tick2}")
                plt.xlabel(f"Returns of {tick1}")
                plt.ylabel(f"Returns of {tick2}")
                plt.axhline(0, color='black', linewidth=0.2)
                plt.axvline(0, color='black', linewidth=0.2)
                plt.grid(True, linestyle="--", alpha=0.3)
                plt.legend()
                plt.show()
                correlation_dict[f"{tick1} and {tick2}"] = float(r)
    print(
        f"The Correlation Between the stocks are as following: {correlation_dict}")


# ================ CALLING FUNCTIONS ===================

scatter_plot_function(stock_return_dict)
histogram_plot_function(stock_return_dict)
standard_deviation_function(stock_return_dict)
covariance_plot = covariance_plot_function(stock_return_dict)
linear_regg_model_for_covariance(stock_return_dict)
