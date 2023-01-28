from contextlib import contextmanager

@contextmanager
def generic(card_type, sender, receiver):
    card_file = open(card_type, 'r')
    order = open(f'{sender}_generic.txt', 'w')

    try:
        order.write(f'Dear {receiver}, \n')
        order.write(card_file.read())
        order.write(f'Sincerely, {sender}\n')
        yield order
    finally:
        order.close()
        card_file.close()

with generic('thankyou.txt', 'Mwenda', 'Amanda') as order1:
    print('Card Generated')

with open('Mwenda_generic.txt', 'r') as first_order:
    print(first_order.read())


class Personalized:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.file = open(f'{sender}_personalized.txt', 'w')

    def __enter__(self):
        self.file.write(f'Dear {self.receiver} \n')
        return self.file
    def __exit__(self, *args):
        self.file.write(f'Sincerely, {self.sender} \n')
        self.file.close()

with Personalized('John', 'Michael') as order2:
    order2.write('''I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.''')
with open('John_personalized.txt', 'r') as second_order:
    print(second_order.read())