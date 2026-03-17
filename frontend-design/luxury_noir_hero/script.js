document.addEventListener('DOMContentLoaded', () => {
    // Add visible class to body to trigger CSS animations
    setTimeout(() => {
        document.body.classList.add('visible');
    }, 100);

    // Parallax effect on mouse move
    document.addEventListener('mousemove', (e) => {
        const x = e.clientX / window.innerWidth - 0.5;
        const y = e.clientY / window.innerHeight - 0.5;

        const img = document.querySelector('img');
        if (img) {
            img.style.transform = `scale(1.1) translate(${x * 20}px, ${y * 20}px)`;
        }
    });

    // Logo hover interaction
    const logo = document.querySelector('.logo');
    logo.addEventListener('mouseover', () => {
        logo.style.letterSpacing = '0.4em';
        logo.style.transition = '0.5s cubic-bezier(0.19, 1, 0.22, 1)';
    });
    logo.addEventListener('mouseout', () => {
        logo.style.letterSpacing = '0.2em';
    });
});