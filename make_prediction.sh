#!/usr/bin/env bash

PORT=5000
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "EXPERIENCE": 5,
   "TEST": 5,
   "INTERVIEW": 5
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict_api
