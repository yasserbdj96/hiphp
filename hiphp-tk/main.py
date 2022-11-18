#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
import sys
import os

try:
    try:
        sys.path.insert(0,f'..{os.sep}hiphp')
        from hiphp import *
        from hiphp.hiphpversion import __version__
    except:
        # this just if hiphp installed on ubuntu:
        sys.path.insert(0, '/usr/share/hiphp/')
        from hiphp import *
        from hiphp.hiphpversion import __version__
except:
    try:
        from hiphp import *
        from hiphp.hiphpversion import __version__
    except:
        sys.path.insert(0, '..')
        from hiphp import *
        from hiphp.hiphpversion import __version__

from tkinter import *
from tkinter import filedialog
from chardet import detect

ftp_version="1.1.9"

#usage_msg=f"USAGE : python3 {sys.argv[0]} [KEY] [URL]"

try:
    #
    url = os.environ['URL'] if "URL" in os.environ else sys.argv[2]
    password = os.environ['KEY'] if "KEY" in os.environ else sys.argv[1]

except:
    url=""
    password=""
    #print(usage_msg)
    #exit()


# get file encoding type
def get_encoding_type(file):
    with open(file,'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

def get_id():
    p1=hiphp(password,url,retu=True).get_hole()
    print(p1)
    
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
        p1=hiphp(password,url,retu=True).run(f"{del_file}")
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
            p1=hiphp(password,url,retu=True).run(f"echo file_get_contents('{op}');")
            print(p1)

def unzip():
    if var1.get()==0:
        cname=mylist.curselection()
        for i in cname[::-1]:
            op=mylist.get(i)
            p1=hiphp(password,url,retu=True).run(f"""$file='{op}';"""+"""
$zip=new ZipArchive;
$res=$zip->open($file);
if ($res===TRUE){
    $zip->extractTo('./');
    $zip->close();
    echo "The file '$file' has been decompressed.";
}else{
    echo "Error decompressing the file";
}""")
            print(p1)
    Reconnect(url,password)
            
def upSelected():
    file=filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file!=None:
        file_name=file.name.split("/")
        file_name=file_name[len(file_name)-1]
        p1=hiphp(password,url,retu=True).upload(file.name)
        if p1==None:
            print(f"{file.name} has been uploaded.")
    Reconnect(url,password)
        
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
                p1=hiphp(password,url,retu=True).upload(file.name,path+"/")
                if p1==None:
                    print(f"{file.name} has been uploaded to '{path}/'.")
    Reconnect(url,password)
        
root=Tk()
top = Toplevel() #Creates the toplevel window
top.title('hiphp-TK login')
top.geometry('300x250')

root.title('hiphp-TK')

try:
    try:
        photo = PhotoImage(file = "./favicon.png")
        root.iconphoto(False, photo)
        top.iconphoto(False, photo)
    except:
        photo = PhotoImage(file = os.path.dirname(os.path.abspath(__file__))+"/favicon.png")
        root.iconphoto(False, photo)
        top.iconphoto(False, photo)
except ZeroDivisionError:
    pass

Label(top,width="300", text="Please enter details below", bg="orange",fg="white").pack()

#Username Label
#Label(top, text="\n\n\n")
entry1 = Entry(top) #url entry
entry1.insert(END,url)

#Password Label
#Label(top, text="Password * ").place(x=20,y=80)
entry2 = Entry(top,text="Password",show="*") #Password entry
entry2.insert(END,password)


button1 = Button(top, text="Login", command=lambda:command1(), width=10, height=1, bg="orange") #Login button
button2 = Button(top, text="Cancel", command=lambda:cancel(), width=10, height=1) #Cancel button


def cancel():
    top.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script

def command1():
    global url,password
    url=entry1.get()
    password=entry2.get()
    if url!="" and password!="": #Checks whether username and password are correct
        root.deiconify() #Unhides the root window
        top.destroy() #Removes the toplevel window
        Reconnect(url,password)



#root.iconbitmap(r'favicon.png')
root.geometry('700x500')
scrollbar=Scrollbar(root)

mylist=Listbox(root,bd=0,yscrollcommand=scrollbar.set)#,selectmode="multiple"


def Reconnect(url,password):
    if password!="" and url!="": #Checks whether username and password are correct
        root.deiconify() #Unhides the root window
        top.destroy() #Removes the toplevel window
    
        mylist.delete(0,'end')
        p1=hiphp(key=password,url=url,retu=True).run("""
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

        
        if p1!="[✗] We were unable to recognize the hiphp identifier.":
            files_list=p1.split(",")
            del files_list[-1]
            for i in range(len(files_list)):
                files_list[i]=files_list[i].replace("\\","/")
            x=files_list
            for item in range(len(x)): 
                mylist.insert(END,x[item])
                mylist.itemconfig(item,bg="#f6f6f6")
        else:
            select_all_btn["state"] = "disabled"
            unselect_all_btn["state"] = "disabled"
            openSelected_btn["state"] = "disabled"
            upSelected_btn["state"] = "disabled"
            upSelected_to_btn["state"] = "disabled"
            unzip_btn["state"] = "disabled"
            deleteSelected_btn["state"] = "disabled"
            c1["state"] = "disabled"

#Reconnect()

mylist.pack(side=LEFT,padx=0,pady=0,expand=YES,fill="both")
scrollbar.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)

btn_width=20

get_id_btn=Button(root,text="Get ID",command=get_id)
get_id_btn.pack()
get_id_btn.config(width=btn_width)

Reconnect_btn=Button(root,text="Reconnect",command=lambda:Reconnect)
Reconnect_btn.pack()
Reconnect_btn.config(width=btn_width)

select_all_btn=Button(root,text="Select all",command=select_all)
select_all_btn.pack()
select_all_btn.config(width=btn_width)#,height=2

unselect_all_btn=Button(root,text="Unselect all",command=unselect_all)
unselect_all_btn.pack()
unselect_all_btn.config(width=btn_width)

openSelected_btn=Button(root,text="Open",command=openSelected)
openSelected_btn.pack()
openSelected_btn.config(width=btn_width)

upSelected_btn=Button(root,text="Upload",command=upSelected)
upSelected_btn.pack()
upSelected_btn.config(width=btn_width)

upSelected_to_btn=Button(root,text="Upload to",command=upSelected_to)
upSelected_to_btn.pack()
upSelected_to_btn.config(width=btn_width)

unzip_btn=Button(root,text="Unzip",command=unzip)
unzip_btn.pack()
unzip_btn.config(width=btn_width)

deleteSelected_btn=Button(root,text="Delete",command=deleteSelected)
deleteSelected_btn.pack()
deleteSelected_btn.config(width=btn_width)

exit_btn=Button(root,text="Exit",command=lambda:cancel())
exit_btn.pack()
exit_btn.config(width=btn_width)

var1=IntVar()
c1=Checkbutton(root,text='multiple selection',variable=var1,onvalue=1,offvalue=0,command=selectmode)
c1.pack(side="top")

w=Label(root,text=f"hiphp V{__version__} tk V{ftp_version}")
w.pack()
w.place(relx=1.0,rely=1.0,anchor='se')

entry1.pack() #These pack the elements, this includes the items for the main window
entry1.config(width=35)
#entry1.place(x=90,y=42)
entry2.pack()
#entry2.place(x=90,y=82)
entry2.config(width=35)
button1.pack()
button2.pack()

root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
mainloop()
#}END.