
# Create grpahs. 
# Input n numbers. Find the mean, median, and mode of the numbers. Create a histogram of the numbers.
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Website Name")
st.write(" Welcome to the Math Website")

st.header("Modes")
mode = st.selectbox("Choose the mode:", options = ["Graph Plot" , "Statistics" ])

if mode == "Graph Plot":
    st.subheader("Graph Plot")
    equation_type = st.selectbox("Choose the equation type:", options = ["Constant" , "Linear" , "Quadratic" , "Sine" , "Cosine" , "Tangent" ])
    if equation_type == "Constant":
        st.subheader("Constant Equation Plotter")
        constant = st.number_input("Enter the constant value (e.g., 5):" , min_value=0, max_value=250, value=50)
        axis = st.text_input("Enter the axis (x or y):" )
        
        fig, ax = plt.subplots(figsize=(20, 15)) # Creates a main canvas (fig) and an active plot area (ax)
        
        ax.set_xlabel("X Axis")    # Sets the label for the horizontal axis
        ax.set_ylabel("Y Axis")
        ax.axhline(y=0, color='black', linestyle='', linewidth=1)
        ax.axvline(x=0, color='black', linestyle='-', linewidth=1)

        if axis == "x":
            x = np.array([float(constant), float(constant)])
            y = np.array([-500, 500])
            
            ax.set_title(f"X = {constant}")
            ax.grid(True, alpha=0.3)
            ax.plot(x, y,  color='blue', linewidth=1, linestyle='-', label=f"x = {constant}" ) 
            st.pyplot(fig, use_container_width=True)
        else:
            y = np.array([float(constant), float(constant)])
            x = np.array([-500, 500])
            
            ax.set_title(f"Y = {constant}")
            ax.grid(True, alpha=0.3)
            ax.plot(x, y,  color='blue', linewidth=1, linestyle='-', label=f"y = {constant}" ) 
            st.pyplot(fig, use_container_width=True)
    elif equation_type == "Linear":
        st.subheader("Linear Equation Plotter")
        slope = st.number_input("Enter the slope (m):", min_value=-100, max_value=100, value=50)
        intercept = st.number_input("Enter the y-intercept (c):", min_value=-100, max_value=100, value=10)
        x = np.linspace(-100, 100, 1000)
        y = float(slope) * x + float(intercept)
        fig, ax = plt.subplots(figsize=(20, 15))
        ax.set_title(f"Y = {slope}x + {intercept}" )
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
        ax.axvline(x=0, color='black', linestyle='-', linewidth=1)
        ax.grid(True, alpha=0.3)
        ax.plot(x, y,  color='blue', linewidth=1, linestyle='-', label=f"Y = {slope}x + {intercept}" ) 
        st.pyplot(fig, use_container_width=True)
    elif equation_type == "Quadratic":
        st.subheader("Quadratic Equation Plotter")
        a = st.text_input("Enter the coefficient a:")
        b = st.text_input("Enter the coefficient b:")
        c = st.text_input("Enter the coefficient c:")
    elif equation_type == "Sine":
        st.subheader("Sine Equation Plotter")
        amplitude = st.slider(label="Amplitude:", min_value=1, max_value=50, value=10)
        frequency = st.slider(label="Frequency:", min_value=1, max_value=50, value=10)
        x = np.linspace(-4*np.pi, 4*np.pi, 2000)
        y = amplitude * np.sin(frequency * x)
        fig, ax = plt.subplots(figsize=(20, 15))
        ax.set_title("Sine Wave" )
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
        ax.axvline(x=0, color='black', linestyle='-', linewidth=1)
        ax.grid(True, alpha=0.3)
        ax.set_xticks([-4*np.pi, -3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
        ax.set_xticklabels([r"$-4\pi$", r"$-3\pi$", r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"], rotation=0 , color='black', fontsize = 20)
        ax.plot(x, y,  color='blue', linewidth=1, linestyle='-', label="Sine Wave" ) 
        st.pyplot(fig, use_container_width=True)
    elif equation_type == "Cosine":
            st.subheader("Cosine Equation Plotter")
            amplitude = st.slider(label="Amplitude:", min_value=1, max_value=50, value=10)
            frequency = st.slider(label="Frequency:", min_value=1, max_value=50, value=10)
            x = np.linspace(-4*np.pi, 4*np.pi, 2000)
            y = amplitude * np.cos(frequency * x)
            fig, ax = plt.subplots(figsize=(20, 15))
            ax.set_title("Cosine Wave" )
            ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
            ax.axvline(x=0, color='black', linestyle='-', linewidth=1)
            ax.grid(True, alpha=0.3)
            ax.set_xticks([-4*np.pi, -3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
            ax.set_xticklabels([r"$-4\pi$", r"$-3\pi$", r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"], rotation=0 , color='black', fontsize = 20)
            ax.plot(x, y,  color='blue', linewidth=1, linestyle='-', label="Cosine Wave" ) 
            st.pyplot(fig, use_container_width=True)
    elif equation_type == "Tangent":
                st.subheader("Tangent Equation Plotter")
                amplitude = st.slider(label="Amplitude:", min_value=1, max_value=50, value=10)
                frequency = st.slider(label="Frequency:", min_value=1, max_value=50, value=10)
                x = np.linspace(-4*np.pi, 4*np.pi, 2000)
                y = amplitude * np.tan(frequency * x)
                fig, ax = plt.subplots(figsize=(20, 15))
                ax.set_title("Tangent Wave" )
                ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
                ax.axvline(x=0, color='black', linestyle='-', linewidth=1)
                ax.grid(True, alpha=0.3)
                ax.set_xticks([-4*np.pi, -3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
                ax.set_xticklabels([r"$-4\pi$", r"$-3\pi$", r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"], rotation=0 , color='black', fontsize = 20)
                ax.plot(x, y,  color='blue', linewidth=1, linestyle='-', label="Tangent Wave" ) 
                st.pyplot(fig, use_container_width=True)
else: 
     st.subheader("Statistics")
     st.write("Enter the numbers separated by commas (e.g., 1, 2, 3, 4, 5):")


