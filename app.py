
from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
next_id = 1

@app.route("/api/users", methods=["POST"])
def create_user():
    global next_id
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Invalid name"}), 400

    user = {"id": next_id, "name": name.strip()}
    users.append(user)
    next_id += 1

    return jsonify(user), 201

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"})

    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
