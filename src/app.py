from flask import Flask,jsonify,request


app = Flask(__name__)
posts=[
      {
       "id" : 1,  
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
#home
@app.route("/")
def home():
      return "welcome"

#Get
@app.route("/posts",methods=["GET"])
def get_all_post():
       return jsonify(posts),200

#Get by id
@app.route("/post/<int:id>")
def get_post(id):
       for post in posts:
             if post["id"] == id:
                  return jsonify(post), 200  
       return jsonify({"error": "Post not found"}), 404

#post
@app.route("/post",methods=["POST"])
def create_post():
    req_id=request.get_json()
    #this code for generate new unique id
    if "id" not in posts:
          if posts:
                #get the last id from the list and increment by 1
                new_id=posts[-1]["id"]+1
          else:
                new_id=1  
    new_post = {
        "id": len(posts) + 1,
        "title": req_id['title'],
        "content": req_id.get('content', ""),
        "author": req_id.get('author', "")
    }
    posts.append(new_post)
    return jsonify(new_post), 201

#Delete
@app.route("/post/<int:id>",methods=["DELETE"])
def delete_post(id):
      post_to_delete=next((post for post in posts if post['id']==id),None)
      if post_to_delete:
            posts.remove(post_to_delete)
            return jsonify({"message":f"post with id={id} deleted succesfully."}),200
      else:
            return({"error":f"post with id={id} not found in this list."}),404
      
      
             
if __name__ == "__main__":
    app.run(debug=True)