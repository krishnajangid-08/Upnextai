document.addEventListener("DOMContentLoaded", () => {
  const reloadTargets = document.querySelectorAll("[data-trigger-reload]");

  reloadTargets.forEach(target => {
    const destination =
      target.dataset.reloadTarget || target.getAttribute("href") || window.location.origin;

    const navigate = () => {
      try {
        window.location.assign(destination);
      } catch (err) {
        window.location.href = destination;
      }
    };

    const reloadSite = event => {
      event.preventDefault();
      if (document && document.body) {
        document.body.classList.add("page-reload-anim");
      }
      setTimeout(navigate, 180);
    };

    target.addEventListener("click", reloadSite);
    target.addEventListener("keydown", event => {
      if (event.key === "Enter" || event.key === " ") {
        reloadSite(event);
      }
    });
  });
});
