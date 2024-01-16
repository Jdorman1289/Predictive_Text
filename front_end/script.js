const get_suggested_word = (promptWords) => {
  fetch("http://127.0.0.1:8000/suggest/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: `${promptWords}` }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.querySelector(
        "#suggested_word"
      ).innerText = `Suggested Word: ${data.next_word}`;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

setInterval(() => {
  let promptWords = document.querySelector("#wordPrompt").value;
  get_suggested_word(promptWords);
}, 3000);
