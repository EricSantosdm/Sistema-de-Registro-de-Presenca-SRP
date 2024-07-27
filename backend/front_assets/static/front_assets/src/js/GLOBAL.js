const GLOBAL = {
  url: new URL(window.location),

  removeSidebar: () => {
    const sidebar = document.querySelector("#sidebar");
    sidebar.remove();
  },
};
