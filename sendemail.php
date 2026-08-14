<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name'] ?? '');
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
    $phone = htmlspecialchars($_POST['phone'] ?? '');
    $organization = htmlspecialchars($_POST['organization'] ?? '');
    $subjectField = htmlspecialchars($_POST['subject'] ?? '');
    $message = htmlspecialchars($_POST['message'] ?? '');
    $budget = htmlspecialchars($_POST['budget'] ?? '');
    $timeline = htmlspecialchars($_POST['timeline'] ?? '');

    // Redirect back to the page that submitted the form (main site or labs subdomain)
    $back = isset($_SERVER['HTTP_REFERER']) ? strtok($_SERVER['HTTP_REFERER'], '?#') : '/';

    // --- reCAPTCHA verification ---
    // The secret is loaded from recaptcha-config.php, which is gitignored and
    // lives only on the server. It used to be hardcoded here — in a public
    // repository — which burned the previous key. Do not put it back.
    $recaptchaSecret = '';
    $envPath = __DIR__ . '/.env';
    if (is_readable($envPath)) {
        foreach (file($envPath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $line) {
            $line = trim($line);
            if ($line === '' || $line[0] === '#' || strpos($line, '=') === false) { continue; }
            [$k, $v] = explode('=', $line, 2);
            if (trim($k) === 'RECAPTCHA_SECRET') {
                $recaptchaSecret = trim($v, " \t\"'");
                break;
            }
        }
    }
    if ($recaptchaSecret === '' && getenv('RECAPTCHA_SECRET')) {
        $recaptchaSecret = getenv('RECAPTCHA_SECRET');
    }
    // Fail closed. An unconfigured secret must not silently disable the check.
    if ($recaptchaSecret === '') {
        error_log('sendemail.php: reCAPTCHA secret not configured (recaptcha-config.php missing or empty)');
        header("Location: {$back}?status=config#contact");
        exit;
    }

    $recaptchaResponse = $_POST['g-recaptcha-response'] ?? '';
    $captchaOk = false;
    if ($recaptchaResponse !== '') {
        $postData = http_build_query([
            'secret'   => $recaptchaSecret,
            'response' => $recaptchaResponse,
            'remoteip' => $_SERVER['REMOTE_ADDR'] ?? '',
        ]);
        $verifyJson = false;
        if (function_exists('curl_init')) {
            $ch = curl_init("https://www.google.com/recaptcha/api/siteverify");
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
            curl_setopt($ch, CURLOPT_TIMEOUT, 10);
            $verifyJson = curl_exec($ch);
            curl_close($ch);
        }
        if ($verifyJson === false && ini_get('allow_url_fopen')) {
            $context = stream_context_create(['http' => [
                'method'  => 'POST',
                'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                'content' => $postData,
                'timeout' => 10,
            ]]);
            $verifyJson = @file_get_contents("https://www.google.com/recaptcha/api/siteverify", false, $context);
        }
        if ($verifyJson !== false) {
            $verify = json_decode($verifyJson, true);
            // v3 returns a score (0.0 - 1.0); require a reasonable threshold.
            // v2 has no score, so success alone is enough.
            $scoreOk = !isset($verify['score']) || $verify['score'] >= 0.5;
            $captchaOk = !empty($verify['success']) && $scoreOk;
        }
    }
    if (!$captchaOk) {
        header("Location: {$back}?status=captcha#contact");
        exit;
    }

    $to = "info@thealphanova.com";
    $subject = $subjectField !== '' ? "Website Inquiry: $subjectField" : "New Message from Contact Form";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\n";
    if ($organization !== '') { $body .= "Organization: $organization\n"; }
    // Qualification fields from the project-enquiry form.
    if ($budget !== '')   { $body .= "Budget: $budget\n"; }
    if ($timeline !== '') { $body .= "Timeline: $timeline\n"; }
    $body .= "\nMessage:\n$message";
    $headers = "From: $email\r\nReply-To: $email\r\nX-Mailer: PHP/" . phpversion();

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
