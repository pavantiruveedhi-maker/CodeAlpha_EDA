# Exploratory Data Analysis: Unemployment in India

## Overview

This project performs Exploratory Data Analysis on unemployment data from India. The analysis examines unemployment rates across states, dates, and rural or urban areas. Python libraries including Pandas, NumPy, Matplotlib, and Seaborn were used for data cleaning, statistical analysis, visualization, trend identification, and correlation analysis. The project also identifies missing values, duplicate records, outliers, regional differences, and changes in unemployment over time.

## Dataset

- **Source:** `data/Unemployment-in-India.csv`
- **Period:** May 2019 – June 2020
- **Observations:** 740 monthly records
- **States/UTs:** 28
- **Areas:** Rural and Urban
- **Variables:**
  - `Region` – State or Union Territory
  - `Date` – Monthly observation date
  - `Frequency` – Data frequency (Monthly)
  - `Estimated Unemployment Rate (%)`
  - `Estimated Employed`
  - `Estimated Labour Participation Rate (%)`
  - `Area` – Rural or Urban

## Research Questions

1. Which states have the highest average unemployment rate?
2. Is unemployment higher in rural or urban areas?
3. How did unemployment change from 2019 to 2020?
4. Which states experienced the largest unemployment increases?
5. Is there a relationship between unemployment rate and labour participation rate?
6. Which month had the highest average unemployment rate?
7. Does the number of employed people decrease when unemployment rate increases?

## Methods

- **Data cleaning:** removed blank rows, converted dates and numeric columns, handled missing values, removed duplicates.
- **Descriptive statistics:** mean, median, min, max for key variables.
- **Group analysis:** by state, by area (rural/urban), by month.
- **Visualization:** bar plots, line plots, boxplots, correlation heatmap.
- **Correlation analysis:** between unemployment rate, employed count, and labour participation rate.
- **Outlier detection:** boxplots and sorting by extreme values.

## Key Findings

- Urban areas show higher average unemployment (**13.17%**) than rural areas (**10.32%**).
- Top 5 states by average unemployment:
  - Tripura (**28.35%**)
  - Haryana (**26.28%**)
  - Jharkhand (**20.59%**)
  - Bihar (**18.92%**)
  - Himachal Pradesh (**18.54%**)
- National unemployment spiked in **April–May 2020** (**23.64%** and **24.88%**) compared to ~9–10% in 2019.
- Highest individual rates observed in **Puducherry** (up to **76.74%** in April 2020).
- Weak negative correlation between unemployment rate and number of employed people (**−0.22**).
- Almost no linear relationship between unemployment rate and labour participation rate (**0.003**).

## Files

- `EDA_Unemployment_India.ipynb` – Jupyter notebook with full analysis
- `data/Unemployment-in-India.csv` – raw dataset
- `outputs/` – generated charts and insights
  - `unemployment_by_state.png`
  - `rural_vs_urban.png`
  - `monthly_trend.png`
  - `state_area_breakdown.png`
  - `correlation_heatmap.png`
  - `boxplot_by_area.png`
  - `insights.md`

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

1. Place `Unemployment-in-India.csv` in the `data/` folder.
2. Open `EDA_Unemployment_India.ipynb` in Jupyter Notebook or VS Code.
3. Run all cells to regenerate analysis and charts.

## Author

TIRUVEEDHI VENKATA PAVAN KUMAR 
CodeAlpha Data Analytics Internship – Task 2: Exploratory Data Analysis