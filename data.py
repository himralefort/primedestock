categories = [
    "Boissons",
    "Produits frais",
    "Épicerie",
    "Surgelés",
    "Produits laitiers",
    "Viandes et poissons"
]

products = [
    {
        "id": 1,
        "name": "Lot de 10 foie gras Labeyrie 285g",
        "description": "Foie gras de canard entier, mi-cuit, 285g par boîte.",
        "price": 257.00,
        "category": "Produits frais",
        "stock": 15,
        "featured": False,
        "images": ["foie-gras.jpg", "foie-gras-2.jpg", "foie-gras-3.jpg"],
        "details": {
            "marque": "Labeyrie",
            "poids": "2.85kg (10x285g)",
            "conservation": "Au réfrigérateur",
            "origine": "France"
        }
    },
    {
        "id": 2,
        "name": "Saumon fumé Norvège",
        "description": "Saumon fumé de Norvège, tranches épaisses, 200g.",
        "price": 24.99,
        "category": "Produits frais",
        "stock": 30,
        "featured": False,
        "images": ["saumon-fume.jpg", "saumon-fume-2.jpg", "saumon-fume-3.jpg"],
        "details": {
            "marque": "Norvège Premium",
            "poids": "200g",
            "conservation": "Au réfrigérateur",
            "origine": "Norvège"
        }
    },
    {
        "id": 3,
        "name": "Assortiment fromages AOP",
        "description": "Assortiment de 5 fromages français AOP, 1kg.",
        "price": 39.99,
        "category": "Produits laitiers",
        "stock": 20,
        "featured": False,
        "images": ["fromages.jpg", "fromages-2.jpg", "fromages-3.jpg"],
        "details": {
            "marque": "Fromagerie Tradition",
            "poids": "1kg",
            "conservation": "Au réfrigérateur",
            "origine": "France"
        }
    },
    {
        "id": 4,
        "name": "Champagne Brut Millésimé",
        "description": "Champagne brut millésimé, bouteille 75cl.",
        "price": 49.90,
        "category": "Boissons",
        "stock": 25,
        "featured": True,
        "images": ["champagne.jpg", "champagne-2.jpg", "champagne-3.jpg"],
        "details": {
            "marque": "Maison de Champagne",
            "volume": "75cl",
            "alcool": "12%",
            "origine": "Champagne, France"
        }
    },
    {
        "id": 5,
        "name": "Café en grains Arabica",
        "description": "Café en grains 100% Arabica, paquet de 1kg.",
        "price": 19.90,
        "category": "Épicerie",
        "stock": 40,
        "featured": False,
        "images": ["cafe.jpg", "cafe-2.jpg", "cafe-3.jpg"],
        "details": {
            "marque": "Café Premium",
            "poids": "1kg",
            "torréfaction": "Moyenne",
            "origine": "Colombie"
        }
    },
    {
        "id": 6,
        "name": "Filet de boeuf wagyu",
        "description": "Filet de boeuf wagyu A5, pièce de 500g.",
        "price": 199.00,
        "category": "Viandes et poissons",
        "stock": 8,
        "featured": False,
        "images": ["wagyu.jpg", "wagyu-2.jpg", "wagyu-3.jpg"],
        "details": {
            "marque": "Wagyu Excellence",
            "poids": "500g",
            "conservation": "Surgelé",
            "origine": "Japon"
        }
    },
    {
        "id": 100,
        "name": "Palette de Coca-Cola (144 bouteilles)",
        "description": "Lot de 144 bouteilles de Coca-Cola 1L - Destockage exceptionnel.",
        "price": 1550.00,
        "category": "Boissons",
        "stock": 10,
        "featured": True,
        "images": ["palette-coca.jpg", "palette-coca1.jpg", "palette-coca2.jpg"],
        "image_config": {
            "type": "palette",
            "dimensions": {"width": 1000, "height": 600},
            "zoomable": True
        }
    },
    {
        "id": 101,
        "name": "Palette de RedBull (150 canettes)",
        "description": "Lot de 150 canettes de RedBull 250ml - Date limite longue.",
        "price": 1670.00,
        "category": "Boissons",
        "stock": 8,
        "featured": True,
        "images": ["palette-redbull.jpg", "palette-redbull1.jpg", "palette-redbull2.jpg"]
    },
    {
        "id": 102,
        "name": "Fanta Orange 1,5L",
        "description": "Boisson gazeuse rafraîchissante au goût d'orange naturelle, sans conservateurs.",
        "price": 1.89,
        "category": "Boissons",
        "stock": 120,
        "featured": False,
        "images": ["fanta.jpg", "fanta-2.jpg", "fanta-3.jpg"],
        "details": {
            "marque": "Fanta",
            "volume": "1.5L",
            "saveur": "Orange",
            "origine": "Pays-Bas"
        }
    },
    {
        "id": 103,
        "name": "Monster Energy 500ml",
        "description": "Boisson énergisante Monster Energy pour un coup de boost instantané.",
        "price": 2.29,
        "category": "Boissons",
        "stock": 95,
        "featured": True,
        "images": ["monster.jpg", "monster-2.jpg", "monster-3.jpg"],
        "details": {
            "marque": "Monster",
            "volume": "500ml",
            "type": "Énergisante",
            "origine": "USA"
        }
    },
    {
        "id": 104,
        "name": "Orangina 1,5L",
        "description": "Boisson pétillante à base de jus d'orange avec pulpe, rafraîchissante et unique.",
        "price": 2.10,
        "category": "Boissons",
        "stock": 110,
        "featured": False,
        "images": ["orangina.jpg", "orangina-2.jpg", "orangina-3.jpg"],
        "details": {
            "marque": "Orangina",
            "volume": "1.5L",
            "saveur": "Orange",
            "origine": "France"
        }
    },
    {
        "id": 105,
        "name": "Nutella Pot 1kg",
        "description": "Pâte à tartiner au cacao et aux noisettes, idéale pour le petit déjeuner.",
        "price": 6.49,
        "category": "Épicerie",
        "stock": 80,
        "featured": True,
        "images": ["nutella.jpg", "nutella-2.jpg", "nutella-3.jpg"],
        "details": {
            "marque": "Nutella",
            "poids": "1kg",
            "composition": "Noisettes, cacao, lait écrémé",
            "origine": "Italie"
        }
    },
    {
        "id": 112,
        "name": "Palette de 1200 paquets de biscuits Nutella 220g",
        "description": "Palette contenant 1200 paquets de biscuits Nutella de 220g.",
        "price": 3600.00,
        "category": "Épicerie",
        "stock": 5,
        "featured": False,
        "images": ["biscuits-nutella.jpg", "biscuits-nutella-2.jpg", "biscuits-nutella-3.jpg"],
        "details": {
            "marque": "Nutella",
            "quantité": "1200x220g",
            "origine": "France"
        }
    },
    {
        "id": 113,
        "name": "Palette de 144 bouteilles de Coca-Cola Zero 1L",
        "description": "Palette contenant 144 bouteilles de Coca-Cola Zero de 1L.",
        "price": 1550.00,
        "category": "Boissons",
        "stock": 10,
        "featured": False,
        "images": ["coca-zero.jpg", "coca-zero-2.jpg", "coca-zero-3.jpg"],
        "details": {
            "marque": "Coca-Cola",
            "quantité": "144x1L",
            "origine": "France"
        }
    },
    {
        "id": 114,
        "name": "Palette de 600 bouteilles d'eau gazeuse San Pellegrino 50cl",
        "description": "Palette contenant 600 bouteilles d'eau gazeuse San Pellegrino de 50cl.",
        "price": 3600.00,
        "category": "Boissons",
        "stock": 8,
        "featured": False,
        "images": ["san-pellegrino.jpg", "san-pellegrino-2.jpg", "san-pellegrino-3.jpg"],
        "details": {
            "marque": "San Pellegrino",
            "quantité": "600x50cl",
            "origine": "Italie"
        }
    },
    {
        "id": 115,
        "name": "Palette de 1320 canettes de bière Heineken 33cl",
        "description": "Palette contenant 1320 canettes de bière Heineken de 33cl.",
        "price": 3960.00,
        "category": "Boissons",
        "stock": 6,
        "featured": False,
        "images": ["heineken.jpg", "heineken-2.jpg", "heineken-3.jpg"],
        "details": {
            "marque": "Heineken",
            "quantité": "1320x33cl",
            "origine": "Pays-Bas"
        }
    },
    {
        "id": 116,
        "name": "Palette de 960 bouteilles d'eau gazeuse Perrier fines bulles 50cl",
        "description": "Palette contenant 960 bouteilles d'eau gazeuse Perrier fines bulles de 50cl.",
        "price": 3990.00,
        "category": "Boissons",
        "stock": 7,
        "featured": False,
        "images": ["perrier-fines-bulles.jpg", "perrier-fines-bulles-2.jpg", "perrier-fines-bulles-3.jpg"],
        "details": {
            "marque": "Perrier",
            "quantité": "960x50cl",
            "origine": "France"
        }
    },
    {
        "id": 117,
        "name": "Palette de 960 bouteilles d'eau Volvic citron 50cl",
        "description": "Palette contenant 960 bouteilles d'eau Volvic citron de 50cl.",
        "price": 3990.00,
        "category": "Boissons",
        "stock": 7,
        "featured": False,
        "images": ["volvic-citron.jpg", "volvic-citron-2.jpg", "volvic-citron-3.jpg"],
        "details": {
            "marque": "Volvic",
            "quantité": "960x50cl",
            "origine": "France"
        }
    },
    {
        "id": 118,
        "name": "Palette de 960 canettes de Lipton Ice Tea pêche 33cl",
        "description": "Palette contenant 960 canettes de Lipton Ice Tea pêche de 33cl.",
        "price": 3990.00,
        "category": "Boissons",
        "stock": 7,
        "featured": False,
        "images": ["lipton-ice-tea.jpg", "lipton-ice-tea-2.jpg", "lipton-ice-tea-3.jpg"],
        "details": {
            "marque": "Lipton",
            "quantité": "960x33cl",
            "origine": "France"
        }
    },
    {
        "id": 119,
        "name": "Palette de 720 boîtes de capsules de café Café Royal Espresso (36 capsules)",
        "description": "Palette contenant 720 boîtes de capsules de café Café Royal Espresso, chaque boîte contenant 36 capsules.",
        "price": 3990.00,
        "category": "Épicerie",
        "stock": 5,
        "featured": True,
        "images": ["cafe-royal.jpg", "cafe-royal-2.jpg", "cafe-royal-3.jpg"],
        "details": {
            "marque": "Café Royal",
            "quantité": "720x36 capsules",
            "origine": "Suisse"
        }
    },
    {
        "id": 120,
        "name": "Palette de 720 paquets de dosettes de café Senseo Classique (54 dosettes)",
        "description": "Palette contenant 720 paquets de dosettes de café Senseo Classique, chaque paquet contenant 54 dosettes.",
        "price": 3990.00,
        "category": "Épicerie",
        "stock": 5,
        "featured": False,
        "images": ["senseo-classique.jpg", "senseo-classique-2.jpg", "senseo-classique-3.jpg"],
        "details": {
            "marque": "Senseo",
            "quantité": "720x54 dosettes",
            "origine": "France"
        }
    },
    {
        "id": 121,
        "name": "Palette de 720 boîtes de capsules de café L'Or Espresso Delizioso (50 capsules)",
        "description": "Palette contenant 720 boîtes de capsules de café L'Or Espresso Delizioso, chaque boîte contenant 50 capsules.",
        "price": 3990.00,
        "category": "Épicerie",
        "stock": 5,
        "featured": False,
        "images": ["lor-espresso.jpg", "lor-espresso-2.jpg", "lor-espresso-3.jpg"],
        "details": {
            "marque": "L'Or",
            "quantité": "720x50 capsules",
            "origine": "France"
        }
    },
    {
        "id": 200,
        "name": "Palette de Moët & Chandon Brut Impérial (600 bouteilles)",
        "description": "Palette contenant 600 bouteilles de Moët & Chandon Brut Impérial 75cl.",
        "price": 36000.00,
        "category": "Boissons",
        "stock": 2,
        "featured": True,
        "images": ["moet-chandon.jpg","moet-chandon-1.jpg","moet-chandon-2.jpg"],
        "details": {
            "marque": "Moët & Chandon",
            "volume": "75cl",
            "origine": "Champagne, France"
        }
    },
    {
        "id": 201,
        "name": "Palette de Ruinart Blanc de Blancs (600 bouteilles)",
        "description": "Palette contenant 600 bouteilles de Ruinart Blanc de Blancs 75cl.",
        "price": 48000.00,
        "category": "Boissons",
        "stock": 1,
        "featured": True,
        "images": ["ruinart.jpg","ruinart-1.jpg","ruinart-3.jpg"],
        "details": {
            "marque": "Ruinart",
            "volume": "75cl",
            "origine": "Champagne, France"
        }
    },
    {
        "id": 202,
        "name": "Palette de Dom Pérignon Vintage (480 bouteilles)",
        "description": "Palette contenant 480 bouteilles de Dom Pérignon Vintage 75cl.",
        "price": 72000.00,
        "category": "Boissons",
        "stock": 1,
        "featured": True,
        "images": ["dom-perignon.jpg","dom-perignon-1.jpg","dom-perignon-2.jpg"],
        "details": {
            "marque": "Dom Pérignon",
            "volume": "75cl",
            "origine": "Champagne, France"
        }
    },
    {
        "id": 203,
        "name": "Palette de jus d'orange 1L (600 bouteilles)",
        "description": "Palette contenant 600 bouteilles de jus d'orange pur 1L.",
        "price": 3000.00,
        "category": "Boissons",
        "stock": 6,
        "featured": False,
        "images": ["jus-orange.jpg"],
    },
    {
        "id": 204,
        "name": "Palette de jus de pomme 1L (600 bouteilles)",
        "description": "Palette contenant 600 bouteilles de jus de pomme pur 1L.",
        "price": 3000.00,
        "category": "Boissons",
        "stock": 6,
        "featured": False,
        "images": ["jus-pomme.jpg"],
    },
    {
        "id": 205,
        "name": "Palette de jus d'ananas 1L (600 bouteilles)",
        "description": "Palette contenant 600 bouteilles de jus d'ananas pur 1L.",
        "price": 3600.00,
        "category": "Boissons",
        "stock": 6,
        "featured": False,
        "images": ["jus-ananas.jpg"],
    },
    {
        "id": 206,
        "name": "Palette de biscuits Nutella 220g (1200 paquets)",
        "description": "Palette contenant 1200 paquets de biscuits Nutella 220g.",
        "price": 3600.00,
        "category": "Épicerie",
        "stock": 5,
        "featured": False,
        "images": ["biscuits-nutella.jpg"],
    },
    {
        "id": 207,
        "name": "Palette de lait UHT 1L (1200 bouteilles)",
        "description": "Palette contenant 1200 bouteilles de lait UHT 1L.",
        "price": 1200.00,
        "category": "Produits laitiers",
        "stock": 5,
        "featured": False,
        "images": ["lait-uht.jpg"],
    },
    {
        "id": 122,
        "name": "Palette de 960 tablettes de chocolat J.D. Gross Dubaï 122g",
        "description": "Palette contenant 960 tablettes de chocolat J.D. Gross Dubaï de 122g.",
        "price": 3990.00,
        "category": "Épicerie",
        "stock": 5,
        "featured": False,
        "images": ["jd-gross-dubai.jpg", "jd-gross-dubai-2.jpg", "jd-gross-dubai-3.jpg"],
        "details": {
            "marque": "J.D. Gross",
            "quantité": "960x122g",
            "origine": "Allemagne"
        }
    }
]
