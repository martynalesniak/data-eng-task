# MovieLens Data Analysis with Docker and PostgreSQL

## Overview
This project uses Docker to set up an environment for analyzing the MovieLens dataset with PostgreSQL as the database. It includes two Docker containers: one for the PostgreSQL database and another for running Python scripts that handle data analysis. The system imports the MovieLens dataset, and the analysis offers insights into movie ratings, user activity, and popular movie genres.

## Technologies

Technologies used:

- **Docker** v27.2.0
- **PostgreSQL** v17.0
- **Python** v3.12.1
  - **pandas** 
  - **psycopg2**
- **Jupyter** v7.2.2

## Dataset

The analysis is based on the MovieLens dataset, which is a dataset used for movie recommendations. The dataset includes user ratings of movies, movie metadata (titles, genres, etc.), and timestamps. 

- **Dataset Source**: [MovieLens Dataset](https://grouplens.org/datasets/movielens/latest/)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/martynalesniak/data-eng-task.git
   cd <path-to-repository-directory>
2. **Ensure Docker and Docker Compose are installed**
    You can run following commands:
    ```bash
    docker --version
    docker-compose --version
3. **Run the containers**
    ```bash
    docker-compose up
4. Open your web browser and go to page http://localhost:8888. Open the transform.ipynb file, use the provided functions create_tables() and load_data() to import MovieLens dataset into the PostgreSQL database.
5. Use the functions in the notebook to answer the analysis questions.

## Description of the solution

My solution consists of two docker containers configured using a 'docker-compose.yml' file.

### Containers

- PostgreSQL Container: This container runs a PostgreSQL database where the MovieLens dataset is imported and stored.
- Analytics Container:  The second container, located in the `analytics` subfolder, runs Python and Jupyter Notebook. It is used for importing datasets into the PostgreSQL database and analyzing the data using Python. This container connects to the PostgreSQL container to load data and execute queries.

### Dockerfile

The `Dockerfile` in the `analytics` subfolder defines the environment setup for running Python scripts and Jupyter Notebook.

### Data Analysis

All data loading and analysis is done in the `transform.ipynb` file. This Jupyter Notebook contains:

- Functions to create tables in the PostgreSQL database.
- Functions to load the MovieLens dataset into the database.
- SQL queries and Python scripts (using `psycopg2`) to answer the required questions.

All the answers to the analysis questions are documented directly in this notebook using Markdown.