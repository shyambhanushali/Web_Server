<?php
echo "HELLO, Executing handleGet.php\n";
if(isset($_GET) && isset($_GET['firstName']) && isset($_GET['lastName'])){
    echo $_GET['firstName']." ".$_GET['lastName'];
}else{
    echo "John Wick";
}