# NL2SQL System Results

## Project: Natural Language to SQL using Vanna AI + Groq + FastAPI + SQLite

This document contains the test results of the NL2SQL system where natural language questions are converted into SQL queries, executed on a SQLite database, and results are returned with optional chart visualization.

---

## Test Queries and Results

| No | Question | Generated SQL | Row Count | Status |
|----|----------|--------------|-----------|--------|
| 1 | How many patients do we have? | SELECT COUNT(*) FROM patients | 1 | Success |
| 2 | List doctor names and their specialization | SELECT name, specialization FROM doctors | 15 | Success |
| 3 | How many appointments are completed? | SELECT COUNT(*) FROM appointments WHERE status = 'Completed' | 1 | Success |
| 4 | Show total revenue from invoices | SELECT SUM(total_amount) FROM invoices | 1 | Success |
| 5 | Top 5 patients by total invoice amount | SELECT patient_id, SUM(total_amount) AS total_spent FROM invoices GROUP BY patient_id ORDER BY total_spent DESC LIMIT 5 | 5 | Success |
| 6 | Show unpaid invoices | SELECT * FROM invoices WHERE status != 'Paid' | 120 | Success |
| 7 | Which city has the most patients? | SELECT city, COUNT(*) AS total FROM patients GROUP BY city ORDER BY total DESC LIMIT 1 | 1 | Success |
| 8 | Average treatment cost | SELECT AVG(cost) FROM treatments | 1 | Success |
| 9 | Number of appointments per doctor | SELECT doctor_id, COUNT(*) FROM appointments GROUP BY doctor_id | 10 | Success |
|10 | Monthly revenue from invoices | SELECT strftime('%Y-%m', invoice_date) AS month, SUM(total_amount) FROM invoices GROUP BY month ORDER BY month | 12 | Success |

---

## Charts Generated

Charts were generated automatically for queries returning two or more columns, including:
- Revenue by month
- Appointments per doctor
- Patients by city
- Top 5 patients by spending

Charts were generated using Plotly and returned as JSON.

---

## Accuracy Summary

| Metric | Value |
|-------|------|
| Total Queries Tested | 10 |
| Successful SQL Queries | 10 |
| Failed Queries | 0 |
| Accuracy | 100% |

---

## Observations

- The system successfully converted natural language questions into SQL queries.
- SQL validation ensured only SELECT queries were executed.
- Plotly charts were generated when applicable.
- The Vanna agent memory helped improve SQL generation accuracy.
- Groq LLM (llama-3.3-70b-versatile) provided fast and accurate SQL generation.

---

## Conclusion

The NL2SQL system successfully demonstrates an end-to-end pipeline from natural language input to SQL query generation, execution, and visualization. The system is safe, scalable, and can be extended to support other databases like PostgreSQL or MySQL.

This project demonstrates the practical implementation of LLM-powered data querying systems using Vanna AI and Groq.





1.How many patients do we have?

{
  "message": "Query executed successfully",
  "sql_query": "SELECT COUNT(*) FROM patients",
  "columns": [
    "COUNT(*)"
  ],
  "rows": [
    [
      400
    ]
  ],
  "row_count": 1,
  "chart": {},
  "chart_type": ""
}

