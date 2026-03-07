import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import removeAttributes from "rollup-plugin-jsx-remove-attributes"
import { ViteImageOptimizer as imageOptimizer } from "vite-plugin-image-optimizer"
import version from "vite-plugin-package-version"
import simpleHtml from "vite-plugin-simple-html"
import webFontDownload from "vite-plugin-webfont-dl"
import { defineConfig } from "vitest/config"

export default defineConfig({
  build: {
    chunkSizeWarningLimit: 750
  },
  plugins: [
    imageOptimizer(),
    react(),
    removeAttributes({
      usage: "vite"
    }),
    simpleHtml({
      minify: true,
      inject: {
        data: {
          title: "m00d"
        }
      }
    }),
    tailwindcss(),
    webFontDownload(["https://fonts.googleapis.com/css2?family=Righteous&display=swap"], {
      assetsSubfolder: "fonts",
      injectAsStyleTag: false
    }),
    version()
  ],
  test: {
    environment: "jsdom",
    globals: true,
    include: ["./src/**/*.test.tsx"],
    reporters: [["verbose", { summary: true }]],
    setupFiles: "./src/setup.ts",
    silent: true
  }
})
