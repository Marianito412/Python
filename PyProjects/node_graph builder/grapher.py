import networkx as nx
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as soup

#This script scrapes a site holding my study program for Mechatronical engineering and creates a node graph where every node is a
#course and every edge (line) means that one course is a requirement for the other course, it allowed me to better visualize my major's path
#and it was pretty fun to build

url = "https://www.tec.ac.cr/planes-estudio/licenciatura-ingenieria-mecatr%C3%B3nica"
site = requests.get(url)
page_soup = soup(site.text, "html.parser")

table = page_soup.find_all("section", class_="field-text-study-plan-json-feed")
bloques = table[0].find_all("div", class_="accordion-wrapper")

G = nx.Graph()

def makeNode(G, name):
    G.add_node(name)

def makeEdge(G, edge):
    G.add_edge(edge[0], edge[1])

def showGraph(G):
    nx.draw(G, with_labels=True)
    plt.savefig("simple_path.png")
    plt.show()

for bloque in bloques:
    nombre = bloque.find("h2", class_="accordion-topic")
    cursos = bloque.find_all("div", class_="accordion-item")
    for curso in cursos:
        codigo, nombre = curso.find_all("h3", class_="accordion-title")[0].text.split(" - ")
        print(f"{codigo} - {nombre}")
        subinfo = curso.find("div", class_="accordion-body").table.tbody
        subinfo = subinfo.find_all("tr")[1]

        creditos = subinfo.find_all("td")[0].text
        horas = subinfo.find_all("td")[1].text
        requisitos = subinfo.find_all("td")[2].text
        correquisitos = subinfo.find_all("td")[3].text

        print(requisitos)
        for requisito in requisitos.split(", "):
            if requisito != "NO HAY REQUISITOS EN EL PLAN":
                edge = (codigo, requisito)
                makeEdge(G, edge)

        print(f"Créditos: {creditos} Horas: {horas} Requisitos: {requisitos} Correquisitos: {correquisitos}")
        print("_"*150)
        makeNode(G, codigo)
print(G.nodes())
showGraph(G)
