# eShop Project

Welcome to the eShop project! This project is aimed at creating an e-commerce platform where users can browse, search for, and purchase various products online.

![eShop Screenshot](https://github.com/waqasbcs/E-shop-project-in-django/blob/main/screenshot/eshop.png)

## Features

- **User Authentication**: Users can create accounts, log in, and log out securely.
- **Product Management**: Admin users can add, edit, and delete products.
- **Product Categories**: Products are organized into categories for easy browsing.
- **Search Functionality**: Users can search for products by name or category.
- **Shopping Cart**: Users can add products to their shopping cart for later purchase.
- **Checkout Process**: Secure checkout process for users to complete their purchases.
- **Order Tracking**: Users can track the status of their orders.
- **Responsive Design**: The platform is responsive and works well on different devices.

## Technologies Used

- **Backend Framework**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (can be replaced with other databases supported by Django)
- **Authentication**: Django Authentication System
- **Payment Processing**: Stripe API
- **Deployment**: Heroku (for deployment on production)

## Setup Instructions

1. Clone the repository: `git clone https://github.com/waqasbcs/E-shop-project-in-django`
2. Navigate to the project directory: `cd eshop-project`
3. Install dependencies: 

pip install -r requirements.txt
4. Apply database migrations:
python manage.py migrate

5. Create a superuser (admin) account:
python manage.py createsuperuser

6. Start the development server:
python manage.py runserver

7. Access the application at `http://localhost:8000` in your web browser.

## Configuration

1. Set up environment variables:
- Create a `.env` file in the project root directory.
- Define the following variables:
  ```
  SECRET_KEY=your_django_secret_key
  DEBUG=True
  DATABASE_URL=sqlite:///db.sqlite3
  STRIPE_SECRET_KEY=your_stripe_secret_key








