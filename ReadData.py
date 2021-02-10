# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:07:15 2018

@author: mpfou
"""

import json
import pandas as pd

#Converting JSON data into Pandas Dataframe
class Preprocess:
    def __init__(self,filename):
        with open(filename) as f:
            lt=[]
            for line in f:
                data=json.loads(line)
                lt.append(data)
            self.Data=pd.DataFrame(lt)
            self.doc_sort=self.get_sorted(self.Data)
    def get_sorted(self,Data):
            doc_sort=Data[Data['event_type']=='read']['subject_doc_id'].value_counts()
            return doc_sort


