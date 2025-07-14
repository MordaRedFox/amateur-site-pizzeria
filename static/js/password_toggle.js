document.addEventListener('DOMContentLoaded', function() {
    const togglePassword = (button) => {
        const wrapper = button.closest('.password-wrapper');
        if (!wrapper) {
            console.error('No password wrapper found');
            return;
        }

        // Ищем input внутри wrapper, учитывая, что Django может обернуть его
        // в дополнительные элементы
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

        // Переключаем тип input
        input.type = input.type === 'password' ? 'text' : 'password';

        // Переключаем иконки
        icon.classList.toggle('fa-eye');
        icon.classList.toggle('fa-eye-slash');
    };

    // Обработчик для всех кнопок переключения пароля
    document.querySelectorAll('.password-toggle').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            togglePassword(button);
        });
    });
});
