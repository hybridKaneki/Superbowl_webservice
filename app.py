#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)

superbowl = [
    {
        'year': 2000,
        'Winner':{'team': u'Packers','touchdowns':5,'pass-yards': 267, 'run-yards': 97,'Team Players':{'Qb':'Arron Rodgers','Wr':'Devante Adams','De':'Clay Mathews'}},
        'Looser': u'Steelers',
        'Stadium': u'AT&T Stadium'
    },
    {
        'year': 2001,
        'Winner':{'team': u'Patriots','touchdowns':6,'pass-yards': 345, 'run-yards': 125,'Team Players':{'Qb':'Tom Brady','Wr':'Julian Edelman','De':'Hightower'}},
        'Looser': u'Eagles',
        'Stadium': u'Soldier Field Stadium'
    },
    {
        'year': 2002,
        'Winner':{'team': u'Saints','touchdowns':3,'pass-yards': 167, 'run-yards': 77,'Team Players':{'Qb':'Drew Breese','Wr':'Michael Thomas','De':'Jerry Rice'}},
        'Looser': u'Lions',
        'Stadium': u'ArrowHead Stadium'
    },
    {
        'year': 2003,
        'Winner':{'team': u'Cardinals','touchdowns':3,'pass-yards': 145, 'run-yards': 65,'Team Players':{'Qb':'Allen Jerry','Wr':'Beckam Jr','De':'Laurence Hardy'}},
        'Looser': u'Dolphins',
        'Stadium': u'Levis Stadium'
    },
    {
        'year': 2004,
        'Winner':{'team': u'Ravens','touchdowns':4,'pass-yards': 198, 'run-yards': 103,'Team Players':{'Qb':'Alex Smith','Wr':'Robert Brown','De':'Josh Gordan'}},
        'Looser': u'Bengals',
        'Stadium': u'Hard Rock Stadium'
    },
    {
        'year': 2005,
        'Winner':{'team': u'Dolphins','touchdowns':5,'pass-yards': 285, 'run-yards': 75,'Team Players':{'Qb':'Nick Foles','Wr':'Alvin Kamara','De':'Mason Rudolph'}},
        'Looser': u'Raiders',
        'Stadium': u'Met Life Stadium'
    },
    {
        'year': 2006,
        'Winner':{'team': u'Browns','touchdowns':7,'pass-yards': 357, 'run-yards': 67,'Team Players':{'Qb':'Dak Prescot','Wr':'Leson Mckoy','De':'Jacob Brisket'}},
        'Looser': u'Jaguars',
        'Stadium': u'Ford Field Stadium'
    },
    {
        'year': 2007,
        'Winner':{'team': u'Texans','touchdowns':6,'pass-yards': 345, 'run-yards': 125,'Team Players':{'Qb':'Jimmy Garry','Wr':'Thomas Kittle','De':'J.J. Watt'}},
        'Looser': u'Cowboys',
        'Stadium': u'Gillete Stadium'
    }
]

@app.route('/')
def index():
    return "NFL SUPERBOWL\n"

@app.route('/superbowl', methods=['GET'])
def get_superbowl():
    return jsonify({'superbowl': superbowl})

@app.route('/superbowl/<int:nfl_id>', methods=['GET'])
def get_year(nfl_id):
    nfl = [nfl for nfl in superbowl if nfl['year'] == nfl_id]
    if len(nfl) == 0:
        abort(404)
    return jsonify({'SuperBowl Year': nfl[0]})

@app.route('/superbowl/<int:nfl_id>/Winner', methods=['GET'])
def get_winner(nfl_id):
    nfl = [nfl for nfl in superbowl if nfl['year'] == nfl_id]
    if len(nfl) == 0:
        abort(404)
    return jsonify({'Winner ScoreCard': nfl[0]['Winner']})


@app.route('/superbowl/<int:nfl_id>/Winner/Team Players', methods=['GET'])
def get_team(nfl_id):
    nfl = [nfl for nfl in superbowl if nfl['year'] == nfl_id]
    if len(nfl) == 0:
        abort(404)
    return jsonify({'Team Players': nfl[0]['Winner']['Team Players']})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Data Not Found'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

