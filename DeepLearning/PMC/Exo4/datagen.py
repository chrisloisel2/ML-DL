import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 100000

# Feature generation
age = np.random.randint(18, 65, n_samples)
education_level = np.random.randint(1, 5, n_samples)  # 1: High School, 2: Associate, 3: Bachelor's, 4: Master's or higher
years_of_experience = np.random.randint(0, 47, n_samples)
industry = np.random.randint(1, 6, n_samples)  # 1 to 5 representing different industries
role = np.random.randint(1, 10, n_samples)  # 1 to 10 representing different roles
hours_worked_per_week = np.random.randint(20, 65, n_samples)
job_satisfaction = np.random.randint(1, 6, n_samples)  # Likert scale 1 to 5
number_of_projects_completed = np.random.randint(0, 20, n_samples)

# Binary target variable 'Performance' generation
# Here, a simple heuristic is used to determine performance. This is purely for example purposes.
# In reality, this should be based on actual performance data.
performance = np.where(
    (years_of_experience >= 5) &
    (education_level >= 2) &
    (hours_worked_per_week > 40) &
    (job_satisfaction > 3) &
    (number_of_projects_completed >= 5),
    1,  # Good Worker
    0   # Bad Worker
)

# Create DataFrame
data = pd.DataFrame({
    'Age': age,
    'Education Level': education_level,
    'Years of Experience': years_of_experience,
    'Industry': industry,
    'Role': role,
    'Hours Worked per Week': hours_worked_per_week,
    'Job Satisfaction': job_satisfaction,
    'Number of Projects Completed': number_of_projects_completed,
    'Performance': performance
})

data.head()

data.to_csv('employee_performance.csv', index=False)
