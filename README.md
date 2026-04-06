# 🚀 Data Migration Testing Project

## 📌 Overview
This project simulates real-world data migration testing where data is moved from System A (source) to System B (target).

The goal is to validate that:
- Data is migrated completely
- Data is accurate
- Transformations are correctly applied

---

## 🧠 Business Context
A client migrated customer and order data to a new system.

If migration is incorrect:
- Reports become unreliable
- Business decisions become wrong
- Customer data may be lost or corrupted

---

## ⚠️ Risks Identified
- Missing records
- Duplicate records
- Incorrect transformations
- Invalid formats (dates, country names)
- Null values in key fields

---

## 🧪 Testing Performed

### ✔️ Data Validation
- Row count validation
- Schema validation
- Null value checks
- Duplicate checks

### ✔️ Transformation Testing
- Country code → country name
- Date format conversion
- Amount rounding

### ✔️ Business Validation
- Record consistency
- Data integrity

---

## 📂 Project Structure
