document.addEventListener("DOMContentLoaded", () => {
    console.log("Dashboard JS loaded.");
    // Beispiel: Aktualisiere Statistiken alle 10 Sekunden
    setInterval(() => {
        fetch("/stats")
            .then(response => response.text())
            .then(html => {
                console.log("Stats updated.");
                // Hier könnte man den HTML-Content dynamisch aktualisieren
            })
            .catch(err => console.error(err));
    }, 10000);
});
