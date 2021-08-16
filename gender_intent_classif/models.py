from transformers import Pipeline


def get_model(checkpoint_name: str) -> Pipeline:
    """
    Load a HuggingFace model from a checkpoint name.
    Args:
        checkpoint_name: Namer of the model or path to the checkpoint.

    Returns:
        Pipeline where one can make prediction and have access to:
            - `tokenizer`, to tokenize utterances.
            - `model`, to make prediction
            - Prediction with `pipeline(['your_sentence'])`
    """
    return None
