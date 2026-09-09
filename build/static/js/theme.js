(function () {
  const storageKey = "theme";
  const root = document.documentElement;
  const button = document.querySelector("[data-theme-toggle]");

  function systemTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function currentTheme() {
    return root.getAttribute("data-theme") || systemTheme();
  }

  function apply(theme, persist) {
    root.setAttribute("data-theme", theme);
    if (button) {
      const next = theme === "dark" ? "light" : "dark";
      button.setAttribute("aria-label", "Switch to " + next + " mode");
      button.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
    }
    if (persist) {
      try {
        localStorage.setItem(storageKey, theme);
      } catch (_error) {
        // Ignore private-mode storage failures.
      }
    }
  }

  apply(currentTheme(), false);

  if (button) {
    button.addEventListener("click", function () {
      apply(currentTheme() === "dark" ? "light" : "dark", true);
    });
  }

  const media = window.matchMedia("(prefers-color-scheme: dark)");
  media.addEventListener("change", function (event) {
    try {
      if (localStorage.getItem(storageKey)) {
        return;
      }
    } catch (_error) {
      return;
    }
    apply(event.matches ? "dark" : "light", false);
  });
})();
