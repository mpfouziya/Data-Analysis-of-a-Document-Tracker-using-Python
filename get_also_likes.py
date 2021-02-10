# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:52:54 2018

@author: mpfou
"""

from graphviz import Digraph
import numpy as np
import tempfile
from tkinter import messagebox

from show_plot import show_dict_histo

class Also:
    #Getting visitors list of a document
    def visitors_doc(self,Data,doc_uuid):
        filtered=Data[(Data['event_type']=='read')& (Data['subject_doc_id']==doc_uuid)]
        visitors=filtered['visitor_uuid'].unique()
        return visitors
    
    #Getting document lists of a particular visitor 
    def also_read(self,Data,visitor):
        filtered=Data[Data['visitor_uuid']==visitor]
        docs=filtered['subject_doc_id'].unique()
        return docs    
    
    #Getting also likes list        
    def also_likes(self,Data,doc_sort,doc_id,user_id):
        
        if len(doc_id)==0:
            messagebox.showinfo("Warning","Enter the document id")
        elif len(user_id)==0:
            messagebox.showinfo("Warning","Enter the user id")
        else: 
            try:   
                #Getting users who read the given document
                other_users=self.visitors_doc(Data,doc_id)
                doc_hits={}
                user_doc={}
                
                #Getting other documents read by the above obtained users
                for each in other_users:
                    user_doc[each]=self.also_read(Data,each).tolist() 
                    
                #Creating graph
                g = Digraph('G', filename='hello.gv')       
                for each in user_doc:
                    for i in user_doc[each]:
                        if i is np.nan:
                            i=i                
                        else:    
                            g.node(each[-4:],shape='square')
                            doc_hits[i]=doc_sort[i]
                            g.edge(each[-4:],i[-4:])
                g.node_attr.update(color='lightblue2', style='filled')
                g.node(user_id[-4:],style='filled',fillcolor='green',shape='square')
                g.node(doc_id[-4:],color='green',style='filled')
                g.edge(user_id[-4:], doc_id[-4:])
                
                #Obtaining documents from the also likes list in sorted order
                doc_hits=sorted(doc_hits.items(), key=lambda y: y[1],reverse=True)
                
                
                if doc_hits!=[]:
                    first=doc_hits[0][0]
                    print("Sorted Order of document views:")
                    print(dict(doc_hits))
                    g.node(first[-4:],color='red',style='filled')
                    an={}
                    for i in doc_hits:
                        c=i[0][-4:]
                        an[c]=i[1]
                    show_dict_histo(an,title="Also Likes Document List",x='Documents',y='Count') 
                    g.view(tempfile.mktemp('hello.gv')) 
                else:
                    messagebox.showinfo("Error","Enter a valid Document ID")  
            except Exception:
                messagebox.showinfo("Error","Check the IDs you entered")  
    
        
    def also_likes_sorted(self,Data,doc_sort,doc_id,user_id):
        
        if len(doc_id)==0:
            messagebox.showinfo("Warning","Enter the document id")
        elif len(user_id)==0:
            messagebox.showinfo("Warning","Enter the user id")
        else: 
            try:   
                #Getting users who read the given document
                other_users=self.visitors_doc(Data,doc_id)
                doc_hits={}
                user_doc={}
                
                #Getting other documents read by the above obtained users
                for each in other_users:
                    user_doc[each]=self.also_read(Data,each).tolist() 
                    
                #Creating sorted list
                for each in user_doc:
                    for i in user_doc[each]:
                        if i is np.nan:
                            i=i                
                        else:    
                            doc_hits[i]=doc_sort[i]                
            
                #Obtaining documents from the also likes list in sorted order
                doc_hits=sorted(doc_hits.items(), key=lambda y: y[1],reverse=True)
                if doc_hits=={}:
                    messagebox.showinfo("Warning","Entered document ID does not exist")
                else:    
                    print("Sorted Order of other documents viewed:")
                    print(dict(doc_hits))
                 
            except Exception:
                messagebox.showinfo("Error","Check the IDs you entered")                  
          