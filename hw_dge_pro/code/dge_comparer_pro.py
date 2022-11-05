######################################################################################################################
# this programme computes dge of two groups, corrects for multiple tests, outputs parameters to not/prove difference #
######################################################################################################################

import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import ztest
from scipy.stats import ttest_ind, ttest_rel, mannwhitneyu
from statsmodels.stats.multitest import multipletests
import warnings


def expression_differentiator_pro(first_cell_type_expressions_path,
                                  second_cell_type_expressions_path,
                                  save_results_table,
                                  method='ztest', correct=None, alpha=0.05):
    # read the files
    one = pd.read_csv(first_cell_type_expressions_path, index_col=0)
    two = pd.read_csv(second_cell_type_expressions_path, index_col=0)

    # create a storage for the outputs
    test_results, test_p_values, dge_not_equal = [], [], []
    mean_diff = []
    naming = []
    test_calling = {'ztest': ztest, 'ttest_ind': ttest_ind,
                    'ttest_rel': ttest_rel, 'mannwhitneyu': mannwhitneyu}

    # check the compatibility
    if set(one.columns) != set(two.columns):
        warnings.warn("""The two datasets have unequal sets of columns. 
        The analysis will be continued with the overlapping ones.""")

    # get only those genes that are in both datasets
    overlap = set(one.columns) & set(two.columns)

    for i in overlap:
        # name of the gene for bookkeeping
        naming.append(i)

        # could those expressions based on a test be considered different?
        res = test_calling[method](one[i], two[i])
        test_results.append(res[0])
        dge_not_equal.append(res[1] < alpha)
        test_p_values.append(res[1])

        # what is the difference between two means?
        mean_different = np.mean(one[i]) - np.mean(two[i])
        mean_diff.append(mean_different)

    # transfer results to the table
    results = {'name': naming,
               "mean_diff": mean_diff,
               method + "_results": test_results,
               "test_p_values": test_p_values}

    # we can do better: correct the result for multiple tests
    if correct:
        adjusted_p = multipletests(test_p_values, alpha=alpha, method=correct)
        results["adjusted_p_value"] = adjusted_p[1]
        results["reject_H0"] = adjusted_p[0]
    # or rest with all good test results
    if not correct:
        results["reject_H0"] = dge_not_equal

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

print('''\nBE AWARE: there is an additional first column with gene names,
because the scrip is using a union of sets, so the order is messed up...''')

print('''\nWhat test would you like? Please, select one from the brackets below:
z-test (ztest), t-test for independent variables (ttest_ind), t-test for dependent 
(ttest_rel), Mann-Whitney U test (mannwhitneyu), ... for more create ur own script.''')
method = input('If this step is skipped, the z-test is performed automatically: ')

print('''\nYou can also choose one of methods to correct for multiple comparisons as listed below:
bonferroni, sidak, holm-sidak, holm, simes-hochberg, hommel, fdr_bh, fdr_by, fdr_tsbh, fdr_tsbky.
    *For more information or the meaning of these abbreviations, please, read the info for 
statsmodels.stats.multitest.multipletests v0.12.2 that is used here.''')
correct = input('If you want nothing but rest in peace, skip this step by pressing Enter: ')

alpha = input('\nAdditionally, you can adjust threshold for those tests, default is 0.05: ')

if method:
    pass
else:
    method = 'ztest'

if correct:
    pass
else:
    correct = None

if alpha:
    pass
else:
    alpha = 0.05

expression_differentiator_pro(path_one, path_two, output_name,
                              method=method, correct=correct, alpha=alpha)

print('\nThe programme has run, pls check the output. Bye bye')
