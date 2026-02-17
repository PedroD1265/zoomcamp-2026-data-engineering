# Module 4 Homework: Analytics Engineering with dbt

## Question 1: dbt Lineage and Execution

**Answer:** **`int_trips_unioned` only**

### Explanation:

The command:

```bash
dbt run --select int_trips_unioned
```

does not include any graph operators (`+`). By default, dbt builds only the explicitly selected model.

To include upstream dependencies (such as staging models), we would need:

```bash
dbt run --select +int_trips_unioned
```

To include downstream dependencies, we would use:

```bash
dbt run --select int_trips_unioned+
```

Since no graph operators are present, only the `int_trips_unioned` model is executed.

---

## Question 2: dbt Tests

**Answer:** **dbt will fail the test, returning a non-zero exit code**

### Explanation:

The `accepted_values` test enforces strict validation of column values. Given:

```yaml
columns:
  - name: payment_type
    data_tests:
      - accepted_values:
          arguments:
            values: [1, 2, 3, 4, 5]
            quote: false
```

If a new value `6` appears in the data, it violates the defined constraint.

By default, dbt tests have `severity: error`. Therefore, when the invalid value is detected, dbt:

* Flags the failing rows
* Marks the test as failed
* Exits with a non-zero exit code

This behavior ensures data quality issues are caught immediately.

### Verification Query:

```sql
SELECT payment_type, COUNT(*)
FROM `your_project.your_dataset_prod.stg_yellow_tripdata`
WHERE payment_type = 6
GROUP BY payment_type;
```

---

## Question 3: Counting Records in `fct_monthly_zone_revenue`

**Answer:** **12,184**

### Query Used:

```sql
SELECT COUNT(*) 
FROM `your_project.your_dataset.fct_monthly_zone_revenue`;
```

### Explanation:

After building the full dbt project (with staging filters and aggregation logic applied), the `fct_monthly_zone_revenue` mart contains exactly **12,184 rows**.

This represents the aggregated monthly revenue per zone across both taxi services within the dataset timeframe.

---

## Question 4: Best Performing Zone for Green Taxis (2020)

**Answer:** **East Harlem North**

### Explanation:

To determine the best-performing zone:

* Filter for `service_type = 'Green'`
* Filter for year `2020`
* Group by `pickup_zone`
* Sum `revenue_monthly_total_amount`
* Order descending

**East Harlem North** has the highest total revenue for Green taxis in 2020.

### Verification Query:

```sql
SELECT pickup_zone,
       SUM(revenue_monthly_total_amount) AS total_revenue
FROM `your_project.your_dataset.fct_monthly_zone_revenue`
WHERE service_type = 'Green'
  AND SUBSTR(pickup_monthly, 1, 4) = '2020'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
```

---

## Question 5: Green Taxi Trip Counts (October 2019)

**Answer:** **384,624**

### Query Used:

```sql
SELECT SUM(total_monthly_trips)
FROM `your_project.your_dataset.fct_monthly_zone_revenue`
WHERE service_type = 'Green'
  AND SUBSTR(pickup_monthly, 1, 7) = '2019-10';
```

### Explanation:

After applying transformation logic (including filtering invalid records in staging), summing `total_monthly_trips` for Green taxis in October 2019 returns **384,624 trips**.

This reflects the cleaned and transformed dataset.

---

## Question 6: Build a Staging Model for FHV Data

**Answer:** **43,244,693**

### Explanation:

A new staging model `stg_fhv_tripdata` was created from raw 2019 FHV data.

The transformation logic included:

1. Renaming columns:

   * `PUlocationID` → `pickup_location_id`
   * `DOlocationID` → `dropoff_location_id`
2. Filtering out records where:

   ```sql
   dispatching_base_num IS NULL
   ```

After running:

```bash
dbt run --select stg_fhv_tripdata
```

A count query returned:

```sql
SELECT COUNT(*)
FROM `your_project.your_dataset.stg_fhv_tripdata`;
```

The model contains **43,244,693 records**.
