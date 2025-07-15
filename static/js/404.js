// Скрипт для ошибки 404 / Script for 404 error
document.addEventListener('DOMContentLoaded', function() {
    const darkenOverlay = document.querySelector('.darken-overlay');
    const whisperSound = document.getElementById('whisper-sound');
    const ringSound = document.getElementById('ring-sound');
    const staticSound = document.getElementById('static-sound');

    // Фоновый статический шум / Background static noise
    staticSound.volume = 0.2;
    staticSound.play().catch(e => console.log(
        'Автовоспроизведение звука заблокировано'));

    // Параметры мерцания / Flicker parameters
    const flickerParams = {
        minDelay: 3000,
        maxDelay: 7000,
        minDuration: 300,
        maxDuration: 500,
        minIntensity: 0.6,
        maxIntensity: 1
    };

    // Плавное мерцание / Smooth flickering
    function gentleFlicker() {
        // Случайные параметры для текущего мерцания / Random parameters
        // for current flicker
        const duration = randomBetween(flickerParams.minDuration,
            flickerParams.maxDuration);
        const intensity = randomBetween(flickerParams.minIntensity,
            flickerParams.maxIntensity);

        // Плавное появление затемнения / Smooth appearance of dimming
        darkenOverlay.style.backgroundColor = `rgba(0, 0, 0, ${intensity})`;
        darkenOverlay.style.transitionDuration = `${duration/2}ms`;

        // Случайный звук с 30% вероятностью / Random sound with 30%
        // probability
        if (Math.random() < 0.3) {
            playRandomSound();
        }

        // Плавное исчезновение затемнения / Smooth fading of darkening
        setTimeout(() => {
            darkenOverlay.style.backgroundColor = 'rgba(0, 0, 0, 0)';
            darkenOverlay.style.transitionDuration = `${duration/2}ms`;

            // Следующее мерцание через случайный интервал / Next blink at
            // random interval
            const nextFlicker = randomBetween(flickerParams.minDelay,
                flickerParams.maxDelay);
            setTimeout(gentleFlicker, nextFlicker);
        }, duration);
    }

    // Воспроизведение случайного звука / Play random sound
    function playRandomSound() {
        const sounds = [whisperSound, ringSound];
        const randomSound = sounds[Math.floor(Math.random() * sounds.length)];
        randomSound.currentTime = 0;
        randomSound.volume = randomBetween(0.3, 0.7);
        randomSound.play().catch(e => console.log(
            'Автовоспроизведение звука заблокировано'));
    }

    // Вспомогательная функция для случайных значений в диапазоне / Helper
    // function for random values in a range
    function randomBetween(min, max) {
        return Math.random() * (max - min) + min;
    }

    // Начальное мерцание через 1 секунду / Initial flicker after 1 second
    setTimeout(gentleFlicker, 1000);
});
