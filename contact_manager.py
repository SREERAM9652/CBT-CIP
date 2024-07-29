import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create a table for storing contacts if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    address TEXT,
    company TEXT,
    notes TEXT
)
''')

def add_contact(name, phone, email, address, company, notes):
    cursor.execute('''
    INSERT INTO contacts (name, phone, email, address, company, notes)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, phone, email, address, company, notes))
    conn.commit()

def delete_contact(contact_id):
    cursor.execute('DELETE FROM contacts WHERE id=?', (contact_id,))
    conn.commit()

def search_contacts(query):
    cursor.execute('''
    SELECT * FROM contacts WHERE
    name LIKE ? OR phone LIKE ? OR email LIKE ? OR address LIKE ? OR company LIKE ? OR notes LIKE ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'))
    return cursor.fetchall()

def list_contacts():
    cursor.execute('SELECT * FROM contacts')
    return cursor.fetchall()

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contacts")
        print("4. List All Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            company = input("Enter company: ")
            notes = input("Enter notes: ")
            add_contact(name, phone, email, address, company, notes)
            print("Contact added successfully.")

        elif choice == '2':
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
            print("Contact deleted successfully.")

        elif choice == '3':
            query = input("Enter search query: ")
            results = search_contacts(query)
            print("\nSearch Results:")
            for contact in results:
                print(contact)

        elif choice == '4':
            contacts = list_contacts()
            print("\nAll Contacts:")
            for contact in contacts:
                print(contact)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

# Close the database connection when the script ends
conn.close()
