import streamlit as st

skill_col_size = 5


info = {
    "name": "Gopi Vardhan Gunta",
    "location": "Tallahassee, Florida",
    "brief" : """
            I am a Master’s student in Data Science at Florida State University with a passion for leveraging machine learning, data engineering, and analytics to solve real-world challenges. 
    Currently interning as a Finance Analyst at Aramark, I have automated workflows, developed dynamic dashboards, and streamlined operations to enhance data-driven decision-making. 
    My academic coursework, hands-on projects, and internship experience have equipped me with expertise in Python, SQL, and advanced machine learning techniques, enabling me to handle complex datasets and derive actionable insights. 
    I thrive in collaborative environments and enjoy solving intricate problems with innovative approaches, whether it's building scalable data pipelines or exploring cutting-edge AI technologies. 
    Outside of work, I stay active at the gym, love traveling to new destinations, and enjoy experimenting with creative recipes in the kitchen. 
    As I approach graduation, I am eager to apply my skills and passion for data science to contribute meaningfully to innovative teams in the field of data and AI.
    """,
    "fun_facts": [
        "I'm captivated by the endless possibilities of AI and its transformative potential to reshape the world.",
      "I thrive on solving complex problems and collaborating with cross-functional teams to bring innovative ideas to life.",
      "When I'm not diving into data projects, you'll find me hitting the gym, exploring new travel destinations, or perfecting a new recipe in the kitchen as an avid home chef."

    ]
}

skills = [
    "Python", "SQL", "R", "Java", "C++",
    "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "PyTorch",
    "Hugging Face Transformers", "Flask", "Streamlit", "FastAPI",
    "SQLAlchemy", "Matplotlib", "Seaborn", "Plotly", "Dash",
    "Tableau", "Power BI", "NLTK", "spaCy", "Tfidf Vectorizer",
    "Naive Bayes", "KNN", "Decision Trees", "SVM", "Neural Networks",
    "GANs", "BERT", "GPT", "RAGs ",
    "MongoDB", "PostgreSQL", "Snowflake", "BigQuery", "Oracle",
    "Docker", "Kubernetes", "Airflow", "MLflow", "Version Control", 
    "Agile Methodology",  "LangChain"
]
#   "Apache Spark", "Databricks", "Hadoop", 
    # "AWS (S3, EC2, SageMaker)", "GCP (BigQuery, AutoML)", "LangChain", 
    # "Graph Databases (Neo4j)", "NetworkX", "Prophet", "Statsmodels"
experience = {
    "aramark": {
        "company": "Aramark",
        "title": "Finance Analyst Intern",
        "duration": "Aug 2024 – Present",
        "location": "Tallahassee, FL",
        "details": """
        - Generated and analyzed daily sales reports, providing actionable insights to improve revenue streams.
        - Utilized advanced Excel functions, including VLOOKUP, Pivot Tables, and Power BI for visualization and reporting.
        - Prepared and uploaded sales data for GFF systems, ensuring accurate financial tracking and reporting.
        - Created and distributed AR snapshots to track outstanding invoices and payment trends.
        - Developed automated templates for invoice generation, reducing manual workload by 30%.
        - Supported month-end closing activities, including variance analysis, financial forecasting, and balance sheet reconciliations.
        """
    },
    "visakhapatnam_port_trust": {
        "company": "Visakhapatnam Port Trust",
        "title": "Software Development Intern",
        "duration": "May 2022 – Jul 2022",
        "location": "Visakhapatnam, India",
        "details": """
        - Designed and developed a scalable web application using Flask and MongoDB, improving user engagement by 30%.
        - Enhanced UI with intuitive design elements, leading to a 40% increase in user satisfaction.
        - Optimized data workflows and interactions, improving operational efficiency by 25%.
        """
    },
    "zawn": {
        "company": "ZAWN",
        "title": "Software Engineering Intern",
        "duration": "Feb 2021 – Apr 2021",
        "location": "Ottawa, Canada",
        "details": """
        - Identified critical issues in the alert and complaint submission pages, reducing customer complaints by 30%.
        - Revamped UI with improved design elements, increasing user engagement by 15%.
        - Led a team in implementing automated testing scripts, reducing manual testing time significantly.
        """
    }
}

education = [
    {
        "degree": "Master of Science in Data Science",
        "school": "Florida State University",
        "year": "Expected May 2025",
        "details": """
        - GPA: 3.91
        - Coursework includes Big Data Analytics, Advanced Machine Learning, and Deep Learning.
        """
    },
    {
        "degree": "Bachelor of Technology in Computer Science",
        "school": "Gitam University",
        "year": "Graduated May 2023",
        "details": """
        - GPA: 3.34
        - Focused on software development and data science with academic distinction.
        """
    }
]

