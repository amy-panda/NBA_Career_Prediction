# NBA Career Prediction
Following the Cross-Industry Standard Process for Data Mining (CRISP-DM) methodology, this project undertook data processing and developed multiple classification models to forecast whether a rookie player would continue playing in the NBA league for at least five years. These models encompassed Logistic Regression, Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Random Forest, AdaBoost, and XGBoost. The top-performing classifiers, Logistic Regression and XGBoost, were identified based on key performance metrics, including ROC-AUC scores and Confusion matrix.

## 🤝 Contributors
- Amy Yang
- Chanthru Vimalasri
- Yatindra Vegunta


## 🗼 Project Organization

    ├── README.md          <- README file with project details.
    |
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- Including training and validation sets.
    │   └── raw            <- Including 2022_train.csv and 2022_test.csv files.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Including the data preprocessing and two best models. 
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    |
    |
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── sets.py  
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        |
        └── models         <- Scripts to train models and then use trained models to make
            │                 predictions
            ├── null.py
            └── performance.py
    
Note: The project organisation above is adapted with the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/).


## 🛠 Tools and Techniques
- Feature engineering
- Imputation methods such as single imputation by using mean/median, multiple imputation and Nearest neighbour imputation
- Imbalance data treatment including oversampling, undersampling, STOME and hyperparameter setting
- Model training with the packages including [lazypredict](https://pypi.org/project/lazypredict/) and [scikit-learn](https://pypi.org/project/scikit-learn/)
- Hyperparameter tuning with random search, grid search and automatic search using the Hyperopt package
- Model evaluation with ROC-AUC score and Confusion Matrix plot




## ℹ️ Data Source

Kaggle Competition [[UTS AdvDSI 2022-11] NBA Career Prediction](https://www.kaggle.com/competitions/uts-advdsi-2022-11-nba-career-prediction/overview)




