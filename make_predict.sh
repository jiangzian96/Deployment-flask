#!/usr/bin/env bash

PORT=80
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "EXPERIENCE":{  
      "0":5
   },
   "TEST":{  
      "0":5
   },
   "INTERVIEW":{  
      "0":5
   }
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict_api
