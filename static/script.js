document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const reg_mailForm = document.getElementById("sendCodeBtn");
  const regForm = document.getElementById("regForm");
  const sendMailcodeForm = document.getElementById("send_mailcodeForm");
  const updatePwdForm = document.getElementById("updatePwdForm");

  loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(loginForm);
    fetch("/user/login", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.msg);
        if (data.success) {
          window.location.href = "/home";
        }
      })
      .catch((error) => console.error("Error:", error));
  });

  reg_mailForm.addEventListener("click", (e) => {
    e.preventDefault();
    const formData = new FormData(regForm);
    fetch("/user/reg", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.msg);
      })
      .catch((error) => console.error("Error:", error));
  });

  regForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(regForm);
    fetch("/user/mail_check", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.msg);
      })
      .catch((error) => console.error("Error:", error));
  });

  sendMailcodeForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(sendMailcodeForm);
    fetch("/user/send_mailcode", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.msg);
        if (data.success) {
          document.getElementById("send_mailcodeForm").style.display = "none";
          document.getElementById("updatePasswordSection").style.display =
            "block";
        }
      })
      .catch((error) => console.error("Error:", error));
  });

  updatePwdForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(updatePwdForm);
    fetch("/user/update_password", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.msg);
      })
      .catch((error) => console.error("Error:", error));
  });
});

function showSection(sectionId) {
  const sections = ["loginSection", "registerSection", "forgotPasswordSection"];
  sections.forEach((id) => {
    document.getElementById(id).style.display = "none";
  });
  document.getElementById(sectionId).style.display = "block";
  if (sectionId === "forgotPasswordSection") {
    document.getElementById("send_mailcodeForm").style.display = "block";
    document.getElementById("updatePasswordSection").style.display = "none";
  }
}
