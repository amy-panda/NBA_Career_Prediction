def print_class_perf( y_actuals, y_probs,set_name=None):
    """Print the ROC AUC score for the provided data

    Parameters
    ----------
    y_preds : Numpy Array
        Predicted target
    y_actuals : Numpy Array
        Actual target
    set_name : str
        Name of the set to be printed

    Returns
    -------
    """
    from sklearn.metrics import roc_auc_score
    
    print(f'ROC AUC Score {set_name}: {roc_auc_score(y_actuals, y_probs)}')


