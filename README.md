# Restaurant Management System Design

A desktop restaurant management application developed in Python using Object-Oriented Programming (OOP), the Model-View-Controller (MVC) architecture, and Tkinter.

## Features

- Customer registration, searching, editing, and deletion
- Restaurant menu management, including adding, updating, and removing food items
- Order registration, searching, and management
- Invoice generation and saving
- Sales statistics, including total sales, order count, and average order value
- Exporting order information to Excel
- Persistent data storage using Pickle
- Backup validation and recovery support for order data
- Error handling and data validation
- Graphical user interface using Tkinter

## Project Architecture

The application follows the MVC architecture:

- **Model:** Manages customers, menu items, orders, and data persistence.
- **View:** Provides the Tkinter graphical interface.
- **Controller:** Handles application operations and connects the user interface with the data models.

## Technologies

- Python 3
- Tkinter
- Object-Oriented Programming (OOP)
- MVC Architecture
- Pickle
- Excel Export

## Installation and Execution

1. Clone the repository:

```bash
git clone https://github.com/mojmoj575-bot/Restaurant-Management-System_Design.git
```

2. Open the project directory:

```bash
cd Restaurant-Management-System_Design
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python main.py
```

## Testing

Run the project's tests using:

```bash
python test_restaurant.py
```

## Data Storage

The application stores restaurant information locally using Pickle files. Runtime data files are excluded from the Git repository to protect customer and order information.

## Project Purpose

This project demonstrates practical implementation of Python OOP principles, MVC architecture, graphical interface development, persistent data management, and software testing in a restaurant management application.