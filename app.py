from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Guardaremos las reservas en una lista (en memoria, solo para pruebas)
reservas = []


def get_semana():
    hoy = datetime.now().date()
    semana = [(hoy + timedelta(days=i)) for i in range(7)]
    return semana


HORAS = [
    "09:00",
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00",
    "19:00",
    "20:00",
]


@app.route("/")
def home():
    return "¡Hola, Club de Paddle!"


@app.route("/reservas", methods=["GET", "POST"])
def reservas_view():
    mensaje = ""
    # Cancelar reserva
    if request.method == "POST" and "fecha_cancelar" in request.form:
        fecha = request.form["fecha_cancelar"]
        hora = request.form["hora_cancelar"]
        for r in reservas:
            if r["fecha"] == fecha and r["hora"] == hora:
                reservas.remove(r)
                mensaje = "Reserva cancelada."
                break
    # Nueva reserva
    elif request.method == "POST":
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        nombre = request.form["nombre"]
        for r in reservas:
            if r["fecha"] == fecha and r["hora"] == hora:
                mensaje = "¡Ya existe una reserva para esa fecha y hora!"
                break
        else:
            reservas.append({"fecha": fecha, "hora": hora, "nombre": nombre})
            mensaje = "¡Reserva realizada con éxito!"

    # Preparar datos para el calendario
    semana = get_semana()
    fechas_semana = [d.strftime("%Y-%m-%d") for d in semana]
    reservas_dict = {(r["fecha"], r["hora"]): r for r in reservas}
    dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

    return render_template(
        "reservas.html",
        mensaje=mensaje,
        reservas=reservas,
        semana=dias_semana,
        fechas_semana=fechas_semana,
        horas=HORAS,
        reservas_dict=reservas_dict,
    )


if __name__ == "__main__":
    app.run(debug=True)
