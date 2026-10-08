# MathCanvas

Interactive math explorer for graphing equations, running statistics on data, and simulating projectile motion.

**Live app:** [mathcanvas.streamlit.app](https://mathcanvas.streamlit.app/)

MathCanvas is a website that turns formulas and numbers into plots. Pick a mode, change the inputs, and the graph updates so the relationship is easy to see.

Built by [Nivedh Govil](https://github.com/NivedhGovil).

## Features

### Graph Plot

Plot common function families on a coordinate grid with axes and a light grid.

| Type | User Inputs | 
| --- | --- | 
| Constant | Value and axis (`x` or `y`) | 
| Linear | Slope \(m\) and y-intercept \(c\) |
| Quadratic | Coefficients \(a\), \(b\), and \(c\) | 
| Sine | Amplitude and frequency | 
| Cosine | Amplitude and frequency | 
| Tangent | Amplitude and frequency |


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

- Time of flight
- Range
- Maximum height

Gravity is fixed at 9.81 m/s^2. 

## Demo

Open the hosted app:

**[https://mathcanvas.streamlit.app/](https://mathcanvas.streamlit.app/)**

## Run locally


```bash
git clone https://github.com/NivedhGovil/MathCanvas.git
cd MathCanvas
pip install -r requirements.txt
streamlit run app.py
```


## Project structure

```text
MathCanvas/
├── app.py              # Streamlit website code. 
├── requirements.txt    # streamlit, numpy, matplotlib. 
└── README.md
```



## Author

**Nivedh Govil** — [GitHub](https://github.com/NivedhGovil)


