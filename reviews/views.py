from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from books.models import Book
from .models import Review
from .forms import ReviewForm


def review_list(request):
    """
    Display a list of all reviews with their details.
    """
    reviews = Review.objects.all().select_related('user', 'book').order_by('-created_at')
    
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/review_list.html', context)


@login_required(login_url='login')
def add_review(request, slug: str):
    """
    Allow authenticated users to add a review for a book.
    If they already have a review, redirect them to edit it instead.
    """
    book = get_object_or_404(Book, slug=slug)
    
    # Check if user already reviewed this book
    existing_review = Review.objects.filter(book=book, user=request.user).first()
    if existing_review:
        messages.info(request, 'You can only review a book once. Click "Edit" to update your review.')
        return redirect('edit_review', review_id=existing_review.id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been posted successfully!')
            return redirect('book_detail', slug=book.slug)
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'book': book,
        'is_editing': False,
    }
    return render(request, 'reviews/add_review.html', context)


@login_required(login_url='login')
def edit_review(request, review_id: int):
    """
    Allow authenticated users to edit their own review.
    """
    review = get_object_or_404(Review, pk=review_id)
    
    # Check if the user owns this review
    if review.user != request.user:
        messages.error(request, 'You can only edit your own reviews.')
        return HttpResponseForbidden('You cannot edit this review.')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated successfully!')
            return redirect('book_detail', slug=review.book.slug)
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form': form,
        'book': review.book,
        'is_editing': True,
        'review': review,
    }
    return render(request, 'reviews/add_review.html', context)
