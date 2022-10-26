#####################################################################################################################
# this programme compares gene expressions in two groups and outputs parameters to prove or not possible difference #
#####################################################################################################################

import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import ztest
import scipy.stats as st


def expression_differentiator(first_cell_type_expressions_path,
                              second_cell_type_expressions_path,
                              save_results_table):
    # read the files
    one = pd.read_csv(first_cell_type_expressions_path, index_col=0)
    two = pd.read_csv(second_cell_type_expressions_path, index_col=0)

    # create a storage for the outputs
    ci_test_results = []
    z_test_results, z_test_p_values = [], []
    mean_diff = []
    naming = []

    # check the compatibility
    if set(one.columns) != set(two.columns):
        print("""The two datasets have unequal sets of columns. 
    The analysis will be continued with the overlapping ones.""")

    # get only those genes that are in both datasets
    overlap = set(one.columns) & set(two.columns)

    for i in overlap:
        # are the confidence intervals of those intersecting?
        one_ci = st.t.interval(alpha=0.95, df=len(one[i]) - 1,
                               loc=np.mean(one[i]), scale=st.sem(one[i]))
        two_ci = st.t.interval(alpha=0.95, df=len(two[i]) - 1,
                               loc=np.mean(two[i]), scale=st.sem(two[i]))
        intersect = (one_ci[0] < two_ci[1]) & (two_ci[0] < one_ci[1])
        ci_test_results.append(intersect)
        naming.append(i)

        # could those expressions based on z-test be considered different?
        z_res = ztest(one[i], two[i])
        z_test_results.append(z_res[1] < 0.05)
        z_test_p_values.append(z_res[1])

        # what is the difference between two means?
        mean_different = np.mean(one[i]) - np.mean(two[i])
        mean_diff.append(mean_different)

    # transfer all results to the table and save it
    results = {'name': naming,
               "ci_test_results": ci_test_results,
               "z_test_results": z_test_results,
               "z_test_p_values": z_test_p_values,
               "mean_diff": mean_diff}

    results = pd.DataFrame(results)
    results.to_csv(f"{save_results_table}.csv", index=False)


print('Hi, welcome to the differential gene expression comparer!\n')

print("""WARNING! 
This works only with TWO datasets! 
Use it to compare gene expressions for TWO groups. 
It's better to contain similar sets of genes...\n""")

path_one = input('Please, indicate the path to ur first dataset, including the file name: ')
path_two = input('Please, indicate the path to ur second dataset, including the file name: ')
output_name = input('Please, indicate the desirable name for the output without .csv: ')

print('''\n! BE AWARE ! 
There is an additional first column with gene names,
because the scrip is using union of sets, so the order is messed up...''')

expression_differentiator(path_one, path_two, output_name)

print('\nThe programme has run, pls check the output. Bye bye')
