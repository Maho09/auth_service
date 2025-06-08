# Auth_service

A Django-based authentication system that enhances user security utilizing One-Time Password (OTP) verification.
This project includes features like user registration, login, changing password, and device-specific login verification.

## Features

- **User Registration**: Create an account with email, username, and phone number.
- **Email Verification**: Upon registration, an OTP is sent to the user's email for verification.
- **Login with OTP**: Secure login process requiring OTP verification.
- **Password Recovery**: Request an OTP to reset your password.
- **Device-Specific Login**: OTP verification when logging in from a new device.
- **Account Locking**: After 3 failed login attempts, the account is locked until email verification is completed.
- **Logging**: Detailed logging of application events and debugging info.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- Django 4.0 or higher
- A working email service for sending OTPs (configured in Django settings)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/maho09/auth_service.git
   ```
2. Create a virtual environment and activate it:

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  ```

3. Apply migrations to set up your database:
  
  ```bash
  python manage.py migrate
  ```

4. Create a superuser to access the Django admin:

  ```bash
  python manage.py createsuperuser
  ```

5. Run the development server:

  ```bash
  python manage.py runserver
  ```
Visit http://127.0.0.1:8000/ in your browser to access the application.

## Usage
- Register: Navigate to /register to create a new account.

- Login: Use /login to sign in. If it's your first time logging in from a device, you'll receive an OTP via email.

- Forgot Password: Go to /forgot-pass to initiate the password recovery process.

- Change Password: After receiving the OTP, change your password at /change-pass.

- Logout: Use /logout to sign out.

- Logging: The application uses Django's built-in logging framework configured in `settings.py`.
  Logs are saved to a file named `debug.log` in the project root directory. Logging captures debug information for the following modules:
    - `perfumes.views`
    - `perfumes.signals`

## Key project Structure
- models.py: Defines the User and Otp models.

- views.py: Contains the logic for user authentication, OTP generation, and email handling.

- urls.py: Maps URLs to views.

- signals.py: Automatically sends an OTP email upon user creation.

- create_key.py: Generates OTPs based on the username.

- register.js: Client-side validation for password strength during registration.

  #### The repo is still under development. Any comment is most welcome😁
