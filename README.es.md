# Portafolio de Hokkaido

[简体中文](README.md) · [English](README.en.md) · **Español** · [日本語](README.ja.md)

**[Abrir el portafolio en español](https://hokkaidoooo.github.io/es/)** · [Apuntes](https://hokkaidoooo.github.io/blog/es/) · [Perfil de GitHub](https://github.com/Hokkaidoooo)

Sigue el recorrido de una petición HTTP por un servidor C++, compara políticas de reemplazo de caché o explora cómo se propaga el riesgo en una cadena de suministro. Cada proyecto enlaza con su repositorio. También encontrarás un planificador de materiales, herramientas de lectura sin conexión, un modelo de levantamiento multihaz y un año de registros meteorológicos de Nankín. Los pies de imagen distinguen las capturas, los diagramas y los datos sintéticos. El índice del blog está en español; los artículos están en chino.

## Ver en local

Abre `es/index.html` directamente o ejecuta este comando desde la raíz del repositorio y visita <http://127.0.0.1:4186/es/>:

```sh
python -m http.server 4186 --bind 127.0.0.1
```

El sitio utiliza HTML y CSS estáticos. No necesita JavaScript, fuentes de terceros, analítica, cookies ni compilación del frontend. Las imágenes se sirven desde el propio sitio. GitHub Pages y los sitios externos tienen sus propias políticas de servicio.

## Estructura e imágenes

- [`index.html`](index.html) contiene la estructura compartida, los textos en chino y los enlaces a los proyectos. Las traducciones se encuentran en [`tools/home-copy.json`](tools/home-copy.json). Con Python 3.10 o posterior, ejecuta `python tools/localize.py` tras editar y `python tools/localize.py --check` para comprobar que las tres páginas estén al día.
- Todos los idiomas comparten [`assets/site.css`](assets/site.css). La navegación ofrece un enlace para saltar al contenido, foco visible y compatibilidad con la preferencia de movimiento reducido. GitHub Pages publica los archivos de la raíz de `main`.
- Las [imágenes](assets/) proceden de los proyectos públicos enlazados. El laboratorio muestra su interfaz real; el caso de riesgo usa datos sintéticos; los gráficos meteorológicos resumen los registros de 2023. Los gráficos del servidor, del MRP y del portal de noticias son esquemas. [Créditos y detalles de recorte, en chino](README.md#图片来源).
