# Input Validation Rules

## Registration Form (`accounts/forms.py`)

### Email Field
- **Required**: Yes
- **Type**: Valid email format (RFC 5322)
- **Validation**: 
  - Must be a valid email address (enforced by Django's EmailValidator)
  - Must not already exist in the database
  - **Error**: "Please enter a valid email address." or "An account with this email already exists."

### Username Field
- **Required**: Yes
- **Type**: String
- **Validation**:
  - Cannot be empty
  - Must be unique in the database
  - **Error**: "Username is required." or "This username is already taken."

### Password Field (password1)
- **Required**: Yes
- **Type**: String
- **Validation**:
  - Cannot be empty
  - **Minimum length**: 8 characters
  - **Error**: "Password is required." or "Password must be at least 8 characters long."

### Confirm Password Field (password2)
- **Required**: Yes
- **Type**: String
- **Validation**:
  - Cannot be empty
  - Must match password1 exactly
  - **Error**: "Please confirm your password." or "Passwords do not match."

## Login Form (`accounts/forms.py`)

### Email Field
- **Required**: Yes
- **Type**: Valid email format
- **Validation**: Must be a valid email address
- **Error**: "Please enter a valid email address."

### Password Field
- **Required**: Yes
- **Type**: String
- **Error**: "Invalid email or password." (if credentials don't match)

## Error Response Handling

### Registration View (`accounts/views.py`)
1. **Successful Registration**:
   - User is automatically logged in
   - Redirected to home page
   - Success message: "Registration successful! Welcome to Devread, {username}."

2. **Form Validation Errors**:
   - All validation errors are displayed as messages
   - User stays on registration page with form populated
   - Each field error is shown with an error icon

3. **Database Integrity Errors**:
   - If an IntegrityError occurs during save, user gets error message
   - Message: "An error occurred during registration. Please try again."
   - Form is reset for retry

### Login View (`accounts/views.py`)
1. **Successful Login**:
   - User is logged in
   - Redirected to home page
   - Success message: "Welcome back, {username}!"

2. **Invalid Credentials**:
   - Generic error message: "Invalid email or password."
   - User stays on login page
   - Form fields are cleared for security

3. **Already Authenticated**:
   - User is redirected to home page (cannot re-login while logged in)

### Logout View (`accounts/views.py`)
1. **Successful Logout**:
   - Session is cleared
   - User is redirected to home page
   - Success message: "You have been logged out successfully."

2. **Not Authenticated**:
   - User is redirected to login page (protected by @login_required)

## Template Error Display

Both registration and login templates display:
- **Success Messages**: Green background with check icon
- **Error Messages**: Red background with error icon
- **Field-level Errors**: Red text with warning icons, listed under each field
- **Input Validation Icons**: Red error icon appears on invalid fields
