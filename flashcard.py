import tkinter as tk
import random

# Define the flashcards
german_cards = [    {'front': 'Guten Tag', 'back': 'Hello'},    {'front': 'Danke', 'back': 'Thank you'},    {'front': 'Ja', 'back': 'Yes'},    {'front': 'Nein', 'back': 'No'},]

spanish_cards = [    {'front': 'Hola', 'back': 'Hello'},    {'front': 'Gracias', 'back': 'Thank you'},    {'front': 'Sí', 'back': 'Yes'},    {'front': 'No', 'back': 'No'},]

english_cards = [    {'front': 'Apple', 'back': 'Apfel'},    {'front': 'Book', 'back': 'Buch'},    {'front': 'House', 'back': 'Haus'},    {'front': 'Car', 'back': 'Auto'},]

# Shuffle the cards
random.shuffle(german_cards)
random.shuffle(spanish_cards)
random.shuffle(english_cards)

# Define a function to flip the card
def flip_card():
    if show_front:
        current_card.config(text=current_card_details['back'])
    else:
        current_card.config(text=current_card_details['front'])
    global show_front
    show_front = not show_front

# Create the GUI window
window = tk.Tk()
window.title('Flashcards')

# Define the card display
current_card_details = None
show_front = True
current_card = tk.Label(window, text='', font=('Arial', 24), bg='white', width=20, height=10, relief='raised')
current_card.pack(pady=20)

# Define the language buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

german_button = tk.Button(button_frame, text='German', font=('Arial', 16), width=10, height=2, command=lambda: start_game(german_cards))
german_button.pack(side='left', padx=10)

spanish_button = tk.Button(button_frame, text='Spanish', font=('Arial', 16), width=10, height=2, command=lambda: start_game(spanish_cards))
spanish_button.pack(side='left', padx=10)

english_button = tk.Button(button_frame, text='English', font=('Arial', 16), width=10, height=2, command=lambda: start_game(english_cards))
english_button.pack(side='left', padx=10)

# Define the game function
def start_game(cards):
    global current_card_details, show_front
    current_card_details = cards.pop()
    show_front = True
    current_card.config(text=current_card_details['front'])

    if len(cards) == 0:
        german_button.config(state='disabled')
        spanish_button.config(state='disabled')
        english_button.config(state='disabled')

# Start the GUI loop
window.mainloop()
