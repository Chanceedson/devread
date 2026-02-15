# Testing Guide: User Avatar & Profile Settings

## Pre-Test Setup

1. Ensure the application is running:
   ```bash
   python manage.py runserver
   ```

2. Navigate to: `http://localhost:8000/`

## Test Cases

### TEST 1: Avatar Display in Navbar (No Image)
**Objective**: Verify avatar badge shows first letter when no image uploaded

**Steps**:
1. Create a new account (e.g., "john" / "john@example.com")
2. Log in with that account
3. Check navbar top right corner

**Expected Result**:
- Avatar badge appears
- Shows "J" (first letter in uppercase)
- Badge is circular with purple-to-pink gradient
- Badge has purple border

**Status**: ✓ Pass / ✗ Fail

---

### TEST 2: Avatar Clickability
**Objective**: Verify avatar is clickable and navigates to profile

**Steps**:
1. While logged in, click the avatar badge in navbar
2. Observe URL and page

**Expected Result**:
- Page navigates to `/accounts/profile/`
- Profile settings page loads
- Current user's information is displayed

**Status**: ✓ Pass / ✗ Fail

---

### TEST 3: Profile Page Layout
**Objective**: Verify profile page displays correctly on desktop

**Steps**:
1. Navigate to `/accounts/profile/`
2. Check browser width (desktop, ~1200px or wider)
3. Observe layout

**Expected Result**:
- Left sidebar (1 column) with avatar preview and quick info
- Right form area (3 columns) with input fields
- Two sections: "Basic Information" and "Professional Information"
- Both "Save Changes" and "Cancel" buttons visible

**Status**: ✓ Pass / ✗ Fail

---

### TEST 4: Mobile Responsive Design
**Objective**: Verify profile page is responsive on mobile

**Steps**:
1. Navigate to `/accounts/profile/`
2. Open browser DevTools (F12)
3. Toggle Device Toolbar (iPhone size)
4. Observe layout

**Expected Result**:
- Form stacks vertically
- Avatar preview and form fields stack properly
- All buttons are clickable on mobile
- Text is readable without zooming
- No horizontal scrolling needed

**Status**: ✓ Pass / ✗ Fail

---

### TEST 5: Update Username
**Objective**: Verify username can be updated and validated

**Steps**:
1. On profile page, find "Username" field
2. Clear current username
3. Enter new username: "newusername"
4. Click "Save Changes"
5. Check for success message
6. Refresh page to verify change persisted

**Expected Result**:
- Green success message: "Your profile has been updated successfully."
- Username field shows "newusername" after refresh
- Avatar in navbar doesn't change (still shows first letter)

**Status**: ✓ Pass / ✗ Fail

---

### TEST 6: Update Email
**Objective**: Verify email can be updated with validation

**Steps**:
1. On profile page, find "Email" field
2. Clear current email
3. Enter new email: "newemail@example.com"
4. Click "Save Changes"
5. Check for success message

**Expected Result**:
- Green success message appears
- Email field shows new email
- No errors displayed
- Can still log in with new email

**Status**: ✓ Pass / ✗ Fail

---

### TEST 7: Duplicate Email Validation
**Objective**: Verify duplicate emails are rejected

**Pre-requisite**: Have 2 user accounts (account1, account2)

**Steps**:
1. Log in as account1
2. Go to `/accounts/profile/`
3. Try to change email to account2's email
4. Click "Save Changes"
5. Observe error message

**Expected Result**:
- Red error message: "This email is already in use."
- Email field not updated
- User stays on profile page
- Can correct and retry

**Status**: ✓ Pass / ✗ Fail

---

### TEST 8: Duplicate Username Validation
**Objective**: Verify duplicate usernames are rejected

**Pre-requisite**: Have 2 user accounts

**Steps**:
1. Log in as account1
2. Go to `/accounts/profile/`
3. Try to change username to account2's username
4. Click "Save Changes"
5. Observe error message

**Expected Result**:
- Red error message: "This username is already taken."
- Username field not updated
- Can correct and retry

**Status**: ✓ Pass / ✗ Fail

---

### TEST 9: Upload Avatar Image
**Objective**: Verify avatar image can be uploaded

**Steps**:
1. On profile page, find "Profile Picture" field
2. Click "Choose File"
3. Select an image file from computer
4. Click "Save Changes"
5. Check avatar in navbar
6. Refresh page

**Expected Result**:
- Green success message appears
- Avatar in navbar shows the uploaded image
- Avatar is circular with border
- Image displays after page refresh
- Sidebar shows image in profile preview

**Status**: ✓ Pass / ✗ Fail

---

### TEST 10: Non-Image File Upload Rejection
**Objective**: Verify only images can be uploaded

**Steps**:
1. On profile page, find "Profile Picture" field
2. Try to select a non-image file (e.g., .txt, .pdf)
3. Try to save if possible

**Expected Result**:
- Either file picker doesn't show non-image files
- OR form shows error: invalid file type
- Avatar is not updated

**Status**: ✓ Pass / ✗ Fail

---

### TEST 11: Update All Profile Fields
**Objective**: Verify all fields can be updated together

**Steps**:
1. On profile page, fill in all optional fields:
   - First Name: "John"
   - Last Name: "Doe"
   - Bio: "Full-stack developer passionate about Python"
   - Tech Stack: "Python/Django, JavaScript/React"
   - GitHub Username: "johndoe"
   - Website: "https://johndoe.com"
2. Click "Save Changes"
3. Check sidebar for updated info

