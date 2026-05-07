## CORS and GitHub Codespaces (May 2026)

- Added `django-cors-headers` to the project: 
    - `corseheaders` in `INSTALLED_APPS`
    - `corsheaders.middlewar.CorsMiddleware` at the top of `MIDDLEWARE`
- Configured CORS to allow the frontend origin from GitHub Codspaces: 
    - `CORS_ALLOWED_ORIGINS = ["https://<frontend-url>-5500.app.github.dev"]`
- Added a publid `/api/ping/` endpoint (`AllowAny`) as a simple health and CORS test. 
- In GitHub Codespaces, cross-origin `fetch` calls from port 5500 to port 8000 are sometimes redirected (HTTP 302) to `https://github.dev/pf-singin` by the Codespaces tunnel. 
- These 302 responses come from GitHub, not from Django, and do not include any `Access-Controle-Allow-Origin` header, wich causes CORS errors in the browser. 
- This is an infrastructure limitation of the Codespaces proxy, not a bug in the Django CORS setup. 
- Expectations: on local machine (e.g. `http://localhost:8000` and `http://localhost:5500`) the same CORS configuration should work as documented.  