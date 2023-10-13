from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/graph/fields')
def fetch_graph_fields():
    nodes_fields = [{"field_name": "id", "type": "string"},
                    {"field_name": "title", "type": "string",
                     },
                    {"field_name": "subTitle", "type": "string"},
                    {"field_name": "mainStat", "type": "string"},
                    {"field_name": "secondaryStat", "type": "number"},
                    {"field_name": "arc__failed",
                     "type": "number", "color": "red", "displayName": "Failed"},
                    {"field_name": "arc__passed",
                     "type": "number", "color": "green", "displayName": "Passed"},
                    {"field_name": "detail__role",
                     "type": "string", "displayName": "Role"}]
    edges_fields = [
        {"field_name": "id", "type": "string"},
        {"field_name": "source", "type": "string"},
        {"field_name": "target", "type": "string"},
        {"field_name": "mainStat", "type": "number"},
    ]
    result = {"nodes_fields": nodes_fields,
              "edges_fields": edges_fields}
    return jsonify(result)


@app.route('/api/graph/data')
def fetch_graph_data():

    nodes = [{"id": "1", "title": "Faiz Mir", "subTitle": "instance:#2", "color":"red"},
             {"id": "2", "title": "Service2", "subTitle": "instance:#2","color":"yellow"},
             {"id": "3", "title": "Service3", "subTitle": "instance:#3"},
             {"id": "4", "title": "Service3", "subTitle": "instance:#1"},
             {"id": "5", "title": "Service4", "subTitle": "instance:#5"}]
    edges = [{"id": "1", "source": "1", "target": "2", "mainStat": 53},
             {"id": "2", "source": "2", "target": "3", "mainStat": 53},
             {"id": "2", "source": "1", "target": "4", "mainStat": 5},
             {"id": "3", "source": "3", "target": "5", "mainStat": 70},
             {"id": "4", "source": "2", "target": "5", "mainStat": 100}]
    result = {"nodes":nodes,"edges":edges}
    return jsonify(result)


@app.route('/api/health')
def check_health():
    return "API is working well!"


app.run(host='0.0.0.0', port=5000)
