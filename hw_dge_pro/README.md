# Differencial gene expression Pro

The purpose of this homework is to design a **more advanced** tool to compare gene expression in two different groups of something (for example, between B- and NK-cells). Among other cons, the previous version obtains less customisation. Moreover, testing many hypotheses can be a little dangerous.

The output for the programme shows:
  - the name of a gene;
  - the delta between expression means (```mean(1st) - mean(2nd)```);
  - test results (z-test, t-test for independent or dependent variables, Mann–Whitney U test);
  - its p-value;
  - _optional_: corrected p-value for multiple tests (for options run the code);
  - ```bool```: if expressions are different and $H_0$ should be rejected.

</br>

> The input is expected to have genes as columns, where each observation has a new row. While output will have column names as stated above.
> :exclamation:**Be aware:**:exclamation: due to the script features, the order of genes will be not the same as for input files.

</br>

The default settings are:
  - for test is ```z-test```;
  - for correction method is ```None```;
  - for threshold is ```0.05```.
