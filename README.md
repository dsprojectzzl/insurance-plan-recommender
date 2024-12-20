*Project Name*

**Insurance Plan Recommendation System**

**Overview**

    This project provides an end-to-end system for recommending and displaying insurance plans based on user-provided health data. The system includes a backend API powered by Flask and a frontend interface for user interaction.

**Features**

    1. Data Submission: Users can submit health-related data, including:

        Heart Rate (BPM)

        Sleep Duration (Hours)

        Physical Activity Steps

        Mood Rating

    2. Insurance Plan Recommendation: The backend calculates a recommendation score using a trained machine learning model and returns a plan UID.

    3. Plan Details Retrieval: The frontend fetches detailed information about the recommended plan from the backend.

    4. Model Update Logic: The backend updates the machine learning model every 7 days to incorporate new data.

**Technologies Used**

***Backend***

    Python

    Flask

    pyodbc (Database interaction)

    pandas, scikit-learn (Data processing and ML model)

***Frontend***

    HTML, CSS, JavaScript

***Database***

    Microsoft Azure SQL Database

***Project Structure***

    project/
    ├── README.md                       # Documentation about the project
    ├── .env                            # Environment variables (credentials, secrets)
    ├── requirements.txt                # Python dependencies
    ├── app.py                          # Flask app entry point
    ├── backend/                        # Backend logic and database handling
    │   ├── __init__.py                 # Initializes the backend module
    │   ├── database.py                 # Database connection and queries
    │   ├── logic.py                    # Business logic (e.g., score calculation, insurance mapping)
    │   ├── model.py                    # Machine learning model handling (training and predictions)
    │   ├── scheduler.py                # Scheduler logic for periodic model updates
    ├── frontend/                       # Frontend files
    │   ├── index.html                  # Data submission form
    │   ├── input_style.css             # Data submission style
    │   ├── result.html                 # Insurance plan details page
    │   ├── style.css                   # Insurance display style
    │   ├── app.js                      # Frontend logic for API calls
    ├── models/                         # Saved ML models
    │   └── trained_model.pkl           # Pickled trained ML model
    ├── tests/                          # Unit tests
    │   ├── __init__.py                 # Initializes the tests module
    │   ├── test_app.py                 # Tests for Flask endpoints
    │   ├── test_database.py            # Tests for database functions
    │   ├── test_logic.py               # Tests for backend logic
    │   ├── test_scheduler.py           # Tests for scheduler logic


**Endpoints**

    1. Predict Insurance Plan

    URL: /predict

    Method: POST

    Description: Predicts an insurance plan based on user data.

    Request Body:

    {
        "Heart_Rate_BPM": 85,
        "Sleep_Duration_Hours": 7.5,
        "Physical_Activity_Steps": 12000,
        "Mood_Rating": 8
    }

    Response:

    {
        "plan_uid": 2
    }

    2. Get Insurance Plan Details

    URL: /plans/<int:plan_uid>

    Method: GET

    Description: Retrieves details of all insurance plans from the database and marks the plan matching the provided plan_uid as the recommended plan.

    Response:
    [
        {
            "UID": 1,
            "Plan": "Standard",
            "Premium": "$100-$200",
            "Deductible": "$1000",
            "Coverage": "Limited coverage",
            "AdditionalBenefits": "None",
            "is_recommended": false
        },
        {
            "UID": 2,
            "Plan": "Standard Plus",
            "Premium": "$200-$400",
            "Deductible": "$500",
            "Coverage": "Comprehensive coverage for chronic conditions",
            "AdditionalBenefits": "Free gym membership",
            "is_recommended": true
        },
        {
            "UID": 3,
            "Plan": "Premium",
            "Premium": "$400-$600",
            "Deductible": "$200",
            "Coverage": "Full coverage",
            "AdditionalBenefits": "Priority support",
            "is_recommended": false
        }
    ]


**Future Improvements**

    Enhance the machine learning model for more accurate recommendations.

    Add user authentication and role-based access.

    Improve frontend design with a modern UI framework.

    Deploy the application to a cloud platform like AWS or Azure.

**Contact**

    For any questions or support, contact:

    Email: liuzhy1403@gmail.com

