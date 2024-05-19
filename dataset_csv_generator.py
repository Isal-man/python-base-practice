import pandas as pd
import numpy as np

# Define the total number of rows and chunk size
total_rows = 500000000  # Total number of rows needed
chunk_size = 100000  # Process in chunks

# Define random date range
min_date = pd.to_datetime('2020-01-01')
max_date = pd.to_datetime('2024-05-18')

# Function to generate a chunk of data
def generate_chunk(chunk_size):
    order_date = min_date + (max_date - min_date) * np.random.rand(chunk_size)
    order_id = np.random.randint(1000000, size=chunk_size, dtype=np.int32)
    ship_days = np.random.randint(1, 14, size=chunk_size)
    ship_date = order_date + pd.to_timedelta(ship_days, unit='D')
    ship_mode = np.random.choice(['Standard Class', 'Second Class', 'First Class', 'Same Day'], chunk_size)
    customer_segment = np.random.choice(['Consumer', 'Corporate', 'Home Office'], chunk_size)
    country = np.random.choice(['United States'], chunk_size)
    customer_name = np.random.choice([
        'Alejandro Grove', 'Andrew Allen', 'Brendan Sweed', 'Brosina Hoffman', 'Christopher Schild', 'Claire Gute',
        'Darren Powers', 'Darrin Van', 'Duane Noonan', 'Elpida Rittenbach', 'Emily Burns', 'Eric Hoffmann', 'Erin Smith',
        'Gary Mitchum', 'Gene Hale', 'Harold Pawlan', 'Henry MacAllister', 'Irene Maddox', 'Janet Molinari', 'Jim Sink',
        'Joel Eaton', 'Julie Creighton', 'Karen Daniels', 'Karl Braun', 'Katherine Ducich', 'Ken Black', 'Ken Brennan',
        'Kunst Miller', 'Lena Hernandez', 'Linda Cazamias', 'Matt Abelman', 'Odella Nelson', 'Parhena Norri', 'Patrick ODonne',
        'Paul Gonzalez', 'Paul Stevenson', 'Pete Kriz', 'Rick Bensley', 'Roger Barcio', 'Ruben Ausman', 'Sandra Flanaga',
        'Sean ODonne', 'Steve Nguyen', 'Stewart Carmichael', 'Ted Butterfield', 'Tracy Blumstein', 'Zuschuss Donatelli'
    ], chunk_size)
    city = np.random.choice([
        'Chicago', 'Columbia', 'Concord', 'Decatur', 'Dover', 'Durham', 'Eagan', 'Fremont', 'Gilbert', 'Henderson', 'Houston',
        'Jackson', 'Madison', 'Melbourne', 'Memphis', 'Minneapolis', 'Naperville', 'Orem', 'Philadelphia', 'Portland',
        'Richardson', 'Rochester', 'Seattle', 'Springfield', 'Troy', 'Westland'
    ], chunk_size)
    state = np.random.choice([
        'Illinois', 'Alabama', 'Delaware', 'Minnesota', 'Florida', 'Texas', 'Nebraska', 'Arizona', 'Kentucky', 'Michigan',
        'California', 'Wisconsin', 'Tennessee', 'Utah', 'Pennsylvania', 'Oregon', 'Virginia'
    ], chunk_size)
    postal = np.random.randint(10000, 99999, size=chunk_size)
    region = np.random.choice(['East', 'West', 'Central', 'South'], chunk_size)
    category = np.random.choice(['Furniture', 'Office Supplies', 'Technology'], chunk_size)
    sub_category = np.random.choice([
        'Bookcases', 'Chairs', 'Labels', 'Tables', 'Storage', 'Furnishings', 'Art', 'Phones', 'Binders', 'Appliances',
        'Paper', 'Accessories', 'Fasteners', 'Envelopes'
    ], chunk_size)
    product_name = np.random.choice([
        "Bush Somerset Collection Bookcase", "Hon Deluxe Fabric Upholstered Stacking Chairs", "Self-Adhesive Address Labels",
        "Bretford CR4500 Series Slim Rectangular Table", "Eldon Fold 'N Roll Cart System", "Eldon Expressions Desk Accessories",
        "Newell 322", "Mitel 5320 IP Phone", "DXL Angle-View Binders", "Belkin F5C206VTEL 6 Outlet Surge",
        "Chromcraft Rectangular Conference Tables", "Konftel 250 Conference phone", "Xerox 1967", "Fellowes PB200 Plastic Comb Binding Machine",
        "Holmes Replacement Filter for HEPA Air Cleaner", "Storex DuraTech Recycled Plastic Frosted Binders", "Fellowes Super Stor/Drawer",
        "Newell 341", "Cisco SPA 501G IP Phone", "Wilson Jones Hanging View Binder", "Acco Six-Outlet Power Strip",
        "Global Deluxe Stacking Chair", "Riverside Palais Royal Lawyers Bookcase", "Howard Miller Wall Clock",
        "Poly String Tie Envelopes", "BOSTON Electric Pencil Sharpeners", "Imation 8GB Mini TravelDrive", "C-Line Peel & Stick Filing Pockets"
    ], chunk_size)
    sales = np.random.rand(chunk_size) * 1000
    quantity = np.random.randint(1, 10, size=chunk_size)
    discount = np.random.rand(chunk_size) * 0.2
    profit = sales * (np.random.rand(chunk_size) * 0.1) - (discount * sales)
    manufacturer = np.random.choice([
        "Bush", "Hon", "Universal", "Bretford", "Eldon", "Newell", "Mitel", "DXL", "Belkin", "Chromcraft", "Xerox", "Fellowes",
        "Holmes", "Storex", "Cisco", "Wilson Jones", "Acco", "Global", "Riverside", "Avery", "Howard Miller", "Poly", "Boston",
        "GE", "Electrix", "Atlantic", "Plantronics", "Panasonic", "Advantus", "Verbatim", "Gould Plastics", "Imation", "Prang",
        "Luxo", "Hunt", "Tenex", "SAFCO", "Novimex", "Logitech", "Seth Thomas", "Ibico"
    ], chunk_size)

    return pd.DataFrame({
        'Order Date': order_date,
        'Order ID': order_id,
        'Ship Date': ship_date,
        'Ship Mode': ship_mode,
        'Customer Name': customer_name,
        'Segment': customer_segment,
        'Country/Region': country,
        'City': city,
        'State': state,
        'Postal': postal,
        'Region': region,
        'Category': category,
        'Sub-Category': sub_category,
        'Product Name': product_name,
        'Sales': sales,
        'Quantity': quantity,
        'Discount': discount,
        'Profit': profit,
        'Manufacturer': manufacturer
    })

# Initialize the first chunk and write to CSV
df = generate_chunk(chunk_size)
df.to_csv('superstore-dataset.csv', index=False)

# Append subsequent chunks
for _ in range(total_rows // chunk_size - 1):
    df = generate_chunk(chunk_size)
    df.to_csv('superstore-dataset.csv', mode='a')

print("Done Abangkuuu🔥🔥")