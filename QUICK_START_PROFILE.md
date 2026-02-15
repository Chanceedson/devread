# Quick Start: User Avatar & Profile Settings

## What Changed?

### Navbar (when logged in)
- **Before**: "Profile" button (non-functional)
- **After**: Avatar badge showing user's first letter or profile picture
  - Circular, 40x40px
  - Purple-to-pink gradient
  - Clickable - navigates to profile page

### New Page: `/accounts/profile/`
- Complete profile management interface
- View and edit all profile information
- Upload and manage avatar image
- Responsive design (works on mobile and desktop)

## Quick Actions

### 1. View Your Profile
```
Step 1: Log in to your account
Step 2: Click the avatar circle in the top right navbar
Step 3: You're now on the profile settings page
```

### 2. Update Your Avatar
```
Step 1: Go to Profile Settings
Step 2: Scroll to "Profile Picture" field
Step 3: Click "Choose File" and select an image
Step 4: Click "Save Changes"
Step 5: Avatar updates in navbar immediately
```

### 3. Update Basic Information
```
On Profile Settings page, Basic Information section:
- Username (required)
- Email (required)
- First Name (optional)
- Last Name (optional)
- Bio (optional, max 500 characters)
```

### 4. Add Professional Information
```
On Profile Settings page, Professional Information section:
- Tech Stack: e.g., "Python/Django"
- GitHub Username: Your GitHub username
- Personal Website: Your portfolio or personal site URL
```

## Features Explained

### Avatar Display
- **With Image**: Shows your uploaded profile picture
- **Without Image**: Shows the first letter of your username in a gradient circle

### Avatar Storage
- Uploaded images saved to: `/media/avatars/`
- Supported formats: JPG, PNG, GIF, WebP, etc.
- Recommended: Square images (200x200px or larger)

### Profile Sidebar
Shows quick info about your account:
- Current avatar
- Username
- Email
- Tech stack (if set)
- GitHub link (if set)
- Website link (if set)
- Member since date

### Validation
All fields have real-time validation:
- **Email**: Must be unique and valid format
- **Username**: Must be unique
- **Website**: Must include https:// or http://
- **Avatar**: Must be an image file
- **Bio**: Maximum 500 characters

## Error Handling

### If you see an error:
1. **"This email is already in use."**
   - Email is taken by another account
   - Use a different email address

2. **"This username is already taken."**
   - Username is taken by another account
   - Choose a different username

3. **Invalid file error**
   - Make sure you're uploading an image file (JPG, PNG, etc.)
   - Don't upload non-image files

4. **"Invalid URL" or similar**
   - Website URL must start with https:// or http://
   - Example: https://myportfolio.com

## Dark Mode Support
- All pages automatically adapt to dark mode
- Avatar and profile work in both light and dark themes
- Your settings are preserved regardless of theme

## Mobile Usage
- Profile page is fully responsive
- Works perfectly on phones and tablets
- Touch-friendly buttons and inputs

## URL Reference
- View/Edit Profile: `/accounts/profile/`
- Login: `/accounts/login/`
- Register: `/accounts/register/`
- Logout: Navigate via navbar

## Troubleshooting

### Avatar doesn't show in navbar
- Refresh the page (Ctrl+R or Cmd+R)
- Make sure you're logged in
- Check browser's image loading is enabled

### Changes not saved
- Make sure form validates (check for error messages)
- Click "Save Changes" button (not "Cancel")
- Check internet connection

### Can't upload image
- File must be an actual image (JPG, PNG, GIF, etc.)
- Try a smaller file size
- Try a different image format

### Forgot something?
- All fields except Username and Email are optional
- You can leave blank and come back to update later
- Click "Cancel" to discard changes

## File Sizes
- Avatar image: No strict limit, but keep under 5MB
- Bio text: Maximum 500 characters
- GitHub username: Maximum 100 characters
- Website URL: Maximum 100 characters
- Tech stack: Maximum 100 characters
