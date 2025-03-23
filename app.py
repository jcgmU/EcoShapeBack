from flask import Flask, request, jsonify
from flask_cors import CORS
import math
from sympy import symbols, pi, Integer  # Importación explícita

app = Flask(__name__)

CORS(
    app,
    resources={
        r"/api/*": {
            "origins": ["http://localhost:3000"],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type"],
            "expose_headers": ["Content-Type"],
            "supports_credentials": True,
        }
    },
)


@app.route("/api/volumen-maceta", methods=["POST"])
def volumen_maceta():
    data = request.get_json()
    try:
        R = float(data["R"])
        H = float(data["H"])
        t = float(data["t"])
        if R <= 0 or H <= 0 or t <= 0 or t >= R:
            return (
                jsonify(
                    {"error": "Valores inválidos. Asegúrese que R>0, H>0, t>0 y t<R."}
                ),
                400,
            )
        # Cálculo del volumen (script herramienta1_calcular_volumen)
        V_externo = math.pi * (R**2) * H
        V_interno = math.pi * ((R - t) ** 2) * H
        V_material = V_externo - V_interno
        return jsonify(
            {
                "volumen_externo": round(V_externo, 2),
                "volumen_interno": round(V_interno, 2),
                "volumen_material": round(V_material, 2),
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/resistencia-maceta", methods=["POST"])
def resistencia_maceta():
    data = request.get_json()
    try:
        C = float(data["C"])
        H_mm = float(data["H_mm"])
        t_mm = float(data["t_mm"])
        sigma_adm = float(data["sigma_adm"])
        if C <= 0 or H_mm <= 0 or t_mm <= 0 or sigma_adm <= 0:
            return jsonify({"error": "Todos los valores deben ser positivos."}), 400
        # Cálculo del sigma_max (script herramienta2_verificar_resistencia)
        sigma_max = (C * H_mm) / t_mm
        cumple = sigma_max <= sigma_adm
        return jsonify(
            {"sigma_max": round(sigma_max, 2), "sigma_adm": sigma_adm, "cumple": cumple}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/volumen-cono", methods=["POST"])
def volumen_cono():
    data = request.get_json()
    try:
        R = float(data["R"])
        e = float(data["e"])
        H = float(data["H"])
        if R <= 0 or e <= 0 or H <= 0 or e >= R:
            return (
                jsonify(
                    {"error": "Valores inválidos. Asegúrese que R>0, H>0, e>0 y e<R."}
                ),
                400,
            )

        # Cálculo del volumen usando sympy
        R_sym, e_sym, H_sym = symbols("R e H", positive=True)
        V_ext = (Integer(1) / 3) * pi * (R_sym**2) * H_sym
        V_int = (Integer(1) / 3) * pi * ((R_sym - e_sym) ** 2) * H_sym
        V_mat = V_ext - V_int
        V_resultado = V_mat.subs({R_sym: R, e_sym: e, H_sym: H}).evalf()

        return jsonify({"volumen": round(float(V_resultado), 3)})
    except Exception as e:
        print(f"Error: {str(e)}")  # Log para debugging
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
