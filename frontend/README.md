# <img src="./public/m00d.png" title="m00d" alt="m00d logo" width="64" height="64"> m00d (Frontend)

> - Mood tracker

---

### 🏗️ Architecture <!-- markdownlint-disable-line MD001 -->

#### Docker Compose Flow:

```mermaid
flowchart LR
ui@{shape: rounded, label: "UI"}
uiPort@{shape: rounded, label: "http://localhost:92"}
ui-->uiPort
```

---

#### React Component Hierarchy:

```mermaid
flowchart TD
index(index.html)
main(src/main.tsx)
display(src/components/display/index.tsx)
index-->main-->display
port@{shape: brace, label: "&nbsp; Nginx exposes port 80"}
```

---

### 🛠️ Environment Management

#### Node.js ([n](https://github.com/tj/n "n") manager):

|     📋 Task      |     🔧 Command     |
|:----------------:|:------------------:|
| Manage Versions  |      `sudo n`      |
| Install Specific | `sudo n [version]` |

#### NPM ([pnpm](https://github.com/pnpm/pnpm "pnpm") manager):

|   📋 Task    |          🔧 Command           |
|:------------:|:-----------------------------:|
|    Enable    |    `corepack enable pnpm`     |
|     Use      |  `corepack use pnpm@latest`   |
| Use Specific | `corepack use pnpm@[version]` |
|    Update    |         `corepack up`         |

### 📦 Dependency Management

#### Installation & Removal:

|        📋 Task         |               🔧 Command (Full)                |        🔧 Command (Short)         |
|:----------------------:|:----------------------------------------------:|:---------------------------------:|
|      Install DEV       |                 `pnpm install`                 |             `pnpm i`              |
|      Install PROD      |             `pnpm install --prod`              |            `pnpm i -P`            |
|     Add dependency     |   `pnpm add --save-prod [package][@version]`   |  `pnpm add [package][@version]`   |
|   Add devDependency    |   `pnpm add --save-dev [package][@version]`    | `pnpm add -D [package][@version]` |
| Add optionalDependency | `pnpm add --save-optional [package][@version]` | `pnpm add -O [package][@version]` |
|   Add peerDependency   |   `pnpm add --save-peer [package][@version]`   |              &mdash;              |
|       Add Global       |    `pnpm add --global [package][@version]`     | `pnpm add -g [package][@version]` |
|   Remove Dependency    |            `pnpm remove [package]`             |        `pnpm rm [package]`        |

#### Maintenance & Quality:

|     📋 Task     |    🔧 Command (Full)    | 🔧 Command (Short)  |
|:---------------:|:-----------------------:|:-------------------:|
|  Check Updates  |     `pnpm outdated`     |       &mdash;       |
|   Update All    |      `pnpm update`      |      `pnpm up`      |
| Update Specific | `pnpm update [package]` | `pnpm up [package]` |
| Security Audit  |      `pnpm audit`       |       &mdash;       |
|   Run Script    |   `pnpm run [script]`   |   `pnpm [script]`   |
|      List       |       `pnpm list`       |      `pnpm ls`      |
|   List Extra    |   `pnpm list --long`    |      `pnpm ll`      |
|    Hierarchy    |  `pnpm why [package]`   |       &mdash;       |

### 🧪 Development

#### Scripts:

|       📜 Script        |      🔧 Command       |
|:----------------------:|:---------------------:|
|     Lint All (DEV)     |    `pnpm run lint`    |
|     Lint All (CI)      |  `pnpm run lint:ci`   |
|       Lint Biome       | `pnpm run lint:biome` |
|        Lint CSS        |  `pnpm run lint:css`  |
|       Lint HTML        | `pnpm run lint:html`  |
| Run Tests (Hot Reload) |  `pnpm run test:dev`  |
|     Run Tests (CI)     |    `pnpm run test`    |
|       Build DEV        | `pnpm run build:dev`  |
|       Build PROD       |   `pnpm run build`    |

#### Docker Deployment:

|   📋 Task   |  🔧 Command   |
|:-----------:|:-------------:|
|    Full     | `./build.sh`  |
| Docker Only | `./docker.sh` |

---

### 🛰️ Git & CI/CD

- **Pre-Commit:** Staged files are automatically linted and tested
- **Github Actions:** Lints, tests, builds, and pushes multi-architecture images to repository
  - latest
    - amd64
    - arm64
