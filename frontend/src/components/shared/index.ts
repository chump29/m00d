// biome-ignore lint/suspicious/noExplicitAny: can be any type
// biome-ignore lint/nursery/useExplicitType: can be any type
export const log = (obj: any): void => {
  const d = new Date()
  console.error(
    `%c[${d.getHours().toString().padStart(2, "0")}:${d.getMinutes().toString().padStart(2, "0")}:${d.getSeconds().toString().padStart(2, "0")}] %c${obj}`,
    "color: white; font-weight: bold;",
    "color: red;"
  )
}
