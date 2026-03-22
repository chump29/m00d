# <img src="./frontend/public/m00d.png" title="m00d" alt="m00d logo" style="vertical-align: middle;"> m00d

> - Mood tracker

---

### 📷 Screenshot <!-- markdownlint-disable-line MD001 -->

<img src="./images/screenshot.png" title="Screenshot" alt="Screenshot">

---

### 🔀 Docker Compose Flow

```mermaid
flowchart LR
frontend@{shape: rounded, label: "m00d-frontend:80"}
frontendPort@{shape: rounded, label: "http://localhost:92"}
backend@{shape: rounded, label: "m00d-backend:5558"}
backendPort@{shape: rounded, label: "http://localhost:5558"}
frontend-->frontendPort
backend-->backendPort
```

---

### 🛠️ Building

```bash
./build.sh
```

---

### ℹ️ Documentation

- [Frontend](./frontend/README.md "Frontend")
- [Backend](./backend/README.md "Backend")
