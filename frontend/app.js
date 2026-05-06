const API_BASE = "https://curly-space-broccoli-45gpp4wjw572qq7-8000.app.github.dev/api";

let authToken = null; 

const loginError = document.getElementById("login-error");
const loginButton = document.getElementById("login-button");
const usernameInput = document.getElementById("login-username");
const passwordInput = document.getElementById("login-password");

async function login() {
    loginError.classList.add("hidden");
    loginError.textContent = ""; 

    const username = usernameInput.value.trim();
    const password = passwordInput.value;

    try {
        const response = await fetch(`${API_BASE}/auth/login/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password})
        });

        if (!response.ok) {
            loginError.textContent = "Login fehlgeschlagen. Prüfe Benutzername/Passwort.";
            loginError.classList.remove("hidden");
            return; 
        }

        const data = await response.json();
        authToken = data.token;

        console.log("Eingeloggt, Token:", authToken);
        alert("Login erfolgreich, Token in Konsole."); 
    } catch (err) {
        loginError.textContent = "Netzwerkfehler beim Login.";
        loginError.classList.remove("hidden");
    }
}

loginButton.addEventListener("click", login); 