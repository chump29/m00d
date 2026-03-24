import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import removeAttributes from "rollup-plugin-jsx-remove-attributes"
import version from "vite-plugin-package-version"
import simpleHtml from "vite-plugin-simple-html"
import webFontDownload from "vite-plugin-webfont-dl"
import { defineConfig } from "vitest/config"

export default defineConfig({
  build: {
    chunkSizeWarningLimit: 750,
    rolldownOptions: {
      output: {
        codeSplitting: {
          groups: [
            {
              name: "vendor",
              test: /node_modules/
            }
          ]
        }
      }
    }
  },
  plugins: [
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
    webFontDownload(
      [
        "https://fonts.googleapis.com/css2?family=Righteous&display=swap"
      ],
      {
        assetsSubfolder: "fonts",
        injectAsStyleTag: false
      }
    ),
    version()
  ],
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: "./src/setup.ts",
    silent: true,
    coverage: {
      enabled: true,
      reporter: [
        "text"
      ]
    },
    include: [
      "./src/**/*.test.tsx"
    ],
    reporters: [
      [
        "verbose",
        {
          summary: true
        }
      ]
    ]
  }
})
