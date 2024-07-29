from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import datetime

def create_receipt(transaction_id, customer_name, items, total_amount, file_name):
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2.0, height - inch, "Payment Receipt")

    # Transaction Details
    c.setFont("Helvetica", 12)
    c.drawString(inch, height - 2 * inch, f"Transaction ID: {transaction_id}")
    c.drawString(inch, height - 2.5 * inch, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(inch, height - 3 * inch, f"Customer Name: {customer_name}")

    # Items Table
    c.drawString(inch, height - 3.5 * inch, "Items Purchased:")
    c.drawString(inch, height - 4 * inch, "----------------------------------------")
    y = height - 4.5 * inch
    for item, price in items:
        c.drawString(inch, y, f"{item}: ${price:.2f}")
        y -= 0.5 * inch

    # Total Amount
    c.drawString(inch, y, "----------------------------------------")
    y -= 0.5 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(inch, y, f"Total Amount: ${total_amount:.2f}")

    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(inch, y - 2 * inch, "Thank you for your purchase!")

    c.save()

# Example usage
transaction_id = "1234567890"
customer_name = "THURAKA SREERAM"
items = [("Item A", 10.00), ("Item B", 20.00), ("Item C", 30.00)]
total_amount = sum(price for _, price in items)
file_name = "payment_receipt.pdf"

create_receipt(transaction_id, customer_name, items, total_amount, file_name)
print(f"Receipt saved as {file_name}")