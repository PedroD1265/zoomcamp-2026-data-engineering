
# Homework 2 – Workflow Orchestration  
**Data Engineering Zoomcamp 2026**

This directory contains the solution for **Homework 2: Workflow Orchestration**, using **Kestra** and **PostgreSQL**.

Below are the quiz questions and the selected answers, with supporting evidence.

---

## Question 1  
**Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file `yellow_tripdata_2020-12.csv` of the `extract` task)?**

![Question 1](question_01.png)

**Answer:**  
- **128.3 MiB**

---

## Question 2  
**What is the rendered value of the variable `file` when the inputs `taxi` is set to `green`, `year` is set to `2020`, and `month` is set to `04` during execution?**

![Question 2](question_02.png)

**Answer:**  
- **`green_tripdata_2020-04.csv`**

---

## Question 3  
**How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?**

![Question 3](question_03.png)

**Answer:**  
- **24,648,499**

---

## Question 4  
**How many rows are there for the Green Taxi data for all CSV files in the year 2020?**

![Question 4](question_04.png)

**Answer:**  
- **1,734,051**

---

## Question 5  
**How many rows are there for the Yellow Taxi data for the March 2021 CSV file?**

![Question 5](question_05.png)

**Answer:**  
- **1,925,152**

---

## Question 6  
**How would you configure the timezone to New York in a Schedule trigger?**

**Answer:**  
- **Add a `timezone` property set to `America/New_York` in the Schedule trigger configuration**
