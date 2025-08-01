# Sea Level Predictor

This project analyzes the global average sea level change since 1880 using data from the US Environmental Protection Agency (EPA) and CSIRO. It uses historical sea level data to predict future sea level rise through the year 2050.

## Overview

The dataset (`epa-sea-level.csv`) contains the yearly global average absolute sea level changes from 1880 to 2014. This project:

- Loads and visualizes the data using Pandas and Matplotlib.
- Uses linear regression (via `scipy.stats.linregress`) to find the best-fit line representing the sea level trend.
- Predicts sea level rise in 2050 based on the entire dataset.
- Predicts sea level rise in 2050 based only on data from the year 2000 onward, reflecting recent trends.
- Plots both lines of best fit along with the original data points.

## Files

- `sea_level_predictor.py` — Contains the main logic for loading data, performing regression, and plotting.
- `epa-sea-level.csv` — Dataset of sea level changes (should be included or linked).
- `main.py` — Optional testing script to run and visualize the results.
- `test_module.py` — Contains unit tests for the project.

