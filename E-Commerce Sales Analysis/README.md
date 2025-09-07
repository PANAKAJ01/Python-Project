# E-commerce Sales Analysis Dashboard (Python)

This project is a **Python-based E-commerce Sales Analysis Dashboard** that simulates sales data, performs detailed analysis using **Pandas** and **NumPy**, and visualizes insights with **Matplotlib**. It helps understand sales trends, best-selling products, category performance, and monthly revenue trends.

---

## 🚀 Features

- Generate **random e-commerce sales data** with realistic fields:
  - `order_id`, `customer_id`, `product`, `category`, `quantity`, `price`, `date`, `revenue`
- **Key metrics computation**:
  - Total Revenue
  - Total Orders
  - Average Order Value
  - Best-selling Product
  - Best-selling Category
- **Top Products & Categories** insights
- **Monthly sales trends**:
  - Revenue per month
  - Number of orders per month
- **Data visualization** using Matplotlib:
  - Top 5 Products by Revenue (Bar chart)
  - Category Revenue Distribution (Pie chart)
  - Monthly Revenue Trend (Line chart)
  - Monthly Orders (Bar chart)
- Fully **randomized dataset** on every run for simulation purposes.

---

## 📊 Dataset Structure

| Column       | Description                                      |
|-------------|--------------------------------------------------|
| order_id    | Unique identifier for each order                 |
| customer_id | Unique customer identifier                        |
| product     | Product name                                     |
| category    | Product category (Electronics, Sports, Home)     |
| quantity    | Number of units sold                             |
| price       | Price per unit                                   |
| date        | Order date                                       |
| revenue     | Total revenue for the order (quantity × price)   |

---

## 💻 Technologies Used

- Python 3.x  
- Pandas for data manipulation  
- NumPy for numerical calculations  
- Matplotlib for visualizations  

---

## ⚡ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis
