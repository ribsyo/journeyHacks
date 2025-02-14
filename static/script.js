document.addEventListener("DOMContentLoaded", function () {
    const tacoContainer = document.querySelector(".taco-container");

    function createTaco() {
        const taco = document.createElement("div");
        taco.classList.add("taco");
        taco.textContent = "🌮";

        // Random position (0% to 100% of screen width)
        taco.style.left = Math.random() * 100 + "vw";

        // Random animation duration (3s - 6s)
        taco.style.animationDuration = Math.random() * 3 + 3 + "s";

        // Append taco to the container
        tacoContainer.appendChild(taco);

        // Remove taco after it falls
        setTimeout(() => {
            taco.remove();
        }, 6000);
    }

    // Keep adding tacos every 300ms
    setInterval(createTaco, 300);
});