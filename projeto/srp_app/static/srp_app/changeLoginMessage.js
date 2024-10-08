window.onload = () => {
    const url = new URL(window.location.href);

    if (url.href.includes("admin/login")) {
        const form = document.querySelector('form');
        const patternDiv = form.closest('div');
        const spans = patternDiv.querySelectorAll('span');
        
        spans.forEach(span => {
            span.classList.remove("block");
        });

        spans[0].innerHTML = "Seja bem-vindo(a) ao";
    }
}