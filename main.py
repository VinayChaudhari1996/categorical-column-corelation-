from scipy import stats
import numpy as np

def calculate_categorial_covariance(dataframe,columns, target):
    
    collect_all_metrics = []

    for column in columns:
        print(f"{column} vs {target}")

        sample_df = pd.crosstab(index = dataframe[column], columns = dataframe[target])

        
        all_pattern = ""
        counter = 0
        rows = sample_df.shape[0]

        for row in range(rows):
                        
            pattern = f"sample_df.iloc[{row}].values"
            
            all_pattern += pattern + ","
                    
                
        (chi2, p, dof, _) = stats.chi2_contingency([eval(all_pattern)])
        
        CrammerV = np.sqrt(chi2/(dataframe.shape[0])) 
        
        
        pattern = {"Column" : column,
                   "Target" : target,
                   "Chi2":chi2,
                   "CrammerV":CrammerV,
                   "P-Value":p,
                   "P-Value<0.05":p <0.05,
                   "DegreeOfFreedom" :dof}
        
        
        collect_all_metrics.append(pattern)
    
    final_data = pd.DataFrame(collect_all_metrics)
        
    return final_data.sort_values("CrammerV",ascending=False)
