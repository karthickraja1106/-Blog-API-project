from flask import Flask, jsonify, request
app = Flask(__name__)

posts = [
    {
        "id": 1,
        "title": "My First Blog",
        "content": "This is a test post",
        "author": "Karthickraja"
    },
    {
        "id": 2,
        "title": "My Second Blog",
        "content": "This is a test post",
        "author": "Abinesh"
    }
]

@app.route("/")
def home():
    return "Welcome"
#get
@app.route("/posts", methods=["GET"])
def get_all_post():
    return jsonify(posts), 200

#get by id
@app.route("/post/<int:id>")
def get_post(id):
    for post in posts:
        if post["id"] == id:
            return jsonify(post), 200
    return jsonify({"error": "Post not found"}), 404

#post
@app.route("/post", methods=["POST"])
def create_post():
    if not request.is_json:
        return jsonify({"error": "Invalid content type, expected JSON"}), 400

    data = request.get_json()
    required_fields = ["title", "content", "author"]
    missing_fields = [field for field in required_fields if field not in data or not data[field]]

    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    new_id = posts[-1]["id"] + 1 if posts else 1
    new_post = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"],
        "author": data["author"]
    }
    posts.append(new_post)
    return jsonify(new_post), 201

#Delete
@app.route("/post/<int:id>", methods=["DELETE"])
def delete_post(id):
    post_to_delete = next((post for post in posts if post['id'] == id), None)
    if post_to_delete:
        posts.remove(post_to_delete)
        return jsonify({"message": f"Post with id={id} deleted successfully."}), 200
    else:
        return jsonify({"error": f"Post with id={id} not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)
