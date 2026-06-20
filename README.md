# Sistema de Inventario

Aplicación web para controlar stock, movimientos de productos y proveedores. Desarrollada como proyecto del módulo de Django.

## Tecnologías

- Python 3.14
- Django 6.0.5
- PostgreSQL 16 (Docker)
- Tailwind CSS (CDN)

## Modelos del sistema

- **Category**: clasificación de productos (ej. repuestos, lubricantes).
- **Supplier**: proveedores con datos de contacto y página de pedidos.
- **Product**: productos del inventario, con stock actual, stock mínimo y relación many-to-many con proveedores.
- **StockMovement**: registro histórico de entradas y salidas de stock por producto.

## Funcionalidades

- CRUD completo de productos, proveedores, categorías y movimientos de stock.
- Actualización automática del stock actual al registrar una entrada o salida.
- Alerta visual cuando el stock actual de un producto es igual o menor al stock mínimo.
- Filtro de productos por categoría.
- Filtro de productos por proveedor (relación many-to-many).

## Instalación local

1. Clonar el repositorio:
   ```bash
   git clone <url-del-repo>
   cd sistema_inventario
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crear archivo `.env` en la raíz con las variables de PostgreSQL:
   ```
   POSTGRES_USER=tu_usuario
   POSTGRES_PASSWORD=tu_password
   POSTGRES_DB=sistema_inventario
   POSTGRES_HOST=127.0.0.1
   POSTGRES_PORT=5432
   ```

5. Levantar PostgreSQL en Docker:
   ```bash
   docker run --name postgres-inventario \
     -e POSTGRES_USER=tu_usuario \
     -e POSTGRES_PASSWORD=tu_password \
     -e POSTGRES_DB=sistema_inventario \
     -p 5432:5432 \
     -d postgres:16
   ```

6. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

7. Levantar el servidor:
   ```bash
   python manage.py runserver
   ```

8. Abrir en el navegador: `http://127.0.0.1:8000/inventory/`

## Estado del proyecto

Proyecto funcional en entorno local. Despliegue a producción pendiente.

## Autor

Germán Lescano — [GitHub](https://github.com/g120795)