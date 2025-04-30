<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uşaq Geyimləri</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</head>
<body>
    <!-- Navigasiya -->
    <nav>
        <div class="logo">
            <h1>Uşaq Geyimləri</h1>
        </div>
        <ul>
            <li><a href="/">Ana səhifə</a></li>
            <li><a href="/login">Daxil ol</a></li>
            <li><a href="/register">Qeydiyyat</a></li>
            <li><a href="/cart">Səbət</a></li>
            <li><a href="/contact">Əlaqə</a></li>
        </ul>
    </nav>

    <!-- Ana səhifə başlığı -->
    <header>
        <h2>Uşaqlar üçün şirin geyimlər</h2>
        <p>Ən yeni və şirin uşaq geyimlərini buradan tapın!</p>
        <input type="text" placeholder="Axtarış..." id="search">
    </header>

    <!-- Məhsul siyahısı -->
    <section id="products">
        <div class="product">
            <img src="{{ url_for('static', filename='images/product1.jpg') }}" alt="Məhsul 1">
            <h3>Məhsul 1</h3>
            <p>Rəng: Yaşıl, Ölçü: 3-4 yaş</p>
            <p class="price">₼45</p>
            <a href="/product/1" class="view-details">Ətraflı bax</a>
        </div>
        <div class="product">
            <img src="{{ url_for('static', filename='images/product2.jpg') }}" alt="Məhsul 2">
            <h3>Məhsul 2</h3>
            <p>Rəng: Mavi, Ölçü: 4-5 yaş</p>
            <p class="price">₼55</p>
            <a href="/product/2" class="view-details">Ətraflı bax</a>
        </div>
        <!-- Daha çox məhsul əlavə ediləcək -->
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2025 Uşaq Geyimləri - Bütün hüquqlar qorunur.</p>
    </footer>

</body>
</html>
