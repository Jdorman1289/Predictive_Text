let typingTimer;
const doneTypingInterval = 200; // ms

const inputField = document.querySelector("#wordPrompt");
const suggestionsContainer = document.querySelector("#suggestions");

inputField.addEventListener('input', function() {
    clearTimeout(typingTimer);
    if (inputField.value) {
        typingTimer = setTimeout(getSuggestions, doneTypingInterval);
    } else {
        suggestionsContainer.innerHTML = '';
    }
});

function getSuggestions() {
    const promptWords = inputField.value.trim();
    fetch("http://127.0.0.1:8000/suggest/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: promptWords })
    })
    .then(response => response.json())
    .then(data => {
        suggestionsContainer.innerHTML = '';
        if (data.suggestions && data.suggestions.length > 0) {
            data.suggestions.forEach(suggestion => {
                const suggestionBtn = document.createElement('button');
                suggestionBtn.classList.add('suggestion-btn');
                suggestionBtn.textContent = suggestion;
                suggestionBtn.addEventListener('click', () => {
                    inputField.value += ' ' + suggestion;
                    inputField.value = inputField.value.trim();
                    getSuggestions(); // Trigger suggestions update after selection
                });
                suggestionsContainer.appendChild(suggestionBtn);
            });
        } else {
            suggestionsContainer.textContent = 'No suggestions available';
        }
    })
    .catch(error => console.error('Error:', error));
}
