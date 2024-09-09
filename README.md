
# Cashify - Mobile Selling E-Commerce Website

a simple mobile selling e-commerce website, (it was hard to find a name so I take cashify )

## Project Overview
**Cashify** is a simple e-commerce platform designed for selling mobile phones. Users can browse available phones, add items to their cart, and proceed to checkout. The platform is built with a focus on user-friendly navigation and a smooth purchasing experience.

## Features
- Browse a catalog of mobile phones.
- Add items to the shopping cart.
- View product details and pricing.
- Proceed to checkout with payment options.
- Responsive design for a seamless mobile and desktop experience.

## Prerequisites
To run the project locally, you need the following installed:
- Python 3.x (for the backend)
- Django (as the web framework)
- A web browser for accessing the application
- MySql database

## Installation

1. **Clone the repository**:
   ```powershell
   git clone https://github.com/Ankursinsinwar/Like_cashify.git
   cd cashify
   ```
2. **Create a virtual environment**:
##### Bash
   ```bash
   python3 -m venv env
  source env/bin/activate

```

##### powershell
  ```powershell
    python -m venv env
   .\env\Scripts\Activate
```
3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up MySQL database**:
   - Create a MySQL database named `cashify`.
   - Update the `DATABASES` settings in your `settings.py` file as follows:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'cashify',
             'USER': 'your_mysql_user',
             'PASSWORD': 'your_mysql_password',
             'HOST': '127.0.0.1',
             'PORT': '3306',
         }
     }
     ```
   - Ensure MySQL server is running, and the credentials in the `settings.py` file match your MySQL configuration.

5. **Set up Django**: Run the following command to make migrations and migrate the database:
   ```
   python manage.py makemigrations
   python manage.py migrate

6. **Run the Django server:**

   ```
   python manage.py runserver
   ```

## Usage

- **Browse Products**: View available mobile phones from the catalog.
- **Add to Cart**: Select the mobile phone you want to buy and add it to the cart.
- **Add a Mobile**: Staf user can add a mobile phone to Cashify for sell.

## Project Structure

- `manage.py`: Django project management script.
- `cashify_app`: Django app that manages the mobile phones listed for sale.
  - `models.py`: Defines the mobile phone model.
  - `views.py`: Handles product listing and cart management.
  - `urls.py`: Defines the URL patterns for navigating the site.
- `templates/`: Contains HTML files for the user interface.
  - `index.html`: Homepage displaying the catalog.
  - `divice_detail.html`: Displays product details.
  - `device_list.html`: Shopping cart interface.
  - `divice_form.html`: Add a new mobile.


# Demo

## Wabepage 
![Screenshot 2024-07-23 152443](https://github.com/user-attachments/assets/859ba816-85b0-4131-91c3-60fb083c6463)


## Login 

![image](https://github.com/user-attachments/assets/3f86a87d-7bb8-49e6-aaa2-84305478ec4d)


## Device list ( cart )

![image](https://github.com/user-attachments/assets/5f395d33-ffb5-4490-82a0-fe397c47c3c5)


## adding new device to website for sell 

![image](https://github.com/user-attachments/assets/1190538d-59b4-45d3-8e90-399d5a31c447)

