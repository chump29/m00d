import { render, screen } from "@testing-library/react"

import Display from "."

beforeEach(() => {
  render(<Display />)
})

describe("Display", () => {
  it("should display date", () => {
    expect(screen.queryByTestId("date"), "Date not found").toBeInTheDocument()
  })
})
