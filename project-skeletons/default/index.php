<?php
    $currentPath = $_SERVER['REQUEST_URI'];
?>
<?php include("partials/_header.php") ?>
<?php
    switch($currentPath)
    {
        case '/':
        case '/index':
            break;
    }
?>
<?php include("partials/_footer.php") ?>