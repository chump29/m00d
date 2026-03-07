import { StrictMode } from "react"

import { createRoot } from "react-dom/client"

import Display from "./components/display"

const api_url: string = import.meta.env.VITE_API_URL || ""

const getVersion = (version: string): string => {
  return version.length ? `v${version}` : "N/A"
}

const frontend: HTMLElement | null = document.getElementById("frontend")
if (frontend) {
  frontend.innerText = getVersion(import.meta.env.PACKAGE_VERSION)
}

const obj: HTMLElement | null = document.getElementById("backend")
fetch(`${api_url}/api/version`, {
  method: "GET",
  signal: AbortSignal.timeout(3000)
})
  .then((response: Response) => {
    if (!response.ok) {
      throw new Error(`Status: ${response.status}`)
    }
    return response.text()
  })
  .then((text: string) => {
    if (!text.length) {
      throw new Error("Invalid response")
    }
    if (obj) {
      obj.innerText = getVersion(text.replaceAll('"', ""))
    }
  })
  .catch((e: Error) => {
    console.error(e)
    if (obj) {
      obj.innerText = "N/A"
    }
  })

const root: HTMLElement | null = document.getElementById("root")
if (import.meta.env.DEV) {
  if (root) {
    createRoot(root).render(<Display />)
  }
} else {
  if (root) {
    createRoot(root).render(
      <StrictMode>
        <Display />
      </StrictMode>
    )
  }
}
