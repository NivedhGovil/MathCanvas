# MathCanvas

Interactive math explorer for graphing equations, running statistics on data, and simulating projectile motion.

**Live app:** [mathcanvas.streamlit.app](https://mathcanvas.streamlit.app/)

MathCanvas is a website that turns formulas and numbers into plots. Pick a mode, change the inputs, and the graph updates so the relationship is easy to see.

Built by [Nivedh Govil](https://github.com/NivedhGovil).

## Features

### Graph Plot

Plot common function families on a coordinate grid with axes and a light grid.

| Type | What you control | Equation |
| --- | --- | --- |
| Constant | Value and axis (`x` or `y`) | \(x = c\) or \(y = c\) |
| Linear | Slope \(m\) and y-intercept \(c\) | \(y = mx + c\) |
| Quadratic | Coefficients \(a\), \(b\), and \(c\) | \(y = ax^2 + bx + c\) |
| Sine | Amplitude and frequency | \(y = A \sin(\omega x)\) |
| Cosine | Amplitude and frequency | \(y = A \cos(\omega x)\) |
| Tangent | Amplitude and frequency | \(y = A \tan(\omega x)\) |

Sine and cosine are drawn from \(-4\pi\) to \(4\pi\), with tick labels in multiples of \(\pi\).

### Statistics

Enter 3 to 10 observations and get:

- Mean
- Median
- Standard deviation
- Variance
- Minimum, maximum, and range

With three observations, MathCanvas also draws a bar chart of those measures.

### Projectile Motion

Set the launch angle, initial speed, mass, and a time on the flight, then read:

- Time of flight: \(T = \dfrac{2u\sin\theta}{g}\)
- Range: \(R = \dfrac{u^2\sin 2\theta}{g}\)
- Maximum height: \(H = \dfrac{u^2\sin^2\theta}{2g}\)

Gravity is fixed at \(g = 9.81\ \mathrm{m/s^2}\). The trajectory is plotted from launch until the projectile returns to the ground. If the chosen time is past the time of flight, the app asks you to lower it.

## Demo

Open the hosted app — no install required:

**[https://mathcanvas.streamlit.app/](https://mathcanvas.streamlit.app/)**

## Run locally

Python 3.9 or newer is recommended.

```bash
git clone https://github.com/NivedhGovil/MathCanvas.git
cd MathCanvas
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints (usually [http://localhost:8501](http://localhost:8501)).

## Project structure

```text
MathCanvas/
├── app.py              # Streamlit app (modes, inputs, and plots)
├── requirements.txt    # streamlit, numpy, matplotlib
└── README.md
```

## Stack

- [Streamlit](https://streamlit.io/) for the interface and hosting
- [NumPy](https://numpy.org/) for calculations
- [Matplotlib](https://matplotlib.org/) for plots

## Roadmap

- Finish the quadratic plot from the \(a\), \(b\), and \(c\) inputs
- Wire the Tangent option to the tangent plotter
- Show the statistics bar chart for every observation count
- Add a histogram of the entered numbers
- Let users download a plot as an image

## Author

**Nivedh Govil** — [GitHub](https://github.com/NivedhGovil)

## License

No license file is included yet. Add one (for example MIT) if you want others to reuse the code.
