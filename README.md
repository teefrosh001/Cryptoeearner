# CryptoEarner Website

Modern cryptocurrency investment platform prototype.

## Files
- index.html (Home)
- plans.html
- login.html
- register.html
- dashboard.html
- admin.html
- And more (about.html, faq.html etc. can be duplicated similarly)

## How to Launch / View

1. **On Desktop**:
   - Open any HTML file directly in Chrome/Firefox (double-click).
   - Best viewed with `index.html`.

2. **On Mobile Phone**:
   - Copy the entire `cryptoeearner` folder to your phone (via USB, cloud, email, etc.).
   - Install a free file manager app (like CX File Explorer or Total Commander).
   - Navigate to the folder and open `index.html` with your browser (Chrome recommended).
   - Or use a local server app like "Simple HTTP Server" or Termux:
     ```
     # In Termux (Android):
     pkg install python
     cd /path/to/cryptoeearner
     python -m http.server 8080
     ```
     Then open http://localhost:8080 in browser.

3. **Demo Flows**:
   - Home → Plans
   - Login with any credentials (demo auto logs in)
   - Admin: Footer "Admin Login" button or login page. Username: `makeit001` / Password: `Makemoney@12`

**Backend Server (Python Flask)**: Run `python server.py` for a full backend with real API endpoints. Data is managed server-side (in-memory - resets on restart). This makes admin actions (approve deposits, update balances) truly functional across pages.

Enjoy the dark blue & gold modern crypto theme!
