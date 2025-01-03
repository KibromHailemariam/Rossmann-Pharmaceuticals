# Notebooks

This folder contains Jupyter notebooks for the project.

# Customer Purchasing Behavior Analysis Notebook

## Overview
This Jupyter notebook contains the exploratory data analysis (EDA) for the customer purchasing behavior project. The analysis aims to uncover insights regarding how promotions, store openings, and other factors influence customer purchasing behavior.

## Contents
- **Data Loading**: Loading datasets from CSV files.
- **Data Cleaning**: Handling missing values and outliers.
- **Data Visualization**: Various plots to analyze sales, promotions, and customer behavior.

## Logging
This notebook uses logging to track the steps taken during the analysis. The log file `analysis.log` contains information about data loading, processing, and any errors encountered.

## Analysis Questions
The following questions guide the analysis:
1. Are promotions distributed similarly between training and test sets?
2. How does sales behavior change before, during, and after holidays?
3. What seasonal purchasing behaviors can be identified?
4. What is the correlation between sales and the number of customers?
5. How do promotions affect sales and customer attraction?
6. Which stores should promotions be deployed in?
7. What trends are observed during store opening and closing times?
8. How does assortment type affect sales?
9. What is the impact of distance to competitors on sales?
10. How do new competitors affect existing stores?

## Requirements
Ensure you have the following libraries installed:
- pandas
- seaborn
- matplotlib

You can install them using:

```bash
pip install -r ../requirements.txt
```

## Usage
Open this notebook in Jupyter to explore the analysis interactively. Run each cell to see the results of the analysis and visualizations.

## License
This notebook is part of the Week 4 Project and is licensed under the MIT License.
