# MathCanvas

MathCanvas is an **interactive math and physics explorer** that turns formulas and numbers into plots. You can graph equations, running statistics on data, and simulating projectile motion.
Pick a mode, change the inputs, and the graph updates. 

The interesting thing is that this website **didn't use any HTML tag**! It was built using the python libraries **Streamlit**, **Numpy** and **Matplotlib**. 

**Live app:** [mathcanvas.streamlit.app](https://mathcanvas.streamlit.app/)

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


<img width="572" height="653" alt="Preview" src="https://github.com/user-attachments/assets/574b0d17-ac48-4ad3-ac3f-6f58c7f762a6" />



## Author

**Nivedh Govil** — [GitHub](https://github.com/NivedhGovil)


