// Скрипт для ошибки 404
document.addEventListener('DOMContentLoaded', function() {
    const darkenOverlay = document.querySelector('.darken-overlay');
    const whisperSound = document.getElementById('whisper-sound');
    const ringSound = document.getElementById('ring-sound');
    const staticSound = document.getElementById('static-sound');

    // Фоновый статический шум
    staticSound.volume = 0.2;
    staticSound.play().catch(e => console.log(
        'Автовоспроизведение звука заблокировано'));

    // Параметры мерцания
    const flickerParams = {
        minDelay: 3000,    // Минимальная задержка между мерцаниями (мс)
        maxDelay: 7000,    // Максимальная задержка
        minDuration: 300,  // Минимальная длительность мерцания
        maxDuration: 500,  // Максимальная длительность
        minIntensity: 0.6, // Минимальная интенсивность затемнения
        maxIntensity: 1    // Максимальная интенсивность
    };

    // Плавное мерцание
    function gentleFlicker() {
        // Случайные параметры для текущего мерцания
        const duration = randomBetween(flickerParams.minDuration,
            flickerParams.maxDuration);
        const intensity = randomBetween(flickerParams.minIntensity,
            flickerParams.maxIntensity);

        // Плавное появление затемнения
        darkenOverlay.style.backgroundColor = `rgba(0, 0, 0, ${intensity})`;
        darkenOverlay.style.transitionDuration = `${duration/2}ms`;

        // Случайный звук с 30% вероятностью
        if (Math.random() < 0.3) {
            playRandomSound();
        }

        // Плавное исчезновение затемнения
        setTimeout(() => {
            darkenOverlay.style.backgroundColor = 'rgba(0, 0, 0, 0)';
            darkenOverlay.style.transitionDuration = `${duration/2}ms`;

            // Следующее мерцание через случайный интервал
            const nextFlicker = randomBetween(flickerParams.minDelay,
                flickerParams.maxDelay);
            setTimeout(gentleFlicker, nextFlicker);
        }, duration);
    }

    // Воспроизведение случайного звука
    function playRandomSound() {
        const sounds = [whisperSound, ringSound];
        const randomSound = sounds[Math.floor(Math.random() * sounds.length)];
        randomSound.currentTime = 0;
        randomSound.volume = randomBetween(0.3, 0.7);
        randomSound.play().catch(e => console.log(
            'Автовоспроизведение звука заблокировано'));
    }

    // Вспомогательная функция для случайных значений в диапазоне
    function randomBetween(min, max) {
        return Math.random() * (max - min) + min;
    }

    // Начальное мерцание через 1 секунду
    setTimeout(gentleFlicker, 1000);
});