**Expected Result**:
- Green success message
- All fields updated
- Sidebar shows:
  - Full name as "John Doe"
  - Bio displayed
  - Tech Stack shown
  - GitHub link is clickable
  - Website link is clickable
- Refreshing page preserves all data

**Status**: ✓ Pass / ✗ Fail

---

### TEST 12: Bio Character Limit
**Objective**: Verify bio has 500 character limit

**Steps**:
1. On profile page, find "Bio" field
2. Try to enter text with >500 characters
3. Click "Save Changes"

**Expected Result**:
- Either form field cuts off at 500 chars
- OR error message appears
- Bio is not saved with >500 characters
- Sidebar shows bio is limited to 500 chars

**Status**: ✓ Pass / ✗ Fail

---

### TEST 13: Invalid URL Format
**Objective**: Verify website URL validation

**Steps**:
1. On profile page, find "Personal Website" field
2. Enter: "notavalidurl" (without https://)
3. Click "Save Changes"
4. Observe error

**Expected Result**:
- Red error message appears
- Website field not updated
- Can correct and retry with proper URL

**Status**: ✓ Pass / ✗ Fail

---

### TEST 14: Valid Website URLs
**Objective**: Verify various valid URL formats work

**Steps**:
1. Test URL: "https://example.com"
2. Save and verify
3. Test URL: "http://example.com"
4. Save and verify
5. Check sidebar shows clickable link

**Expected Result**:
- Both https:// and http:// accepted
- URLs saved and displayed in sidebar
- Sidebar links are clickable and open in new tab

**Status**: ✓ Pass / ✗ Fail

---

### TEST 15: GitHub Link Integration
**Objective**: Verify GitHub username creates proper link

**Steps**:
1. On profile page, enter GitHub username: "torvalds"
2. Click "Save Changes"
3. Check sidebar for GitHub section
4. Click the GitHub link

**Expected Result**:
- Success message
- Sidebar shows "@torvalds" as link
- Clicking opens "https://github.com/torvalds" in new tab

**Status**: ✓ Pass / ✗ Fail

---

### TEST 16: Cancel Button
**Objective**: Verify cancel button discards unsaved changes

**Steps**:
1. On profile page, make changes (e.g., change username)
2. Click "Cancel" button instead of saving
3. Observe result

**Expected Result**:
- Changes are discarded
- Redirected to home page
- No success or error message
- Profile data unchanged when checking again

**Status**: ✓ Pass / ✗ Fail

---

### TEST 17: Login Required for Profile
**Objective**: Verify unauthenticated users can't access profile

**Steps**:
1. Log out from any account
2. Try to navigate directly to `/accounts/profile/`
3. Observe redirect

**Expected Result**:
- Redirected to login page
- URL shows: `/accounts/login/?next=/accounts/profile/`
- Can log in and then access profile

**Status**: ✓ Pass / ✗ Fail

---

### TEST 18: Dark Mode Display
**Objective**: Verify profile page works in dark mode

**Steps**:
1. Toggle dark mode (theme button in navbar)
2. Navigate to `/accounts/profile/`
3. Observe styling and readability

**Expected Result**:
- All text is readable
- Form fields have appropriate dark mode colors
- Buttons are visible and styled correctly
- Avatar has good contrast

**Status**: ✓ Pass / ✗ Fail

---

### TEST 19: Form Error Display
**Objective**: Verify form errors display correctly

**Steps**:
1. Try to save with invalid data (e.g., invalid email)
2. Observe error messages

**Expected Result**:
- Red error boxes appear above relevant fields
- Warning icons display on invalid fields
- Error messages are clear and descriptive
- Form doesn't submit

**Status**: ✓ Pass / ✗ Fail

---

### TEST 20: Avatar Updates Across Site
**Objective**: Verify avatar changes reflect everywhere

**Steps**:
1. Upload new avatar
2. Navigate to home page
3. Go back to profile
4. Check navbar on another page
5. Navigate back to profile page

**Expected Result**:
- New avatar displays consistently in navbar
- Avatar visible in profile sidebar
- No broken image links
- Avatar persists across page navigation

**Status**: ✓ Pass / ✗ Fail

---

## Summary Report

Total Test Cases: 20

| Test | Status | Notes |
|------|--------|-------|
| 1. Avatar Display (No Image) | ✓ / ✗ | |
| 2. Avatar Clickability | ✓ / ✗ | |
| 3. Profile Page Layout | ✓ / ✗ | |
| 4. Mobile Responsive | ✓ / ✗ | |
| 5. Update Username | ✓ / ✗ | |
| 6. Update Email | ✓ / ✗ | |
| 7. Duplicate Email Validation | ✓ / ✗ | |
| 8. Duplicate Username Validation | ✓ / ✗ | |
| 9. Upload Avatar Image | ✓ / ✗ | |
| 10. Non-Image File Rejection | ✓ / ✗ | |
| 11. Update All Fields | ✓ / ✗ | |
| 12. Bio Character Limit | ✓ / ✗ | |
| 13. Invalid URL Validation | ✓ / ✗ | |
| 14. Valid Website URLs | ✓ / ✗ | |
| 15. GitHub Link Integration | ✓ / ✗ | |
| 16. Cancel Button | ✓ / ✗ | |
| 17. Login Required | ✓ / ✗ | |
| 18. Dark Mode Display | ✓ / ✗ | |
| 19. Form Error Display | ✓ / ✗ | |
| 20. Avatar Updates Across Site | ✓ / ✗ | |

**Overall Status**: ___ / 20 passed

---

## Known Issues / Notes

(Document any issues found during testing here)

