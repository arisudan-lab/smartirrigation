document.addEventListener("DOMContentLoaded", () => {
  const progressValue = document.querySelector(".progress-value");
  const liquid = document.querySelector(".liquid");

  eel.expose(setWaterLevel);
  function setWaterLevel(percentage) {
    percentage = Math.max(0, Math.min(100, percentage)); // clamp 0–100
    progressValue.textContent = percentage + "%";
    liquid.style.height = percentage + "%";
  }
});

