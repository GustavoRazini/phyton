dicionario_antigo = {
    "id": 341,
    "dateBaseAppointment": "2021-07-06T00:00:00",
    "baseStatus": "Closed",
    "status": "Fechado",
    "createdDate": "2021-07-06T18:24:03.0210116",
    "resolvedIn": "2021-07-06T18:25:46.0076574",
    "closedIn": "2021-07-09T18:53:30.8272894",
    "resolvedInFirstCall": True,
    "slaAgreement": "Contrato Padrão",
    "clients": [
        {
            "id": "777629059",
            "businessName": "WORKDB TECNOLOGIA",
            "email": "suporte@workdb.com.br",
            "personType": 2,
            "profileType": 2
        }
    ],
    "actions": [
        {
            "id": 1,
            "type": 2,
            "origin": 0,
            "description": " \nFoi trocado no arquivo\n/var/www/html/site/resources/views/layouts/site/site-social.blade.php\n \n \n \nMikio Nakamaru \nAnalista de Suporte\n----------------------------------- \n\uD83D\uDCDE (47) 3237-7084 \uD83D\uDCF1 (47) 99946-0041 \n✉ mikio.nakamaru@workdb.com.br\n www.workdb.com.br\n",
            "status": "Resolvido",
            "createdDate": "2021-07-06T18:25:46.0366590",
            "createdBy": {
                "id": "e9e7ddae-8aa4-483e-",
                "businessName": "Mikio Nakamaru",
                "email": "mikio.nakamaru@workdb.com.br",
                "personType": 1,
                "profileType": 2
            },
            "isDeleted": False,
            "timeAppointments": [
                {
                    "id": 34820332,
                    "activity": "Manutenção",
                    "date": "2021-07-06T00:00:00",
                    "workTime": "00:30:00",
                    "accountedTime": 0.5,
                    "workTypeName": "Normal"
                }
            ],
            "tags": []
        }
    ],
    "owner": {
        "id": "e9e7ddae-8aa4-483e-",
        "businessName": "Mikio Nakamaru",
        "email": "mikio.nakamaru@workdb.com.br",
        "personType": 1,
        "profileType": 2
    },
    "satisfactionSurveyResponses": [],
    "subject": "Trocar o link do instagram no site da WorkDB",
    "createdBy": {
        "id": "e9e7ddae-8aa4-483e-",
        "businessName": "Mikio Nakamaru",
        "email": "mikio.nakamaru@workdb.com.br",
        "personType": 1,
        "profileType": 2
    }
}

dict_novo = {"id": dicionario_antigo["id"],
             "requester": dicionario_antigo["clients"][0]["businessName"],
             "topic": dicionario_antigo["subject"],
             "actioon": dicionario_antigo["actions"][0]["description"],
             "agent": dicionario_antigo["createdBy"]["businessName"],
             "date": dicionario_antigo["actions"][0]["timeAppointments"][0]["date"],
            "time_accounted": dicionario_antigo["actions"][0]["timeAppointments"][0]["accountedTime"],
             "worlTime": dicionario_antigo["actions"][0]["timeAppointments"][0]["workTime"],
             "hour_type": dicionario_antigo["actions"][0]["timeAppointments"][0]["workTypeName"],
             "status": dicionario_antigo["actions"][0]["timeAppointments"][0]["activity"],
             "email": dicionario_antigo["owner"]["email"],
             "client": dicionario_antigo["owner"]["businessName"]}
print(dict_novo)
