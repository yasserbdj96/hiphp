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
#
def scandir(dirx="./"):
    x="""
$fileList=array();
$path='"""+dirx+"""';
if($handle=opendir($path)){
    while(false!==($entry=readdir($handle))){
        if($entry!="." && $entry!=".."){
            if(is_dir($entry)){
                $entry=$path.$entry."/";
            }else{
                $entry=$path.$entry;
            }
            $fileList[]=$entry;
        }
    }
    closedir($handle);
}
echo json_encode($fileList);"""
    return x
#
def scandir_all(dirx="./"):
    x="""
function getDirContents($dir="./",$relativePath=false){
    $fileList=array();
    $iterator=new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir));
    foreach($iterator as $file){
        if ($file->isDir()) continue;
        $path=$file->getPathname();
        if ($relativePath) {
            $path=str_replace($dir,'',$path);
            $path=ltrim($path, '/');
        }
        $fileList[]=$path;
    }
    return $fileList;
}
echo json_encode(getDirContents('"""+dirx+"""'));"""
    return x
#
def file_get_contents(dirx):
    return f"""echo file_get_contents('{dirx}');"""

#
def zip_path(path="./"):
    php_zip_code="""// Get real path for our folder
$rootPath = realpath('"""+path+"""');

$hash=date("ymdHis");

// Initialize archive object
$zip = new ZipArchive();
$zip->open($hash.'.zip', ZipArchive::CREATE | ZipArchive::OVERWRITE);

// Create recursive directory iterator
/** @var SplFileInfo[] $files */
$files = new RecursiveIteratorIterator(
    new RecursiveDirectoryIterator($rootPath),
    RecursiveIteratorIterator::LEAVES_ONLY
);

foreach ($files as $name => $file)
{
    // Skip directories (they would be added automatically)
    if (!$file->isDir())
    {
        // Get real and relative path for current file
        $filePath = $file->getRealPath();
        $relativePath = substr($filePath, strlen($rootPath) + 1);

        // Add current file to archive
        $zip->addFile($filePath, $relativePath);
    }
}

// Zip archive will be created only after closing object
$zip->close();
echo $hash.".zip";"""
    return php_zip_code

#
def file_to_b64(path):
    code="""
$file='"""+path+"""';
$fp=fopen($file, "rb");
$binary=fread($fp,filesize($file));
echo base64_encode($binary);"""
    return code

#
def php_info():
    code="""header('Content-type: text/plain');
    echo "OS : ".php_uname();
    echo "\n";
    echo "your_ip: ".$_SERVER['REMOTE_ADDR'];
    echo "\n";
    echo "HTTP_HOST : ".$_SERVER['HTTP_HOST'];
    echo "\n";
    echo "REQUEST_METHOD : ".$_SERVER['REQUEST_METHOD'];
    echo "\n";
    echo "SERVER_ADMIN : ".$_SERVER['SERVER_ADMIN'];
    echo "\n";
    echo "SERVER_PORT : ".htmlentities($_SERVER['SERVER_PORT'], ENT_QUOTES, 'UTF-8');
    echo "\n";
    echo "server_ip : ".gethostbyname($_SERVER["HTTP_HOST"]);
    echo "\n";
    echo "PHP_SELF : ".$_SERVER['PHP_SELF'];
    echo "\n";
    echo "GATEWAY_INTERFACE : ".$_SERVER['GATEWAY_INTERFACE'];
    echo "\n";
    echo "SERVER_ADDR : ".$_SERVER['SERVER_ADDR'];
    echo "\n";
    echo "SERVER_NAME : ".$_SERVER['SERVER_NAME'];
    echo "\n";
    echo "SERVER_PROTOCOL : ".$_SERVER['SERVER_PROTOCOL'];
    echo "\n";
    echo "REQUEST_TIME : ".$_SERVER['REQUEST_TIME'];
    echo "\n";
    echo "QUERY_STRING : ".$_SERVER['QUERY_STRING'];
    echo "\n";
    echo "HTTP_ACCEPT : ".$_SERVER['HTTP_ACCEPT'];
    echo "\n";
    echo "HTTP_ACCEPT_CHARSET : ".$_SERVER['HTTP_ACCEPT_CHARSET'];
    echo "\n";
    echo "HTTP_REFERER : ".$_SERVER['HTTP_REFERER'];
    echo "\n";
    echo "HTTPS : ".$_SERVER['HTTPS'];
    echo "\n";
    echo "REMOTE_HOST : ".$_SERVER['REMOTE_HOST'];
    echo "\n";
    echo "REMOTE_PORT : ".$_SERVER['REMOTE_PORT'];
    echo "\n";
    echo "SCRIPT_FILENAME : ".$_SERVER['SCRIPT_FILENAME'];
    echo "\n";
    echo "SERVER_SIGNATURE : ".$_SERVER['SERVER_SIGNATURE'];
    echo "\n";
    echo "PATH_TRANSLATED : ".$_SERVER['PATH_TRANSLATED'];
    echo "\n";
    echo "SCRIPT_NAME : ".$_SERVER['SCRIPT_NAME'];
    echo "\n";
    echo "SCRIPT_URI : ".$_SERVER['SCRIPT_URI'];
    echo "\n";
    echo "server_software : ".getenv("SERVER_SOFTWARE");
    echo "\n";
    echo "Php Version : ".phpversion();
    echo "\n";
    echo "Zend : ".htmlentities(zend_version(), ENT_QUOTES, 'UTF-8');
    echo "\n";
    echo "Oracle : ".$Oracle2=function_exists('ocilogon')?("ON"):("OFF");   
    echo "\n";
    echo "MySQL : ".$MySQL2=function_exists('mysql_connect')?("ON"):("OFF");
    echo "\n";
    echo "MSSQL : ".$MSSQL2=function_exists('mssql_connect')?("ON"):("OFF");
    echo "\n";
    echo "PostgreSQL : ".$pg_connect2=function_exists('pg_connect')?("ON"):("OFF");
    echo "\n";
    echo "disabled_functions : ".$r=ini_get('disable_functions') ? ini_get('disable_functions'):'none';
    echo "\n";"""
    return code
#}END.
