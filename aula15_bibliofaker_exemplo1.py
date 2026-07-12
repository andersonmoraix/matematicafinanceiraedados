#aula 15 - tratando dados com faker

from faker import Faker

fake = Faker('pt_BR')

# Demonstração de geradores básicos
print(f"Nome Fictício: {fake.name()}")
print(f"Empresa Fictícia: {fake.company()}")
print(f"Texto Fictício: {fake.paragraph(nb_sentences=2)}")
