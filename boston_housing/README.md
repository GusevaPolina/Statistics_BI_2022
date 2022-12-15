# Boston suburbs housing in 1970s-80s. Linear modelling

In this project, data about several features of houses are used to build a linear model describing a house price.

> Please, be aware that this dataset is retracted from many places because of racism claims :shipit:

The dataset contains such describing parameters of the area as:
 - geography (`zn`, `chas`, `rad`) and ecology (`nox`);
 - population (`b`, `lstat`);
 - other social factors (`crim`, `indus`, `dis`, `tax`, `ptratio`);
 - house characteristics (`rm`, `age`, `medv`).

The abbreviation deciphering is inside of the report in form of a .ipynb notebook is in the _report_ folder.

The data is inside the _data_ folder. 


<br />

**Conclusion**: 

Yet there are not enough data for a good model, the current one suggests to build as following:
  - To do: a) with a high proportion of industrial businesses around, b) a significant proportion of largely residential land zones, c) desirably with enough amount of rooms per dwelling;
  - Not to do: d) around radial highways, e) heavily taxed, f) around ghettos.
