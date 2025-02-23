
-- The password to connect to the database is outland_adven

CREATE USER 'outland_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'outland_adven';

GRANT ALL PRIVILEGES ON outland_adventures.* TO 'outland_user'@'localhost';


CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE trips (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_name VARCHAR(100) NOT NULL,
    region ENUM('Africa', 'Asia', 'Southern Europe') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    min_bookings INT NOT NULL,
    visa_required BOOLEAN DEFAULT FALSE,
    vaccination_required BOOLEAN DEFAULT FALSE,
    airfare_included BOOLEAN DEFAULT FALSE,
    status ENUM('Upcoming', 'Ongoing', 'Completed', 'Canceled') DEFAULT 'Upcoming'
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    trip_id INT NOT NULL,
    status ENUM('Pending', 'Confirmed', 'Canceled') DEFAULT 'Pending',
    deposit_paid DECIMAL(10,2) DEFAULT 0.00,
    total_price DECIMAL(10,2) NOT NULL,
    full_payment_due DATE NOT NULL,
    cancellation_fee DECIMAL(10, 2),
    booking_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id) ON DELETE CASCADE
);

CREATE TABLE guides (
    guide_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    experience_years INT NOT NULL,
    hire_date DATE NOT NULL,
    specialty VARCHAR(100)
);

CREATE TABLE trip_guides (
    trip_id INT NOT NULL,
    guide_id INT NOT NULL,
    PRIMARY KEY (trip_id, guide_id),
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id) ON DELETE CASCADE,
    FOREIGN KEY (guide_id) REFERENCES guides(guide_id) ON DELETE CASCADE
);

CREATE TABLE equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    status ENUM('available', 'rented', 'soldout') NOT NULL,
    inventory_quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    rental_return_date DATE,
    purchase_date DATE NOT NULL,
    equipment_condition ENUM('New', 'Good', 'Worn', 'Needs Repair') DEFAULT 'New',
    review_flag BOOLEAN DEFAULT FALSE
);

CREATE TABLE equipment_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    equipment_id INT NOT NULL,
    transaction_type ENUM('Purchase', 'Rental') NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE
);

CREATE TABLE marketing_campaigns (
    campaign_id INT AUTO_INCREMENT PRIMARY KEY,
    campaign_name VARCHAR(100) NOT NULL,
    strategy VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    budget DECIMAL(10,2) NOT NULL,
    effectiveness_score DECIMAL(5, 2)
);

CREATE TABLE customer_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    trip_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id) ON DELETE CASCADE
);

CREATE TABLE revenue (
    revenue_id INT AUTO_INCREMENT PRIMARY KEY,
    source ENUM('Trip Booking', 'Equipment Sale', 'Equipment Rental') NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);