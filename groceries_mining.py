import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules

def associationRuleMining(support,confidence,tableName='groceries_cleaned.csv'):
    # importing the cleaned dataset
    dataset = pd.read_csv(tableName)
    
    # Taking user input for minimum support and minimum confidence
    # support=float(input("Enter the minimum support(0-1): "))
    # confidence =float(input("Enter the minimum confidence(0-1):"))
    
    # Applying apriori algorithm
    frequent_itemset = apriori(dataset, min_support=support, use_colnames=True)
    
    # Generating association rules on frequent_itemset
    rules = association_rules(frequent_itemset, metric="confidence", min_threshold=confidence)
    
    # formatting the output
    formatted_rules = []
    for _,rule in rules.iterrows():
        antecedents = list(rule['antecedents'])
        consequents = list(rule['consequents'])
        confidence = "{:.2f}".format(rule['confidence'])
        lift = "{:.2f}".format(rule['lift'])
    
        formated_rule= f"{",".join(antecedents)} -> {",".join(consequents)} lift: {lift} confidence: {lift}"
        formatted_rules.append(formated_rule)
    
    # writing the output to a file groceries_rules.txt
    tableName=tableName.split(".")[0]
    outputTableName=tableName+'_rules.txt'
    with open(outputTableName, 'w') as f:
        f.write('\n'.join(formatted_rules))
    print("association done")
    return outputTableName
