#!/usr/bin/env python
"""
Test script to verify input validation for authentication system.
Run: python manage.py shell < test_validation.py
"""

from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm
from accounts.models import User

# Clean up test data
User.objects.filter(email='test@example.com').delete()
User.objects.filter(username='testuser').delete()

print("\n" + "="*60)
print("VALIDATION TEST SUITE")
print("="*60)

# Test 1: Valid Registration
print("\n[Test 1] Valid Registration Form")
form_data = {
    'email': 'test@example.com',
    'username': 'testuser',
    'password1': 'securepass123',
    'password2': 'securepass123',
}
form = CustomUserCreationForm(form_data)
print(f"Valid form: {form.is_valid()}")
if form.is_valid():
    print("✓ PASS: All validation rules passed")
else:
    print(f"✗ FAIL: {form.errors}")

# Test 2: Password too short
print("\n[Test 2] Password Too Short (< 8 chars)")
form_data = {
    'email': 'test2@example.com',
    'username': 'testuser2',
    'password1': 'short',
    'password2': 'short',
}
form = CustomUserCreationForm(form_data)
print(f"Form is valid: {form.is_valid()}")
if not form.is_valid() and 'password1' in form.errors:
    print(f"✓ PASS: Error detected - {form.errors['password1'][0]}")
else:
    print("✗ FAIL: Should reject password < 8 characters")

# Test 3: Invalid email format
print("\n[Test 3] Invalid Email Format")
form_data = {
    'email': 'notanemail',
    'username': 'testuser3',
    'password1': 'securepass123',
    'password2': 'securepass123',
}
form = CustomUserCreationForm(form_data)
print(f"Form is valid: {form.is_valid()}")
if not form.is_valid() and 'email' in form.errors:
    print(f"✓ PASS: Error detected - {form.errors['email'][0]}")
else:
    print("✗ FAIL: Should reject invalid email")

# Test 4: Passwords don't match
print("\n[Test 4] Passwords Don't Match")
form_data = {
    'email': 'test4@example.com',
    'username': 'testuser4',
    'password1': 'securepass123',
    'password2': 'differentpass123',
}
form = CustomUserCreationForm(form_data)
print(f"Form is valid: {form.is_valid()}")
if not form.is_valid() and 'password2' in form.errors:
    print(f"✓ PASS: Error detected - {form.errors['password2'][0]}")
else:
    print("✗ FAIL: Should reject mismatched passwords")

# Create a test user for duplicate tests
if form_data := {
    'email': 'duplicate@example.com',
    'username': 'duplicateuser',
    'password1': 'securepass123',
    'password2': 'securepass123',
}:
    form = CustomUserCreationForm(form_data)
    if form.is_valid():
        form.save()

# Test 5: Duplicate email
print("\n[Test 5] Duplicate Email")
form_data = {
    'email': 'duplicate@example.com',
    'username': 'differentuser',
    'password1': 'securepass123',
    'password2': 'securepass123',
}
form = CustomUserCreationForm(form_data)
print(f"Form is valid: {form.is_valid()}")
if not form.is_valid() and 'email' in form.errors:
    print(f"✓ PASS: Error detected - {form.errors['email'][0]}")
else:
    print("✗ FAIL: Should reject duplicate email")

# Test 6: Duplicate username
print("\n[Test 6] Duplicate Username")
form_data = {
    'email': 'different@example.com',
    'username': 'duplicateuser',
    'password1': 'securepass123',
    'password2': 'securepass123',
}
form = CustomUserCreationForm(form_data)
print(f"Form is valid: {form.is_valid()}")
if not form.is_valid() and 'username' in form.errors:
    print(f"✓ PASS: Error detected - {form.errors['username'][0]}")
else:
    print("✗ FAIL: Should reject duplicate username")

# Test 7: Empty fields
print("\n[Test 7] Empty Required Fields")
form_data = {
    'email': '',
    'username': '',
    'password1': '',
    'password2': '',
}
form = CustomUserCreationForm(form_data)
print(f"Form is valid: {form.is_valid()}")
has_errors = any(field in form.errors for field in ['email', 'username', 'password1', 'password2'])
if not form.is_valid() and has_errors:
    print(f"✓ PASS: Multiple errors detected as expected")
else:
    print("✗ FAIL: Should reject empty fields")

# Cleanup
User.objects.filter(email='test@example.com').delete()
User.objects.filter(email='duplicate@example.com').delete()
User.objects.filter(username='duplicateuser').delete()

print("\n" + "="*60)
print("TEST SUITE COMPLETE")
print("="*60 + "\n")
