// Скрипт для главной страницы / Script for the main page
document.addEventListener('DOMContentLoaded', () => {
    // Кэширование DOM-элементов / Caching DOM elements
    const elements = {
        terminalLines: document.querySelectorAll('.terminal-line'),
        clickSound: document.getElementById('clickSound'),
        secretSound: document.getElementById('secretSound'),
        screamSound: document.getElementById('screamSound'),
        statusDots: document.querySelector('.status-dots'),
        secretMessage: document.querySelector('.secret-message'),
        darkenOverlay: document.getElementById('darkenOverlay'),
        screamerVideo: document.getElementById('screamerVideo'),
        hiddenLetters: document.querySelectorAll('.hidden-letter'),
    };

    // Константы / Constants
    const TARGET_SEQUENCE = ['I', 'T', "'", 'S', 'M', 'E'];
    const ANIMATION_DELAY = 500;
    const SCREAMER_DELAY = 60000;

    let currentSequence = [];
    let isAnimating = false;

    // Мигание троеточия / Flashing ellipses
    setInterval(() => {
        elements.statusDots.style.visibility = 
        elements.statusDots.style.visibility === 
        'hidden' ? 'visible' : 'hidden';}, 500);

    // Обработчик кликов / Click handler
    const handleLetterClick = (event) => {
        if (isAnimating) return;

        const clickedLetter = event.target.getAttribute('data-letter');
        const expectedLetter = TARGET_SEQUENCE[currentSequence.length];

        if (clickedLetter === expectedLetter) {
            processCorrectLetter(event.target);
        } else if (currentSequence.length > 0) {
            resetSequence();
        }
    };

    // Обработка правильной буквы / Processing the correct letter
    const processCorrectLetter = (element) => {
        currentSequence.push(element.getAttribute('data-letter'));
        element.classList.add('active');
        elements.clickSound.currentTime = 0;
        elements.clickSound.play();

        if (currentSequence.length === TARGET_SEQUENCE.length) {
            activateSecretSequence();
        }
    };

    // Активация секретной последовательности / Activating the secret sequence
    const activateSecretSequence = () => {
        isAnimating = true;

        setTimeout(() => {
            elements.secretSound.play();
            elements.statusDots.style.display = 'none';
            elements.secretMessage.style.display = 'inline';
            elements.secretMessage.style.animation = 'fadeIn 2s forwards';

            // Эффект затемнения / Darkening effect
            animateDarkenOverlay();

            // Запуск скримера с задержкой / Delayed start of screamer
            setTimeout(activateScreamer, SCREAMER_DELAY);
        }, ANIMATION_DELAY);
    };

    // Анимация затемнения / Fade out animation
    const animateDarkenOverlay = () => {
        elements.darkenOverlay.style.backgroundColor = 'rgba(0, 0, 0, 0)';
        setTimeout(() => {
            elements.darkenOverlay.style.backgroundColor =
                'rgba(0, 0, 0, 1)';
        }, 10);
    };

    // Активация скримера / Activating the screamer
    const activateScreamer = () => {
        elements.screamerVideo.style.display = 'block';
        elements.screamerVideo.play();
        elements.screamSound.currentTime = 0;
        elements.screamSound.play();

        elements.screamerVideo.onended = () => {
            elements.screamerVideo.style.display = 'none';
            elements.darkenOverlay.style.backgroundColor =
                'rgba(0, 0, 0, 0)';
            isAnimating = false;
        };
    };

    // Сброс последовательности / Reset sequence
    const resetSequence = () => {
        isAnimating = true;
        setTimeout(() => {
            document.querySelectorAll('.hidden-letter.active').forEach(el => {
                el.classList.remove('active');
            });
            currentSequence = [];
            isAnimating = false;
        }, ANIMATION_DELAY);
    };

    // Назначение обработчиков событий / Assigning event handlers
    elements.hiddenLetters.forEach(letter => {
        letter.addEventListener('click', handleLetterClick);
    });
});
