"""
Steps:
1. Load the dataset
2. Load the model
3. Run your predictions on an augmented dataset
4. Compare.
"""

import gender_intent_classif as gic
ds = gic.data.load_dataset('YOUR_DATASET')