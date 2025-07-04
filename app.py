from flask import Flask
from routes.clubs import club_bp
from routes.members import member_bp
from routes.roles import role_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(club_bp, url_prefix='/clubs')
app.register_blueprint(member_bp, url_prefix='/members')
app.register_blueprint(role_bp, url_prefix='/roles')

@app.route('/')
def home():
    return 'CIMP Admin Backend Running!'

if __name__ == '__main__':
    app.run(debug=True)