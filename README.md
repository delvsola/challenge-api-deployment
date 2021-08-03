
# challenge-api-deployment

A Becode project consisting of deploying a Flask API in a Docker container on Heroku.




## API Reference

The API currently only contain a single route. You can access the API [here](https://salty-mesa-39646.herokuapp.com/)

#### Predict the price of a house

```http
  POST /predict
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `zip-code` | `int` | **Required**. Belgian Zip code |
| `area` | `int` | **Required**. Livable area in m² |
| `property-type` | `string` | **Required**. "HOUSE" or "APARTMENT |
| `rooms-number` | `int` | **Required**. Number of bedrooms |
| `property-subtype` | `string` | See Immoweb subtypes. All uppercase. |
| `equipped-kitchen` | `bool` | Has an equipped kitchen.|
| `furnished` | `bool` | Includes furniture. |
| `open-fire` | `bool` |  Includes a fireplace.|
| `terrace` | `bool` | Includes Terrace.|
| `terrace-area` | `int` | Terrace area in m².|
| `garden` | `bool` |  Includes garden.|
| `garden-area` | `int` |  Garden area in m²|
| `land-area` | `int` |  Plot area in m²|
| `facades-number` | `int` |  Number of house facades.|
| `swimming-pool` | `bool` | Has a Swimming Pool.|
| `building-state` | `string` | `NEW`, `GOOD`, `TO RENOVATE`, `JUST RENOVATED` or `TO REBUILD`  |


  