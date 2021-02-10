# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 01:51:22 2018

@author: mpfou
"""

import getopt
import sys
from tkinter import messagebox

from show_plot import show_pd_histo
from new_show_all import Actions
from get_also_likes import Also
from ReadData import Preprocess
import GUI

def main():
    #Initialising the arguments values as empty
    user_uuid = ''
    doc_uuid = ''
    file_name=''
    task_id = 0
    
    objActions=Actions()
    
    #argv for getting argument from user
    argv=sys.argv[1:]
    
    try:
        opts, args = getopt.getopt(argv, "u:d:t:f:")
    except getopt.GetoptError as err:
        print(err)
        opts=[]
    
    #Setting the arguments
    for opt, arg in opts:
        if opt in ("-u"):
            user_uuid = arg
        elif opt in ("-d"):
            doc_uuid = arg
        elif opt in ("-t"):
            task_id = arg
        elif opt in ('-f'):
            file_name=arg
            obj=Preprocess(file_name)
    
    #Calling functions for corresponding tasks
    objAlso=Also()        
    if task_id == '2a':
        if (doc_uuid == '')|(file_name == ''):
            messagebox.showinfo("Warning","Enter the Filename and Subject Document ID")
        else:
            objActions.get_country(obj.Data,doc_uuid)
    elif task_id == '2b':
        if (doc_uuid == '')|(file_name == ''):
            messagebox.showinfo("Warning","Enter the Filename and Subject Document ID")
        else:
            objActions.get_continent(obj.Data,doc_uuid)
    elif task_id == '3a':
        if (file_name == ''):
            messagebox.showinfo("Warning","Enter the Filename")
        else:    
            objActions.get_full_browser(obj.Data)
    elif task_id == '3b':
        if (file_name == ''):
            messagebox.showinfo("Warning","Enter the Filename")
        else:    
            objActions.get_browser(obj.Data)
    elif task_id == '3b-a':
        if (file_name == ''):
            messagebox.showinfo("Warning","Enter the Filename")
        else:    
            objActions.all_browsers(obj.Data)        
    elif task_id == '4d':
        if (user_uuid == '') | (doc_uuid == '')|(file_name == ''):
            messagebox.showinfo("Warning","Enter the Filename,Subject Document ID and User ID")
        else:
            top_doc=obj.doc_sort.head(10)
            objAlso.also_likes_sorted(obj.Data,obj.doc_sort,doc_uuid,user_uuid)
            show_pd_histo(top_doc,orient='bar',title="Top ten documents from the whole data",x='Documents',y='Count')        
    elif task_id == '5':
        if (user_uuid == '') | (doc_uuid == '')|(file_name == ''):
            print("Provide filename,user_id and document_id...")
        else:
            objAlso.also_likes(obj.Data,obj.doc_sort,doc_uuid,user_uuid)
    elif task_id == 'gui':
        GUI.gui()        


if __name__ == "__main__":
    main()