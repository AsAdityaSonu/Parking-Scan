# Parking Scan

Parking Scan is a Python application built using Tkinter, designed for managing and visualizing data from a parking lot detection system. It offers a user-friendly interface with features including a login screen, real-time parking lot status visualization, and detailed reports. The application leverages vision-based technology for cost-effective parking guidance.

## Features

- **Easy Login:** Simple and secure login and registration process.
- **Real-Time Parking Lot Status Visualization:** View the status of parking lots in real-time.
- **User-Friendly Interface:** Intuitive and easy-to-navigate interface.
- **Vision-Based Parking Slot Detection and Classification:** Detect and classify parking slots using image-based analysis.
- **High Efficiency in Parking Slot Detection:** Accurate detection of parking slots with high efficiency.
- **High Accuracy in Parking Slot Occupancy Classification:** Reliable classification of parking slot occupancy.

## Project Description

Parking Scan serves as an interface for Parking Guidance Information (PGI) systems, aimed at providing drivers with information about the nearest parking lots and the number of vacant parking slots. Vision-based solutions are employed as a cost-effective alternative to traditional PGI systems that rely on hardware sensors mounted on each parking slot.

Vision-based systems analyze parking occupancy using images captured by cameras monitoring parking lots. Developing these systems poses challenges such as handling various viewpoints, weather conditions, and object occlusions. Additionally, manual labeling of parking slot locations in images is required, which is sensitive to changes in camera angles, replacements, or maintenance.

This project introduces an algorithm for Automatic Parking Slot Detection and Occupancy Classification (APSD-OC) based solely on input images. The approach involves:
1. Detecting vehicles in a series of parking lot images and applying clustering in a bird's eye view to identify parking slots.
2. Classifying each detected parking slot as occupied or vacant using a specifically trained ResNet34 deep classifier.

The 2-step approach is extensively evaluated on publicly available datasets (PKLot and CNRPark+EXT), demonstrating high efficiency in parking slot detection and a notable degree of robustness against illegal parking or passing vehicles. The trained classifier achieves high accuracy in parking slot occupancy classification.

## About Us

Our project is developed by a dedicated team of students under the guidance of experienced mentors. We aim to create innovative solutions for parking lot management using vision-based technologies.

### Mentors

- Prof. Kulbir Singh
- Dr. Neeru Jindal
- Dr. Sandeep Mandia
- Dr. Shishir Maheshwari

### Students

- **Aditya Pandey** - [GitHub Profile](https://github.com/asadityasonu)
- **Vaibhav Baldeva**
- **Mridula Pal** 
- **Nitika Joshi**
- **Dhwani** 

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AsAdityaSonu/Parking-Scan.git
   ```

2. **Install Dependencies:**


   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   ```bash
   ParkingScan.py
   ```

## Contributing

We welcome contributions to improve the project! To contribute:

1. **Open an Issue:** If you find a bug or have a feature request, please [open an issue](https://github.com/AsAdityaSonu/Parking-Scan/issues) on GitHub.

2. **Submit a Pull Request:** If you want to propose changes, please fork the repository, make your changes, and submit a [pull request](https://github.com/AsAdityaSonu/Parking-Scan/pulls). Ensure that your code adheres to the project's coding standards and includes appropriate tests.

3. **Code of Conduct:** Please follow our [Code of Conduct](CODE_OF_CONDUCT.md) when participating in this project.

## Contact

For any questions or feedback, please contact [asadityasonu@gmail.com](mailto:asadityasonu@gmail.com).

