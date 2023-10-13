from flask import Flask, jsonify,request

app = Flask(__name__)


@app.route('/api/graph/fields')
def fetch_graph_fields():
    nodes_fields = [{"field_name": "id", "type": "string"},
                    {"field_name": "title", "type": "string"}
                    # {"field_name": "subTitle", "type": "string"},
                    # {"field_name": "mainStat", "type": "string"},
                    # {"field_name": "secondaryStat", "type": "number"},
                    # {"field_name": "arc__failed",
                    #  "type": "number", "color": "red", "displayName": "Failed"},
                    # {"field_name": "arc__passed",
                    #  "type": "number", "color": "green", "displayName": "Passed"},
                    # {"field_name": "detail__role",
                    #  "type": "string", "displayName": "Role"}
                     ]
    edges_fields = [
        {"field_name": "id", "type": "string"},
        {"field_name": "source", "type": "string"},
        {"field_name": "target", "type": "string"}
        # {"field_name": "mainStat", "type": "number"},
    ]
    result = {"nodes_fields": nodes_fields,
              "edges_fields": edges_fields}
    return jsonify(result)


@app.route('/api/graph/data')
def fetch_graph_data():
    param1 = request.args.get('processId')
    param2 = request.args.get('instanceId')
    print(param1)
    print(param2)
    nodes = [{"id": "1", "title": "Faiz Mir"},
             {"id": "2", "title": "Service2"},
             {"id": "3", "title": "Service3"},
             {"id": "4", "title": "Service3"},
             {"id": "5", "title": "Service4"}]
    edges = [{"id": "1", "source": "1", "target": "2"},
             {"id": "2", "source": "2", "target": "3"},
             {"id": "2", "source": "1", "target": "4"},
             {"id": "3", "source": "3", "target": "5"},
             {"id": "4", "source": "2", "target": "5"}]
    result = {"nodes":nodes,"edges":edges}
    return jsonify(result)


@app.route('/api/health')
def check_health():
    return "API is working well!"


app.run(host='0.0.0.0', port=5000)
