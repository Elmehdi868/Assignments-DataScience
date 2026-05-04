# TechLabs Sommer26: Machine Learning Fundamentals

Welcome to the learning phase of your Data Science journey! Over the next 6 weeks, you will learn the fundamentals of Python, Data Wrangling, and Machine Learning by solving the **Spaceship Titanic** challenge.

## 🚀 The Mission
The year is 2912. The spaceship *Titanic* was an interstellar passenger liner. While rounding Alpha Centauri, it collided with a space-time anomaly hidden within a dust cloud. Almost half of the passengers were transported to another dimension! 

**Your goal:** Predict which passengers were transported using records recovered from the ship’s damaged computer system.

---

## 📂 Project Structure
```text
├── data/               # Project datasets
│   └── train.csv       
├── src/                # Your code goes here
│   ├── assignment_1.py 
│   ├── assignment_2.py 
│   └── assignment_3.py 
├── tests/              # Automated tests (don't modify)
├── requirements.txt    # Required libraries
└── .github/            # GitHub Actions logic
```

---

## 🛠 Setup Instructions

1. **Fork this repository:**
   Click the **"Fork"** button at the top right of this GitHub page. This creates a copy of the project in your own GitHub account.

2. **Clone your fork:**
   ```bash
   git clone https://github.com/TechLabs-Dusseldorf/Assignments-DataScience.git
   cd Assignments-DataScience
   ```

3. **Set up a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **The Data:**
   The `train.csv` file is already provided in the `data/` folder. You can use this for all your analysis and modeling.
   Please do not delete the file, as you will need it throughout the assignments.

6. **Testing:**
   You can test your own code by running the corresponding terminal command as it is written for each assignment.
   Please do not delete or change the code inside the tests/ folder

---

## 📝 Assignments

### 1. Assignment 1: Data Logistics (Week 2)
Focus: Data loading, cleaning missing values, and type conversion.
- **Run Tests:** `pytest tests/test_assignment_1.py`

### 2. Assignment 2: The Data Scientist (Week 4)
Focus: Feature engineering (vectorization, string parsing) and statistical outlier detection (IQR).
- **Run Tests:** `pytest tests/test_assignment_2.py`

### 3. Assignment 3: The Navigator (Week 6)
Focus: Machine learning pipeline, target encoding, data splitting, and model evaluation.
- **Run Tests:** `pytest tests/test_assignment_3.py`

---

## 📤 How to Submit
1. Create a new branch for each assignment in **your fork**:
   ```bash
   git checkout -b feature/assignment-X-yourname
   ```
2. Commit and push your changes to **your fork**.
3. Open a **Pull Request (PR)** from your fork's branch to the **original repository's `main` branch**.
4. The **GitHub Action** will automatically run the tests.
   - ❌ **Note:** Your PR will **not** be merged into the main repository. This is intentional! The PR serves as your submission, and the test results (green checkmark ✅) are your grade.
