
# Agenda Telefonica

Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el Primer Nombre, Apellido Paterno, Teléfono, Email y DNI  Además deberá mostrar un menú con las siguientes opciones

-   Añadir contacto
-   Lista de contactos
-   Buscar contacto
-   Editar contacto
-   Eliminar contacto
-   Cerrar agenda

### Validaciones
- Realizar Fork al repositorio de GitLab [Click Aqui](https://gitlab.com/pachaqtec_backend/challengue_week_04.git)

- Realizar un clone mediante git SSH. **No usar HTTPS**

- El campo teléfono deberá empezar con 9, debe contener 9 digitos.
- El campo Primer Nombre, deberá guardarse solo la primera Letra en Mayusculas, el resto en minúsculas. No se permite el ingreso de números.
- El campo Apellido Paterno, deberá guardarse solo la primera Letra en Mayusculas, el resto en minúsculas. No se permite el ingreso de números.
- El campo Email, debe tener como mínimo el símbolo @, y debe tener mas de 8 caracteres, y deberá guardarse solo en minúsculas, ademas debe finalizar con **".com"**
- El campo DNI deberá contener solo 8 digitos. Ojo puede empezar con cero por lo tanto debe ser un string. Solo ingresos de números.
- Existen 02 formas de buscar un contacto, búsqueda por DNI o por Nombre. Ejemplo si ingreso ***ala***, me deberá mostrar todos los contactos que empiecen por esa palabra.
- Para Editar y Eliminar un contacto solo se buscara por numero de DNI, y deberá validar lo indicado lineas arriba.

### Links
- [Métodos de Validación](https://uniwebsidad.com/libros/python/capitulo-6/metodos-de-validacion)
- [SSH-Keygen GitLab - Documentacion](https://docs.gitlab.com/ee/ssh/)
- [SSH-Keygen GitLab Video](https://www.youtube.com/watch?v=j-zmv-ITQb8)

### Conceptos que se aplicaran

-	Listas
-	Diccionarios
-	Rebanadas de Listas
-	Validaciones de Input
-	Búsqueda de Listas
-	IF
-	For
-	While
-	POO
-   Excepcions