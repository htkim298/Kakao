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

    if return_str == '카카오':
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
                }]
                },
                "context": {
                    "values": [
                      {
                        "name": "abc",
                        "lifeSpan": 10,
                        "params": {
                          "key1": "val1",
                          "key2": "val2"
                        }
                      },
                      {
                        "name": "def",
                        "lifeSpan": 5,
                        "params": {
                          "key3": "1",
                          "key4": "true",
                          "key5": "{\"jsonKey\": \"jsonVal\"}"
                        }
                      },
                      {
                        "name": "ghi",
                        "lifeSpan": 0
                      }
                    ]
                  },
                  "data": {
                    "msg":"HI",
                    "name":"Ryan",
                    "position":"Senior Managing Director"
                  }

        })
