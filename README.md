# E-commerce Website using Python and Django

![Project Image](project_image.png)

This is an e-commerce website developed using Python and the Django framework, offering a secure and user-friendly platform for online shopping. The project was completed within a week and includes essential features to ensure efficient website administration, a seamless user experience, and secure online transactions.

## Features

- User Authentication: The website provides a secure login and registration system for users, allowing them to create accounts and log in securely.

- Email Verification: Users are required to verify their email addresses during the registration process, enhancing security and preventing unauthorized access.

- Product Management: Admins can easily manage products through the Django admin panel, allowing them to add, update, or delete products from the website.

- Add to Cart: The "Add to Cart" system is seamlessly integrated, enabling users to add products to their cart and continue shopping or proceed to checkout.

- Apply Coupon Code: A robust "Apply Coupon Code" feature has been implemented to enhance the user experience and encourage sales.

- Razor-pay Payment Gateway: For secure and hassle-free online transactions, the website integrates the Razor-pay payment gateway using Django REST Framework.

## Project Structure

├── my_project/<br/>
│ ├── app1/<br/>
│ ├── app2/<br/>
│ ├── manage.py<br/>
│ └── my_project/<br/>
│ ├── settings.py<br/>
│ └── ...<br/>
├── templates/<br/>
│ ├── base.html<br/>
│ ├── home.html<br/>
│ └── ...<br/>
├── static/<br/>
│ ├── css/<br/>
│ ├── js/<br/>
│ └── ...<br/>
├── requirements.txt<br/>
└── README.md<br/>


- `my_project/`: Contains the main project settings and configuration.
- `app1/`, `app2/`: Django apps that handle different parts of the website (e.g., user authentication, product management, etc.).
- `templates/`: HTML templates used for rendering the website pages.
- `static/`: Static files, such as CSS and JavaScript, used for the frontend.
- `requirements.txt`: Lists all the required Python packages and their versions to run the project.

## How to Run the Project

1. Clone the repository: `git clone https://github.com/your_username/your_repository.git`
2. Navigate to the project directory: `cd your_repository`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install the required packages: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Create a superuser (admin): `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`
9. Access the website at `http://localhost:8000/`

## Collaboration

This project was a collaborative effort, with close collaboration between backend and frontend developers. The seamless communication between the two components ensured a smooth and cohesive user experience throughout the website.

## Technologies Used

- Python and Django framework were used to build the backend infrastructure.
- Django REST Framework facilitated the integration of the Razor-pay payment gateway for secure online transactions.
- HTML and CSS were utilized to create a visually appealing and responsive frontend interface.
- Industry-standard technologies like VS Code and React were employed to streamline development processes and maintain code quality.

## Contributions

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.


