function updateDateTime() {
    const now = new Date();

    const options = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
    };

    const datetimeElement = document.getElementById("datetime");

    if (datetimeElement) {
        datetimeElement.textContent = now.toLocaleString("en-IN", options);
    }
}

updateDateTime();
setInterval(updateDateTime, 1000);