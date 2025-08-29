document.addEventListener('DOMContentLoaded', function () {
    const togglePassword = (button) => {
        const wrapper = button.closest('.password-wrapper');
        const input = wrapper.querySelector('input[type="password"], input[type="text"]');
        const icon = button.querySelector('i');
        if (input && icon) {
            input.type = input.type === 'password' ? 'text' : 'password';
            icon.classList.toggle('fa-eye');
            icon.classList.toggle('fa-eye-slash');
        }
    };
    document.querySelectorAll('.password-toggle').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            togglePassword(button);
        });
    });
});
