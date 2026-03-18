import { render, screen } from "@testing-library/react"

import Display from "."

beforeEach(() => {
  render(<Display />)
})

describe("Display", () => {
  it("should display date", () => {
    expect(screen.queryByTestId("date"), "Date not found").toBeInTheDocument()
  })

  it("should display form", () => {
    expect(screen.queryByTestId("form"), "Form not found").toBeInTheDocument()
  })

  it("should display chart", () => {
    expect(screen.queryByTestId("chart"), "Chart not found").toBeInTheDocument()
  })
})