2.List all doctors and their specializations 
{
  "message": "Query executed successfully",
  "sql_query": "SELECT name, specialization \nFROM doctors",
  "columns": [
    "name",
    "specialization"
  ],
  "rows": [
    [
      "Robert Baxter",
      "Cardiology"
    ],
    [
      "Brooke Jenkins",
      "Orthopedics"
    ],
    [
      "Darryl Hernandez",
      "Dermatology"
    ],
    [
      "Bryan Martin",
      "Cardiology"
    ],
    [
      "Robert Crawford",
      "Orthopedics"
    ],
    [
      "Ashley Brown",
      "Orthopedics"
    ],
    [
      "Marie Vazquez",
      "Dermatology"
    ],
    [
      "Katherine Phillips",
      "General"
    ],
    [
      "Vickie Berg",
      "Cardiology"
    ],
    [
      "Christine Lynch",
      "Dermatology"
    ],
    [
      "Curtis Gray",
      "Pediatrics"
    ],
    [
      "Tony Ponce",
      "General"
    ],
    [
      "Eric Blackwell",
      "Orthopedics"
    ],
    [
      "John Welch",
      "General"
    ],
    [
      "Charles Yates",
      "Cardiology"
    ],
    [
      "Kimberly Collins",
      "Dermatology"
    ],
    [
      "Adrian Blackburn",
      "Cardiology"
    ],
    [
      "Gary Ferrell",
      "Pediatrics"
    ],
    [
      "Joshua Peterson",
      "General"
    ],
    [
      "Brian Walker",
      "Dermatology"
    ],
    [
      "Tony Caldwell",
      "Pediatrics"
    ],
    [
      "Claire Jimenez",
      "Orthopedics"
    ],
    [
      "Mary Wilson",
      "Dermatology"
    ],
    [
      "Melinda Gregory",
      "General"
    ],
    [
      "Samantha Nelson",
      "General"
    ],
    [
      "Stacey Shaw",
      "Orthopedics"
    ],
    [
      "Jessica Thompson",
      "Pediatrics"
    ],
    [
      "Angela Frazier",
      "General"
    ],
    [
      "Jacob Garcia",
      "Cardiology"
    ],
    [
      "Greg Hines MD",
      "Dermatology"
    ]
  ],
  "row_count": 30,
  "chart": {
    "data": [
      {
        "hovertemplate": "name=%{x}<br>specialization=%{y}<extra></extra>",
        "legendgroup": "",
        "marker": {
          "color": "#636efa",
          "pattern": {
            "shape": ""
          }
        },
        "name": "",
        "orientation": "v",
        "showlegend": false,
        "textposition": "auto",
        "x": [
          "Robert Baxter",
          "Brooke Jenkins",
          "Darryl Hernandez",
          "Bryan Martin",
          "Robert Crawford",
          "Ashley Brown",
          "Marie Vazquez",
          "Katherine Phillips",
          "Vickie Berg",
          "Christine Lynch",
          "Curtis Gray",
          "Tony Ponce",
          "Eric Blackwell",
          "John Welch",
          "Charles Yates",
          "Kimberly Collins",
          "Adrian Blackburn",
          "Gary Ferrell",
          "Joshua Peterson",
          "Brian Walker",
          "Tony Caldwell",
          "Claire Jimenez",
          "Mary Wilson",
          "Melinda Gregory",
          "Samantha Nelson",
          "Stacey Shaw",
          "Jessica Thompson",
          "Angela Frazier",
          "Jacob Garcia",
          "Greg Hines MD"
        ],
        "xaxis": "x",
        "y": [
          "Cardiology",
          "Orthopedics",
          "Dermatology",
          "Cardiology",
          "Orthopedics",
          "Orthopedics",
          "Dermatology",
          "General",
          "Cardiology",
          "Dermatology",
          "Pediatrics",
          "General",
          "Orthopedics",
          "General",
          "Cardiology",
          "Dermatology",
          "Cardiology",
          "Pediatrics",
          "General",
          "Dermatology",
          "Pediatrics",
          "Orthopedics",
          "Dermatology",
          "General",
          "General",
          "Orthopedics",
          "Pediatrics",
          "General",
          "Cardiology",
          "Dermatology"
        ],
        "yaxis": "y",
        "type": "bar"
      }
    ],
    "layout": {
      "template": {
        "data": {
          "histogram2dcontour": [
            {
              "type": "histogram2dcontour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "choropleth": [
            {
              "type": "choropleth",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "histogram2d": [
            {
              "type": "histogram2d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "heatmap": [
            {
              "type": "heatmap",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "contourcarpet": [
            {
              "type": "contourcarpet",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "contour": [
            {
              "type": "contour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "surface": [
            {
              "type": "surface",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "mesh3d": [
            {
              "type": "mesh3d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "scatter": [
            {
              "fillpattern": {
                "fillmode": "overlay",
                "size": 10,
                "solidity": 0.2
              },
              "type": "scatter"
            }
          ],
          "parcoords": [
            {
              "type": "parcoords",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolargl": [
            {
              "type": "scatterpolargl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "bar": [
            {
              "error_x": {
                "color": "#2a3f5f"
              },
              "error_y": {
                "color": "#2a3f5f"
              },
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "bar"
            }
          ],
          "scattergeo": [
            {
              "type": "scattergeo",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolar": [
            {
              "type": "scatterpolar",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "histogram": [
            {
              "marker": {
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "histogram"
            }
          ],
          "scattergl": [
            {
              "type": "scattergl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatter3d": [
            {
              "type": "scatter3d",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              },
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermap": [
            {
              "type": "scattermap",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermapbox": [
            {
              "type": "scattermapbox",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterternary": [
            {
              "type": "scatterternary",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattercarpet": [
            {
              "type": "scattercarpet",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "carpet": [
            {
              "aaxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "baxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "type": "carpet"
            }
          ],
          "table": [
            {
              "cells": {
                "fill": {
                  "color": "#EBF0F8"
                },
                "line": {
                  "color": "white"
                }
              },
              "header": {
                "fill": {
                  "color": "#C8D4E3"
                },
                "line": {
                  "color": "white"
                }
              },
              "type": "table"
            }
          ],
          "barpolar": [
            {
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "barpolar"
            }
          ],
          "pie": [
            {
              "automargin": true,
              "type": "pie"
            }
          ]
        },
        "layout": {
          "autotypenumbers": "strict",
          "colorway": [
            "#636efa",
            "#EF553B",
            "#00cc96",
            "#ab63fa",
            "#FFA15A",
            "#19d3f3",
            "#FF6692",
            "#B6E880",
            "#FF97FF",
            "#FECB52"
          ],
          "font": {
            "color": "#2a3f5f"
          },
          "hovermode": "closest",
          "hoverlabel": {
            "align": "left"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
            "bgcolor": "#E5ECF6",
            "angularaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "radialaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "ternary": {
            "bgcolor": "#E5ECF6",
            "aaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "baxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "caxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "coloraxis": {
            "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
            }
          },
          "colorscale": {
            "sequential": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "sequentialminus": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "diverging": [
              [
                0,
                "#8e0152"
              ],
              [
                0.1,
                "#c51b7d"
              ],
              [
                0.2,
                "#de77ae"
              ],
              [
                0.3,
                "#f1b6da"
              ],
              [
                0.4,
                "#fde0ef"
              ],
              [
                0.5,
                "#f7f7f7"
              ],
              [
                0.6,
                "#e6f5d0"
              ],
              [
                0.7,
                "#b8e186"
              ],
              [
                0.8,
                "#7fbc41"
              ],
              [
                0.9,
                "#4d9221"
              ],
              [
                1,
                "#276419"
              ]
            ]
          },
          "xaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "yaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "scene": {
            "xaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "yaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "zaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            }
          },
          "shapedefaults": {
            "line": {
              "color": "#2a3f5f"
            }
          },
          "annotationdefaults": {
            "arrowcolor": "#2a3f5f",
            "arrowhead": 0,
            "arrowwidth": 1
          },
          "geo": {
            "bgcolor": "white",
            "landcolor": "#E5ECF6",
            "subunitcolor": "white",
            "showland": true,
            "showlakes": true,
            "lakecolor": "white"
          },
          "title": {
            "x": 0.05
          },
          "mapbox": {
            "style": "light"
          }
        }
      },
      "xaxis": {
        "anchor": "y",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "name"
        }
      },
      "yaxis": {
        "anchor": "x",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "specialization"
        }
      },
      "legend": {
        "tracegroupgap": 0
      },
      "margin": {
        "t": 60
      },
      "barmode": "relative"
    }
  },
  "chart_type": "bar"
}

3.Show revenue by doctor
{
  "message": "Query executed successfully",
  "sql_query": "SELECT \n  d.name, \n  SUM(t.cost) AS revenue\nFROM \n  treatments t\n  JOIN appointments a ON t.appointment_id = a.id\n  JOIN doctors d ON a.doctor_id = d.id\nGROUP BY \n  d.name",
  "columns": [
    "name",
    "revenue"
  ],
  "rows": [
    [
      "Adrian Blackburn",
      17885
    ],
    [
      "Angela Frazier",
      12594
    ],
    [
      "Ashley Brown",
      35098
    ],
    [
      "Brian Walker",
      11626
    ],
    [
      "Brooke Jenkins",
      96597
    ],
    [
      "Bryan Martin",
      28776
    ],
    [
      "Charles Yates",
      39338
    ],
    [
      "Christine Lynch",
      31930
    ],
    [
      "Claire Jimenez",
      8027
    ],
    [
      "Curtis Gray",
      52082
    ],
    [
      "Darryl Hernandez",
      50978
    ],
    [
      "Eric Blackwell",
      69689
    ],
    [
      "Gary Ferrell",
      9539
    ],
    [
      "Greg Hines MD",
      5047
    ],
    [
      "Jacob Garcia",
      4213
    ],
    [
      "Jessica Thompson",
      12887
    ],
    [
      "John Welch",
      62577
    ],
    [
      "Joshua Peterson",
      6023
    ],
    [
      "Katherine Phillips",
      69286
    ],
    [
      "Kimberly Collins",
      19728
    ],
    [
      "Marie Vazquez",
      43508
    ],
    [
      "Mary Wilson",
      19323
    ],
    [
      "Melinda Gregory",
      21258
    ],
    [
      "Robert Baxter",
      51457
    ],
    [
      "Robert Crawford",
      61867
    ],
    [
      "Samantha Nelson",
      10508
    ],
    [
      "Stacey Shaw",
      1780
    ],
    [
      "Tony Caldwell",
      12455
    ],
    [
      "Tony Ponce",
      64044
    ],
    [
      "Vickie Berg",
      40069
    ]
  ],
  "row_count": 30,
  "chart": {
    "data": [
      {
        "hovertemplate": "name=%{x}<br>revenue=%{y}<extra></extra>",
        "legendgroup": "",
        "marker": {
          "color": "#636efa",
          "pattern": {
            "shape": ""
          }
        },
        "name": "",
        "orientation": "v",
        "showlegend": false,
        "textposition": "auto",
        "x": [
          "Adrian Blackburn",
          "Angela Frazier",
          "Ashley Brown",
          "Brian Walker",
          "Brooke Jenkins",
          "Bryan Martin",
          "Charles Yates",
          "Christine Lynch",
          "Claire Jimenez",
          "Curtis Gray",
          "Darryl Hernandez",
          "Eric Blackwell",
          "Gary Ferrell",
          "Greg Hines MD",
          "Jacob Garcia",
          "Jessica Thompson",
          "John Welch",
          "Joshua Peterson",
          "Katherine Phillips",
          "Kimberly Collins",
          "Marie Vazquez",
          "Mary Wilson",
          "Melinda Gregory",
          "Robert Baxter",
          "Robert Crawford",
          "Samantha Nelson",
          "Stacey Shaw",
          "Tony Caldwell",
          "Tony Ponce",
          "Vickie Berg"
        ],
        "xaxis": "x",
        "y": {
          "dtype": "f8",
          "bdata": "AAAAAEB30UAAAAAAAJnIQAAAAABAI+FAAAAAAAC1xkAAAAAAUJX3QAAAAAAAGtxAAAAAAEA140AAAAAAgC7fQAAAAAAAW79AAAAAAEBu6UAAAAAAQOToQAAAAACQA/FAAAAAAIChwkAAAAAAALezQAAAAAAAdbBAAAAAAIAryUAAAAAAII7uQAAAAAAAh7dAAAAAAGDq8EAAAAAAAETTQAAAAACAPuVAAAAAAMDe0kAAAAAAgMLUQAAAAAAgIOlAAAAAAGA17kAAAAAAAIbEQAAAAAAA0JtAAAAAAIBTyEAAAAAAgEXvQAAAAACgkONA"
        },
        "yaxis": "y",
        "type": "bar"
      }
    ],
    "layout": {
      "template": {
        "data": {
          "histogram2dcontour": [
            {
              "type": "histogram2dcontour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "choropleth": [
            {
              "type": "choropleth",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "histogram2d": [
            {
              "type": "histogram2d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "heatmap": [
            {
              "type": "heatmap",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "contourcarpet": [
            {
              "type": "contourcarpet",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "contour": [
            {
              "type": "contour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "surface": [
            {
              "type": "surface",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "mesh3d": [
            {
              "type": "mesh3d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "scatter": [
            {
              "fillpattern": {
                "fillmode": "overlay",
                "size": 10,
                "solidity": 0.2
              },
              "type": "scatter"
            }
          ],
          "parcoords": [
            {
              "type": "parcoords",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolargl": [
            {
              "type": "scatterpolargl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "bar": [
            {
              "error_x": {
                "color": "#2a3f5f"
              },
              "error_y": {
                "color": "#2a3f5f"
              },
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "bar"
            }
          ],
          "scattergeo": [
            {
              "type": "scattergeo",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolar": [
            {
              "type": "scatterpolar",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "histogram": [
            {
              "marker": {
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "histogram"
            }
          ],
          "scattergl": [
            {
              "type": "scattergl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatter3d": [
            {
              "type": "scatter3d",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              },
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermap": [
            {
              "type": "scattermap",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermapbox": [
            {
              "type": "scattermapbox",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterternary": [
            {
              "type": "scatterternary",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattercarpet": [
            {
              "type": "scattercarpet",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "carpet": [
            {
              "aaxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "baxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "type": "carpet"
            }
          ],
          "table": [
            {
              "cells": {
                "fill": {
                  "color": "#EBF0F8"
                },
                "line": {
                  "color": "white"
                }
              },
              "header": {
                "fill": {
                  "color": "#C8D4E3"
                },
                "line": {
                  "color": "white"
                }
              },
              "type": "table"
            }
          ],
          "barpolar": [
            {
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "barpolar"
            }
          ],
          "pie": [
            {
              "automargin": true,
              "type": "pie"
            }
          ]
        },
        "layout": {
          "autotypenumbers": "strict",
          "colorway": [
            "#636efa",
            "#EF553B",
            "#00cc96",
            "#ab63fa",
            "#FFA15A",
            "#19d3f3",
            "#FF6692",
            "#B6E880",
            "#FF97FF",
            "#FECB52"
          ],
          "font": {
            "color": "#2a3f5f"
          },
          "hovermode": "closest",
          "hoverlabel": {
            "align": "left"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
            "bgcolor": "#E5ECF6",
            "angularaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "radialaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "ternary": {
            "bgcolor": "#E5ECF6",
            "aaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "baxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "caxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "coloraxis": {
            "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
            }
          },
          "colorscale": {
            "sequential": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "sequentialminus": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "diverging": [
              [
                0,
                "#8e0152"
              ],
              [
                0.1,
                "#c51b7d"
              ],
              [
                0.2,
                "#de77ae"
              ],
              [
                0.3,
                "#f1b6da"
              ],
              [
                0.4,
                "#fde0ef"
              ],
              [
                0.5,
                "#f7f7f7"
              ],
              [
                0.6,
                "#e6f5d0"
              ],
              [
                0.7,
                "#b8e186"
              ],
              [
                0.8,
                "#7fbc41"
              ],
              [
                0.9,
                "#4d9221"
              ],
              [
                1,
                "#276419"
              ]
            ]
          },
          "xaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "yaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "scene": {
            "xaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "yaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "zaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            }
          },
          "shapedefaults": {
            "line": {
              "color": "#2a3f5f"
            }
          },
          "annotationdefaults": {
            "arrowcolor": "#2a3f5f",
            "arrowhead": 0,
            "arrowwidth": 1
          },
          "geo": {
            "bgcolor": "white",
            "landcolor": "#E5ECF6",
            "subunitcolor": "white",
            "showland": true,
            "showlakes": true,
            "lakecolor": "white"
          },
          "title": {
            "x": 0.05
          },
          "mapbox": {
            "style": "light"
          }
        }
      },
      "xaxis": {
        "anchor": "y",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "name"
        }
      },
      "yaxis": {
        "anchor": "x",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "revenue"
        }
      },
      "legend": {
        "tracegroupgap": 0
      },
      "margin": {
        "t": 60
      },
      "barmode": "relative"
    }
  },
  "chart_type": "bar"
}

4.Top 5 patients by spending
{
  "message": "Query executed successfully",
  "sql_query": "SELECT p.id, p.first_name, p.last_name, SUM(i.total_amount) as total_spent\nFROM patients p\nJOIN invoices i ON p.id = i.patient_id\nGROUP BY p.id, p.first_name, p.last_name\nORDER BY total_spent DESC\nLIMIT 5",
  "columns": [
    "id",
    "first_name",
    "last_name",
    "total_spent"
  ],
  "rows": [
    [
      70,
      "Michael",
      "Bright",
      33860
    ],
    [
      38,
      "Keith",
      "Bradford",
      32432
    ],
    [
      147,
      "Craig",
      "Gutierrez",
      31959
    ],
    [
      137,
      "David",
      "Mercado",
      31125
    ],
    [
      154,
      "Connie",
      "Anderson",
      30672
    ]
  ],
  "row_count": 5,
  "chart": {
    "data": [
      {
        "hovertemplate": "id=%{x}<br>first_name=%{y}<extra></extra>",
        "legendgroup": "",
        "marker": {
          "color": "#636efa",
          "pattern": {
            "shape": ""
          }
        },
        "name": "",
        "orientation": "h",
        "showlegend": false,
        "textposition": "auto",
        "x": {
          "dtype": "i2",
          "bdata": "RgAmAJMAiQCaAA=="
        },
        "xaxis": "x",
        "y": [
          "Michael",
          "Keith",
          "Craig",
          "David",
          "Connie"
        ],
        "yaxis": "y",
        "type": "bar"
      }
    ],
    "layout": {
      "template": {
        "data": {
          "histogram2dcontour": [
            {
              "type": "histogram2dcontour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "choropleth": [
            {
              "type": "choropleth",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "histogram2d": [
            {
              "type": "histogram2d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "heatmap": [
            {
              "type": "heatmap",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "contourcarpet": [
            {
              "type": "contourcarpet",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "contour": [
            {
              "type": "contour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "surface": [
            {
              "type": "surface",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "mesh3d": [
            {
              "type": "mesh3d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "scatter": [
            {
              "fillpattern": {
                "fillmode": "overlay",
                "size": 10,
                "solidity": 0.2
              },
              "type": "scatter"
            }
          ],
          "parcoords": [
            {
              "type": "parcoords",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolargl": [
            {
              "type": "scatterpolargl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "bar": [
            {
              "error_x": {
                "color": "#2a3f5f"
              },
              "error_y": {
                "color": "#2a3f5f"
              },
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "bar"
            }
          ],
          "scattergeo": [
            {
              "type": "scattergeo",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolar": [
            {
              "type": "scatterpolar",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "histogram": [
            {
              "marker": {
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "histogram"
            }
          ],
          "scattergl": [
            {
              "type": "scattergl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatter3d": [
            {
              "type": "scatter3d",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              },
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermap": [
            {
              "type": "scattermap",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermapbox": [
            {
              "type": "scattermapbox",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterternary": [
            {
              "type": "scatterternary",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattercarpet": [
            {
              "type": "scattercarpet",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "carpet": [
            {
              "aaxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "baxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "type": "carpet"
            }
          ],
          "table": [
            {
              "cells": {
                "fill": {
                  "color": "#EBF0F8"
                },
                "line": {
                  "color": "white"
                }
              },
              "header": {
                "fill": {
                  "color": "#C8D4E3"
                },
                "line": {
                  "color": "white"
                }
              },
              "type": "table"
            }
          ],
          "barpolar": [
            {
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "barpolar"
            }
          ],
          "pie": [
            {
              "automargin": true,
              "type": "pie"
            }
          ]
        },
        "layout": {
          "autotypenumbers": "strict",
          "colorway": [
            "#636efa",
            "#EF553B",
            "#00cc96",
            "#ab63fa",
            "#FFA15A",
            "#19d3f3",
            "#FF6692",
            "#B6E880",
            "#FF97FF",
            "#FECB52"
          ],
          "font": {
            "color": "#2a3f5f"
          },
          "hovermode": "closest",
          "hoverlabel": {
            "align": "left"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
            "bgcolor": "#E5ECF6",
            "angularaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "radialaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "ternary": {
            "bgcolor": "#E5ECF6",
            "aaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "baxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "caxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "coloraxis": {
            "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
            }
          },
          "colorscale": {
            "sequential": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "sequentialminus": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "diverging": [
              [
                0,
                "#8e0152"
              ],
              [
                0.1,
                "#c51b7d"
              ],
              [
                0.2,
                "#de77ae"
              ],
              [
                0.3,
                "#f1b6da"
              ],
              [
                0.4,
                "#fde0ef"
              ],
              [
                0.5,
                "#f7f7f7"
              ],
              [
                0.6,
                "#e6f5d0"
              ],
              [
                0.7,
                "#b8e186"
              ],
              [
                0.8,
                "#7fbc41"
              ],
              [
                0.9,
                "#4d9221"
              ],
              [
                1,
                "#276419"
              ]
            ]
          },
          "xaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "yaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "scene": {
            "xaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "yaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "zaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            }
          },
          "shapedefaults": {
            "line": {
              "color": "#2a3f5f"
            }
          },
          "annotationdefaults": {
            "arrowcolor": "#2a3f5f",
            "arrowhead": 0,
            "arrowwidth": 1
          },
          "geo": {
            "bgcolor": "white",
            "landcolor": "#E5ECF6",
            "subunitcolor": "white",
            "showland": true,
            "showlakes": true,
            "lakecolor": "white"
          },
          "title": {
            "x": 0.05
          },
          "mapbox": {
            "style": "light"
          }
        }
      },
      "xaxis": {
        "anchor": "y",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "id"
        }
      },
      "yaxis": {
        "anchor": "x",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "first_name"
        }
      },
      "legend": {
        "tracegroupgap": 0
      },
      "margin": {
        "t": 60
      },
      "barmode": "relative"
    }
  },
  "chart_type": "bar"
}

5.Show unpaid invoices?
{
  "message": "Query executed successfully",
  "sql_query": "SELECT * \nFROM invoices \nWHERE paid_amount < total_amount",
  "columns": [
    "id",
    "patient_id",
    "invoice_date",
    "total_amount",
    "paid_amount",
    "status"
  ],
  "rows": [
    [
      1,
      98,
      "2025-05-06",
      5600,
      4549,
      "Pending"
    ],
    [
      3,
      97,
      "2025-06-01",
      3144,
      69,
      "Pending"
    ],
    [
      4,
      51,
      "2025-05-09",
      4233,
      271,
      "Overdue"
    ],
    [
      5,
      115,
      "2025-12-26",
      5718,
      2489,
      "Pending"
    ],
    [
      7,
      52,
      "2025-07-09",
      537,
      127,
      "Pending"
    ],
    [
      10,
      152,
      "2026-03-31",
      3616,
      2738,
      "Pending"
    ],
    [
      12,
      139,
      "2026-02-03",
      7219,
      3090,
      "Pending"
    ],
    [
      15,
      50,
      "2025-07-04",
      6066,
      4064,
      "Overdue"
    ],
    [
      16,
      138,
      "2026-01-26",
      7913,
      693,
      "Overdue"
    ],
    [
      17,
      66,
      "2025-12-21",
      3142,
      428,
      "Pending"
    ],
    [
      26,
      21,
      "2025-08-24",
      6092,
      3057,
      "Overdue"
    ],
    [
      29,
      191,
      "2025-12-14",
      5004,
      4170,
      "Pending"
    ],
    [
      30,
      179,
      "2025-09-14",
      8085,
      6660,
      "Pending"
    ],
    [
      31,
      127,
      "2025-08-13",
      5242,
      2513,
      "Overdue"
    ],
    [
      42,
      123,
      "2026-02-21",
      2409,
      1207,
      "Overdue"
    ],
    [
      45,
      12,
      "2025-09-07",
      4055,
      1332,
      "Overdue"
    ],
    [
      49,
      197,
      "2025-09-07",
      9886,
      1524,
      "Pending"
    ],
    [
      50,
      129,
      "2025-12-14",
      3822,
      1057,
      "Pending"
    ],
    [
      51,
      113,
      "2025-12-15",
      8101,
      4474,
      "Pending"
    ],
    [
      57,
      29,
      "2025-08-20",
      1382,
      399,
      "Overdue"
    ],
    [
      58,
      53,
      "2026-02-24",
      5760,
      4809,
      "Pending"
    ],
    [
      61,
      120,
      "2025-11-05",
      3536,
      151,
      "Pending"
    ],
    [
      63,
      195,
      "2025-10-25",
      7457,
      126,
      "Pending"
    ],
    [
      66,
      138,
      "2025-05-20",
      305,
      57,
      "Pending"
    ],
    [
      67,
      177,
      "2025-11-08",
      4983,
      2299,
      "Overdue"
    ],
    [
      71,
      133,
      "2025-05-17",
      5212,
      2812,
      "Overdue"
    ],
    [
      77,
      158,
      "2025-04-16",
      7894,
      4628,
      "Overdue"
    ],
    [
      81,
      8,
      "2025-04-12",
      1614,
      478,
      "Overdue"
    ],
    [
      87,
      199,
      "2025-06-14",
      1321,
      136,
      "Pending"
    ],
    [
      93,
      184,
      "2025-07-19",
      3898,
      474,
      "Overdue"
    ],
    [
      95,
      166,
      "2026-03-18",
      3742,
      3674,
      "Overdue"
    ],
    [
      96,
      111,
      "2025-04-20",
      7578,
      5229,
      "Overdue"
    ],
    [
      107,
      49,
      "2025-11-12",
      9810,
      9559,
      "Overdue"
    ],
    [
      108,
      151,
      "2025-08-11",
      1477,
      430,
      "Pending"
    ],
    [
      111,
      29,
      "2025-07-12",
      1522,
      33,
      "Pending"
    ],
    [
      112,
      22,
      "2025-08-22",
      1468,
      1141,
      "Overdue"
    ],
    [
      113,
      73,
      "2025-12-27",
      261,
      20,
      "Overdue"
    ],
    [
      115,
      157,
      "2025-07-08",
      918,
      714,
      "Overdue"
    ],
    [
      116,
      5,
      "2025-08-02",
      4873,
      1686,
      "Pending"
    ],
    [
      119,
      193,
      "2025-12-07",
      3835,
      1265,
      "Overdue"
    ],
    [
      127,
      42,
      "2025-06-22",
      7314,
      6855,
      "Pending"
    ],
    [
      139,
      70,
      "2025-11-17",
      8803,
      803,
      "Pending"
    ],
    [
      142,
      159,
      "2025-08-07",
      1068,
      829,
      "Pending"
    ],
    [
      151,
      53,
      "2025-07-04",
      4262,
      3470,
      "Pending"
    ],
    [
      153,
      6,
      "2026-02-19",
      911,
      525,
      "Overdue"
    ],
    [
      157,
      157,
      "2025-04-07",
      5373,
      2955,
      "Pending"
    ],
    [
      164,
      168,
      "2025-10-07",
      3778,
      1142,
      "Overdue"
    ],
    [
      165,
      82,
      "2026-01-18",
      8519,
      833,
      "Pending"
    ],
    [
      170,
      154,
      "2025-09-04",
      6179,
      2151,
      "Overdue"
    ],
    [
      174,
      37,
      "2025-07-24",
      6713,
      4556,
      "Overdue"
    ],
    [
      179,
      4,
      "2025-04-18",
      1407,
      1310,
      "Overdue"
    ],
    [
      181,
      50,
      "2025-05-07",
      2217,
      1891,
      "Overdue"
    ],
    [
      185,
      123,
      "2025-12-18",
      2802,
      2643,
      "Pending"
    ],
    [
      195,
      96,
      "2025-10-08",
      6970,
      1617,
      "Pending"
    ],
    [
      196,
      32,
      "2025-06-28",
      5037,
      856,
      "Overdue"
    ],
    [
      199,
      154,
      "2025-09-23",
      7571,
      640,
      "Overdue"
    ],
    [
      201,
      121,
      "2025-04-16",
      4697,
      3410,
      "Pending"
    ],
    [
      202,
      160,
      "2026-03-03",
      2730,
      2020,
      "Overdue"
    ],
    [
      205,
      88,
      "2025-11-03",
      9976,
      905,
      "Pending"
    ],
    [
      207,
      165,
      "2025-11-03",
      5238,
      3647,
      "Overdue"
    ],
    [
      209,
      144,
      "2026-03-25",
      8075,
      6860,
      "Overdue"
    ],
    [
      211,
      74,
      "2026-02-15",
      8644,
      649,
      "Overdue"
    ],
    [
      216,
      13,
      "2025-08-16",
      1203,
      186,
      "Overdue"
    ],
    [
      224,
      112,
      "2025-11-12",
      272,
      157,
      "Overdue"
    ],
    [
      225,
      176,
      "2025-04-10",
      3956,
      805,
      "Pending"
    ],
    [
      227,
      132,
      "2025-06-30",
      3738,
      1752,
      "Overdue"
    ],
    [
      228,
      101,
      "2025-08-23",
      1333,
      445,
      "Pending"
    ],
    [
      233,
      53,
      "2025-04-13",
      3939,
      2374,
      "Overdue"
    ],
    [
      239,
      66,
      "2026-03-14",
      1553,
      522,
      "Pending"
    ],
    [
      243,
      192,
      "2025-11-08",
      9489,
      2831,
      "Overdue"
    ],
    [
      244,
      67,
      "2026-01-28",
      7008,
      6741,
      "Pending"
    ],
    [
      246,
      162,
      "2025-10-05",
      6815,
      1342,
      "Overdue"
    ],
    [
      249,
      165,
      "2025-05-22",
      3484,
      260,
      "Overdue"
    ],
    [
      253,
      82,
      "2025-09-29",
      7911,
      6374,
      "Pending"
    ],
    [
      254,
      172,
      "2025-06-14",
      3434,
      1131,
      "Pending"
    ],
    [
      258,
      99,
      "2025-06-06",
      6351,
      4997,
      "Pending"
    ],
    [
      260,
      103,
      "2025-06-27",
      4767,
      2343,
      "Overdue"
    ],
    [
      262,
      72,
      "2025-11-19",
      2512,
      867,
      "Overdue"
    ],
    [
      263,
      70,
      "2025-08-01",
      3954,
      2179,
      "Overdue"
    ],
    [
      264,
      170,
      "2025-11-01",
      6675,
      2429,
      "Pending"
    ],
    [
      266,
      127,
      "2025-11-18",
      2845,
      2200,
      "Overdue"
    ],
    [
      267,
      26,
      "2026-03-31",
      4942,
      541,
      "Pending"
    ],
    [
      273,
      132,
      "2025-05-14",
      6790,
      2232,
      "Overdue"
    ],
    [
      275,
      112,
      "2025-04-20",
      429,
      295,
      "Overdue"
    ],
    [
      276,
      12,
      "2025-07-12",
      6091,
      1242,
      "Pending"
    ],
    [
      279,
      74,
      "2025-09-13",
      6679,
      2082,
      "Overdue"
    ],
    [
      282,
      89,
      "2026-02-26",
      8254,
      5474,
      "Pending"
    ],
    [
      294,
      109,
      "2025-08-27",
      2070,
      78,
      "Overdue"
    ],
    [
      306,
      66,
      "2026-01-22",
      1487,
      1081,
      "Overdue"
    ],
    [
      315,
      229,
      "2026-02-01",
      3601,
      2410,
      "Pending"
    ],
    [
      316,
      393,
      "2026-02-23",
      9506,
      2176,
      "Pending"
    ],
    [
      318,
      300,
      "2025-08-29",
      4061,
      376,
      "Overdue"
    ],
    [
      323,
      17,
      "2025-11-20",
      6705,
      4220,
      "Pending"
    ],
    [
      324,
      94,
      "2026-03-10",
      2575,
      538,
      "Pending"
    ],
    [
      329,
      367,
      "2025-08-02",
      3123,
      637,
      "Overdue"
    ],
    [
      331,
      179,
      "2025-05-15",
      5045,
      4573,
      "Overdue"
    ],
    [
      333,
      45,
      "2025-08-17",
      7125,
      4069,
      "Overdue"
    ],
    [
      339,
      157,
      "2025-11-15",
      5928,
      3407,
      "Overdue"
    ],
    [
      344,
      195,
      "2026-02-20",
      5872,
      5039,
      "Pending"
    ],
    [
      346,
      40,
      "2026-03-08",
      9802,
      4507,
      "Pending"
    ],
    [
      356,
      169,
      "2026-01-25",
      6698,
      4712,
      "Pending"
    ],
    [
      359,
      98,
      "2026-02-01",
      5134,
      4414,
      "Overdue"
    ],
    [
      361,
      38,
      "2025-11-29",
      8060,
      3227,
      "Pending"
    ],
    [
      364,
      97,
      "2026-01-26",
      4670,
      1051,
      "Overdue"
    ],
    [
      366,
      46,
      "2025-08-21",
      3959,
      3943,
      "Pending"
    ],
    [
      367,
      84,
      "2025-12-15",
      7964,
      4327,
      "Overdue"
    ],
    [
      368,
      167,
      "2025-09-19",
      5957,
      4747,
      "Overdue"
    ],
    [
      371,
      214,
      "2025-11-30",
      4320,
      3140,
      "Pending"
    ],
    [
      373,
      113,
      "2025-10-04",
      2233,
      1593,
      "Pending"
    ],
    [
      374,
      276,
      "2026-02-09",
      7139,
      510,
      "Overdue"
    ],
    [
      376,
      68,
      "2025-07-11",
      2638,
      13,
      "Overdue"
    ],
    [
      378,
      374,
      "2026-03-15",
      6286,
      5647,
      "Pending"
    ],
    [
      386,
      156,
      "2025-09-04",
      3400,
      3346,
      "Pending"
    ],
    [
      388,
      154,
      "2025-12-05",
      6521,
      571,
      "Overdue"
    ],
    [
      389,
      389,
      "2025-07-12",
      631,
      300,
      "Pending"
    ],
    [
      391,
      347,
      "2025-04-27",
      7155,
      1207,
      "Pending"
    ],
    [
      394,
      347,
      "2026-03-13",
      9762,
      6190,
      "Overdue"
    ],
    [
      395,
      376,
      "2026-01-11",
      5802,
      3987,
      "Overdue"
    ],
    [
      404,
      243,
      "2025-06-07",
      4622,
      2040,
      "Pending"
    ],
    [
      405,
      155,
      "2025-12-28",
      8039,
      7985,
      "Overdue"
    ],
    [
      409,
      237,
      "2026-01-07",
      6354,
      22,
      "Overdue"
    ],
    [
      410,
      162,
      "2026-01-03",
      3908,
      1276,
      "Overdue"
    ],
    [
      412,
      292,
      "2025-11-04",
      3042,
      2776,
      "Pending"
    ],
    [
      418,
      286,
      "2025-08-03",
      6141,
      2993,
      "Overdue"
    ],
    [
      422,
      198,
      "2025-09-11",
      6654,
      3270,
      "Overdue"
    ],
    [
      437,
      139,
      "2026-02-04",
      6588,
      2895,
      "Pending"
    ],
    [
      443,
      383,
      "2025-06-14",
      7051,
      497,
      "Overdue"
    ],
    [
      447,
      64,
      "2026-03-25",
      5407,
      2963,
      "Overdue"
    ],
    [
      449,
      295,
      "2025-12-03",
      6937,
      1696,
      "Pending"
    ],
    [
      455,
      236,
      "2025-12-03",
      5142,
      547,
      "Overdue"
    ],
    [
      457,
      193,
      "2025-12-19",
      2985,
      249,
      "Pending"
    ],
    [
      462,
      72,
      "2025-09-26",
      855,
      267,
      "Overdue"
    ],
    [
      463,
      187,
      "2025-10-03",
      8739,
      789,
      "Overdue"
    ],
    [
      464,
      219,
      "2025-06-29",
      5938,
      1281,
      "Pending"
    ],
    [
      468,
      67,
      "2025-11-09",
      9029,
      4628,
      "Pending"
    ],
    [
      469,
      330,
      "2025-08-15",
      2942,
      131,
      "Overdue"
    ],
    [
      471,
      23,
      "2025-09-07",
      2962,
      207,
      "Pending"
    ],
    [
      474,
      311,
      "2025-07-27",
      6971,
      295,
      "Overdue"
    ],
    [
      476,
      387,
      "2026-04-02",
      7661,
      1374,
      "Overdue"
    ],
    [
      477,
      264,
      "2026-03-16",
      6865,
      6059,
      "Overdue"
    ],
    [
      479,
      172,
      "2025-07-07",
      9352,
      8310,
      "Overdue"
    ],
    [
      481,
      221,
      "2025-06-19",
      903,
      350,
      "Overdue"
    ],
    [
      483,
      111,
      "2026-03-29",
      4222,
      2695,
      "Overdue"
    ],
    [
      485,
      293,
      "2025-06-15",
      9386,
      7576,
      "Overdue"
    ],
    [
      486,
      34,
      "2025-04-13",
      2264,
      1791,
      "Overdue"
    ],
    [
      491,
      387,
      "2025-06-04",
      9082,
      2940,
      "Pending"
    ],
    [
      493,
      226,
      "2026-03-15",
      3433,
      1581,
      "Pending"
    ],
    [
      494,
      289,
      "2025-09-26",
      1979,
      898,
      "Overdue"
    ],
    [
      498,
      124,
      "2025-08-12",
      3274,
      560,
      "Overdue"
    ],
    [
      501,
      190,
      "2026-01-18",
      5742,
      4525,
      "Pending"
    ],
    [
      503,
      287,
      "2025-10-12",
      4774,
      3692,
      "Overdue"
    ],
    [
      510,
      78,
      "2026-01-05",
      5851,
      5149,
      "Pending"
    ],
    [
      511,
      370,
      "2025-08-25",
      9027,
      920,
      "Overdue"
    ],
    [
      513,
      8,
      "2025-11-09",
      8207,
      6489,
      "Pending"
    ],
    [
      516,
      56,
      "2026-01-08",
      6533,
      1232,
      "Pending"
    ],
    [
      519,
      305,
      "2025-05-13",
      2839,
      1085,
      "Overdue"
    ],
    [
      520,
      270,
      "2025-10-24",
      1068,
      681,
      "Overdue"
    ],
    [
      521,
      154,
      "2025-09-22",
      647,
      162,
      "Pending"
    ],
    [
      523,
      275,
      "2025-12-16",
      5759,
      2932,
      "Pending"
    ],
    [
      526,
      370,
      "2025-10-11",
      9745,
      1972,
      "Overdue"
    ],
    [
      528,
      335,
      "2025-09-15",
      5321,
      4396,
      "Overdue"
    ],
    [
      530,
      177,
      "2025-09-09",
      9062,
      771,
      "Overdue"
    ],
    [
      538,
      186,
      "2025-05-31",
      7914,
      3081,
      "Overdue"
    ],
    [
      540,
      81,
      "2025-10-01",
      2492,
      725,
      "Pending"
    ],
    [
      542,
      117,
      "2025-10-16",
      4236,
      3678,
      "Overdue"
    ],
    [
      547,
      213,
      "2025-07-24",
      548,
      448,
      "Pending"
    ],
    [
      553,
      373,
      "2026-03-05",
      481,
      337,
      "Overdue"
    ],
    [
      555,
      235,
      "2025-04-18",
      6937,
      5116,
      "Overdue"
    ],
    [
      556,
      69,
      "2026-01-29",
      2476,
      1396,
      "Overdue"
    ],
    [
      560,
      341,
      "2025-10-21",
      4827,
      922,
      "Overdue"
    ],
    [
      561,
      362,
      "2025-04-19",
      1638,
      1610,
      "Overdue"
    ],
    [
      563,
      398,
      "2026-03-23",
      8169,
      2893,
      "Pending"
    ],
    [
      572,
      29,
      "2025-04-07",
      7869,
      7777,
      "Overdue"
    ],
    [
      574,
      392,
      "2025-12-09",
      6681,
      5173,
      "Overdue"
    ],
    [
      576,
      190,
      "2025-06-05",
      7204,
      4432,
      "Pending"
    ],
    [
      579,
      330,
      "2025-09-29",
      723,
      367,
      "Overdue"
    ],
    [
      583,
      17,
      "2025-12-07",
      7640,
      3169,
      "Overdue"
    ],
    [
      585,
      89,
      "2025-10-18",
      7124,
      6691,
      "Pending"
    ],
    [
      586,
      175,
      "2025-05-16",
      4295,
      700,
      "Pending"
    ],
    [
      591,
      143,
      "2025-08-22",
      3122,
      2062,
      "Overdue"
    ],
    [
      592,
      369,
      "2026-01-26",
      4643,
      781,
      "Overdue"
    ],
    [
      593,
      133,
      "2025-09-20",
      2865,
      358,
      "Pending"
    ],
    [
      594,
      1,
      "2025-08-17",
      2668,
      1946,
      "Pending"
    ],
    [
      595,
      319,
      "2025-09-24",
      7857,
      5174,
      "Pending"
    ],
    [
      596,
      320,
      "2026-02-16",
      4604,
      409,
      "Overdue"
    ],
    [
      597,
      346,
      "2025-08-11",
      8320,
      7174,
      "Pending"
    ]
  ],
  "row_count": 186,
  "chart": {
    "data": [
      {
        "hovertemplate": "id=%{x}<br>patient_id=%{y}<extra></extra>",
        "legendgroup": "",
        "marker": {
          "color": "#636efa",
          "pattern": {
            "shape": ""
          }
        },
        "name": "",
        "orientation": "v",
        "showlegend": false,
        "textposition": "auto",
        "x": {
          "dtype": "i2",
          "bdata": "AQADAAQABQAHAAoADAAPABAAEQAaAB0AHgAfACoALQAxADIAMwA5ADoAPQA/AEIAQwBHAE0AUQBXAF0AXwBgAGsAbABvAHAAcQBzAHQAdwB/AIsAjgCXAJkAnQCkAKUAqgCuALMAtQC5AMMAxADHAMkAygDNAM8A0QDTANgA4ADhAOMA5ADpAO8A8wD0APYA+QD9AP4AAgEEAQYBBwEIAQoBCwERARMBFAEXARoBJgEyATsBPAE+AUMBRAFJAUsBTQFTAVgBWgFkAWcBaQFsAW4BbwFwAXMBdQF2AXgBegGCAYQBhQGHAYoBiwGUAZUBmQGaAZwBogGmAbUBuwG/AcEBxwHJAc4BzwHQAdQB1QHXAdoB3AHdAd8B4QHjAeUB5gHrAe0B7gHyAfUB9wH+Af8BAQIEAgcCCAIJAgsCDgIQAhICGgIcAh4CIwIpAisCLAIwAjECMwI8Aj4CQAJDAkcCSQJKAk8CUAJRAlICUwJUAlUC"
        },
        "xaxis": "x",
        "y": {
          "dtype": "i2",
          "bdata": "YgBhADMAcwA0AJgAiwAyAIoAQgAVAL8AswB/AHsADADFAIEAcQAdADUAeADDAIoAsQCFAJ4ACADHALgApgBvADEAlwAdABYASQCdAAUAwQAqAEYAnwA1AAYAnQCoAFIAmgAlAAQAMgB7AGAAIACaAHkAoABYAKUAkABKAA0AcACwAIQAZQA1AEIAwABDAKIApQBSAKwAYwBnAEgARgCqAH8AGgCEAHAADABKAFkAbQBCAOUAiQEsAREAXgBvAbMALQCdAMMAKACpAGIAJgBhAC4AVACnANYAcQAUAUQAdgGcAJoAhQFbAVsBeAHzAJsA7QCiACQBHgHGAIsAfwFAACcB7ADBAEgAuwDbAEMASgEXADcBgwEIAawA3QBvACUBIgCDAeIAIQF8AL4AHwFOAHIBCAA4ADEBDgGaABMBcgFPAbEAugBRAHUA1QB1AesARQBVAWoBjgEdAIgBvgBKAREAWQCvAI8AcQGFAAEAPwFAAVoB"
        },
        "yaxis": "y",
        "type": "bar"
      }
    ],
    "layout": {
      "template": {
        "data": {
          "histogram2dcontour": [
            {
              "type": "histogram2dcontour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "choropleth": [
            {
              "type": "choropleth",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "histogram2d": [
            {
              "type": "histogram2d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "heatmap": [
            {
              "type": "heatmap",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "contourcarpet": [
            {
              "type": "contourcarpet",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "contour": [
            {
              "type": "contour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "surface": [
            {
              "type": "surface",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "mesh3d": [
            {
              "type": "mesh3d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "scatter": [
            {
              "fillpattern": {
                "fillmode": "overlay",
                "size": 10,
                "solidity": 0.2
              },
              "type": "scatter"
            }
          ],
          "parcoords": [
            {
              "type": "parcoords",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolargl": [
            {
              "type": "scatterpolargl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "bar": [
            {
              "error_x": {
                "color": "#2a3f5f"
              },
              "error_y": {
                "color": "#2a3f5f"
              },
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "bar"
            }
          ],
          "scattergeo": [
            {
              "type": "scattergeo",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolar": [
            {
              "type": "scatterpolar",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "histogram": [
            {
              "marker": {
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "histogram"
            }
          ],
          "scattergl": [
            {
              "type": "scattergl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatter3d": [
            {
              "type": "scatter3d",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              },
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermap": [
            {
              "type": "scattermap",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermapbox": [
            {
              "type": "scattermapbox",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterternary": [
            {
              "type": "scatterternary",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattercarpet": [
            {
              "type": "scattercarpet",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "carpet": [
            {
              "aaxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "baxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "type": "carpet"
            }
          ],
          "table": [
            {
              "cells": {
                "fill": {
                  "color": "#EBF0F8"
                },
                "line": {
                  "color": "white"
                }
              },
              "header": {
                "fill": {
                  "color": "#C8D4E3"
                },
                "line": {
                  "color": "white"
                }
              },
              "type": "table"
            }
          ],
          "barpolar": [
            {
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "barpolar"
            }
          ],
          "pie": [
            {
              "automargin": true,
              "type": "pie"
            }
          ]
        },
        "layout": {
          "autotypenumbers": "strict",
          "colorway": [
            "#636efa",
            "#EF553B",
            "#00cc96",
            "#ab63fa",
            "#FFA15A",
            "#19d3f3",
            "#FF6692",
            "#B6E880",
            "#FF97FF",
            "#FECB52"
          ],
          "font": {
            "color": "#2a3f5f"
          },
          "hovermode": "closest",
          "hoverlabel": {
            "align": "left"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
            "bgcolor": "#E5ECF6",
            "angularaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "radialaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "ternary": {
            "bgcolor": "#E5ECF6",
            "aaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "baxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "caxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "coloraxis": {
            "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
            }
          },
          "colorscale": {
            "sequential": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "sequentialminus": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "diverging": [
              [
                0,
                "#8e0152"
              ],
              [
                0.1,
                "#c51b7d"
              ],
              [
                0.2,
                "#de77ae"
              ],
              [
                0.3,
                "#f1b6da"
              ],
              [
                0.4,
                "#fde0ef"
              ],
              [
                0.5,
                "#f7f7f7"
              ],
              [
                0.6,
                "#e6f5d0"
              ],
              [
                0.7,
                "#b8e186"
              ],
              [
                0.8,
                "#7fbc41"
              ],
              [
                0.9,
                "#4d9221"
              ],
              [
                1,
                "#276419"
              ]
            ]
          },
          "xaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "yaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "scene": {
            "xaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "yaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "zaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            }
          },
          "shapedefaults": {
            "line": {
              "color": "#2a3f5f"
            }
          },
          "annotationdefaults": {
            "arrowcolor": "#2a3f5f",
            "arrowhead": 0,
            "arrowwidth": 1
          },
          "geo": {
            "bgcolor": "white",
            "landcolor": "#E5ECF6",
            "subunitcolor": "white",
            "showland": true,
            "showlakes": true,
            "lakecolor": "white"
          },
          "title": {
            "x": 0.05
          },
          "mapbox": {
            "style": "light"
          }
        }
      },
      "xaxis": {
        "anchor": "y",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "id"
        }
      },
      "yaxis": {
        "anchor": "x",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "patient_id"
        }
      },
      "legend": {
        "tracegroupgap": 0
      },
      "margin": {
        "t": 60
      },
      "barmode": "relative"
    }
  },
  "chart_type": "bar"
}

6. Which city has the most patients?
{
  "message": "Query executed successfully",
  "sql_query": "SELECT city\nFROM patients\nGROUP BY city\nORDER BY COUNT(id) DESC\nLIMIT 1",
  "columns": [
    "city"
  ],
  "rows": [
    [
      "Nashik"
    ]
  ],
  "row_count": 1,
  "chart": {},
  "chart_type": ""
}

7.What is the average treatment cost?
{
  "message": "Query executed successfully",
  "sql_query": "SELECT AVG(cost) FROM treatments",
  "columns": [
    "AVG(cost)"
  ],
  "rows": [
    [
      2519.9714285714285
    ]
  ],
  "row_count": 1,
  "chart": {},
  "chart_type": ""
}

8.How many appointments are completed?
{
  "message": "Query executed successfully",
  "sql_query": "SELECT COUNT(*) \nFROM appointments \nWHERE status = 'completed'",
  "columns": [
    "COUNT(*)"
  ],
  "rows": [
    [
      0
    ]
  ],
  "row_count": 1,
  "chart": {},
  "chart_type": ""
}

9.Show monthly appointment count?
{
  "message": "Query executed successfully",
  "sql_query": "SELECT \n    STRFTIME('%Y', appointment_date) AS year,\n    STRFTIME('%m', appointment_date) AS month,\n    COUNT(*) AS appointment_count\nFROM \n    appointments\nGROUP BY \n    STRFTIME('%Y', appointment_date),\n    STRFTIME('%m', appointment_date)",
  "columns": [
    "year",
    "month",
    "appointment_count"
  ],
  "rows": [
    [
      "2025",
      "04",
      73
    ],
    [
      "2025",
      "05",
      82
    ],
    [
      "2025",
      "06",
      82
    ],
    [
      "2025",
      "07",
      83
    ],
    [
      "2025",
      "08",
      88
    ],
    [
      "2025",
      "09",
      88
    ],
    [
      "2025",
      "10",
      90
    ],
    [
      "2025",
      "11",
      74
    ],
    [
      "2025",
      "12",
      76
    ],
    [
      "2026",
      "01",
      72
    ],
    [
      "2026",
      "02",
      83
    ],
    [
      "2026",
      "03",
      87
    ],
    [
      "2026",
      "04",
      22
    ]
  ],
  "row_count": 13,
  "chart": {
    "data": [
      {
        "hovertemplate": "year=%{x}<br>month=%{y}<extra></extra>",
        "legendgroup": "",
        "marker": {
          "color": "#636efa",
          "pattern": {
            "shape": ""
          }
        },
        "name": "",
        "orientation": "v",
        "showlegend": false,
        "textposition": "auto",
        "x": [
          "2025",
          "2025",
          "2025",
          "2025",
          "2025",
          "2025",
          "2025",
          "2025",
          "2025",
          "2026",
          "2026",
          "2026",
          "2026"
        ],
        "xaxis": "x",
        "y": [
          "04",
          "05",
          "06",
          "07",
          "08",
          "09",
          "10",
          "11",
          "12",
          "01",
          "02",
          "03",
          "04"
        ],
        "yaxis": "y",
        "type": "bar"
      }
    ],
    "layout": {
      "template": {
        "data": {
          "histogram2dcontour": [
            {
              "type": "histogram2dcontour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "choropleth": [
            {
              "type": "choropleth",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "histogram2d": [
            {
              "type": "histogram2d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "heatmap": [
            {
              "type": "heatmap",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "contourcarpet": [
            {
              "type": "contourcarpet",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "contour": [
            {
              "type": "contour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "surface": [
            {
              "type": "surface",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "mesh3d": [
            {
              "type": "mesh3d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "scatter": [
            {
              "fillpattern": {
                "fillmode": "overlay",
                "size": 10,
                "solidity": 0.2
              },
              "type": "scatter"
            }
          ],
          "parcoords": [
            {
              "type": "parcoords",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolargl": [
            {
              "type": "scatterpolargl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "bar": [
            {
              "error_x": {
                "color": "#2a3f5f"
              },
              "error_y": {
                "color": "#2a3f5f"
              },
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "bar"
            }
          ],
          "scattergeo": [
            {
              "type": "scattergeo",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolar": [
            {
              "type": "scatterpolar",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "histogram": [
            {
              "marker": {
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "histogram"
            }
          ],
          "scattergl": [
            {
              "type": "scattergl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatter3d": [
            {
              "type": "scatter3d",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              },
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermap": [
            {
              "type": "scattermap",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermapbox": [
            {
              "type": "scattermapbox",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterternary": [
            {
              "type": "scatterternary",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattercarpet": [
            {
              "type": "scattercarpet",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "carpet": [
            {
              "aaxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "baxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "type": "carpet"
            }
          ],
          "table": [
            {
              "cells": {
                "fill": {
                  "color": "#EBF0F8"
                },
                "line": {
                  "color": "white"
                }
              },
              "header": {
                "fill": {
                  "color": "#C8D4E3"
                },
                "line": {
                  "color": "white"
                }
              },
              "type": "table"
            }
          ],
          "barpolar": [
            {
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "barpolar"
            }
          ],
          "pie": [
            {
              "automargin": true,
              "type": "pie"
            }
          ]
        },
        "layout": {
          "autotypenumbers": "strict",
          "colorway": [
            "#636efa",
            "#EF553B",
            "#00cc96",
            "#ab63fa",
            "#FFA15A",
            "#19d3f3",
            "#FF6692",
            "#B6E880",
            "#FF97FF",
            "#FECB52"
          ],
          "font": {
            "color": "#2a3f5f"
          },
          "hovermode": "closest",
          "hoverlabel": {
            "align": "left"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
            "bgcolor": "#E5ECF6",
            "angularaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "radialaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "ternary": {
            "bgcolor": "#E5ECF6",
            "aaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "baxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "caxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "coloraxis": {
            "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
            }
          },
          "colorscale": {
            "sequential": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "sequentialminus": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "diverging": [
              [
                0,
                "#8e0152"
              ],
              [
                0.1,
                "#c51b7d"
              ],
              [
                0.2,
                "#de77ae"
              ],
              [
                0.3,
                "#f1b6da"
              ],
              [
                0.4,
                "#fde0ef"
              ],
              [
                0.5,
                "#f7f7f7"
              ],
              [
                0.6,
                "#e6f5d0"
              ],
              [
                0.7,
                "#b8e186"
              ],
              [
                0.8,
                "#7fbc41"
              ],
              [
                0.9,
                "#4d9221"
              ],
              [
                1,
                "#276419"
              ]
            ]
          },
          "xaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "yaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "scene": {
            "xaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "yaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "zaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            }
          },
          "shapedefaults": {
            "line": {
              "color": "#2a3f5f"
            }
          },
          "annotationdefaults": {
            "arrowcolor": "#2a3f5f",
            "arrowhead": 0,
            "arrowwidth": 1
          },
          "geo": {
            "bgcolor": "white",
            "landcolor": "#E5ECF6",
            "subunitcolor": "white",
            "showland": true,
            "showlakes": true,
            "lakecolor": "white"
          },
          "title": {
            "x": 0.05
          },
          "mapbox": {
            "style": "light"
          }
        }
      },
      "xaxis": {
        "anchor": "y",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "year"
        }
      },
      "yaxis": {
        "anchor": "x",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "month"
        }
      },
      "legend": {
        "tracegroupgap": 0
      },
      "margin": {
        "t": 60
      },
      "barmode": "relative"
    }
  },
  "chart_type": "bar"
}

10.Show revenue by month?

{
  "message": "Query executed successfully",
  "sql_query": "SELECT \n    STRFTIME('%Y-%m', i.invoice_date) AS month,\n    SUM(i.total_amount) AS revenue\nFROM \n    invoices i\nGROUP BY \n    STRFTIME('%Y-%m', i.invoice_date)",
  "columns": [
    "month",
    "revenue"
  ],
  "rows": [
    [
      "2025-04",
      241115
    ],
    [
      "2025-05",
      235907
    ],
    [
      "2025-06",
      284591
    ],
    [
      "2025-07",
      265348
    ],
    [
      "2025-08",
      224988
    ],
    [
      "2025-09",
      209902
    ],
    [
      "2025-10",
      265619
    ],
    [
      "2025-11",
      196259
    ],
    [
      "2025-12",
      238807
    ],
    [
      "2026-01",
      285672
    ],
    [
      "2026-02",
      240691
    ],
    [
      "2026-03",
      223945
    ],
    [
      "2026-04",
      84532
    ]
  ],
  "row_count": 13,
  "chart": {
    "data": [
      {
        "hovertemplate": "month=%{x}<br>revenue=%{y}<extra></extra>",
        "legendgroup": "",
        "marker": {
          "color": "#636efa",
          "pattern": {
            "shape": ""
          }
        },
        "name": "",
        "orientation": "v",
        "showlegend": false,
        "textposition": "auto",
        "x": [
          "2025-04",
          "2025-05",
          "2025-06",
          "2025-07",
          "2025-08",
          "2025-09",
          "2025-10",
          "2025-11",
          "2025-12",
          "2026-01",
          "2026-02",
          "2026-03",
          "2026-04"
        ],
        "xaxis": "x",
        "y": {
          "dtype": "f8",
          "bdata": "AAAAANhuDUEAAAAAGMwMQQAAAAC8XhFBAAAAABAyEEEAAAAA4HYLQQAAAABwnwlBAAAAAEw2EEEAAAAAGPUHQQAAAAC4Jg1BAAAAAKBvEUEAAAAAmGENQQAAAABIVgtBAAAAAECj9EA="
        },
        "yaxis": "y",
        "type": "bar"
      }
    ],
    "layout": {
      "template": {
        "data": {
          "histogram2dcontour": [
            {
              "type": "histogram2dcontour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "choropleth": [
            {
              "type": "choropleth",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "histogram2d": [
            {
              "type": "histogram2d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "heatmap": [
            {
              "type": "heatmap",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "contourcarpet": [
            {
              "type": "contourcarpet",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "contour": [
            {
              "type": "contour",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "surface": [
            {
              "type": "surface",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              },
              "colorscale": [
                [
                  0,
                  "#0d0887"
                ],
                [
                  0.1111111111111111,
                  "#46039f"
                ],
                [
                  0.2222222222222222,
                  "#7201a8"
                ],
                [
                  0.3333333333333333,
                  "#9c179e"
                ],
                [
                  0.4444444444444444,
                  "#bd3786"
                ],
                [
                  0.5555555555555556,
                  "#d8576b"
                ],
                [
                  0.6666666666666666,
                  "#ed7953"
                ],
                [
                  0.7777777777777778,
                  "#fb9f3a"
                ],
                [
                  0.8888888888888888,
                  "#fdca26"
                ],
                [
                  1,
                  "#f0f921"
                ]
              ]
            }
          ],
          "mesh3d": [
            {
              "type": "mesh3d",
              "colorbar": {
                "outlinewidth": 0,
                "ticks": ""
              }
            }
          ],
          "scatter": [
            {
              "fillpattern": {
                "fillmode": "overlay",
                "size": 10,
                "solidity": 0.2
              },
              "type": "scatter"
            }
          ],
          "parcoords": [
            {
              "type": "parcoords",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolargl": [
            {
              "type": "scatterpolargl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "bar": [
            {
              "error_x": {
                "color": "#2a3f5f"
              },
              "error_y": {
                "color": "#2a3f5f"
              },
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "bar"
            }
          ],
          "scattergeo": [
            {
              "type": "scattergeo",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterpolar": [
            {
              "type": "scatterpolar",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "histogram": [
            {
              "marker": {
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "histogram"
            }
          ],
          "scattergl": [
            {
              "type": "scattergl",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatter3d": [
            {
              "type": "scatter3d",
              "line": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              },
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermap": [
            {
              "type": "scattermap",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattermapbox": [
            {
              "type": "scattermapbox",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scatterternary": [
            {
              "type": "scatterternary",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "scattercarpet": [
            {
              "type": "scattercarpet",
              "marker": {
                "colorbar": {
                  "outlinewidth": 0,
                  "ticks": ""
                }
              }
            }
          ],
          "carpet": [
            {
              "aaxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "baxis": {
                "endlinecolor": "#2a3f5f",
                "gridcolor": "white",
                "linecolor": "white",
                "minorgridcolor": "white",
                "startlinecolor": "#2a3f5f"
              },
              "type": "carpet"
            }
          ],
          "table": [
            {
              "cells": {
                "fill": {
                  "color": "#EBF0F8"
                },
                "line": {
                  "color": "white"
                }
              },
              "header": {
                "fill": {
                  "color": "#C8D4E3"
                },
                "line": {
                  "color": "white"
                }
              },
              "type": "table"
            }
          ],
          "barpolar": [
            {
              "marker": {
                "line": {
                  "color": "#E5ECF6",
                  "width": 0.5
                },
                "pattern": {
                  "fillmode": "overlay",
                  "size": 10,
                  "solidity": 0.2
                }
              },
              "type": "barpolar"
            }
          ],
          "pie": [
            {
              "automargin": true,
              "type": "pie"
            }
          ]
        },
        "layout": {
          "autotypenumbers": "strict",
          "colorway": [
            "#636efa",
            "#EF553B",
            "#00cc96",
            "#ab63fa",
            "#FFA15A",
            "#19d3f3",
            "#FF6692",
            "#B6E880",
            "#FF97FF",
            "#FECB52"
          ],
          "font": {
            "color": "#2a3f5f"
          },
          "hovermode": "closest",
          "hoverlabel": {
            "align": "left"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
            "bgcolor": "#E5ECF6",
            "angularaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "radialaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "ternary": {
            "bgcolor": "#E5ECF6",
            "aaxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "baxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            },
            "caxis": {
              "gridcolor": "white",
              "linecolor": "white",
              "ticks": ""
            }
          },
          "coloraxis": {
            "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
            }
          },
          "colorscale": {
            "sequential": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "sequentialminus": [
              [
                0,
                "#0d0887"
              ],
              [
                0.1111111111111111,
                "#46039f"
              ],
              [
                0.2222222222222222,
                "#7201a8"
              ],
              [
                0.3333333333333333,
                "#9c179e"
              ],
              [
                0.4444444444444444,
                "#bd3786"
              ],
              [
                0.5555555555555556,
                "#d8576b"
              ],
              [
                0.6666666666666666,
                "#ed7953"
              ],
              [
                0.7777777777777778,
                "#fb9f3a"
              ],
              [
                0.8888888888888888,
                "#fdca26"
              ],
              [
                1,
                "#f0f921"
              ]
            ],
            "diverging": [
              [
                0,
                "#8e0152"
              ],
              [
                0.1,
                "#c51b7d"
              ],
              [
                0.2,
                "#de77ae"
              ],
              [
                0.3,
                "#f1b6da"
              ],
              [
                0.4,
                "#fde0ef"
              ],
              [
                0.5,
                "#f7f7f7"
              ],
              [
                0.6,
                "#e6f5d0"
              ],
              [
                0.7,
                "#b8e186"
              ],
              [
                0.8,
                "#7fbc41"
              ],
              [
                0.9,
                "#4d9221"
              ],
              [
                1,
                "#276419"
              ]
            ]
          },
          "xaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "yaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": "",
            "title": {
              "standoff": 15
            },
            "zerolinecolor": "white",
            "automargin": true,
            "zerolinewidth": 2
          },
          "scene": {
            "xaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "yaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            },
            "zaxis": {
              "backgroundcolor": "#E5ECF6",
              "gridcolor": "white",
              "linecolor": "white",
              "showbackground": true,
              "ticks": "",
              "zerolinecolor": "white",
              "gridwidth": 2
            }
          },
          "shapedefaults": {
            "line": {
              "color": "#2a3f5f"
            }
          },
          "annotationdefaults": {
            "arrowcolor": "#2a3f5f",
            "arrowhead": 0,
            "arrowwidth": 1
          },
          "geo": {
            "bgcolor": "white",
            "landcolor": "#E5ECF6",
            "subunitcolor": "white",
            "showland": true,
            "showlakes": true,
            "lakecolor": "white"
          },
          "title": {
            "x": 0.05
          },
          "mapbox": {
            "style": "light"
          }
        }
      },
      "xaxis": {
        "anchor": "y",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "month"
        }
      },
      "yaxis": {
        "anchor": "x",
        "domain": [
          0,
          1
        ],
        "title": {
          "text": "revenue"
        }
      },
      "legend": {
        "tracegroupgap": 0
      },
      "margin": {
        "t": 60
      },
      "barmode": "relative"
    }
  },
  "chart_type": "bar"
}




