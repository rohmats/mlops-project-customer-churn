# End to End MLOps Project - Customer Churn Prediction
## Objective
Predict whether a customer will change telco provider

## Technologies
Cookiecutter: Data science project structure
Data version control (DVC): Version control of the data assets and to make pipeline
Github: For code version control
GitHub Actions: To create the CI-CD pipeline
MLFlow: For model registry
Heroku: To deploy the application
Flask: To create a web app
EvidentlyAI: To evaluate and monitor ML models in production
Pytest: To implement the unit tests

==============================

## Environment Setup
### Cookiecutter
```shell
pip install cookiecutter-data-science
cookiecutter https://github.com/drivendata/cookiecutter-data-science -c v1
```
- project_name: mlops-project-customer-churn
- repo_name: mlops-project-customer-churn
- author_name: rohmats
- description: End to End MLOps Project - Customer Churn Prediction
- Select open_source_license: select MIT(option 1)
- s3_bucket /aws_profile[Optional]: just press enter
- Select python_interpreter:python3 ( Option 1)

### Conda Environment
```shell
conda create -n customer_churn python=3.9 -y 
conda activate customer_churn
```

### DVC
```shell
pip install dvc 
dvc init 
dvc add data/external/train.csv 
```

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
