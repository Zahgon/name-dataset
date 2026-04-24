import re
from collections import Counter
from typing import Dict

import numpy as np

from names_dataset import NameDataset


def _compute_score(ranks: Dict):
    pass


def _score(nd: NameDataset, candidate: str):
    pass


# Function to infer the best split between first and last name
def _infer_best_split(nd: NameDataset, full_name: str):
    pass


def _general_score(nd: NameDataset, candidate: str):
    pass


def try_to_split_with_two_last_names(nd: NameDataset, email: str):
    pass


def extract_names_from_email(nd: NameDataset, email: str):
    pass


def _infer_first_and_last_names(first_name, last_name, nd):
    pass
