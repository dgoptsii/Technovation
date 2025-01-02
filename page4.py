import streamlit as st

def app():
    st.title("Contact us")
  
# Запит 4 імен та відповідних Gmail-адрес
names = []
emails = []

for i in range(4):
    name = input(f"Сафіє {i + 1}: ")
    email = input(f"kadyrovasafie67@gmail.com {name}: ")
    
    # Перевірка, чи це Gmail-адреса
    if "@gmail.com" not in email:
        print("Будь ласка, введіть коректну Gmail-адресу.")
        email = input(f"Повторно введіть Gmail для {name}: ")
    
    names.append(name)
    emails.append(email)

# Виведення імен та Gmail-адрес
print("\nВведені дані:")
for i in range(4):
    print(f"Ім'я: {names[i]}, Gmail: {emails[i]}")

 
