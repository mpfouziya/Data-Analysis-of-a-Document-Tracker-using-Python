# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:06:57 2018

@author: mpfou
"""

import tkinter as tk
from new_show_all import Actions
from get_also_likes import Also
from ReadData import Preprocess
def gui():
    LARGE_FONT=('Verdana',12)
    
    obj=Preprocess('json_data.json')
    objAction=Actions()
    objAlso=Also()
    
    #Creating GUI and adding controls    
    window=tk.Tk()
    window.title("Data Analysis")
    
    
    label=tk.Label(window,text="Data Analysis",font=LARGE_FONT)
    label.grid(row=1,columnspan=4)
    
   
    label_docid=tk.Label(window,text="Document Id")
    label_userid=tk.Label(window,text="User Id")
    
           
    txt_docid=tk.Entry(window)     
    txt_userid=tk.Entry(window)
    
    label_docid.grid(row=5)
    label_userid.grid(row=6)
    
    txt_docid.grid(row=5,column=2)
    txt_userid.grid(row=6,column=2)
    
    btn_country=tk.Button(window,text="Get Country List",command=lambda:objAction.get_country(obj.Data,txt_docid.get()))
    btn_country.grid(row=8,column=1,columnspan=2)
            
    btn_cont=tk.Button(window,text="Get Continent List",command=lambda:objAction.get_continent(obj.Data,txt_docid.get()))
    btn_cont.grid(row=9,column=1,columnspan=2)
            
    btn_full_browser=tk.Button(window,text="Get Full Browser List",command=lambda:objAction.get_full_browser(obj.Data))
    btn_full_browser.grid(row=10,column=1,columnspan=2)
            
    btn_browser=tk.Button(window,text="Get Browser List",command=lambda:objAction.get_browser(obj.Data))
    btn_browser.grid(row=11,column=1,columnspan=2)
            
    btn_also=tk.Button(window,text="Get Also Likes",command=lambda:objAlso.also_likes(obj.Data,obj.doc_sort,txt_docid.get(),txt_userid.get()))
    btn_also.grid(row=12,column=1,columnspan=2)
    
    window.geometry("400x500+100+100")
    window.mainloop()
    #140224101516-e5c074c3404177518bab9d7a65fb578e
    #140228202800-6ef39a241f35301a9a42cd0ed21e5fb0,2f63e0cca690da91--alsolikes

if __name__=='__main__':
    gui()