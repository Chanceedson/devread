from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rating', 'content', 'tech_stack_used', 'is_recommended']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-primary focus:border-transparent',
                'placeholder': 'Give your review a title',
            }),
            'rating': forms.RadioSelect(choices=[
                (1, '1 Star'),
                (2, '2 Stars'),
                (3, '3 Stars'),
                (4, '4 Stars'),
                (5, '5 Stars'),
            ]),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-primary focus:border-transparent',
                'placeholder': 'Share your thoughts about this book...',
                'rows': 6,
            }),
            'tech_stack_used': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-primary focus:border-transparent',
                'placeholder': 'e.g., "Used this to learn TypeScript"',
            }),
            'is_recommended': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-primary',
            }),
        }
        labels = {
            'title': 'Review Title',
            'rating': 'Rating',
            'content': 'Your Review',
            'tech_stack_used': 'Tech Stack Used (Optional)',
            'is_recommended': 'I recommend this book',
        }
