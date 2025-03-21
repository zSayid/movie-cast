from flask import Flask, request, jsonify
from flask_cors import CORS 
from imdb import IMDb 

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/cast', methods=['GET'])
def get_movie_cast():
    movie_name = request.args.get('movie_name')
    ia = IMDb()
    movies = ia.search_movie(movie_name)

   
    
    if movies:
        movie_id = movies[0]
        ia.update(movie_id)
        cast = movie_id.get('cast', [])
        cast_list = []
        for actor in cast[:10]:
            cast_list.append({
                'name': actor['name'],
                'image': actor.get_fullsizeURL() if actor.has_key('fullsizeURL') else None
            })
        return jsonify({'cast': cast_list})
    else:
        return jsonify({'error': 'No movie found with the name {}'.format(movie_name)}), 404

if __name__ == '__main__':
    app.run(debug=True)