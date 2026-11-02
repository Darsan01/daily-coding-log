<?php
// Day 12 — PHP: form handling with validation.
//
// Server-side validation is the safety net: everything in $_POST is
// user input until checked. Errors are collected in an array; the form
// is only processed when the array is empty. Output is escaped with
// htmlspecialchars() to prevent XSS.

function validate_form(array $data): array
{
    $errors = [];
    $name = trim($data['name'] ?? '');
    $email = trim($data['email'] ?? '');
    $message = trim($data['message'] ?? '');

    if ($name === '') {
        $errors['name'] = 'Name is required.';
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Enter a valid email.';
    }
    if (strlen($message) < 10) {
        $errors['message'] = 'Message must be at least 10 characters.';
    }
    return $errors;
}

// CLI test mode: `php form.php` runs the checks below, no web server needed.
if (php_sapi_name() === 'cli') {
    $cases = [
        [['name' => 'Darsan', 'email' => 'd@example.com', 'message' => 'Hello, this is a test.'], []],
        [['name' => '', 'email' => 'd@example.com', 'message' => 'Hello, this is a test.'], ['name' => 'Name is required.']],
        [['name' => 'Darsan', 'email' => 'not-an-email', 'message' => 'Hello, this is a test.'], ['email' => 'Enter a valid email.']],
        [['name' => 'Darsan', 'email' => 'd@example.com', 'message' => 'short'], ['message' => 'Message must be at least 10 characters.']],
        [['name' => '', 'email' => 'bad', 'message' => 'x'], ['name' => 'Name is required.', 'email' => 'Enter a valid email.', 'message' => 'Message must be at least 10 characters.']],
    ];
    $passed = 0;
    foreach ($cases as $i => [$input, $expected]) {
        $got = validate_form($input);
        $ok = $got === $expected;
        echo ($ok ? 'PASS' : 'FAIL') . ": case $i\n";
        if ($ok) $passed++;
    }
    echo "\n$passed/" . count($cases) . " tests passed\n";
    exit($passed === count($cases) ? 0 : 1);
}

// Web mode: validate on POST, re-show the form with errors + old input.
$errors = [];
$name = $email = $message = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $message = trim($_POST['message'] ?? '');
    $errors = validate_form($_POST);
    if (empty($errors)) {
        echo '<p>Thanks, ' . htmlspecialchars($name) . '! Your message was received.</p>';
        exit;
    }
}
?>
<form method="post">
  <label>Name <input name="name" value="<?= htmlspecialchars($name) ?>"></label>
  <?= isset($errors['name']) ? '<span>' . htmlspecialchars($errors['name']) . '</span>' : '' ?><br>
  <label>Email <input name="email" value="<?= htmlspecialchars($email) ?>"></label>
  <?= isset($errors['email']) ? '<span>' . htmlspecialchars($errors['email']) . '</span>' : '' ?><br>
  <label>Message <textarea name="message"><?= htmlspecialchars($message) ?></textarea></label>
  <?= isset($errors['message']) ? '<span>' . htmlspecialchars($errors['message']) . '</span>' : '' ?><br>
  <button type="submit">Send</button>
</form>
