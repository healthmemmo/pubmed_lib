# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/06_result.ipynb.

# %% auto 0
__all__ = ['Result']

# %% ../nbs/06_result.ipynb 4
import logging
from fastcore.all import *
from typing import Dict, List
from pydantic import BaseModel
from datetime import date, datetime


# %% ../nbs/06_result.ipynb 9
from .parser import *
from .author import *

# %% ../nbs/06_result.ipynb 10
class Result(BaseModel):
    """
    Model for results, including all the data taht will be retreived and their type
    """
    pubmed:str
    pmc: Optional[str]
    doi: Optional[str]
    pii: Optional[str]
    abstract: str
    autorlist: List[Autor]
    title: str
    journal: str
    published: Optional[date]
    mayorKeys: List[str]
    mayorMesh: List[str]
    minorMesh: List[str]
          
        

# %% ../nbs/06_result.ipynb 11
@patch
def __eq__(
    self:Result,
    other:Result
) -> bool:
    if isinstance(other, Result):
        return self.pubmed == other.pubmed
    return False

# %% ../nbs/06_result.ipynb 12
@patch
def __neq__(
    self:Result,
    other:Result
) -> bool:
    if isinstance(other, Result):
        return self.pubmed != other.pubmed
    return False
