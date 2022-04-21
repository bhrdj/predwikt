predwikt
==============================
Predict wikipedia contribution or pageview traffic.

- Download wikipedia dumps and external data (i.e. twitter feeds).
- ETL to time series.
- Use previous 6 months of time series to predict the next day.

Current dashboard:
[predwikt.bhrdwj.net](https://predwikt.bhrdwj.net)

---
Project Organization (Cookiecutter)
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Github pages folder
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
