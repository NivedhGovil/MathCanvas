
# Create grpahs. 
# Input n numbers. Find the mean, median, and mode of the numbers. Create a histogram of the numbers.
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.markdown("""
<style>
    .stApp {
        background-color: #c9f3f5;
        font-family: 'sans-serif';
    }
</style>
""", unsafe_allow_html=True)


st.title("Math Canvas")
st.write(" Welcome to the Math Canvas, an interactive platform for exploring mathematical concepts through graph plotting and statistical analysis. Let's make math engaging and insightful!")

st.header("Modes")
mode = st.selectbox("Choose the mode:", options = ["Graph Plot" , "Statistics", "Projectile Motion" ])

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
    elif equation_type == "ECG":
                st.subheader("ECG Equation Plotter")
                amplitude = st.slider(label="Amplitude:", min_value=1, max_value=50, value=10)
                frequency = st.slider(label="Frequency:", min_value=1, max_value=50, value=10)
                x = np.linspace(-4*np.pi, 4*np.pi, 2000)
                y = amplitude * np.tan(frequency * x)
                fig, ax = plt.subplots(figsize=(20, 15))
                ax.set_title("ECG Wave" )
                ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
                ax.axvline(x=0, color='black', linestyle='-', linewidth=1)
                ax.grid(True, alpha=0.3)
                ax.set_xticks([-4*np.pi, -3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
                ax.set_xticklabels([r"$-4\pi$", r"$-3\pi$", r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"], rotation=0 , color='black', fontsize = 20)
                ax.plot(x, y,  color='blue', linewidth=1, linestyle='-', label="Tangent Wave" ) 
                st.pyplot(fig, use_container_width=True)
elif mode == "Statistics": 
     st.subheader("Statistics")
     observations = st.selectbox("No. of observations", options = ["3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"])
     if observations == "3":
         num1 = st.number_input("Enter the first number:")
         num2 = st.number_input("Enter the second number:")
         num3 = st.number_input("Enter the third number:")
         numbers = [num1, num2, num3]
        
         st.write("Mean:", np.mean(numbers))
         st.write("Standard Deviation:", np.std(numbers))
         st.write("Variance:", np.var(numbers))
         st.write("Median:", np.median(numbers))
         st.write("Minimum:", np.min(numbers))
         st.write("Maximum:", np.max(numbers))
         st.write("Range:", np.max(numbers) - np.min(numbers))

         values = [np.mean(numbers), np.std(numbers), np.median(numbers), np.min(numbers), np.max(numbers), np.max(numbers) - np.min(numbers)]

         fig, ax = plt.subplots(figsize=(10, 5))
         ax.bar(["Mean", "Standard Deviation", "Median", "Minimum", "Maximum", "Range"], [np.mean(numbers), np.std(numbers), np.median(numbers), np.min(numbers), np.max(numbers), np.max(numbers) - np.min(numbers)], color="mediumseagreen", edgecolor="black", alpha=0.8)
         y= np.linspace(0, max(values) + 5, 100)
         ax.set_title("Statistics", fontsize=20)
         ax.set_ylabel("Values", fontsize=15)
         ax.set_xlabel("Measures", fontsize=15)
         plt.xticks(rotation=15, ha="right") # Sets rotation of x-axis labels to 15 degrees right. 
         st.pyplot(fig, use_container_width=True)

     elif observations == "4":
         num1 = st.number_input("Enter the first number:")
         num2 = st.number_input("Enter the second number:")
         num3 = st.number_input("Enter the third number:")
         num4 = st.number_input("Enter the fourth number:")
         numbers = [num1, num2, num3, num4]
         
         st.write("Mean:", np.mean(numbers))
         st.write("Standard Deviation:", np.std(numbers))
         st.write("Variance:", np.var(numbers))
         st.write("Median:", np.median(numbers))
         st.write("Minimum:", np.min(numbers))
         st.write("Maximum:", np.max(numbers))
         st.write("Range:", np.max(numbers) - np.min(numbers))
     elif observations == "5":
        num1 = st.number_input("Enter the first number:")
        num2 = st.number_input("Enter the second number:")
        num3 = st.number_input("Enter the third number:")
        num4 = st.number_input("Enter the fourth number:")
        num5 = st.number_input("Enter the fifth number:")
        numbers = [num1, num2, num3, num4, num5]
        
        st.write("Mean:", np.mean(numbers))
        st.write("Standard Deviation:", np.std(numbers))
        st.write("Variance:", np.var(numbers))
        st.write("Median:", np.median(numbers))
        st.write("Minimum:", np.min(numbers))
        st.write("Maximum:", np.max(numbers))
        st.write("Range:", np.max(numbers) - np.min(numbers))
     elif observations == "6":
        num1 = st.number_input("Enter the first number:")
        num2 = st.number_input("Enter the second number:")
        num3 = st.number_input("Enter the third number:")
        num4 = st.number_input("Enter the fourth number:")
        num5 = st.number_input("Enter the fifth number:")
        num6 = st.number_input("Enter the sixth number:")
        numbers = [num1, num2, num3, num4, num5, num6]
        
        st.write("Mean:", np.mean(numbers))
        st.write("Standard Deviation:", np.std(numbers))
        st.write("Variance:", np.var(numbers))
        st.write("Median:", np.median(numbers))
        st.write("Minimum:", np.min(numbers))
        st.write("Maximum:", np.max(numbers))
        st.write("Range:", np.max(numbers) - np.min(numbers))
     elif observations == "7":
        num1 = st.number_input("Enter the first number:")
        num2 = st.number_input("Enter the second number:")
        num3 = st.number_input("Enter the third number:")
        num4 = st.number_input("Enter the fourth number:")
        num5 = st.number_input("Enter the fifth number:")
        num6 = st.number_input("Enter the sixth number:")
        num7 = st.number_input("Enter the seventh number:")
        numbers = [num1, num2, num3, num4, num5, num6, num7]
        
        st.write("Mean:", np.mean(numbers))
        st.write("Standard Deviation:", np.std(numbers))
        st.write("Variance:", np.var(numbers))
        st.write("Median:", np.median(numbers))
        st.write("Minimum:", np.min(numbers))
        st.write("Maximum:", np.max(numbers))
        st.write("Range:", np.max(numbers) - np.min(numbers))
     elif observations == "8":
        num1 = st.number_input("Enter the first number:")
        num2 = st.number_input("Enter the second number:")
        num3 = st.number_input("Enter the third number:")
        num4 = st.number_input("Enter the fourth number:")
        num5 = st.number_input("Enter the fifth number:")
        num6 = st.number_input("Enter the sixth number:")
        num7 = st.number_input("Enter the seventh number:")
        num8 = st.number_input("Enter the eighth number:")
        numbers = [num1, num2, num3, num4, num5, num6, num7, num8]
        st.write("Mean:", np.mean(numbers))
        st.write("Standard Deviation:", np.std(numbers))
        st.write("Variance:", np.var(numbers))
        st.write("Median:", np.median(numbers))
        st.write("Minimum:", np.min(numbers))
        st.write("Maximum:", np.max(numbers))
        st.write("Range:", np.max(numbers) - np.min(numbers))
     elif observations == "9":
        num1 = st.number_input("Enter the first number:")
        num2 = st.number_input("Enter the second number:")
        num3 = st.number_input("Enter the third number:")
        num4 = st.number_input("Enter the fourth number:")
        num5 = st.number_input("Enter the fifth number:")
        num6 = st.number_input("Enter the sixth number:")
        num7 = st.number_input("Enter the seventh number:")
        num8 = st.number_input("Enter the eighth number:")
        num9 = st.number_input("Enter the ninth number:")
        numbers = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
        st.write("Numbers:", numbers)
        st.write("Mean:", np.mean(numbers))
        st.write("Standard Deviation:", np.std(numbers))
        st.write("Variance:", np.var(numbers))
        st.write("Median:", np.median(numbers))
        st.write("Minimum:", np.min(numbers))
        st.write("Maximum:", np.max(numbers))
        st.write("Range:", np.max(numbers) - np.min(numbers))
     else:
        num1 = st.number_input("Enter the first number:")
        num2 = st.number_input("Enter the second number:")
        num3 = st.number_input("Enter the third number:")
        num4 = st.number_input("Enter the fourth number:")
        num5 = st.number_input("Enter the fifth number:")
        num6 = st.number_input("Enter the sixth number:")
        num7 = st.number_input("Enter the seventh number:")
        num8 = st.number_input("Enter the eighth number:")
        num9 = st.number_input("Enter the ninth number:")
        num10 = st.number_input("Enter the tenth number:")
        numbers = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
        st.write("Numbers:", numbers)
        st.write("Mean:", np.mean(numbers))
        st.write("Standard Deviation:", np.std(numbers))
        st.write("Variance:", round(np.var(numbers), 2))
        st.write("Median:", np.median(numbers))
        st.write("Minimum:", np.min(numbers))
        st.write("Maximum:", np.max(numbers))
        st.write("Range:", np.max(numbers) - np.min(numbers))
    
elif mode == "Projectile Motion":
    st.subheader("Projectile Motion")
    st.write("This is where you can experiment with projectile motion and see how the angle of projection affects the trajectory of a projectile.")
    theta = st.slider(label="Angle of Projection:", min_value=0, max_value=90, value=45)
    st.write(r"Acceleration due to gravity (m/$s^2$): 9.81")
    u = st.slider(label="Initial Velocity (m/s):", min_value=1, max_value=100, value=10)
    m = st.slider(label="Mass of the projectile (g):", min_value=1, max_value=10000, value=10)
    time_flight = (2 * u * np.sin(np.radians(theta))) / 9.81
    t = st.slider(label="Time (s):", min_value=0, max_value=100, value=2)
    if t > time_flight:
            st.write("Time exceeds the time of flight. Please adjust the time.")
    else: 
            st.write("")
    
    ucos0 = np.round(u * np.cos(np.radians(theta)), 3)
    usin0 = np.round(u * np.sin(np.radians(theta)) - 9.81 * t, 3)
    time_flight = (2 * u * np.sin(np.radians(theta))) / 9.81
    st.write(f"Time of Flight: {time_flight} s")
    range = (u**2 * np.sin(2 * np.radians(theta))) / 9.81
    st.write(f"Range: {range} m")
    max_height = (u**2 * (np.sin(np.radians(theta)))**2) / (2 * 9.81)
    st.write(f"Maximum Height: {max_height} m")
    
    st.title("Projectile Trajectory Plotter")


    g = 9.81  # Acceleration due to gravity (m/s^2)

    angle_rad = np.radians(theta)
    x = np.linspace(0, time_flight, 500)
 
    y = u * np.sin(angle_rad) * x - 0.5 * g * (x**2)

    
    fig, ax = plt.subplots(figsize=(20, 15))
    ax.plot(x, y, color="dodgerblue", linewidth=2, label="Trajectory")

    # Format axes and labels
    ax.set_title(f"Projectile Trajectory ($v_0 = {u}$ m/s, $\\theta = {theta}^\\circ$)")
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Height (m)")
    ax.set_ylim(bottom=0)  
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()

    st.pyplot(fig)
    

# Number of random dart throws
N = 10000

# Generate random (x, y) coordinates between -1 and 1
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

# Point is inside the unit circle if x^2 + y^2 <= 1
inside_circle = (x**2 + y**2) <= 1

# Ratio of points inside circle to total points approx equals (Area of Circle / Area of Square) = pi / 4
pi_estimate = 4 * np.sum(inside_circle) / N

print(f"Estimated Pi with {N} samples: {pi_estimate}")