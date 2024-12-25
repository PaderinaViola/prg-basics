translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
def translate(text):
    human_input = input("Enter your word: ")
    for key, value in text.items():
         if human_input == key:
            return value
         else:
             return "Translation is unavailable"

print(translate(translations))
