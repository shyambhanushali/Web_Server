<?php
if(isset($_POST) && isset($_POST['firstName']) && isset($_POST['lastName'])){
    echo $_POST['firstName']." ".$_POST['lastName'];
}else{
    echo "John Wick 2";
}
?>