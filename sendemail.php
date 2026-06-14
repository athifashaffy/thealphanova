<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name'] ?? '');
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
    $phone = htmlspecialchars($_POST['phone'] ?? '');
    $organization = htmlspecialchars($_POST['organization'] ?? '');
    $subjectField = htmlspecialchars($_POST['subject'] ?? '');
    $message = htmlspecialchars($_POST['message'] ?? '');

    $to = "info@thealphanova.com";
    $subject = $subjectField !== '' ? "Website Inquiry: $subjectField" : "New Message from Contact Form";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\n";
    if ($organization !== '') { $body .= "Organization: $organization\n"; }
    $body .= "\nMessage:\n$message";
    $headers = "From: $email\r\nReply-To: $email\r\nX-Mailer: PHP/" . phpversion();

    // Redirect back to the page that submitted the form (main site or labs subdomain)
    $back = isset($_SERVER['HTTP_REFERER']) ? strtok($_SERVER['HTTP_REFERER'], '?#') : '/';

    if (mail($to, $subject, $body, $headers)) {
        header("Location: {$back}?status=success#contact");
    } else {
        header("Location: {$back}?status=failed#contact");
    }
    exit;
}

header("Location: /");
exit;
?>
