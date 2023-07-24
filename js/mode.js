// Function to toggle dark mode and store the state in local storage
function toggleDarkMode() {
    const body = document.body;
    const toggleContainer = document.querySelector(".toggle-container");
    const currentMode = toggleContainer.getAttribute("data-mode");
  
    if (currentMode === "light") {
      toggleContainer.setAttribute("data-mode", "dark");
      body.setAttribute("data-mode", "dark");
      localStorage.setItem("darkMode", "true"); // Store dark mode state
    } else {
      toggleContainer.setAttribute("data-mode", "light");
      body.setAttribute("data-mode", "light");
      localStorage.setItem("darkMode", "false"); // Store light mode state
    }
  }
  
  // Function to load the dark mode state from local storage
  function loadDarkMode() {
    const darkMode = localStorage.getItem("darkMode");
    if (darkMode === "true") {
      const body = document.body;
      const toggleContainer = document.querySelector(".toggle-container");
      toggleContainer.setAttribute("data-mode", "dark");
      body.setAttribute("data-mode", "dark");
    }
  }
  
  // Load the dark mode state when the page is loaded
  document.addEventListener("DOMContentLoaded", function () {
    loadDarkMode();
  
    // Trigger a custom event to notify other pages about the dark mode state
    const darkModeEvent = new CustomEvent("darkModeStateChanged", {
      detail: { darkMode: localStorage.getItem("darkMode") === "true" },
    });
    window.dispatchEvent(darkModeEvent);
  });
  