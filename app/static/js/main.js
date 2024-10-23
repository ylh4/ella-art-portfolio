document.addEventListener('DOMContentLoaded', function() {
    // Rating system
    const stars = document.querySelectorAll('.star');
    const averageRating = document.getElementById('average-rating');

    stars.forEach(star => {
        star.addEventListener('click', function() {
            const value = this.getAttribute('data-value');
            const artworkId = this.parentElement.getAttribute('data-artwork-id');
            
            // TODO: Send rating to server via AJAX
            console.log(`Artwork ${artworkId} rated ${value} stars`);

            // Update UI
            updateStars(value);
        });
    });

    function updateStars(value) {
        stars.forEach(star => {
            if (star.getAttribute('data-value') <= value) {
                star.classList.add('active');
            } else {
                star.classList.remove('active');
            }
        });
    }

    // Comment system
    const commentText = document.getElementById('comment-text');
    const submitComment = document.getElementById('submit-comment');

    if (submitComment) {
        submitComment.addEventListener('click', function() {
            const comment = commentText.value;
            // TODO: Send comment to server via AJAX
            console.log(`New comment: ${comment}`);
            commentText.value = '';
        });
    }
});
