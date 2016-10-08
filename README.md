# Basic Geocoder

sample input from a .csv file:

Minneapolis,Minnesota,United States
Cupertino,California,United States
New Orleans,Louisiana,United States
Sao Paolo,,Brazil
Berrien Springs,Michigan,United States
Suwon,,South Korea
New York,New York,United States
Turku,,Finland
Beijing,,China
Oakland,California,United States
San Francisco,California,United States
New Delhi,,India
Jodhpur,,India
Udaipur,,India
Jaipur,,India
Mumbai,,India

sample output as .geojson file:

{"type": "FeatureCollection", "features": [{"geometry": {"type": "Point", "coordinates": [-93.30975269999999, 44.961502]}, "type": "Feature", "properties": {"name": "ChIJMdidFi4zs1IRWSkfPy0KwnY"}}, {"geometry": {"type": "Point", "coordinates": [-121.9552356, 37.35410789999999]}, "type": "Feature", "properties": {"name": "ChIJk8EIXIG3j4ARwL_Ao3ykdeQ"}}, {"geometry": {"type": "Point", "coordinates": [-90.0539603, 29.9146493]}, "type": "Feature", "properties": {"name": "ChIJ8eVlUJOmIIYRp9D28B-LDsA"}}, {"geometry": {"type": "Point", "coordinates": [-46.6139117, -23.538047]}, "type": "Feature", "properties": {"name": "ChIJYxPuU-BYzpQRsZ1qtx7nzEA"}}, {"geometry": {"type": "Point", "coordinates": [-86.378151, 42.0360725]}, "type": "Feature", "properties": {"name": "ChIJH5styNfPEIgRDGI_F9_N5mI"}}, {"geometry": {"type": "Point", "coordinates": [126.8311887, 37.1994932]}, "type": "Feature", "properties": {"name": "ChIJIfZd0f8SezURp-W-4kU9FD0"}}, {"geometry": {"type": "Point", "coordinates": [-74.0776417, 40.72815749999999]}, "type": "Feature", "properties": {"name": "ChIJ3a-_JdJQwokR2SXNohPwSQI"}}, {"geometry": {"type": "Point", "coordinates": [22.2920919, 60.4494196]}, "type": "Feature", "properties": {"name": "ChIJW9K6N-Z2jEYRUckYPFK1ACY"}}, {"geometry": {"type": "Point", "coordinates": [116.443108, 39.92147000000001]}, "type": "Feature", "properties": {"name": "ChIJR2lzI-6r8TUROoHQJjCLu9c"}}, {"geometry": {"type": "Point", "coordinates": [-122.2416355, 37.7652065]}, "type": "Feature", "properties": {"name": "ChIJlRXP8tiAj4ARFG8BYM-Z_2Y"}}, {"geometry": {"type": "Point", "coordinates": [-122.4056395, 37.7785189]}, "type": "Feature", "properties": {"name": "ChIJezBipoOAhYARUPnBLQwBmf0"}}, {"geometry": {"type": "Point", "coordinates": [77.2273958, 28.6618976]}, "type": "Feature", "properties": {"name": "ChIJL_P_CXMEDTkRw0ZdG-0GVvw"}}, {"geometry": {"type": "Point", "coordinates": [73.0346244, 26.2486661]}, "type": "Feature", "properties": {"name": "ChIJvQfyw2KMQTkR1kSm41Ju-Kg"}}, {"geometry": {"type": "Point", "coordinates": [73.698774, 24.6089414]}, "type": "Feature", "properties": {"name": "ChIJbfknuwflZzkRcoKcu23mPR0"}}, {"geometry": {"type": "Point", "coordinates": [75.7923778, 26.8809896]}, "type": "Feature", "properties": {"name": "ChIJ4WsnTDC0bTkRzHnHHnw5w1U"}}, {"geometry": {"type": "Point", "coordinates": [72.8726952, 19.1154908]}, "type": "Feature", "properties": {"name": "ChIJMbHfQRu25zsRMazdY3UpaKY"}}]}


![Background](img/geocoder.png)