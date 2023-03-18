from flask import Flask, render_template, request
from googleapiclient.discovery import build

app = Flask(__name__)

@app.route('/')
def index():
    books = [] 

    recommended_books = [
   {
    'titulo': 'Harry Potter y la Piedra Filosofal',
    'autor': 'J.K. Rowling',
    'descripcion': 'La primera aventura del famoso mago Harry Potter.',
    'imagen': 'Piedra.jpg'
},

    {
        'titulo': 'Harry Potter y la Cámara Secreta',
        'autor': 'J.K. Rowling',
        'descripcion': 'La segunda aventura del famoso mago Harry Potter.',
        'imagen': 'Camara.jpg'
    },
    {
        'titulo': 'Harry Potter y el Prisionero de Azkaban',
        'autor': 'J.K. Rowling',
        'descripcion': 'La tercera aventura del famoso mago Harry Potter.',
        'imagen': 'Pris.jpg'
    },
    {
    'titulo': 'El psicoanalista',
    'autor': 'John Katzenbach',
    'descripcion': 'Un thriller psicológico sobre un psicoanalista que es secuestrado por uno de sus pacientes.',
    'imagen': 'psico.jpeg'
    },  
{
    'titulo': 'La ciudad de las bestias',
    'autor': 'Isabel Allende',
    'descripcion': 'Una novela de aventuras que sigue a un joven periodista en una expedición a la selva amazónica.',
    'imagen': 'laci.jpeg'
},
{
    'titulo': 'La elegancia del erizo',
    'autor': 'Muriel Barbery',
    'descripcion': 'Una novela que narra la vida de dos mujeres solitarias en un edificio de apartamentos en París.',
    'imagen': 'erizo.jpeg'
},
{
    'titulo': 'El jardín secreto',
    'autor': 'Frances Hodgson Burnett',
    'descripcion': 'Una novela para niños sobre una niña que descubre un jardín mágico en la finca de su tío.',
    'imagen': 'jardin.jpeg'
},
{
    'titulo': 'El paciente inglés',
    'autor': 'Michael Ondaatje',
    'descripcion': 'Una novela ambientada en la Segunda Guerra Mundial sobre un hombre quemado y herido que se encuentra en una villa italiana.',
    'imagen': 'paciente.jpeg'
},
{
    'titulo': 'El corredor del laberinto',
    'autor': 'James Dashner',
    'descripcion': 'Una novela de ciencia ficción juvenil sobre un grupo de jóvenes que intenta escapar de un laberinto mortal.',
    'imagen': 'laberin.jpeg'
},
{
    'titulo': 'El niño con el pijama de rayas',
    'autor': 'John Boyne',
    'descripcion': 'Una novela sobre la amistad de dos niños durante el Holocausto.',
    'imagen': 'pijama.jpeg'
},
{
    'titulo': 'El médico',
    'autor': 'Noah Gordon',
    'descripcion': 'Una novela histórica sobre un joven inglés que viaja al mundo islámico medieval para estudiar medicina.',
    'imagen': 'medico.jpeg'
},
{
    'titulo': 'El libro de los cinco anillos',
    'autor': 'Miyamoto Musashi',
    'descripcion': 'Un libro de estrategia y filosofía samurái escrito por el legendario guerrero japonés.',
    'imagen': 'anillo.jpeg'
},
{
    'titulo': 'La hoguera de las vanidades',
    'autor': 'Tom Wolfe',
    'descripcion': 'Una sátira sobre la sociedad y la política de la década de 1980 en Nueva York.',
    'imagen': 'hoguera.jpeg'
},

{
    'titulo': '1984',
    'autor': 'George Orwell',
    'descripcion': 'Un clásico distópico sobre una sociedad controlada por un gobierno opresivo.',
    'imagen': 'orwell.jpeg'
},
{
    'titulo': 'El gran Gatsby',
    'autor': 'F. Scoot Fitzgerald',
    'descripcion': 'Una novela que explora la riqueza, la decadencia y el amor.',
    'imagen': 'grat.jpeg'
},

{
    'titulo': 'La metamorfosis',
    'autor': 'Franz Kafka',
    'descripcion': 'Un relato sobre un hombre que se despierta convertido en un insecto.',
    'imagen': 'metamor.jpeg'
},

{
    'titulo': 'Matar a un risueñor',
    'autor': 'Harper Lee',
    'descripcion': 'Un libro sobre la raza, la justicia y la inocencia en el sur de Estados Unidos.',
    'imagen': 'ruiseñor.jpeg'
},

{
    'titulo': 'El retrato de Dorian Gray',
    'autor': 'Oscar Wilde',
    'descripcion': 'Una historia sobre la corrupción y el envejecimiento en la sociedad victoriana.',
    'imagen': 'retrato.jpeg'
},

{
    'titulo': 'El guardián entre el centeno',
    'autor': 'J.D. Salinger',
    'descripcion': 'Una novela sobre un adolescente que lucha con la soledad y la pérdida de inocencia.',
    'imagen': 'guardian.jpeg'
},

{
    'titulo': 'Cien años de soledad',
    'autor': 'Gabriel García Márquez',
    'descripcion': 'Una saga familiar que explora la vida en un pueblo aislado en América Latina.',
    'imagen': 'pdf.jpeg'
},

{
    'titulo': 'El señor de las moscas',
    'autor': 'William Golding',
    'descripcion': 'Un clásico sobre un grupo de niños vetados en una isla desierta y su lucha por la supervivencia .',
    'imagen': 'moscas.jpeg'
},

{
    'titulo': 'Las aventuras de Huckleberry Finn',
    'autor': 'Mark Twain',
    'descripcion': 'Una historia sobre la amistad y la libertad en el sur de Estados Unidos.',
    'imagen': 'mark.jpeg'
},

{
    'titulo': 'Crónica de una muerte anunciada',
    'autor': 'Gabriel García Márquez',
    'descripcion': 'Una novela corta sobre el asesinato de un hombre en un pequeño pueblo colombiano.',
    'imagen': 'cronica.jpeg'
},

{
    'titulo': 'El Diario de Greg 2',
    'autor': 'Jeff Kinney',
    'descripcion': 'En "El Diario de Greg 2: La Ley de Rodrick", Greg Heffley enfrenta desafíos en la escuela y en casa, incluyendo a su problemático hermano mayor Rodrick.',
    'imagen': 'greg.jpg'
},
    
    
    
    
]
    
    return render_template('index.html', books=books, recommended_books=recommended_books)


