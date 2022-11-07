<?php
if (isset($_POST['name'])) {$name = $_POST['name'];}
if (isset($_POST['phone'])) {$phone = $_POST['phone'];}
if (isset($_POST['email'])) {$email = $_POST['email'];}

$to = "askar.ramirov@mail.ru"; /*Укажите ваш адрес электоронной почты*/
$headers = "Content-type: text/plain; charset = utf-8"."\r\n".           "From:sales@factum.agency";
$subject = "Заявка с вашего сайта Uspex";
$message = "Имя пославшего: ".$name."\nТелефон: ".$phone."\nE-mail: ".$email."";
$send = mail ($to, $subject, $message, $headers);


header('Location: /thanks.php');
?>