const createForm = document.getElementById("createForm");

createForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(createForm);
  fetch("/setting/send_headimg", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.msg);
    })
    .catch((error) => console.error("Error:", error));
});
