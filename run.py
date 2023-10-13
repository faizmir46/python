from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/graph/fields')
def fetch_graph_fields():
    nodes_fields = [{"field_name": "id", "type": "string"},
                    {"field_name": "title", "type": "string"}]

                    #    nodes_fields = [{"field_name": "id", "type": "string"},
                    # {"field_name": "title", "type": "string",
                    #  },
                    # {"field_name": "subTitle", "type": "string"},
                    # {"field_name": "mainStat", "type": "string"},
                    # {"field_name": "secondaryStat", "type": "number"},
                    # {"field_name": "arc__failed",
                    #  "type": "number", "color": "red", "displayName": "Failed"},
                    # {"field_name": "arc__passed",
                    #  "type": "number", "color": "green", "displayName": "Passed"},
                    # {"field_name": "detail__role",
                    #  "type": "string", "displayName": "Role"}]
    edges_fields = [
        {"field_name": "id", "type": "string"},
        {"field_name": "source", "type": "string"},
        {"field_name": "target", "type": "string"}
    ]

    #   edges_fields = [
    #     {"field_name": "id", "type": "string"},
    #     {"field_name": "source", "type": "string"},
    #     {"field_name": "target", "type": "string"},
    #     {"field_name": "mainStat", "type": "number"},
    # ]
    result = {"nodes_fields": nodes_fields,
              "edges_fields": edges_fields}
    return jsonify(result)


@app.route('/api/graph/data')
def fetch_graph_data():

    nodes = [{"id": "1", "title": "Service1"},
             {"id": "2", "title": "Service2"},
             {"id": "3", "title": "Service3"},
             {"id": "4", "title": "Service3"},
             {"id": "5", "title": "Service4"}]

            #    nodes = [{"id": "1", "title": "Service1", "subTitle": "instance:#2", "detail__role": "load",
            #   "arc__failed": 0.7, "arc__passed": 0.3, "mainStat": "qaz"},
            #  {"id": "2", "title": "Service2", "subTitle": "instance:#2", "detail__role": "transform",
            #   "arc__failed": 0.5, "arc__passed": 0.5, "mainStat": "qaz"},
            #  {"id": "3", "title": "Service3", "subTitle": "instance:#3", "detail__role": "extract",
            #   "arc__failed": 0.3, "arc__passed": 0.7, "mainStat": "qaz"},
            #  {"id": "4", "title": "Service3", "subTitle": "instance:#1", "detail__role": "transform",
            #   "arc__failed": 0.5, "arc__passed": 0.5, "mainStat": "qaz"},
            #  {"id": "5", "title": "Service4", "subTitle": "instance:#5", "detail__role": "transform",
            #   "arc__failed": 0.5, "arc__passed": 0.5, "mainStat": "qaz"}]
    edges = [{"id": "1", "source": "1", "target": "2"},
             {"id": "2", "source": "2", "target": "3"},
             {"id": "2", "source": "1", "target": "4"},
             {"id": "3", "source": "3", "target": "5"},
             {"id": "4", "source": "2", "target": "5"}]

            #  edges = [{"id": "1", "source": "1", "target": "2", "mainStat": 53},
            #  {"id": "2", "source": "2", "target": "3", "mainStat": 53},
            #  {"id": "2", "source": "1", "target": "4", "mainStat": 5},
            #  {"id": "3", "source": "3", "target": "5", "mainStat": 70},
            #  {"id": "4", "source": "2", "target": "5", "mainStat": 100}]
    result = {
    "edges": [
        {
            "id": "bb8c552d-d3fc-4497-8d18-ddc8ab20dd68",
            "source": "2f907104-5cc6-4803-8113-762d29aa1c75",
            "target": "070754cb-841d-4e47-a856-3444f0dbedd5"
        },
        {
            "id": "e57213dd-3875-461a-a6b8-8777fb2cb7cf",
            "source": "070754cb-841d-4e47-a856-3444f0dbedd5",
            "target": "7dd05c68-2330-4660-8a52-322565d84779"
        },
        {
            "id": "4d3782c4-3a49-45ef-a181-7d3fac1c7547",
            "source": "7dd05c68-2330-4660-8a52-322565d84779",
            "target": "158bf2ae-8c77-4c6f-889a-6eb8f626ad97"
        },
        {
            "id": "e4c35e88-92e1-4c63-aea7-d317dff2188c",
            "source": "158bf2ae-8c77-4c6f-889a-6eb8f626ad97",
            "target": "f638d992-d914-488c-a19d-7046c8ac98f7"
        },
        {
            "id": "266e59ce-98c8-4d4c-85c1-f5d14a38c54d",
            "source": "f638d992-d914-488c-a19d-7046c8ac98f7",
            "target": "d9238f3b-e4d6-45aa-908c-78057439ad2a"
        },
        {
            "id": "3a0d68da-d1b4-40c4-9f48-8bfc78c10337",
            "source": "d9238f3b-e4d6-45aa-908c-78057439ad2a",
            "target": "355e6584-7479-4569-800a-a9b2ff5d9cc8"
        },
        {
            "id": "ac409352-daab-4853-8dcb-5b1fa947b7cc",
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
