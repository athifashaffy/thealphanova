<?php
/**
 * reCAPTCHA configuration — TEMPLATE.
 *
 * Copy this file to `recaptcha-config.php` (same directory) and paste your
 * real keys in. `recaptcha-config.php` is gitignored and must never be
 * committed: the repository is public on GitHub, which is exactly how the
 * previous secret key was exposed.
 *
 *   cp recaptcha-config.sample.php recaptcha-config.php
 *
 * Get a fresh v3 key pair at https://www.google.com/recaptcha/admin
 * The SITE key is public (it appears in page markup). The SECRET key is not,
 * and must only ever live in recaptcha-config.php on the server.
 */

return [
    // Public. Also needs pasting into the pages that carry a form.
    'site_key' => '',

    // Secret. Server-side only. Never commit, never put in HTML.
    'secret'   => '',
];
