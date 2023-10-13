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
    nodes = [{"id": "1", "title": "Faiz Mir", "subTitle": "instance:#2", "color":"red","detail__role": "load",
              "arc__failed": 0.7, "arc__passed": 0.3, "mainStat": "qaz"},
             {"id": "2", "title": "Service2", "subTitle": "instance:#2","color":"yellow", "detail__role": "transform",
              "arc__failed": 0.5, "arc__passed": 0.5, "mainStat": "qaz"},
             {"id": "3", "title": "Service3", "subTitle": "instance:#3", "detail__role": "extract",
              "arc__failed": 0.3, "arc__passed": 0.7, "mainStat": "qaz"},
             {"id": "4", "title": "Service3", "subTitle": "instance:#1", "detail__role": "transform",
              "arc__failed": 0.5, "arc__passed": 0.5, "mainStat": "qaz"},
             {"id": "5", "title": "Service4", "subTitle": "instance:#5", "detail__role": "transform",
              "arc__failed": 0.5, "arc__passed": 0.5, "mainStat": "qaz"}]
    edges = [{"id": "1", "source": "1", "target": "2", "mainStat": 53},
             {"id": "2", "source": "2", "target": "3", "mainStat": 53},
             {"id": "2", "source": "1", "target": "4", "mainStat": 5},
             {"id": "3", "source": "3", "target": "5", "mainStat": 70},
             {"id": "4", "source": "2", "target": "5", "mainStat": 100}]
    result = {
    "edges": [
        {
            "id": "21282b59-cec2-4b84-9fc5-46f8e00ec73c",
            "source": "2f907104-5cc6-4803-8113-762d29aa1c75",
            "target": "070754cb-841d-4e47-a856-3444f0dbedd5"
        },
        {
            "id": "5b0fd034-7564-4a54-be32-384ae0ea0868",
            "source": "070754cb-841d-4e47-a856-3444f0dbedd5",
            "target": "7dd05c68-2330-4660-8a52-322565d84779"
        },
        {
            "id": "68493e8e-6ea3-4da0-96f1-a1892274a095",
            "source": "7dd05c68-2330-4660-8a52-322565d84779",
            "target": "7dd05c68-2330-4660-8a52-322565d81234"
        },
        {
            "id": "e3d4e6a0-3fce-4fd2-ac6f-e29f794a7d50",
            "source": "7dd05c68-2330-4660-8a52-322565d81234",
            "target": "158bf2ae-8c77-4c6f-889a-6eb8f626ad97"
        },
        {
            "id": "9ddbeabd-6ecc-4c14-819d-3612eaadc7cc",
            "source": "158bf2ae-8c77-4c6f-889a-6eb8f626ad97",
            "target": "f638d992-d914-488c-a19d-7046c8ac98f7"
        },
        {
            "id": "56efe65c-65f2-4d0f-8e91-6e3df6e6d100",
            "source": "f638d992-d914-488c-a19d-7046c8ac98f7",
            "target": "d9238f3b-e4d6-45aa-908c-78057439ad2a"
        },
        {
            "id": "35eaf802-8554-474b-aadb-1a60d3c25d71",
            "source": "d9238f3b-e4d6-45aa-908c-78057439ad2a",
            "target": "355e6584-7479-4569-800a-a9b2ff5d9cc8"
        },
        {
            "id": "e0f398b2-8dce-4cee-ace9-d046f539b0e5",
            "source": "d9238f3b-e4d6-45aa-908c-78057439ad2a",
            "target": "82e3f538-8d4f-4161-82a7-923aeeeaaeba"
        }
    ],
    "nodes": [
        {
            "id": "2f907104-5cc6-4803-8113-762d29aa1c75",
            "title": "WEBHOOK_TRIGGER_REGISTRY"
        },
        {
            "id": "070754cb-841d-4e47-a856-3444f0dbedd5",
            "title": "SESSION_START_REGISTRY"
        },
        {
            "id": "7dd05c68-2330-4660-8a52-322565d84779",
            "title": "FORM_REGISTRY"
        },
        {
            "id": "f638d992-d914-488c-a19d-7046c8ac98f7",
            "title": "SESSION_END_REGISTRY"
        },
        {
            "id": "158bf2ae-8c77-4c6f-889a-6eb8f626ad97",
            "title": "PAN_VERIFICATION_REGISTRY"
        },
        {
            "id": "d9238f3b-e4d6-45aa-908c-78057439ad2a",
            "title": "IF_REGISTRY"
        },
        {
            "id": "355e6584-7479-4569-800a-a9b2ff5d9cc8",
            "title": "WHATSAPP_MESSAGE_REGISTRY"
        },
        {
            "id": "82e3f538-8d4f-4161-82a7-923aeeeaaeba",
            "title": "WHATSAPP_MESSAGE_REGISTRY"
        }
    ]
}
    return jsonify(result)


@app.route('/api/health')
def check_health():
    return "API is working well!"


app.run(host='0.0.0.0', port=5000)
