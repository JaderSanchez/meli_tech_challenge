# Prompts usados en la resolución de los problemas

La mayor parte de la prueba fue desarrollada sin IA, esto con el proposito de entender muy bien todo lo que se estaba desarrollando y estar preparado para sustentar, debido a que nunca había utilizado el lenguaje GO, y Python aunque lo conocía no es el que uso diariamente.

Sin embargo se utilizaron prompts apuntando a explicaciones y aprendizajes, como por ejemplo:

## 1. Minesweeper

> ¿Como rompo la referencia a una lista en Python?

> ¿Como documento la versión de Python utilizada en un Script?

## 2. Best in genre

> ¿Que equivalente hay en Python para el package.json de JS para definir las dependencias?

> ¿Que equivalente hay en Python al array.filter() de JS?

> ¿Como realizo peticiones HTTP en Python?

> ¿Como utilizo async / await en python?

> ¿Que equivalente hay en Python al Promise.all() de JS?

> ¿Como puedo ordenar una lista de objetos en Python por una de sus propiedades?

```
Necesito hacer lo siguiente en python usando async / await

Tengo un endpoint https://jsonmock.hackerrank.com/api/tvseries?page=1 que retorna tvshows de esta forma:

{
  "page": 1,
  "per_page": 10,
  "total": 200,
  "total_pages": 20,
  "data": [
    {
    "name": "Game of Thrones",
    "runtime_of_series": "(2011-2019)",
    "certificate": "A",
    "runtime_of_episodes": "57 min",
    "genre": "Action, Adventure, Drama",
    "imdb_rating": 9.3,
    "overview": "Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.",
    "no_of_votes": 1773458,
    "id": 1
    }
  ]
}

Entonces necesito una función que haga lo siguiente:

1. Hacer el GET a la primer pagina, y así obtener los resultados de la primer pagina y ademas obtener el total de paginas
2. Ya conociendo el total de paginas, hacer lo equivalente a un promise.all de js, para hacer el fetch de todas las paginas omitiendo la #1
3. La función finalmente debe retornar los datos de todos los tvshows sin la paginación
```

## 3. SQL: Advertising System Failures Report

En este punto quería poder probar la query desarrollada, entonces le pedí ayuda con el setup de la base de datos:

```
[PDF adjunto]
Revisa el punto #4 y dame el SQL para crear la base de datos, sus tablas y los registros de prueba.
```

## 4. Summarizer

En cuanto a los punteros, en algún momento use C++ y ya tenía el concepto y entendía como usarlos, así que esto no lo consulte, y adicionalmente vi una pequeña introducción a GO en un video para entender la sintaxis.

> ¿Como puedo recibir argumentos al ejecutar mi script desde el CLI (por ejemplo -t y --input)?

> ¿Como recibo argumentos posicionales desde el CLI?

> ¿Como documento la versión usada de GO?

> ¿Como verifico si un archivo existe en el file system con GO?

> ¿Como obtyengo el contenido de un archivo con GO?

> ¿Como lanzo excepciones con GO?

> ¿Como hago peticiones HTTP con GO?

> ¿Que librerias me permiten hacer peticiones HTTP de forma simple con GO?

> Explicame el go.mod

## Al finalizar

> Revisa la solución desarrollada de cada uno de los puntos y dame sugerencias de como mejorar el código, adicionalmente dime si puede haber algo que esté omitiendo.

> Ayudame a generar un README.md que explique como instalar y ejecutar cada script y adicionalmente que documente las versiones de los lenguajes.