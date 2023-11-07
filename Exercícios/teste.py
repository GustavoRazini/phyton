dicionario_antigo = {
    "id": 6309,
    "dateBaseAppointment": "2023-06-30T00:00:00",
    "baseStatus": "Closed",
    "status": "Fechado",
    "createdDate": "2023-06-30T14:22:39.9442868",
    "resolvedIn": "2023-07-03T14:04:29.2896170",
    "closedIn": "2023-07-06T14:04:47.8915006",
    "resolvedInFirstCall": False,
    "slaAgreement": "Contrato Padrão",
    "clients": [
        {
            "id": "1866391327",
            "businessName": "FVO - ALIMENTOS",
            "personType": 2,
            "profileType": 2
        }
    ],
    "actions": [
        {
            "id": 1,
            "type": 2,
            "origin": 0,
            "description": "Nota fiscal 8245 e 8250 filial 20\n \n\n \n\n",
            "status": "Novo",
            "createdDate": "2023-06-30T14:25:21.2628549",
            "createdBy": {
                "id": "53fbe820-656b-42a7-",
                "businessName": "Luiz Lopes",
                "email": "luiz.lopes@workdb.com.br",
                "personType": 1,
                "profileType": 3
            },
            "isDeleted": False,
            "timeAppointments": [
                {
                    "id": 77643044,
                    "activity": "Outros",
                    "date": "2023-06-30T00:00:00",
                    "workTime": "01:00:00",
                    "accountedTime": 1.0,
                    "workTypeName": "Normal"
                }
            ],
            "tags": []
        },
        {
            "id": 2,
            "type": 2,
            "origin": 2,
            "description": "Realizado o cancelamento das notas e aguardando validação da solciitante.\n \n\n",
            "status": "Novo",
            "createdDate": "2023-06-30T20:45:14.2219690",
            "createdBy": {
                "id": "53fbe820-656b-42a7-",
                "businessName": "Luiz Lopes",
                "email": "luiz.lopes@workdb.com.br",
                "personType": 1,
                "profileType": 3
            },
            "isDeleted": False,
            "timeAppointments": [
                {
                    "id": 77643091,
                    "activity": "Outros",
                    "date": "2023-06-30T00:00:00",
                    "workTime": "02:30:00",
                    "accountedTime": 2.5,
                    "workTypeName": "Normal"
                }
            ],
            "tags": []
        }
    ],
    "owner": {
        "id": "53fbe820-656b-42a7-",
        "businessName": "Luiz Lopes",
        "email": "luiz.lopes@workdb.com.br",
        "personType": 1,
        "profileType": 3
    },
    "satisfactionSurveyResponses": [],
    "subject": "Problemas de Cancelamento de Nota Fiscal 8245 e 8250",
    "createdBy": {
        "id": "53fbe820-656b-42a7-",
        "businessName": "Luiz Lopes",
        "email": "luiz.lopes@workdb.com.br",
        "personType": 1,
        "profileType": 3
    }
}

lista_de_apontamentos = []
dict_valores_padrao = {"id": dicionario_antigo["id"],
                       "requester": dicionario_antigo["clients"][0]["businessName"],
                       "topic": dicionario_antigo["subject"],
                       "agent": dicionario_antigo["createdBy"]["businessName"],
                       "email": dicionario_antigo["owner"]["email"],
                       "client": dicionario_antigo["owner"]["businessName"]}
for value in dicionario_antigo["actions"]:
    dict_value = {"actioon": dicionario_antigo["actions"][0]["description"],
             "date": dicionario_antigo["actions"][0]["timeAppointments"][0]["date"],
            "time_accounted": dicionario_antigo["actions"][0]["timeAppointments"][0]["accountedTime"],
             "worlTime": dicionario_antigo["actions"][0]["timeAppointments"][0]["workTime"],
             "hour_type": dicionario_antigo["actions"][0]["timeAppointments"][0]["workTypeName"],
             "status": dicionario_antigo["actions"][0]["timeAppointments"][0]["activity"]}
    dict_value.update(dict_valores_padrao)
    lista_de_apontamentos.append(dict_value)
print(lista_de_apontamentos)
