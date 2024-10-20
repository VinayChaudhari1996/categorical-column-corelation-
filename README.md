# Categorical Correlation Analysis Tool

## Overview
This Python tool calculates the correlation between categorical variables in a dataset using Chi-Square test of independence and Cramér's V statistic. It's particularly useful for data scientists and analysts who need to understand the relationships between categorical variables in their datasets.

## Purpose
The main purposes of this tool are:
- Analyze relationships between categorical variables
- Calculate statistical significance of relationships
- Measure the strength of associations using Cramér's V
- Automate the process for multiple columns against a target variable

## Technical Details

### Dependencies
- Python 3.x
- NumPy
- SciPy
- Pandas

### Key Components
1. **Chi-Square Test**: 
   - Tests the independence between categorical variables
   - Provides p-values to determine statistical significance
   - Calculates degrees of freedom

2. **Cramér's V Statistic**:
   - Measures the strength of association between categorical variables
   - Normalized measure (0 to 1)
   - 0 indicates no association
   - 1 indicates perfect association

### Function Parameters
- `dataframe`: Pandas DataFrame containing the data
- `columns`: List of column names to analyze
- `target`: Target variable name to compare against

### Return Value
Returns a sorted pandas DataFrame containing:
- Column name
- Target variable
- Chi-square statistic
- Cramér's V value
- P-value
- Boolean indicator for p-value < 0.05
- Degrees of freedom

## Usage

```python
from scipy import stats
import numpy as np
import pandas as pd

# Example usage
df = your_dataframe
columns_to_analyze = ['category1', 'category2', 'category3']
target_variable = 'target'

results = calculate_categorial_covariance(
    dataframe=df,
    columns=columns_to_analyze,
    target=target_variable
)

# View results
print(results)
```

## Example Output
```
   Column    Target        Chi2    CrammerV    P-Value    P-Value<0.05    DegreeOfFreedom
0  category1  target    156.789     0.789     0.00001        True              4
1  category2  target     89.456     0.567     0.00340        True              3
2  category3  target     23.123     0.234     0.08900        False             2
```

## Notes
- Ensures all input variables are categorical
- Automatically handles the computation of contingency tables
- Sorts results by Cramér's V for easy interpretation
- Prints progress during analysis with column names

## Limitations
- Only works with categorical variables
- Requires sufficient data in each category for reliable results
- Chi-square test assumptions should be validated (expected frequencies > 5)

## Contributing
Feel free to submit issues and enhancement requests!
