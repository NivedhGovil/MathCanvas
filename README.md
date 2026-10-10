# MathCanvas

MathCanvas is an **interactive math and physics explorer** in which one can graph equations, running statistics on data, and simulate projectile motion.
One can pick a mode, change the inputs, and the graph updates. 


The interesting thing is that this website **didn't use any HTML tag**! It was built using the python libraries **Streamlit**, **Numpy** and **Matplotlib**. 

**Live app:** [mathcanvas.streamlit.app](https://mathcanvas.streamlit.app/) or [https://mathcanvas.onrender.com/](https://mathcanvas.onrender.com/)

Built by [Nivedh Govil](https://github.com/NivedhGovil).

## Features

### Graph Plot


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
- Minimum
- Maximum
- Range

MathCanvas also draws a *bar chart* of those measures of the data

### Projectile Motion

Set the launch angle, initial speed, mass, and a time on the flight, then read:

- Time of flight
- Range
- Maximum height

Gravitational acceleration is fixed at 9.81 m/s^2. 

**View**

Open the hosted website:

**[https://mathcanvas.streamlit.app/](https://mathcanvas.streamlit.app/)** or [https://mathcanvas.onrender.com/](https://mathcanvas.onrender.com/)

## Run locally


```bash
git clone https://github.com/NivedhGovil/MathCanvas.git
cd MathCanvas
pip install -r requirements.txt
streamlit run app.py
```

# Preview


<img width="572" height="653" alt="Preview" src="https://github.com/user-attachments/assets/574b0d17-ac48-4ad3-ac3f-6f58c7f762a6" />



## Author

**Nivedh Govil** — [GitHub](https://github.com/NivedhGovil)


