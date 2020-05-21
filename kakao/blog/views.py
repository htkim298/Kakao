from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })

@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == '테스트':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "테스트 성공입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }],
                "action": {
                    "name": "예제 스킬",
                    "id": "...",
                    "params": {
                      "sys_date": "{\"dateTag\": \"Friday\", \"dateHeadword\": null, \"month\": null, \"year\": null, \"date\": \"2018-11-23\", \"day\": null}",
                      "sys_location": "강남",
                      "sys_number": "{\"amount\": 1, \"unit\": null}"
                    },
                    "detailParams": {
                      "sys_date": {
                        "origin": "금요일",
                        "value": "{\"dateTag\": \"Friday\", \"dateHeadword\": null, \"month\": null, \"year\": null, \"date\": \"2018-11-23\", \"day\": null}",
                        "groupName": ""
                      },
                      "sys_location": {
                        "origin": "강남",
                        "value": "강남",
                        "groupName": ""
                      },
                      "sys_number": {
                        "origin": "1",
                        "value": "{\"amount\": 1, \"unit\": null}",
                        "groupName": ""
                      }
                    }
                  }
            }
        })
