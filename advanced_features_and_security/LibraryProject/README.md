# LibraryProject

This Django project demonstrates the use of advanced features including **custom user models, permissions, groups**, and **security configurations** like HTTPS enforcement and secure headers.

## 📌 Features Implemented

### 🔐 Custom User Model
- `CustomUser` extends `AbstractUser`
- Includes:
  - `email` (unique)
  - `date_of_birth`
  - `profile_photo`
- Uses a custom user manager (`CustomUserManager`) with:
  - `create_user()`
  - `create_superuser()`

### 🔒 Permissions and Groups
- Custom permissions (`can_create`, `can_delete`) added to the `Book` model.
- Groups defined and configured via Django Admin.
- View (`book_list`) protected with permission checks using `@permission_required`.

### 🔐 Security Settings
- Enforced HTTPS:
  - `SECURE_SSL_REDIRECT = True`
  - `SESSION_COOKIE_SECURE = True`
  - `CSRF_COOKIE_SECURE = True`
- HTTP security headers added:
  - `X-Content-Type-Options`
  - `X-Frame-Options`
  - `Strict-Transport-Security` via `SECURE_HSTS_SECONDS`

## 📁 Structure Overview

