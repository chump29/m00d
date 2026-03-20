# <img src="../frontend/public/m00d.png" title="m00d" alt="m00d logo" style="vertical-align: middle;"> m00d (Backend)

> - Mood tracker

---

### 🏗️ Architecture <!-- markdownlint-disable-line MD001 -->

#### API Structure:

```mermaid
flowchart TD
api@{shape: rect, label: "/api"}
add[["`/add`"]]
%% delete[["`/delete/*[pk]*`"]]
get[["`/get`"]]
get_one[["`/get/*[pk]*`"]]
get_by_date[["`/get_by_date/*[date]*`"]]
update[["`/update/*[pk]*`"]]
version[["`/version`"]]
api-->add
%% api-->delete
api-->get
api-->get_one
api-->get_by_date
api-->update
api-->version
port@{shape: brace, label: "&nbsp; FastAPI exposes port 5558"}
```

---

### 🛠️ Environment Management

#### Python ([uv](https://github.com/astral-sh/uv "uv") manager):

|        📋 Task         |           🔧 Command            |
|:----------------------:|:-------------------------------:|
|         Update         |        `uv self update`         |
|        Install         |  `uv python install [version]`  |
|       Uninstall        | `uv python uninstall [version]` |
|          Pin           |    `uv python pin [version]`    |
| Create/Update Lockfile |            `uv lock`            |
|   Create/Update venv   |            `uv sync`            |
| Create/Update env venv |     `uv sync --extra [env]`     |
|   Installed Versions   |        `uv python list`         |

### 📦 Dependency Management

#### Installation & Removal:

|        📋 Task        |               🔧 Command               |
|:---------------------:|:--------------------------------------:|
|    Add Dependency     |           `uv add [package]`           |
|  Add env Dependency   |  `uv add --optional [env] [package]`   |
|   Remove Dependency   |         `uv remove [package]`          |
| Remove env Dependency | `uv remove --optional [env] [package]` |

#### Maintenance & Quality:

|     📋 Task      |               🔧 Command               |
|:----------------:|:--------------------------------------:|
|  Check Updates   |          `uv run pip-review`           |
|   Upgrade All    |          `uv lock --upgrade`           |
|       List       |             `uv pip list`              |
|    List Tree     |               `uv tree`                |
|    Hierarchy     |     `uv tree --package [package]`      |
| Hierarchy Parent | `uv tree --package [package] --invert` |
|   Clean Cache    |            `uv cache clean`            |

### 🧪 Development

#### Scripts:

| 📜 Script | 🔧 Command  |
|:---------:|:-----------:|
|   Lint    | `./lint.sh` |
|   Test    | `./test.sh` |

#### API Deployment:

| 📋 Task |            🔧 Command (Full)            | 🔧 Command (Short) |
|:-------:|:---------------------------------------:|:------------------:|
|   DEV   | `uv run fastapi dev api.py --port 5558` | `./api.py [port]`  |
|  PROD   | `uv run fastapi run api.py --port 5558` |      &mdash;       |

#### API Documentation:

|  📄 UI  |    🌐 URL    |
|:-------:|:------------:|
| Swagger | `/api/docs`  |
|  Redoc  | `/api/redoc` |

#### Docker Deployment:

|   📋 Task   |  🔧 Command   |
|:-----------:|:-------------:|
|    Full     | `./build.sh`  |
| Docker Only | `./docker.sh` |

#### Virtual Environment:

|    📜 Script    |         🔧 Command          |
|:---------------:|:---------------------------:|
|     Create      |          `uv venv`          |
| Create Specific |   `uv venv -p [version]`    |
|    Activate     | `source .venv/bin/activate` |
|   Deactivate    |        `deactivate`         |

---

### 🛰️ Git & CI/CD

- **Pre-Commit:** Staged files are automatically linted and tested
- **Github Actions:** Lints, tests, builds, and pushes multi-architecture images to repository
  - latest
    - amd64
    - arm64
