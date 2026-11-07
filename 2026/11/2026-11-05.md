# Day 12 — 2026-11-05

## Topic: PHP — form handling with validation (PHP)


**Problem:** Build a contact form (name, email, message) that validates on the server: required fields, a valid email address, and a message of at least 10 characters — and re-shows the form with the user's input and error messages instead of wiping it on failure.

## What I learned

- Never trust the browser: client-side validation is for UX, server-side validation is for safety. Everything in `$_POST` is user input until checked, so it gets validated and escaped before it is ever displayed.
- The pattern is: collect errors in an array, and only process the form when the array is empty. That single rule keeps validation readable no matter how many fields you add.
- `filter_var($email, FILTER_VALIDATE_EMAIL)` is PHP's built-in email check — no regex needed for the common case. `htmlspecialchars()` on output stops a `<script>` tag typed into the name field from running in another visitor's browser (XSS).
- Re-populating the form with the submitted values (`value="<?= htmlspecialchars($name) ?>"`) is a small kindness that makes a form feel professional — nobody wants to retype everything because of one bad field.

## Code

See [`form.php`](form.php) in this folder, with tests.

```php
<?php
$errors = [];
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = trim($_POST["name"] ?? "");
    $email = trim($_POST["email"] ?? "");
    if ($name === "") $errors["name"] = "Name is required.";
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors["email"] = "Enter a valid email.";
}
```

## Example

The code file contains the full form + validation, plus a `validate()` function with unit-style checks runnable via `php form.php` in CLI mode (no web server needed for the tests).

## Next

React useState + useEffect: state that re-renders, and effects that fetch.