@app.route('/search')
def search():
    query = request.args.get('query')
    api_key = 'AIzaSyAC2TmYyRxOGLSU-pLPor0M5NzhHrfjxYc'
    service = build('books', 'v1', developerKey=api_key)
    res = service.volumes().list(q=query).execute()
    items = res.get('items', [])


    books = []
    for item in items:
        book = {}
        volume_info = item.get('volumeInfo', {})
        book['titulo'] = volume_info.get('title', '')
        book['autor'] = ', '.join(volume_info.get('authors', []))
        book['descripcion'] = volume_info.get('description', '')
        book['imagen'] = volume_info.get('imageLinks', {}).get('thumbnail', '')
        books.append(book)

    return render_template('search.html', books=books)

@app.route('/book/<book_id>')
def book_details(book_id):
    api_key = 'AIzaSyAC2TmYyRxOGLSU-pLPor0M5NzhHrfjxYc'
    service = build('books', 'v1', developerKey=api_key)
    book = service.volumes().get(volumeId=book_id).execute()


    volume_info = book.get('volumeInfo', {})
    titulo = volume_info.get('title', '')
    autores = ', '.join(volume_info.get('authors', []))
    descripcion = volume_info.get('description', '')
    imagen = volume_info.get('imageLinks', {}).get('thumbnail', '')
    categorias = ', '.join(volume_info.get('categories', []))
    fecha_publicacion = volume_info.get('publishedDate', '')
    editoriales = ', '.join(volume_info.get('publisher', []))
    idioma = volume_info.get('language', '')

    reseñas = []
    reviews = book.get('reviews', [])
    for review in reviews:
        autor = review.get('author', '')
        texto = review.get('snippet', '')
        reseñas.append({'autor': autor, 'texto': texto})
    return render_template('book.html', titulo=titulo, autores=autores, descripcion=descripcion, imagen=imagen, categorias=categorias, fecha_publicacion=fecha_publicacion, editoriales=editoriales, idioma=idioma, reseñas=reseñas)


if __name__ == '__main__':
    app.run(debug=True)