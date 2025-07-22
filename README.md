# ☕ Django Chai Detail Project – Relationship Implementation

This Django project demonstrates the use of **One-to-One**, **One-to-Many**, and **Many-to-Many** relationships through a real-world chai (tea) listing and review system. It allows users to add chai items, associate them with stores and locations, and post reviews.

---

## 🧩 Core Features

- ✅ Add Chai with Name, Description, Image, Type
- ✅ Add Store and Location information
- ✅ Add Reviews for each Chai (linked to User)
- ✅ Upload and display Chai images
- ✅ Django Admin support for managing data
- ✅ Template-based views using Django's templating system
- ✅ Tailwind or static styling supported

---

## 🔗 Relationships Used

- **One-to-One**  
  Example: `ChaiCertificate` linked uniquely to a `Chai`

- **One-to-Many**  
  Example: One `Chai` has many `ChaiReview`s (ForeignKey)

- **Many-to-Many**  
  Example: A `Chai` can be available in multiple `Store`s

---

## 🛠️ Tech Stack

- **Backend**: Django 5.x
- **Database**: SQLite (default)
- **Frontend**: HTML + CSS (or Tailwind)
- **Image Uploads**: Stored in `/media`
- **Version Control**: Git & GitHub

---


