# Module 1 Homework: Docker & SQL — Solutions

## Question 1. Understanding Docker images

What's the version of `pip` in the `python:3.13` image?

- [x] 25.3
- [ ] 24.3.1
- [ ] 24.2.1
- [ ] 23.3.1

---

## Question 2. Understanding Docker networking and docker-compose

Which `hostname` and `port` should pgAdmin use to connect to the Postgres database?

- [ ] postgres:5433
- [ ] localhost:5432
- [ ] db:5433
- [ ] postgres:5432
- [x] db:5432

---

## Question 3. Counting short trips

For trips in November 2025 with `trip_distance <= 1` mile:

- [ ] 7,853
- [x] 8,007
- [ ] 8,254
- [ ] 8,421

---

## Question 4. Longest trip for each day

Pick-up day with the longest trip distance (only considering `trip_distance < 100` miles):

- [x] 2025-11-14
- [ ] 2025-11-20
- [ ] 2025-11-23
- [ ] 2025-11-25

---

## Question 5. Biggest pickup zone

Pickup zone with the largest `total_amount` (sum of all trips) on **November 18th, 2025**:

- [x] East Harlem North
- [ ] East Harlem South
- [ ] Morningside Heights
- [ ] Forest Hills

---

## Question 6. Largest tip

For passengers picked up in **"East Harlem North"** in November 2025, which drop-off zone had the largest tip?

- [ ] JFK Airport
- [x] Yorkville West
- [ ] East Harlem North
- [ ] LaGuardia Airport

---

## Question 7. Terraform Workflow

Correct sequence:

- [ ] terraform import, terraform apply -y, terraform destroy
- [ ] teraform init, terraform plan -auto-apply, terraform rm
- [ ] terraform init, terraform run -auto-approve, terraform destroy
- [x] terraform init, terraform apply -auto-approve, terraform destroy
- [ ] terraform import, terraform apply -y, terraform rm
