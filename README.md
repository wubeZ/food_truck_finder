# Food Truck Finder

## 🌟 Introduction
Welcome to Food Truck Finder! Our platform is designed to help you discover the best street food options, particularly food trucks, in San Francisco. Whether you're a local foodie or a visitor exploring the city, Food Truck Finder has got you covered.

## 🎯 Problem Statement
San Francisco boasts a vibrant street food scene with numerous food trucks offering a variety of delicious cuisines. However, finding these hidden gems can be challenging, especially for newcomers or those unfamiliar with the city's layout. Food Truck Finder aims to solve this problem by providing a convenient way to locate and explore food trucks across San Francisco.

San Francisco's food truck open dataset (csv) is included in this [repo](https://github.com/wubeZ/food_truck_finder/blob/main/food_truck_finder/data/food-truck-data.csv). 

## ⚙️ Tech Stack Used

- **Django**: A powerful web framework for building robust web applications.
- **MongoDB**: A flexible and scalable NoSQL database for storing and managing data.
- **Leaflet.js**: An open-source JavaScript library for interactive maps, allowing users to visualize food truck locations.
- **Pytest**: A testing framework for writing and executing unit tests to ensure code quality and reliability.

## 🏃‍♂️ How to Run

To run Food Truck Finder locally, follow these steps:

1. **Clone the Repository**: Clone the Food Truck Finder repository to your local machine.
   ```bash
   git clone https://github.com/wubeZ/food_truck_finder.git
   ```
2. **Create a Virtual Environment**: Set up a virtual environment for the project to isolate dependencies.
   ```bash
   python -m venv env
   ```
3. **Activate the Virtual Environment**: Activate the virtual environment to install and run dependencies locally.

   - On Windows:
    ```bash
      .\env\Scripts\activate
    ```
   - On MacOS/Linux:
    ```bash
      source env/bin/activate
    ```
4. **Install Dependencies**: Install the required dependencies using the provided requirements.txt file.
   ```bash
   pip install -r requirements.txt
   ```
5. **Set Up MongoDB Atlas**: Create a MongoDB Atlas account and obtain the MongoDB URI. Replace the placeholder values in the `.env.example` file with your actual MongoDB URI and any other required environment variables. Rename the file to `.env`.
6. **Import Data into MongoDB**: Use custom commands to import food truck data from a CSV file into MongoDB.
   ```bash
   cd food_truck_finder
   python manage.py import_csv
   ```
7. **Run the Application**: Start the Django development server to run the Food Truck Finder application.
   ```bash
   python manage.py runserver
   ```
Open your web browser and navigate to http://localhost:8000 to access Food Truck Finder.


## 📸 Screen Shot Preview

- **🏠 Home Page**:
  <div style="display:flex; justify-content: center;">
    <img src="https://github.com/wubeZ/food_truck_finder/blob/main/design/homepage1_design.png" alt="Home Page 1" width="400" height="300">
    <img src="https://github.com/wubeZ/food_truck_finder/blob/main/design/homepage2_design.png" alt="Home Page 2" width="400" height="300">
  </div>
  
- **📝 Details Page**:
  <div style="text-align:center;">
    <img src="https://github.com/wubeZ/food_truck_finder/blob/main/design/details_design.png" alt="Details Page" width="400" height="300">
  </div>
  
- **🔍 Search Result Page**:
  <div style="text-align:center;">
    <img src="https://github.com/wubeZ/food_truck_finder/blob/main/design/search_results_design.png" alt="Search Result Page" width="400" height="300">
  </div>

- **🚨 Error Page**:
  <div style="text-align:center;">
    <img src="https://github.com/wubeZ/food_truck_finder/blob/main/design/error_design.png" alt="Error Page" width="400" height="300">
  </div>




## 🛠️ Workflow

1. **🎨 Configure Django with Tailwind CSS**: Enhance the user interface using Tailwind CSS, a utility-first CSS framework.
2. **🔍 Data Preprocessing**: Extract and preprocess relevant data attributes from the dataset for storage in MongoDB.
3. **🛠️ Custom Commands**: Develop a custom command to import data from the CSV file into MongoDB collection.
4. **🖥️ Views and URLs**: Implement view logic and define URL patterns to handle user requests and responses.
5. **✅ Unit Testing with Pytest**: Write comprehensive unit tests using Pytest to ensure code functionality and reliability.
6. **🎨 UI/UX Refinement**: Continuously refine the user interface and user experience to optimize usability and engagement.

## 🚀 Things to Improve

- **🔧 GitHub Action Workflow**: Address issues related to setting up GitHub Action workflows, particularly regarding database connectivity with MongoDB Atlas.
- 🐳 **Containerization with Docker**: Containerize the project using Docker to ensure consistency in development and deployment environments.
- 🚀 **Deployment on Hosting Service**: Consider deploying the containerized application on a hosting service for improved scalability and availability.
- 🗺️ **Consider using [OSRM (Open Source Routing Machine)](https://project-osrm.org/)**: Unlike the Haversine formula, which calculates distances based on spherical geometry, OSRM takes into account real-world road networks, traffic conditions, and other factors to provide precise routing and distance calculations.


## 📧 Contact

For questions, feedback, or collaboration opportunities, please reach out to [Wubshet Zeleke](mailto:wubezeleke@gmail.com).

