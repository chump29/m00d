import { type ChangeEvent, type JSX, useEffect, useState } from "react"

import { HandThumbDownIcon, HandThumbUpIcon } from "@heroicons/react/24/solid"
import { type ApexOptions } from "apexcharts"
import { format } from "date-fns"
import { toZonedTime } from "date-fns-tz"
import Chart from "react-apexcharts"

import { log } from "../shared"

const API_URL: string = import.meta.env.VITE_API_URL || ""

interface IMood {
  date: string // * NOTE: Converted to DateField in API
  id?: number
  mood: number
}

const Display = (): JSX.Element => {
  const [mood, setMood] = useState<number>(3)
  const [moods, setMoods] = useState<IMood[]>([])

  const handleChange = (event: ChangeEvent<HTMLInputElement>): void => {
    setMood(parseInt(event.target.value, 10))
  }

  const handleClick = async (): Promise<void> => {
    await fetch(`${API_URL}/api/add/`, {
      body: JSON.stringify({
        date: format(new Date(toZonedTime(new Date(), Intl.DateTimeFormat().resolvedOptions().timeZone)), "yyyy-MM-dd"),
        mood: mood
      } as IMood),
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      }
    })
      .then((response: Response) => {
        if (!response.ok) {
          throw new Error(`Status: ${response.status}`)
        }
        return response.json()
      })
      .then((mood: IMood) => {
        if (!mood) {
          log(mood)
          throw new Error("Error adding mood")
        }
        getMoods()
      })
      .catch(log)
  }

  const options: ApexOptions = {
    chart: {
      dropShadow: {
        enabled: true
      },
      toolbar: {
        show: false
      }
    },
    markers: {
      colors: [
        "#48b3af"
      ]
    },
    tooltip: {
      shared: false,
      theme: "dark",
      marker: {
        show: false
      },
      x: {
        show: false
      },
      y: {
        formatter: (num: number): string => {
          return getTitle(num)
        }
      }
    },
    xaxis: {
      labels: {
        rotateAlways: true,
        formatter: (val: string): string => {
          if (!val) {
            return ""
          }
          const parts = val.split("-")
          return `${parts[1]}/${parts[2]}/${parts[0]}`
        },
        style: {
          colors: "#f6ff99"
        }
      },
      title: {
        offsetY: -35,
        text: "DATE",
        style: {
          color: "#d599e3",
          fontFamily: "Righteous",
          fontSize: "16px"
        }
      }
    },
    yaxis: {
      max: 5,
      min: 1,
      labels: {
        style: {
          colors: "#f6ff99"
        }
      },
      title: {
        offsetX: -5,
        text: "MOOD",
        style: {
          color: "#d599e3",
          fontFamily: "Righteous",
          fontSize: "16px"
        }
      }
    }
  }

  const series: ApexOptions["series"] = [
    {
      color: "#f6ff99",
      data: moods,
      name: "Mood",
      parsing: {
        x: "date",
        y: "mood"
      }
    }
  ]

  const getTitle = (num: number): string => {
    switch (num) {
      case 1:
        return "Sad 😢"
      case 2:
        return "Kind of sad 🙁"
      case 3:
        return "Neutral 😐"
      case 4:
        return "Kind of happy 🙂"
      case 5:
        return "Happy 😀"
      default:
        return "Unknown"
    }
  }

  const getMoods = async (): Promise<void> => {
    fetch(`${API_URL}/api/get`)
      .then((response: Response) => {
        if (!response.ok) {
          throw new Error(`Status: ${response.status}`)
        }
        return response.json()
      })
      .then((moods: IMood[]) => {
        setMoods(moods)
      })
      .catch(log)
  }

  // biome-ignore lint/correctness/useExhaustiveDependencies(getMoods): not a dependency
  useEffect(() => {
    getMoods()
  }, [])

  return (
    <>
      <div className="text-center mt-10">
        <div className="mb-10 text-3xl font-bold text-yellow" data-testid="date">
          {format(new Date(toZonedTime(new Date(), Intl.DateTimeFormat().resolvedOptions().timeZone)), "PPPP")}
        </div>
        <div className="mb-1 text-2xl text-green2 font-bold">Current mood:</div>
        <div className="mb-5 text-xs italic text-green1 font-bold">
          (1 = Sad &nbsp; &mdash; &nbsp; 3 = Neutral &nbsp; &mdash; &nbsp; 5 = Happy)
        </div>
        <form className="inline" data-testid="form">
          <HandThumbDownIcon className="size-7 inline mr-5 text-yellow" />
          {[
            ...Array.from(
              {
                length: 5
              },
              (_, i) => i + 1
            )
          ].map((i: number) => (
            <span className="inline" key={i}>
              <label className="mr-1 font-bold text-yellow" htmlFor={`mood${i}`}>
                {i}
              </label>
              <input
                checked={mood === i}
                className="mr-5 cursor-pointer accent-purple"
                id={`mood${i}`}
                name="mood"
                onChange={handleChange}
                title={getTitle(i)}
                type="radio"
                value={i}
              />
            </span>
          ))}
          <HandThumbUpIcon className="size-7 inline text-yellow" />
          <div className="mt-5">
            <button
              className="rounded-lg border border-yellow px-2 py-1 cursor-pointer bg-blue font-bold font-title text-green2"
              onClick={handleClick}
              title="Submit Mood"
              type="button">
              Submit Mood ╰┈➤
            </button>
          </div>
        </form>
      </div>
      <div className="mt-10 text-center mx-10" data-testid="chart">
        {moods?.length ? (
          <div>
            <span className="text-xs float-right italic font-bold mr-5 top-5 relative text-yellow">Scroll to zoom</span>
            <Chart height={300} options={options} series={series} type="line" />
          </div>
        ) : (
          <span className="italic rounded-lg border p-2">No mood data to show</span>
        )}
      </div>
    </>
  )
}

export default Display
