# Club-Paddle: Sistema de Reservas de Pistas de Pádel

`Club-Paddle` es una aplicación web sencilla desarrollada con Flask para gestionar las reservas de pistas de pádel. Permite a los usuarios ver la disponibilidad de las pistas durante la semana actual, realizar nuevas reservas e incluso cancelarlas.

## Características

*   **Visualización de Calendario Semanal:** Muestra un calendario con los próximos 7 días, permitiendo ver las horas disponibles y las ya reservadas.
*   **Realizar Reservas:** Los usuarios pueden seleccionar una fecha y hora disponibles para reservar una pista, proporcionando su nombre.
*   **Cancelar Reservas:** Los usuarios pueden cancelar reservas existentes.
*   **Interfaz Web Sencilla:** Interfaz de usuario intuitiva para una fácil navegación y gestión de reservas.
*   **Almacenamiento en Memoria:** Para fines de demostración y pruebas, las reservas se almacenan en la memoria del servidor (se pierden al reiniciar la aplicación).

## Requisitos Previos

*   Python 3.x
*   Flask

## Instalación y Ejecución

1.  **Clona el repositorio (si aplica) o descarga los archivos del proyecto.**

2.  **Navega al directorio del proyecto:**
    ```bash
    cd ruta/a/club-paddle/paddle_web
    ```

3.  **(Opcional pero recomendado) Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    # venv\Scripts\activate
    # En macOS/Linux
    # source venv/bin/activate
    ```

4.  **Instala las dependencias:**
    ```bash
    pip install Flask
    ```

5.  **Ejecuta la aplicación Flask:**
    ```bash
    python app.py
    ```

6.  Abre tu navegador web y ve a `http://127.0.0.1:5000/` para ver la página de inicio o `http://127.0.0.1:5000/reservas` para acceder al sistema de reservas.

## Futuras Mejoras

*   Implementar una base de datos persistente (ej. SQLite, PostgreSQL) para almacenar las reservas.
*   Añadir autenticación de usuarios.
*   Permitir la gestión de múltiples pistas.
*   Mejorar la interfaz de usuario.
*   Añadir validaciones más robustas.
*   Autenticación de usuarios: Permite que los usuarios se registren e inicien  sesión, así cada reserva queda asociada a un usuario.
*   Confirmación de reserva por email: Envía un correo electrónico al usuario cuando realiza o cancela una reserva.
*   Gestión de varias canchas: Permite elegir entre varias canchas al reservar (por ejemplo, Cancha 1, Cancha 2, etc.).
*   Límite de reservas por usuario: Restringe la cantidad de reservas activas que puede tener un usuario.
*   Historial de reservas: Muestra a cada usuario un historial de sus reservas pasadas y futuras.
*   Integración de pagos: Permite pagar la reserva online (por ejemplo, usando MercadoPago, Stripe, etc.).
*   Panel de administración: Un panel especial para el administrador del club donde pueda ver, editar o eliminar cualquier reserva.
*   Notificaciones automáticas: Envía recordatorios por email o SMS antes de la hora de la reserva.
*   Bloqueo de horarios especiales: Permite al administrador bloquear horarios por mantenimiento o eventos especiales.
*   Mejoras visuales: Usa un framework como Bootstrap para que el sitio se vea más profesional y sea responsivo en celulares.