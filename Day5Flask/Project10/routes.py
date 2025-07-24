

from flask import request, jsonify
from models import db, Candidate, Vote

def register_routes(app):
    @app.route('/candidates', methods=['POST'])
    def add_candidate():
        data = request.get_json()
        candidate = Candidate(name=data['name'], party=data['party'])
        db.session.add(candidate)
        db.session.commit()
        return jsonify({'message': 'Candidate added successfully'}), 201

    @app.route('/vote', methods=['POST'])
    def cast_vote():
        data = request.get_json()
        voter_name = data['voter_name']
        candidate_id = data['candidate_id']

        existing_vote = Vote.query.filter_by(voter_name=voter_name).first()
        if existing_vote:
            return jsonify({'error': 'Duplicate vote detected!'}), 400

        candidate = Candidate.query.get(candidate_id)
        if not candidate:
            return jsonify({'error': 'Candidate not found'}), 404

        vote = Vote(voter_name=voter_name, candidate_id=candidate_id)
        db.session.add(vote)
        db.session.commit()
        return jsonify({'message': 'Vote cast successfully'}), 201

    @app.route('/results', methods=['GET'])
    def get_results():
        candidates = Candidate.query.all()
        results = []
        for candidate in candidates:
            count = Vote.query.filter_by(candidate_id=candidate.id).count()
            results.append({
                'candidate': candidate.name,
                'party': candidate.party,
                'votes': count
            })
        return jsonify(results)
