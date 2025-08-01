// Скрипт для обратного отсчёта времени до разблокировки аккаунта / Script for
// countdown to account unblocking
document.addEventListener('DOMContentLoaded', function() {
    const hoursElement = document.getElementById('countdown-hours');
    const minutesElement = document.getElementById('countdown-minutes');
    const secondsElement = document.getElementById('countdown-seconds');
    const lockoutBox = document.querySelector('.lockout-box');

    // Если блок блокировки не найден - прекращаем выполнение скрипта / If the
    // blocking block is not found, stop executing the script
    if (!lockoutBox) return;

    const unlockTimestamp = parseInt(
        lockoutBox.getAttribute('data-unlock-time'));

    // Проверка на валидность полученного времени разблокировки / Checking the
    // validity of the received unlock time
    if (isNaN(unlockTimestamp) || unlockTimestamp <= 0) {
        // Если время невалидно, устанавливаем блокировку на 1 час от текущего
        // момента / If the time is invalid, set the blocking for 1 hour
        // from the current moment
        const now = Math.floor(Date.now() / 1000);
        startCountdown(now + 3600);
        return;
    }

    // Запускаем отсчёт до указанного момента / Start the countdown to the
    // specified moment
    startCountdown(unlockTimestamp);

    function startCountdown(unlockTimestamp) {
        // Функция обновления таймера (вызывается каждую секунду) / Timer
        // update function (called every second)
        function updateCountdown() {
            const now = Math.floor(Date.now() / 1000);
            let diff = unlockTimestamp - now;

            // Если время вышло - перенаправляем на главную / If time is up,
            // redirect to the main page
            if (diff <= 0) {
                window.location.href = '/';
                return;
            }

            const hours = Math.floor(diff / 3600);
            diff %= 3600;
            const minutes = Math.floor(diff / 60);
            const seconds = diff % 60;

            hoursElement.textContent = hours.toString().padStart(2, '0');
            minutesElement.textContent = minutes.toString().padStart(2, '0');
            secondsElement.textContent = seconds.toString().padStart(2, '0');
        }

        updateCountdown();
        setInterval(updateCountdown, 1000);
    }
});
