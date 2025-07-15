# Moohaar - Your Online Store Builder

**Moohaar** is a powerful e-commerce platform designed to empower entrepreneurs and small businesses, with a special focus on the Pakistani market. Inspired by the ease-of-use of platforms like Shopify, Moohaar aims to provide a "Level 5" user experience that is modern, minimal, and mobile-first, allowing anyone to create a professional online store without needing technical skills or a large budget.

**Our Vision:** "ویب سائٹ آج اور ابھی" (Your Website, Today, Right Now) - To make e-commerce accessible to everyone, enabling them to build their brand and sell online effortlessly.

---

## ✨ Key Features & Vision

The goal is to build a complete, self-service e-commerce platform. Here is a summary of the current features and the future roadmap.

### Core Platform (for Store Owners)
* **User Management:** Secure user registration, login, logout, and password reset functionality.
* **One Store Per Account:** A simplified user flow where each Moohaar account can create and manage one online store.
* **Modern Admin Dashboard:** A professional, mobile-friendly dashboard inspired by Shopify and the "ElaAdmin" theme, featuring a sidebar layout, light/dark modes, and analytics widgets (currently with placeholder data).
* **Store Management Panel:** A dedicated area for managing an individual store, including an overview, product management, and theme selection.
* **Product Management:** Full CRUD (Create, Read, Update, Delete) functionality for a store's products, with styled forms and product lists.
* **Theme Selection System:** A system allowing users to choose and apply different themes to their storefront. Currently supports one theme ("EShopper").

### Storefront (for Customers)
* **Dynamic Theming:** The public-facing store's appearance is determined by the theme selected by the store owner.
* **Integrated "EShopper" Theme:** A professional, responsive storefront theme with a homepage and product detail page has been integrated.

---

## 🛠️ Technology Stack

* **Backend:** Django
* **Frontend:** HTML5, CSS3 with CSS Variables, JavaScript
* **Admin Panel Theme:** Based on "ElaAdmin" (Bootstrap)
* **Default Storefront Theme:** Based on "EShopper" (Bootstrap)
* **Database:** SQLite (for development)

---

## 🚀 Getting Started

Instructions for a software engineer to set up and run the project locally.

### Prerequisites
* Python 3.x
* Pip (Python package installer)
* Git

### Local Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sufi-hassan-tools/webapp.git](https://github.com/sufi-hassan-tools/webapp.git)
    cd webapp
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    *(Note: We need to create a `requirements.txt` file first. Run `pip freeze > requirements.txt` from your current working directory to create it, then commit it to the repository.)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser** to access the Django Admin (`/admin/`):
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

---

## 🗺️ Future Roadmap

The next major features to build are:

1.  **Shopping Cart & Checkout:** Implement full shopping cart and checkout functionality to allow customers to make purchases.
2.  **Payment Gateway Integration:** Integrate local Pakistani payment gateways like JazzCash and Easypaisa.
3.  **Real Dashboard Analytics:** Connect the dashboard widgets and charts to real data from the Orders and an analytics service.
4.  **Theme Customizer:** Build the "Shopify-like" editor for store owners to customize their chosen storefront theme.
5.  **Expand the Theme Store:** Add more high-quality themes for users to choose from.

