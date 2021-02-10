# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:49:22 2018

@author: mpfou
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 17:55:39 2018

@author: mpfou
"""
from tkinter import messagebox
import re

from dict_details import cntry_to_cont,continents
from show_plot import show_dict_histo,show_pd_histo

class Actions:
    def get_country(self,Data,doc_id):
        if doc_id=='':
            messagebox.showinfo("Warning","Enter the Subject Document ID")
        else:    
            try:
                filtered=Data[Data['subject_doc_id']==doc_id]
                show_pd_histo(filtered['visitor_country'].value_counts(),title='Countries from which the given document is viewed',x='Country Names',y='Count')
            except Exception:
                messagebox.showinfo("wARNING","Enter a valid Subject Document Id")
    def get_continent(self,Data,doc_id):
        if doc_id=='':
            messagebox.showinfo("Warning","Enter the Subject Document ID")
        else:    
            filtered=Data[Data['subject_doc_id']==doc_id]
            country_count=filtered['visitor_country'].tolist()
            
            #Mapping of lists using generators
            s_cont=map(lambda x:cntry_to_cont[x],country_count)
            full_cont=map(lambda x:continents[x],list(s_cont))
            
            full_continent={}
            for each in full_cont:
                if each in full_continent:
                    full_continent[each]+=1
                else:
                    full_continent[each]=1
            if full_continent=={}:
                messagebox.showinfo("Warning","Enter a valid Subject Document ID")
            else:    
                show_dict_histo(full_continent,title="Continents from which the given document is viewed",x='Continent Names',y='Count')        
        
    #Getting only first browser name only from each row  
    def split_strings(self,row):
        if re.search("^Mozilla",row) is not None:
            strings=row.split(' ')[0]
        else:
            strings=row.split('/')[0]            
        return strings

    def get_browser(self,Data):
        browser=Data['visitor_useragent'].apply(self.split_strings).value_counts()            
        show_pd_histo(browser,title='Browser Lists',orient='barh',x='Count',y='Browser Names')
    
    #Getting full browser list without any splitting                    
    def get_full_browser(self,Data):
        show_pd_histo(Data['visitor_useragent'].value_counts(),title="Full Browser Lists",x="Browser Names",y="Count",annot=False)
    
    #Getting all browser names as there is multiple browsers in a row 
    def split_all_strings(self,row):
        strings=re.sub("[\(\[].*?[\)\]]", "",row['visitor_useragent'])
        strings=re.sub("Silk-Accelerated=true", "",strings)
        strings=strings.split(' ')
        a=[]
        
        for string in strings:
            if re.search('Mobile$',string) is not None:
                a.append('Mobile')
            if re.search("/[0-9]",string) is not None:
                a.append(string.split('/')[0])
                
        return a
     
    def all_browsers(self,Data):
        d=Data.apply(self.split_all_strings,axis=1)
        b_strings={}
        for each in d:
            for i in each:
                if i in b_strings:
                    b_strings[i]+=1
                else:
                    b_strings[i]=1
        show_dict_histo(b_strings,title="List of all browsers in the document",x='Browser Names',y='Count')                    