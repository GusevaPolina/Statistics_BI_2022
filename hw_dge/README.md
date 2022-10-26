# Differencial gene expression

The purpose of this homework is to design a tool to compare gene expression in two different groups of something (for example, between B- and NK-cells).

The output for the programme shows:
  - the name of a gene;
  - ```bool```: if there is a difference between confidence intervals;
  - ```bool```: if expressions are different based on the z-test;
  - and its p-value;
  - the delta between expression means (```mean(1st) - mean(2nd)```).

The input is expected to have genes as columns, where each observation has a new row. While output will have column names as stated above.

:exclamation:**Be aware:**:exclamation: due to the script features, the order of genes will be not the same as for input files.

Please, find 1) the test data in :point_right: the _data_data_ folder; 2) the test analysis with the programme in :point_right: the _code_ folder.
