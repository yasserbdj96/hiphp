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

#ls:
def php_ls():
    x="""function getDirContents($dir="./",$relativePath=false){
    $fileList=array();
    $iterator=new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir));
    foreach($iterator as $file){
        if ($file->isDir()) continue;
        $path=$file->getPathname();
        if ($relativePath) {
            $path=str_replace($dir,'',$path);
            $path=ltrim($path, '/');
        }
        $fileList[]=$path.":".substr(sprintf('%o', fileperms($path)), -4);
    }
    return $fileList;
}
echo json_encode(getDirContents('./'));"""
    return x
#cat:
def php_cat(path):
    x=f"echo file_get_contents('{path}');"
    return x
#info:
def php_file_info(path):
    x="""
    function formatSizeUnits($bytes){
        if ($bytes >= 1073741824){
            $bytes = number_format($bytes / 1073741824, 2) . ' GB';
        }elseif ($bytes >= 1048576){
            $bytes = number_format($bytes / 1048576, 2) . ' MB';
        }elseif ($bytes >= 1024){
            $bytes = number_format($bytes / 1024, 2) . ' KB';
        }elseif ($bytes > 1){
            $bytes = $bytes . ' bytes';
        }elseif ($bytes == 1){
            $bytes = $bytes . ' byte';
        }else{
            $bytes = '0 bytes';
        }
        return $bytes;
    }"""+f"""
    $filepath = '{path}';
    echo  'File Size: '.formatSizeUnits(filesize($filepath)).'\n';
    $path_parts = pathinfo($filepath);
    echo 'Dir Name: '.$path_parts['dirname'], "\n";
    echo 'Base Name: '.$path_parts['basename'], "\n";
    echo 'Extension: '.$path_parts['extension'], "\n";
    echo 'File Name: '.$path_parts['filename'], "\n";
    echo "Last update: " . date ("F/d/Y H:i:s.", filemtime($path_parts['filename']));"""
    return x
#save:
def php_save(path,content):
    x="""$path=str_replace("./","/",'"""+path+"""');
$path=getcwd().$path;
chmod($path,0777);
$Contents = base64_decode('"""+content+"""');
if(is_writable($path)){
    $myfile=fopen($path,"w") or die("Unable to open file!");
    fwrite($myfile,$Contents);
    fclose($myfile);
    echo "save successfully!";
}elseif(unlink($path)){
    unlink($path);
    $myfile=fopen($path,"w") or die("Unable to open file!");
    fwrite($myfile,$Contents);
    fclose($myfile);
    echo "save successfully!";
}else{echo $path." is't writable!";}"""
    return x
#delete:
def php_delte(path):
    x="""$filename='"""+path+"""';
if(unlink($filename)){echo 'The file '.$filename.' was deleted successfully!';}
else{echo 'There was a error deleting the file '.$filename;}"""
    return x
#rename:
def php_ren(path,newname):
    x="""
$path=str_replace("./","",'/"""+newname+"""');
$file_path=getcwd().pathinfo("$path")['dirname'];
if(!file_exists("$file_path")){mkdir("$file_path",0777,true);}
if(rename('"""+path+"""','"""+newname+"""')){echo "rename successfully!";}
else{"Unable to rename file!";}"""
    return x
#add:
def php_add(path):
    x=f"""$path=str_replace("./","",'/"""+path+"""');
$file_path=getcwd().pathinfo("$path")['dirname'];
if(!file_exists("$file_path")){mkdir("$file_path",0777,true);}
$path=getcwd().$path;
chmod($path,0777);
$myfile=fopen($path,"w") or die("Unable to create file!");
fclose($myfile);
echo "create successfully!";"""
    return x
#permissions:
def php_permi(path,newpermi):
    x=f"""chmod("{path}",{newpermi});
    echo "Permission changed successfully!";"""
    return x
'''
#download:
def php_down(path):
    x=f"""$filename="{path}";
$type=mime_content_type($filename);
//Define header information
header('Content-Description: File Transfer');
header('Content-Type: '.$type);
header("Cache-Control: no-cache, must-revalidate");
header("Expires: 0");
header('Content-Disposition: attachment; filename="'.basename($filename).'"');
header('Content-Length: ' . filesize($filename));
header('Pragma: public');
//Clear system output buffer
flush();
//Read the size of the file
readfile($filename);
//Terminate from the script
die();"""
    return x
'''
#
def down_from_path(path):
    x=f"""
$cont=base64_encode(file_get_contents('{path}'));
$type=mime_content_type('{path}');
$file=basename('{path}');
$cont_type=array("file"=>$file,"type"=>$type,"cont"=>$cont);
echo json_encode($cont_type);"""
    return x
#}END.