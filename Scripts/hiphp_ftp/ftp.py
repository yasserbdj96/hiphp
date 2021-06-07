# EXAMPLES :
#s
import re
from hiphp import hiphp
from tkinter import *
from tkinter import filedialog
import os
from chardet import detect

url="http://localhost/hiphp.php"
password="123"

p1=hiphp(password,url).run("""
function iterateDirectory($i){
    foreach($i as $path){
        if($path->isDir()){
            iterateDirectory($path);
        }else{
            echo $path.",";
        }
    }
}
$dir='.';
$iterator=new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir));
iterateDirectory($iterator);""")

files_list=p1.split(",")
del files_list[-1]
for i in range(len(files_list)):
    files_list[i]=files_list[i].replace("\\","/")  

# get file encoding type
def get_encoding_type(file):
    with open(file,'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']


def selectmode():
    if var1.get()==1:
        mylist['selectmode']="multiple"
    else:
        mylist['selectmode']="SINGLE"

def deleteSelected():
    #selected=[]
    cname=mylist.curselection()
    for i in cname[::-1]:
        op=mylist.get(i)
        #selected.append(op)
        mylist.delete(i)
        del_file='$file_pointer="'+op+'";if(!unlink($file_pointer)){echo("$file_pointer cannot be deleted due to an error");}else{echo("$file_pointer has been deleted");}'
        p1=hiphp(password,url).run(f"{del_file}")
        print(p1)
    unselect_all()
    
def select_all():
    mylist.select_set(0,END)

def unselect_all():
    mylist.selection_clear(0,END)

def openSelected():
    if var1.get()==0:
        cname=mylist.curselection()
        for i in cname[::-1]:
            op=mylist.get(i)
            p1=hiphp(password,url).run(f"echo file_get_contents('{op}');")
            print(p1)
            
def upSelected():
    file=filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file!=None:
        file_name=file.name.split("/")
        file_name=file_name[len(file_name)-1]
        p1=hiphp(password,url).upload(file.name)
        
def upSelected_to():
    if var1.get()==0:
        cname=mylist.curselection()
        
        for i in cname[::-1]:
            op=mylist.get(i)
            op=op.split("/")
            path=""
            for i in range(len(op)-1):
                if path=="":
                    ss=""
                else:
                    ss="/"
                path=path+ss+op[i]

            file=filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
            if file!=None:
                file_name=file.name.split("/")
                file_name=file_name[len(file_name)-1]
        
                p1=hiphp(password,url).upload(file.name,path+"/")
        
root=Tk()
root.title('Hiphp FTP')
#root.iconbitmap(r'favicon.ico')
root.geometry('700x500')
scrollbar=Scrollbar(root)

mylist=Listbox(root,bd=0,yscrollcommand=scrollbar.set)#,selectmode="multiple"

x=files_list
for item in range(len(x)): 
	mylist.insert(END,x[item]) 
	mylist.itemconfig(item,bg="#f6f6f6") 

mylist.pack(side=LEFT,padx=0,pady=0,expand=YES,fill="both")
scrollbar.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)

select_all_btn=Button(root,text="Select all",command=select_all)
select_all_btn.pack()
select_all_btn.config(width=15)#,height=2

unselect_all_btn=Button(root,text="Unselect all",command=unselect_all)
unselect_all_btn.pack()
unselect_all_btn.config(width=15)

openSelected_btn=Button(root,text="Open",command=openSelected)
openSelected_btn.pack()
openSelected_btn.config(width=15)

upSelected_btn=Button(root,text="Upload",command=upSelected)
upSelected_btn.pack()
upSelected_btn.config(width=15)

upSelected_to_btn=Button(root,text="Upload to",command=upSelected_to)
upSelected_to_btn.pack()
upSelected_to_btn.config(width=15)

deleteSelected_btn=Button(root,text="Delete",command=deleteSelected)
deleteSelected_btn.pack()
deleteSelected_btn.config(width=15)

var1=IntVar()
c1=Checkbutton(root,text='multiple selection',variable=var1,onvalue=1,offvalue=0,command=selectmode)
c1.pack(side="bottom")

mainloop()
#e