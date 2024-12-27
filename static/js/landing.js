document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card-holder .card');
    let currentIndex = 0;
    let swipeInterval;

    function switchCard() {
        // Remove 'active' class from the current card
        cards[currentIndex].classList.remove('active');

        // Move to the next card
        currentIndex = (currentIndex + 1) % cards.length;

        // Add 'active' class to the next card
        cards[currentIndex].classList.add('active');
    }

    function startSwiping() {
        swipeInterval = setInterval(switchCard, 3000); // 3seconds
    }

    function stopSwiping() {
        clearInterval(swipeInterval);
    }

    // Start the automatic swipe
    startSwiping();

    // Pause the swipe on hover
    const cardHolder = document.querySelector('.card-holder');
    cardHolder.addEventListener('mouseover', stopSwiping);
    cardHolder.addEventListener('mouseout', startSwiping);
});
