
<?php
$html_template = '<!DOCTYPE html>
<html>
<body>
<h2>Sum of 2 Numbers</h2>
<form action="" method="post">
First Number: <input type="number" name="number1"><br>
Second Number: <input type="number" name="number2"><br>
<input type="submit">
</form>

</body>
</html>
';
 echo $html_template;

 #When form is submitted check of number is empty otherwise will be what is inputted
$num1 = $_POST['number1'];
$num2 = $_POST['number2'];

$num1 = (int)$num1;
$num2 = (int)$num2;

$x = 3;
$y = 2;

$output = exec("python test.py $x $y");

echo $output;
?>