projects = [
    {
        "title": "Retrieval-Augmented Generation (RAG) System",
        "description": """
        **Problem**: Accessing relevant information from large datasets often requires efficient retrieval and contextual generation capabilities.

        **Approach**:
        - Designed a RAG pipeline using **Ollama**, integrating embeddings with a semantic search to retrieve the most relevant documents for a given query.
        - Implemented a query-data pipeline leveraging **vector databases** for fast and accurate information retrieval.
        - Enhanced the system with **custom prompt engineering** to ensure context-aware responses.

        **Solution**:
        - Built a scalable application that dynamically retrieves and generates responses based on user queries.
        - Integrated the solution into a user-friendly interface for seamless interaction.

        **Key Impact**: Demonstrated advanced retrieval capabilities, enabling efficient document processing and interactive query handling.
        """,
        "link": "https://github.com/GOPIVARDHAN1965/rag_ollama_project"
    },
    {
        "title": "Interactive COVID-19 Dashboard",
        "description": """
        **Problem**: Visualizing global COVID-19 statistics in real time for effective monitoring and decision-making.

        **Approach**:
        - Built a responsive dashboard using the **Dash library** and **Plotly** for interactive visualizations.
        - Processed real-time data from APIs to present global and country-specific COVID-19 statistics, including confirmed cases, recoveries, and fatalities.
        - Integrated filtering options for region-specific and time-series analysis.

        **Solution**:
        - Designed an interactive interface displaying charts, maps, and KPIs to enable data exploration.
        - Automated data fetching and pre-processing to keep the dashboard updated dynamically.

        **Key Impact**: Provided an accessible and visually appealing platform for understanding COVID-19 trends, aiding decision-makers and researchers.
        """,
        "link": "https://github.com/GOPIVARDHAN1965/covid19_dashboard"
    },
    {
        "title": "Tally Code Brewers Hackathon (Semifinalist)",
        "description": """
        **Problem**: Existing quiz platforms lacked customization options and security measures, leading to inefficiencies in managing quizzes.

        **Approach**:
        - Designed a secure, scalable quiz platform using **Flask** and **MongoDB**.
        - Implemented dynamic quiz generation, real-time scoring, and customizable quiz templates.
        - Introduced features to prevent quiz re-attempts and ensured secure handling of user data.

        **Solution**:
        - Developed the platform within a tight hackathon timeline, earning semifinalist status among over 200 participants.

        **Key Impact**: Demonstrated the ability to design robust systems under competitive and time-constrained environments.
        """,
        "link": "https://github.com/Bidisha28/TallyCode-QuizCreationPlatform"
    },
    {
        "title": "Shopping Recommendation and Report Generation System",
        "description": """
        **Problem**: Retailers often miss cross-selling opportunities due to a lack of personalized recommendations for customers.

        **Approach**:
        - Designed a **K-Nearest Neighbors (KNN)** based recommendation system that analyzed past purchase histories to suggest complementary products.
        - Implemented dynamic report generation using **Python** to uncover spending patterns and customer segmentation.

        **Solution**:
        - Increased cross-sell opportunities by **25%** through accurate recommendations.
        - Automated spend analysis reports to help retailers identify and target high-value customers effectively.

        **Key Impact**: Improved customer experience and boosted revenue through personalized recommendations and actionable insights.
        """,
        "link": "https://github.com/GOPIVARDHAN1965/final_sem_project"
    },
    {
        "title": "Sentiment Analysis of Restaurant Reviews",
        "description": """
        **Problem**: Businesses often struggle to understand customer feedback due to the sheer volume of reviews, making it difficult to assess overall sentiment.

        **Approach**:
        - Built a sentiment analysis model using **Pandas**, **NumPy**, and **Scikit-learn** to classify restaurant reviews as positive or negative.
        - Preprocessed the data by removing noise and applied **TF-IDF Vectorization** for text representation.

        **Solution**:
        - Trained a **Logistic Regression model**, achieving an accuracy of **88%** on test data.
        - Deployed the model using **Flask** for real-time sentiment predictions, helping restaurant owners prioritize feedback.

        **Key Impact**: Enabled businesses to enhance service quality and optimize marketing strategies based on sentiment analysis.
        """,
        "link": "https://github.com/GOPIVARDHAN1965/sentiment_analysis"
    },
    {
        "title": "Movie Recommendation System",
        "description": """
        **Problem**: Users often struggle to discover movies aligned with their preferences due to a lack of personalized recommendations.

        **Approach**:
        - Built a content-based recommendation system using **Python** and **Pandas**.
        - Extracted metadata such as genre, cast, and keywords to compute similarity scores using the **Cosine Similarity** algorithm.

        **Solution**:
        - Designed an interactive system that suggests movies based on user-selected preferences and past watch history.
        - Deployed the application for public use, allowing users to explore tailored movie recommendations.

        **Key Impact**: Improved user experience and engagement by simplifying the movie discovery process.
        """,
        "link": "https://github.com/GOPIVARDHAN1965/movie_recomend"
    },
    {
        "title": "Flask Task Manager Application",
        "description": """
        **Problem**: Teams and individuals often face challenges in managing tasks efficiently with basic to-do list tools.

        **Approach**:
        - Developed a task management web application using **Flask** and **SQLite**.
        - Included features like user authentication, task creation, due date tracking, and task categorization.

        **Solution**:
        - Delivered a user-friendly platform that streamlines task management workflows.
        - Allowed users to efficiently track and prioritize tasks, leading to improved productivity.

        **Key Impact**: Enhanced organizational efficiency through a customizable and intuitive task manager.
        """,
        "link": "https://github.com/GOPIVARDHAN1965/flask_task"
    }
]


contact = {
    "phone": "+1-234-564-0891",
    "email": "gg23f@fsu.edu",
    "linkedin": "https://www.linkedin.com/in/gopi-vardhan-gunta-6332b418a/",
    "github": "https://github.com/GOPIVARDHAN1965",
    "leetcode": "https://leetcode.com/gopivardhangunta/"
}