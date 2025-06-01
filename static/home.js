document.addEventListener("DOMContentLoaded", (event) => {
  const socket = io();
  const messageInput = document.getElementById("message");
  const chatLog = document.getElementById("chat-log");
  const logoutButton = document.getElementById("logoutButton");
  const sendMessageButton = document.getElementById("sendMessageButton");
  const Gotocreate = document.getElementById("Gotocreate");
  const sns = document.getElementById("sns");
  const setting = document.getElementById("setting");

  socket.on("connect", () => {
    socket.emit("join", "main_room");
  });

  socket.on("message", (msg) => {
    const messageElement = document.createElement("div");
    messageElement.textContent = msg;
    chatLog.appendChild(messageElement);
  });

  function sendMessage() {
    const msg = messageInput.value;
    socket.send(msg);
    messageInput.value = "";
  }

  sendMessageButton.addEventListener("click", sendMessage);

  logoutButton.addEventListener("click", () => {
    fetch("/user/logout", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.msg);
        window.location.href = "/index";
      })
      .catch((error) => console.error("Error:", error));
  });

  Gotocreate.addEventListener("click", () => {
    window.location.href = "/create";
  });

  sns.addEventListener("click", () => {
    window.location.href = "/view";
  });

  setting.addEventListener("click", () => {
    window.location.href = "/setting";
  });
});
