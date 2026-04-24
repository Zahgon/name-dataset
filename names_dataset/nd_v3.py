import copy
import gzip
import operator
import os
import pickle
from collections import defaultdict
from pathlib import Path
from typing import Optional, Dict, List

import pycountry


def _query(search_set, key):
    pass


def _arg(d: dict, f=max) -> str:
    pass


class NameWrapper:

    def __init__(self, d: dict):  # result of NameDataset.search()
        self.d = d

    def _attrib(self, attrib_name):
        pass

    @property
    def country(self):
        pass

    @property
    def gender(self):
        pass

    @property
    def describe(self):
        pass


def _autocomplete_search(
        prefix: str,
        names_dict: Dict[str, Dict],
        n: int = 5,
        gender: Optional[str] = None,
        country_alpha2: Optional[str] = None,
        max_rank: int = 5000
) -> List[Dict]:
    pass


def _fuzzy_search(
        fuzzy_name: str,
        names_dict: Dict[str, Dict],
        n: int = 5,
        gender: Optional[str] = None,
        country_alpha2: Optional[str] = None,
) -> List[Dict]:
    pass


class NameDataset:

    def __init__(self, load_first_names=True, load_last_names=True):
        if not load_first_names and not load_last_names:
            raise ValueError('Select either [load_first_names=True] and/or [load_last_names=True].')
        first_names_filename = Path(os.path.dirname(__file__)) / 'v3/first_names.pkl.gz'
        last_names_filename = Path(os.path.dirname(__file__)) / 'v3/last_names.pkl.gz'
        self.first_names = self._read_pickle_from_gzip(first_names_filename) if load_first_names else None
        self.last_names = self._read_pickle_from_gzip(last_names_filename) if load_last_names else None
        self.country_codes = self.get_country_codes(alpha_2=True)

    def auto_complete(
            self,
            name: str,
            n: int = 5,
            use_first_names: bool = True,
            country_alpha2: Optional[str] = None,
            gender: Optional[str] = None,
            *args, **kwargs
    ) -> List[Dict]:
        pass

    def fuzzy_search(
            self,
            name: str,
            n: int = 5,
            use_first_names: bool = True,
            country_alpha2: Optional[str] = None,
            gender: Optional[str] = None,
    ) -> List[Dict]:
        pass

    @staticmethod
    def _read_pickle_from_gzip(gzip_path):
        pass

    def _process_inputs(
            self,
            name: str,
            use_first_names: bool,
            gender: Optional[str] = None,
            country_alpha2: Optional[str] = None
    ):
        pass

    def search(self, name: str):
        pass

    def get_country_codes(self, alpha_2=False, cache: bool = False):
        pass

    def get_top_names(
            self,
            n: int = 100,
            use_first_names: bool = True,
            country_alpha2: Optional[str] = None,
            gender: Optional[str] = None
    ):
        pass

    @staticmethod
    def _post_process(result):
        pass
