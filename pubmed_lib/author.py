# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_author.ipynb.

# %% auto 0
__all__ = ['Autor']

# %% ../nbs/02_author.ipynb 4
from Bio import Entrez
import sys
# from tinydb import TinyDB, Query, where
import pandas as pd
from datetime import datetime, timedelta, date
from collections import defaultdict, Counter
import  pickle
from fastcore.all import *
from dotenv import load_dotenv
from pydantic import BaseModel, validator, ValidationError


# %% ../nbs/02_author.ipynb 5
class Autor(BaseModel):
    Fname:str 
    Lname:str 
    name:str 
    initials:str
    emails:str
    affiliations:str
    identifier:str 
        
    @validator('name', 'Fname', 'Lname', 'initials', 'affiliations')
    def validate_str(cls, v):
        return v.title()
    
    @validator('identifier', always=True)
    def validate_identifier(cls, v):
        if not v:
            return ''
        else:
            return v
