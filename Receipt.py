p1_name, p1_price = "Paint Palette", 5.99
p2_name, p2_price = "Paint Brushes", 7.49
p3_name, p3_price = "Watercolor Paints", 15.99

company_name = "kuhoo's art supplies"
company_address = "1990 Miltec Ter."
company_city = "Richmond, VA"

message = "Thank you for your purchase!\t\t .\n.\tWe hope you enjoy your items."

print("." * 50)
print(f".\t\t{company_name.title( )}\t\t .")
print(f".\t\t{company_address}\t\t .")
print(f".\t\t{company_city}\t\t\t .")

print("."+"=" * 48+".")
print(f".\t{p1_name.title( )}\t\t${p1_price}\t\t .")
print(f".\t{p2_name.title( )}\t\t${p2_price}\t\t .")
print(f".\t{p3_name.title( )}\t${p3_price}\t\t .")

print("."+"=" * 48+".")
print(".\t\t\tTotal\t\t\t .")
total = p1_price + p2_price + p3_price
print(f".\t\t\t${total}\t\t\t .")

print("."+"=" * 48+".")
print(f".\t\t\t\t\t\t .\n.\t{message}\t\t .\n.\t\t\t\t\t\t .")

print("." * 50)

