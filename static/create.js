const createForm = document.getElementById("createForm");

createForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(createForm);
  fetch("/create/send_content", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.msg);
    })
    .catch((error) => console.error("Error:", error));
});
