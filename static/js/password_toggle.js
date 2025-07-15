// Скрипт для смены видимости пароля / Script to change password visibility
document.addEventListener('DOMContentLoaded', function() {
    const togglePassword = (button) => {
        const wrapper = button.closest('.password-wrapper');
        if (!wrapper) {
            console.error('No password wrapper found');
            return;
        }

        // Ищем input внутри wrapper / Looking for input inside wrapper
        const input = wrapper.querySelector(
            'input[type="password"], input[type="text"]');
        if (!input) {
            console.error('No input field found');
            return;
        }

        const icon = button.querySelector('i');
        if (!icon) {
            console.error('No icon found');
            return;
        }

        // Переключаем тип input / Switching the input type
        input.type = input.type === 'password' ? 'text' : 'password';

        // Переключаем иконки
        icon.classList.toggle('fa-eye');
        icon.classList.toggle('fa-eye-slash');
    };

    // Обработчик для всех кнопок переключения пароля / Handler for all
    // password toggle buttons
    document.querySelectorAll('.password-toggle').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            togglePassword(button);
        });
    });
});
