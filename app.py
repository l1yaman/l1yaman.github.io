<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kids Clothing</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</head>
<body>
    <!-- Navigation Bar -->
    <nav>
        <div class="logo">
            <h1>Kids Clothing</h1>
        </div>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/login">Login</a></li>
            <li><a href="/register">Register</a></li>
            <li><a href="/cart">Cart</a></li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    </nav>

    <!-- Header -->
    <header>
        <h2>Adorable Clothing for Kids</h2>
        <p>Find the newest and cutest kids clothing here!</p>
        <input type="text" placeholder="Search..." id="search">
    </header>

    <!-- Products List -->
    <section id="products">
        <div class="product">
            <img src="{{ url_for('static', filename='images/product1.jpg') }}" alt="Product 1">
            <h3>Product 1</h3>
            <p>Color: Green, Size: 3-
