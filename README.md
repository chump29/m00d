# <img src="./frontend/public/m00d.png" title="m00d" alt="m00d logo" width="64" height="64"> m00d

> - Mood tracker

---

### Docker Compose Flow: <!-- markdownlint-disable-line MD001 -->

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

### To build all images

```bash
./build.sh
```

---

### Additional documentation available

- [Frontend](./frontend/README.md "Frontend")
- [Backend](./backend/README.md "Backend")
