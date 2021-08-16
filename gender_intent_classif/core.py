from typing import Dict, List


def compute_metrics(y_true: List[int], y_pred: List[int], sensitive_attribute: List[int]) -> Dict:
    """
    From the predictions and its sensitive attributes compute metrics.

    Hint: fairlearn.MetricFrame can help you!

    Args:
        y_true: Groundtruth for each utterance
        y_pred: Model predictions for each utterance
        sensitive_attribute: Sensitive attribute for each utterance.

    Returns:
        Scores that we are interested in.
    """
    return None
