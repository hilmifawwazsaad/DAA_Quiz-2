TRAIN_ROUTES = [
    # Jalur Utama Solo-Yogyakarta
    ("surakarta", "klaten", 28),
    ("klaten", "yogyakarta", 28),
    
    # Jalur Solo-Semarang
    ("surakarta", "boyolali", 35),
    ("boyolali", "semarang", 62),
    ("surakarta", "semarang", 108),  # Direct route
    
    # Jalur Semarang-Tegal (Pantura)
    ("semarang", "kendal", 35),
    ("kendal", "batang", 45),
    ("batang", "pekalongan", 25),
    ("pekalongan", "pemalang", 35),
    ("pemalang", "tegal", 29),
    ("tegal", "brebes", 35),
    
    # Jalur Selatan (Yogya-Cilacap)
    ("yogyakarta", "purworejo", 81),
    ("purworejo", "kebumen", 41),
    ("kebumen", "cilacap", 91),
    
    # Jalur Alternatif dan Connecting Routes
    ("wonogiri", "surakarta", 65),   # Via jalur cabang
    ("surakarta", "sragen", 33),     # Jalur cabang ke Sragen
    ("semarang", "demak", 45),       # Jalur lokal
    ("demak", "kudus", 25),          # Jalur lokal
    ("kudus", "pati", 30),           # Jalur lokal
    ("pati", "rembang", 35),         # Jalur cabang
    ("semarang", "magelang", 75),    # Via Ambarawa
    ("magelang", "yogyakarta", 65),  # Jalur cabang
    
    # Jalur Kereta Komuter dan Lokal
    ("semarang", "kota semarang", 15),      # Dalam kota
    ("pekalongan", "kota pekalongan", 8),   # Dalam kota
    ("tegal", "kota tegal", 12),            # Dalam kota
    ("magelang", "kota magelang", 10),      # Dalam kota
    ("salatiga", "kota salatiga", 5),       # Dalam kota (jika ada)
    
    # Jalur Freight dan Industrial
    ("cilacap", "banyumas", 45),     # Jalur industri
    ("banyumas", "purbalingga", 35), # Connecting route
    ("purbalingga", "banjarnegara", 33), # Local connection
    ("banjarnegara", "wonosobo", 40),    # Mountain route
    ("wonosobo", "temanggung", 35),      # Connecting route
    ("temanggung", "magelang", 30),      # Local route
    
    # Express Routes (faster long-distance)
    ("yogyakarta", "semarang", 120),     # Express via Magelang
    ("surakarta", "cilacap", 180),       # Express via Yogya
    ("semarang", "cilacap", 200),        # Express coastal route
]