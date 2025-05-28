
#menggunakan library matplotlib.pyplot untuk menampilkan graf 
import matplotlib.pyplot as plt
#menggunakan library matplotlib.pyplot untuk menampilkan graf 
import networkx as nx

#fungsi process meminta user untuk memasukkan start dan finish yang berupa nama daerah
def process(start, finish):
    #mendefinisikan graf motor, mobil, dan kereta
    Gmotor = nx.Graph()
    Gcar = nx.Graph()
    Gtrain = nx.Graph()

    #menginisialisasi vertex/nodes yang nanti dibuat graph
    nodes = [
        "wonogiri", "klaten", "sukoharjo", "karanganyar", "surakarta", "sragen", "grobogan", "blora", 
        "rembang", "pati", "jepara", "kudus", "demak", "boyolali", "semarang", "kota salatiga", "kota semarang", 
        "magelang", "kota magelang", "temanggung", "kendal", "batang", "wonosobo", "purworejo", "kebumen", "banjarnegara", 
        "pekalongan", "kota pekalongan", "pemalang", "purbalingga", "banyumas", "tegal", "kota tegal", "brebes", "cilacap", "yogyakarta"
    ]
    Gmotor.add_nodes_from(nodes)
    Gcar.add_nodes_from(nodes)

    #menetapkan lokasi vertex bedasarkan canvas yang ditampilkan dengan plt.show()
    pos={
        "wonogiri": (5, -5),
        "klaten": (2.9, -4.862),
        "sukoharjo": (4, -4.685),
        "karanganyar": (5.406, -3.615),
        "surakarta": (4.2, -3.5),
        "sragen": (5.4, -2.1),
        "grobogan": (4.9, -0.9),
        "blora": (5.9, -0.116),
        "rembang": (5.6, 1.1),
        "pati": (4.6, 1.3),
        "jepara": (3.6, 1.1),
        "kudus": (4.2, 0.1),
        "demak": (3.4, 0),
        "boyolali": (3.5, -2.515),
        "semarang": (3.224, -1.118),
        "kota salatiga": (2.3, -1.8),
        "kota semarang": (2.6,0.927),
        "magelang": (2.312, -3.103),
        "kota magelang": (2.170, -4.365),
        "temanggung": (1.6, -1.2),
        "kendal": (1.9, 0.104),
        "batang": (1.0, 0.340),
        "wonosobo": (0.8, -2.303),
        "purworejo": (1.1, -4.60),
        "kebumen": (0.1, -4.263),
        "banjarnegara": (0.2, -1.9),
        "pekalongan": (0.1, 0.3),
        "kota pekalongan": (0.5, 1.8),
        "pemalang": (-0.7, 0),
        "purbalingga": (-0.7, -1.5),
        "banyumas": (-1.2, -2.5),
        "tegal": (-1.3, 0.1),
        "kota tegal": (-1.517, 1.700),
        "brebes": (-2.10, -0.1),
        "cilacap": (-1.8, -4.1),
        "yogyakarta": (1.848, -5.879)
    }


    # membuat graph motor
    edges_with_weights = [
    ("wonogiri", "sukoharjo", 40),
    ("wonogiri", "karanganyar", 26),
    ("klaten", "boyolali", 36),
    ("klaten", "sukoharjo", 26),
    ("sukoharjo", "klaten", 26),
    ("sukoharjo", "boyolali", 40),
    ("sukoharjo", "surakarta", 13),
    ("sukoharjo", "karanganyar", 26),
    ("sukoharjo", "wonogiri", 40),
    ("karanganyar", "wonogiri", 48),
    ("karanganyar", "sukoharjo", 27),
    ("karanganyar", "surakarta", 20),
    ("karanganyar", "boyolali", 48),
    ("karanganyar", "sragen", 27),
    ("surakarta", "sukoharjo", 14),
    ("surakarta", "boyolali", 28),
    ("surakarta", "karanganyar", 20),
    ("sragen", "karanganyar", 30),
    ("sragen", "boyolali", 56),
    ("sragen", "grobogan", 45),
    ("grobogan", "sragen", 45),
    ("grobogan", "boyolali", 84),
    ("grobogan", "semarang", 70),
    ("grobogan", "demak", 51),
    ("grobogan", "kudus", 56),
    ("grobogan", "pati", 60),
    ("grobogan", "blora", 64),
    ("blora", "grobogan", 64),
    ("blora", "pati", 72),
    ("blora", "rembang", 44),
    ("rembang", "blora", 44),
    ("rembang", "pati", 35),
    ("rembang", "blora", 44),
    ("rembang", "grobogan", 92),
    ("rembang", "pati", 35),
    ("rembang", "blora", 44),
    ("pati", "blora", 66),
    ("pati", "grobogan", 60),
    ("pati", "kudus", 26),
    ("pati", "jepara", 62),
    ("pati", "rembang", 35),
    ("jepara", "pati", 62),
    ("jepara", "kudus", 36),
    ("jepara", "demak", 45),
    ("kudus", "grobogan", 56),
    ("kudus", "demak", 38),
    ("kudus", "jepara", 41),
    ("kudus", "pati", 25),
    ("demak", "grobogan", 46),
    ("demak", "semarang", 50),
    ("demak", "kota semarang", 34),
    ("boyolali", "klaten", 32),
    ("boyolali", "magelang", 65),
    ("boyolali", "semarang", 62),
    ("boyolali", "grobogan", 65),
    ("boyolali", "sragen", 44),
    ("boyolali", "karanganyar", 55),	
    ("boyolali", "surakarta", 29),
    ("boyolali", "semarang", 62),
    ("semarang", "magelang", 48),
    ("semarang", "temanggung", 65),
    ("semarang", "kendal", 49),
    ("semarang", "kota semarang", 27),
    ("semarang", "demak", 53),
    ("semarang", "grobogan", 71),
    ("semarang", "boyolali", 60),
    ("semarang", "kota salatiga", 25),
    ("kota salatiga", "semarang", 25),
    ("kota semarang", "semarang", 27),
    ("kota semarang", "kendal", 35),
    ("kota semarang", "demak", 34),
    ("magelang", "purworejo", 55),
    ("magelang", "wonosobo", 60),
    ("magelang", "temanggung", 32),
    ("magelang", "semarang", 48),
    ("magelang", "boyolali", 65),
    ("magelang", "kota magelang", 12),
    ("kota magelang", "magelang", 12),
    ("temanggung", "magelang", 35),
    ("temanggung", "wonosobo", 30),
    ("temanggung", "kendal", 53),
    ("temanggung", "semarang", 65),
    ("kendal", "temanggung", 53),
    ("kendal", "batang", 61),
    ("kendal", "kota semarang", 35),
    ("kendal", "semarang", 49),
    ("batang", "wonosobo", 57),
    ("batang", "banjarnegara", 64),
    ("batang", "pekalongan", 29),
    ("batang", "kota pekalongan", 26),
    ("batang", "kendal", 61),
    ("wonosobo", "purworejo", 50),
    ("wonosobo", "kebumen", 70),
    ("wonosobo", "banjarnegara", 43),
    ("wonosobo", "batang", 57),
    ("wonosobo", "kendal", 73),
    ("wonosobo", "temanggung", 30),
    ("wonosobo", "magelang", 60),
    ("purworejo", "kebumen", 45),
    ("purworejo", "wonosobo", 50),
    ("purworejo", "magelang", 56),
    ("kebumen", "cilacap", 101),
    ("kebumen", "banyumas", 73),
    ("kebumen", "banjarnegara", 56),
    ("kebumen", "purworejo", 45),
    ("banjarnegara", "kebumen", 56),
    ("banjarnegara", "banyumas", 69),
    ("banjarnegara", "purbalingga", 33),
    ("banjarnegara", "pekalongan", 57),
    ("banjarnegara", "batang", 63),
    ("pekalongan", "banjarnegara", 73),
    ("pekalongan", "purbalingga", 86),
    ("pekalongan", "pemalang", 45),
    ("pekalongan", "kota pekalongan", 23),
    ("pekalongan", "batang", 27),
    ("kota pekalongan", "batang", 8),
    ("kota pekalongan", "pekalongan", 23),
    ("pemalang", "purbalingga", 69),
    ("pemalang", "banyumas", 109),
    ("pemalang", "tegal", 32),
    ("pemalang", "pekalongan", 36),
    ("purbalingga", "banjarnegara", 33),
    ("purbalingga", "banyumas", 58),
    ("purbalingga", "tegal", 79),
    ("purbalingga", "pemalang", 66),
    ("purbalingga", "pekalongan", 84),
    ("banyumas", "cilacap", 38),
    ("banyumas", "brebes", 86),
    ("banyumas", "tegal", 88),
    ("banyumas", "pemalang", 109),
    ("banyumas", "purbalingga", 42),
    ("banyumas", "banjarnegara", 56),
    ("banyumas", "kebumen", 74),
    ("tegal", "banyumas", 89),
    ("tegal", "brebes", 30),
    ("tegal", "kota tegal", 14),
    ("tegal", "pemalang", 41),
    ("tegal", "purbalingga", 71),
    ("kota tegal", "brebes", 35),
    ("kota tegal", "tegal", 14),
    ("brebes", "banyumas", 85),
    ("brebes", "cilacap", 115),
    ("brebes", "kota tegal", 35),
    ("brebes", "tegal", 35),
    ("cilacap", "brebes", 115),
    ("cilacap", "banyumas", 45),
    ]

    #menambahkan weight untuk graf
    Gmotor.add_weighted_edges_from(edges_with_weights)
    #meneambahkan edge
    edge_labels = {(u, v): Gmotor[u][v]['weight'] for u, v in Gmotor.edges()}
    #menggambar graf
    nx.draw(Gmotor, pos=pos,with_labels=True,
            node_color="red", node_size=3000,
            font_color="white", font_size=10, font_family="Times New Roman", font_weight="bold",
            width=5)
    # nx.draw_networkx_edge_labels(Gmotor, pos=pos,edge_labels=edge_labels) ----------------- baris ini untuk menggambar graf motor dengan edge berlabel weight
    # plt.show() ---------------- baris ini untuk menampilkan graf yang digunakan yang nantinya ditampilkan di frontend

     
    #membuat graph mobil
    edges_with_weights_car = [
        ("wonogiri", "sukoharjo", 40),
        ("wonogiri", "karanganyar", 26),
        ("klaten", "boyolali", 36),
        ("klaten", "sukoharjo", 26),
        ("sukoharjo", "klaten", 26),
        ("sukoharjo", "boyolali", 40),
        ("sukoharjo", "surakarta", 13),
        ("sukoharjo", "karanganyar", 26),
        ("sukoharjo", "wonogiri", 40),
        ("karanganyar", "wonogiri", 48),
        ("karanganyar", "boyolali", 48),
        ("karanganyar", "sragen", 34),
        ("surakarta", "sukoharjo", 14),
        ("surakarta", "karanganyar", 20),
        ("sragen", "boyolali", 56),
        ("sragen", "grobogan", 45),
        ("grobogan", "sragen", 45),
        ("grobogan", "boyolali", 84),
        ("grobogan", "semarang", 70),
        ("grobogan", "demak", 51),
        ("grobogan", "kudus", 56),
        ("grobogan", "pati", 60),
        ("grobogan", "blora", 64),
        ("blora", "grobogan", 64),
        ("blora", "pati", 72),
        ("blora", "rembang", 44),
        ("rembang", "blora", 44),
        ("rembang", "pati", 35),
        ("rembang", "blora", 44),
        ("rembang", "grobogan", 92),
        ("rembang", "pati", 35),
        ("rembang", "blora", 44),
        ("pati", "blora", 66),
        ("pati", "grobogan", 60),
        ("pati", "kudus", 26),
        ("pati", "jepara", 62),
        ("pati", "rembang", 35),
        ("jepara", "pati", 62),
        ("jepara", "kudus", 36),
        ("jepara", "demak", 45),
        ("kudus", "grobogan", 56),
        ("kudus", "demak", 38),
        ("kudus", "jepara", 41),
        ("kudus", "pati", 25),
        ("demak", "grobogan", 46),
        ("demak", "semarang", 50),
        ("demak", "kota semarang", 34),
        ("boyolali", "klaten", 32),
        ("boyolali", "magelang", 65),
        ("boyolali", "semarang", 62),
        ("boyolali", "grobogan", 65),
        ("boyolali", "sragen", 44),
        ("boyolali", "karanganyar", 55),	
        ("boyolali", "surakarta", 37),
        ("semarang", "magelang", 48),
        ("semarang", "temanggung", 65),
        ("semarang", "kendal", 49),
        ("semarang", "demak", 53),
        ("semarang", "grobogan", 71),
        ("semarang", "boyolali", 63),
        ("semarang", "kota salatiga", 30),
        ("kota semarang", "semarang", 22),
        ("kota semarang", "demak", 34),
        ("magelang", "purworejo", 55),
        ("magelang", "wonosobo", 60),
        ("magelang", "temanggung", 32),
        ("magelang", "semarang", 48),
        ("magelang", "boyolali", 65),
        ("magelang", "kota magelang", 12),
        ("kota magelang", "magelang", 12),
        ("temanggung", "magelang", 35),
        ("temanggung", "wonosobo", 30),
        ("temanggung", "kendal", 53),
        ("temanggung", "semarang", 65),
        ("kendal", "temanggung", 53),
        ("kendal", "kota semarang", 35),
        ("kendal", "semarang", 49),
        ("batang", "wonosobo", 57),
        ("batang", "banjarnegara", 64),
        ("batang", "kota pekalongan", 26),
        ("batang", "kendal", 66),
        ("wonosobo", "purworejo", 50),
        ("wonosobo", "kebumen", 70),
        ("wonosobo", "banjarnegara", 43),
        ("wonosobo", "batang", 57),
        ("wonosobo", "kendal", 73),
        ("wonosobo", "temanggung", 30),
        ("wonosobo", "magelang", 60),
        ("purworejo", "kebumen", 45),
        ("purworejo", "wonosobo", 50),
        ("purworejo", "magelang", 56),
        ("kebumen", "cilacap", 101),
        ("kebumen", "banyumas", 73),
        ("kebumen", "banjarnegara", 56),
        ("kebumen", "purworejo", 45),
        ("banjarnegara", "kebumen", 56),
        ("banjarnegara", "banyumas", 69),
        ("banjarnegara", "purbalingga", 33),
        ("banjarnegara", "pekalongan", 57),
        ("banjarnegara", "batang", 63),
        ("pekalongan", "banjarnegara", 73),
        ("pekalongan", "purbalingga", 86),
        ("pekalongan", "kota pekalongan", 23),
        ("pekalongan", "batang", 8),
        ("kota pekalongan", "batang", 8),
        ("kota pekalongan", "pekalongan", 23),
        ("pemalang", "purbalingga", 69),
        ("pemalang", "banyumas", 109),
        ("pemalang", "pekalongan", 49),
        ("purbalingga", "banjarnegara", 33),
        ("purbalingga", "banyumas", 58),
        ("purbalingga", "tegal", 79),
        ("purbalingga", "pemalang", 66),
        ("purbalingga", "pekalongan", 84),
        ("banyumas", "cilacap", 38),
        ("banyumas", "brebes", 86),
        ("banyumas", "tegal", 88),
        ("banyumas", "pemalang", 109),
        ("banyumas", "purbalingga", 42),
        ("banyumas", "banjarnegara", 56),
        ("banyumas", "kebumen", 74),
        ("tegal", "banyumas", 89),
        ("tegal", "kota tegal", 14),
        ("tegal", "pemalang", 52),
        ("tegal", "purbalingga", 71),
        ("kota tegal", "brebes", 35),
        ("kota tegal", "tegal", 14),
        ("brebes", "banyumas", 85),
        ("brebes", "cilacap", 115),
        ("brebes", "kota tegal", 35),
        ("brebes", "tegal", 12),
        ("cilacap", "brebes", 115),
        ("cilacap", "banyumas", 45)
    ]

    #menambahkan weight ke graph mobil
    Gcar.add_weighted_edges_from(edges_with_weights_car)
    #menambahkan edge ke graph mobil
    edge_labels_car = {(u, v): Gcar[u][v]['weight'] for u, v in Gcar.edges()}

    #menggambar graf mobil
    nx.draw(Gcar, pos=pos,with_labels=True,
            node_color="red", node_size=3000,
            font_color="white", font_size=10, font_family="Times New Roman", font_weight="bold",
            width=5)
    #menggambar edge pada graph dengan label berupa 
    nx.draw_networkx_edge_labels(Gcar, pos=pos,edge_labels=edge_labels_car)

    # plt.show() menampilkan graf yang terbentuk

    #membuat graph kereta
    edges_with_weights_train = [ #data dari arcgis.com
        ("wonogiri", "sukoharjo", 18),
        ("sukoharjo", "surakarta", 19),
        ("surakarta", "klaten", 28),
        ("surakarta", "sragen", 33),
        ("surakarta", "kota semarang", 108),
        ("klaten", "yogyakarta", 28),
        ("yogyakarta", "purworejo", 81),
        ("yogyakarta", "kebumen", 32),
        ("kota semarang", "batang", 83),
        ("batang", "kota pekalongan", 8),
        ("pemalang", "tegal", 29),
        ("pemalang", "kota tegal", 29),
        ("kota tegal", "brebes", 13),
        ("kota tegal", "cilacap", 157),
        ("kota tegal", "kebumen", 175),
        ("cilacap", "kebumen", 91),
        ("kebumen", "purworejo", 41),
        ("kota pekalongan", "pemalang", 32),
    ]

    #menambahkan weight ke graph kereta        
    Gtrain.add_weighted_edges_from(edges_with_weights_train)
    #menambahkan edge ke graph mobil
    edge_label_train = {(u, v): Gtrain[u][v]['weight'] for u, v in Gtrain.edges()}
    #menggambar edge pada graph dengan label berupa
    nx.draw(Gtrain, pos=pos,with_labels=True,
            node_color="red", node_size=3000,
            font_color="white", font_size=10, font_family="Times New Roman", font_weight="bold",
            width=5)
    nx.draw_networkx_edge_labels(Gtrain, pos=pos,edge_labels=edge_label_train)


    # start = "klaten" #start
    # finish = "boyolali" #finish


    shortest_path_length = nx.shortest_path_length(Gmotor, source=start, target=finish, weight="weight") #nilai jalur terpendek yang ditempuh untuk graf motor
    shortest_path_length_car = nx.shortest_path_length(Gcar, source=start, target=finish, weight="weight") #nilai jalur terpendek yang ditempuh untuk graf mobil

    #pada try akan menghitung jarak jarak terpendek yang ditempuh, jika ada graf kereta
    #jika tidak ada graf kereta, maka akan masuk ke "except" yang hanya menghitung jarak terpendek dari graf mobil dan motor

    try:
        shortest_path_length_train = nx.shortest_path_length(Gtrain, source=start, target=finish, weight="weight") #menghiung jarak terpendek kereta
        lengthArr = [shortest_path_length, shortest_path_length_car, shortest_path_length_train] #memasukkan semua nilai terpendek dari semua graf
        min_length = min(lengthArr) #mencari nilai minimum dari ketiga jalur yang sudah ditemukan
        routePath = [] #variabel yang nantinya berisi jalur terpendek

        #percabangan dibawah ini akan membandingkan jarak mana yang lebih pendek diantara mobil, motor, dan kereta
        if min_length == shortest_path_length_train:
            print("rekomendasi kendaraan : kereta")
            routePath = nx.shortest_path(Gtrain, source=start, target=finish, weight="weight")
            print("total cost : ", shortest_path_length_train)
        
        elif min_length == shortest_path_length:
            print("rekomendasi kendaraan : motor")
            routePath = nx.shortest_path(Gmotor, source=start, target=finish, weight="weight")
            print("total cost : ", shortest_path_length)

        elif min_length == shortest_path_length_car:
            print("rekomendasi kendaraan : mobil")
            routePath = nx.shortest_path(Gcar, source=start, target=finish, weight="weight")
            print("total cost : ", shortest_path_length_car)
        result_string_path = " -> ".join(str(num) for num in routePath)
        return shortest_path_length, shortest_path_length_car, shortest_path_length_train, result_string_path

    # pada blok except memiliki cara kerja yang sama, tetapi hanya membandingkan antara motor dan mobil
    except nx.NetworkXNoPath:
        lengthArr = [shortest_path_length, shortest_path_length_car]
        min_length = min(lengthArr)
        routePath = []
        if min_length == shortest_path_length:
            print("rekomendasi kendaraan : motor")
            routePath = nx.shortest_path(Gmotor, source=start, target=finish, weight="weight")
            print("total cost : ", shortest_path_length)
        elif min_length == shortest_path_length_car:
            print("rekomendasi kendaraan : mobil")
            routePath = nx.shortest_path(Gcar, source=start, target=finish, weight="weight")
            print("total cost : ", shortest_path_length_car)
        result_string_path = " -> ".join(str(num) for num in routePath)
        return shortest_path_length, shortest_path_length_car, "-", result_string_path
    except nx.NodeNotFound:
        lengthArr = [shortest_path_length, shortest_path_length_car]
        min_length = min(lengthArr)
        routePath = []
        if min_length == shortest_path_length:
            print("rekomendasi kendaraan : motor")
            routePath = nx.shortest_path(Gmotor, source=start, target=finish, weight="weight")
            print("total cost : ", shortest_path_length)
        elif min_length == shortest_path_length_car:
            print("rekomendasi kendaraan : mobil")
            routePath = nx.shortest_path(Gcar, source=start, target=finish, weight="weight")
            print("total cost : ", shortest_path_length_car)
        result_string_path = " -> ".join(str(num) for num in routePath)
        return shortest_path_length, shortest_path_length_car, "-", result_string_path