// Basic Presentation Logic
document.addEventListener('DOMContentLoaded', () => {
    let currentSlideIndex = 1;
    const totalSlides = 12;

    const progressBar = document.getElementById('progressBar');
    
    // Function to show a specific slide
    function showSlide(n) {
        // Clamp value between 1 and totalSlides
        if (n < 1) n = 1;
        if (n > totalSlides) n = totalSlides;

        currentSlideIndex = n;

        // Remove 'active' class from all slides
        const slides = document.querySelectorAll('.slide');
        slides.forEach(slide => slide.classList.remove('active'));

        // Add 'active' class to current slide
        const currentSlide = document.getElementById(`slide-${currentSlideIndex}`);
        if (currentSlide) {
            currentSlide.classList.add('active');
        }

        // Update progress bar
        const progressPercentage = (currentSlideIndex / totalSlides) * 100;
        progressBar.style.width = `${progressPercentage}%`;
    }

    // Initialize first slide
    showSlide(currentSlideIndex);

    // Global navigation functions
    window.nextSlide = function() {
        if (currentSlideIndex < totalSlides) {
            showSlide(currentSlideIndex + 1);
        }
    };

    window.prevSlide = function() {
        if (currentSlideIndex > 1) {
            showSlide(currentSlideIndex - 1);
        }
    };

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
            window.nextSlide();
        } else if (e.key === 'ArrowLeft') {
            window.prevSlide();
        }
    });

    console.log("Presentation loaded successfully. Use Arrow Keys to navigate.");
});
