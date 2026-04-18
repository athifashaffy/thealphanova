<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $phone = htmlspecialchars($_POST['phone']);
    $message = htmlspecialchars($_POST['message']);

    $to = "info@thealphanova.com";
    $subject = "New Message from Contact Form";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\n\nMessage:\n$message";
    $headers = "From: $email\r\nReply-To: $email\r\nX-Mailer: PHP/" . phpversion();

    if (mail($to, $subject, $body, $headers)) {
        header("Location: /?status=success#contact");
    } else {
        header("Location: /?status=failed#contact");
    }
    exit;
}

header("Location: /");
exit;
?>
