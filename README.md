
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
| `area` | `int` | **Required**. Livable area |
| `property-type` | `string` | **Required**. "HOUSE" or "APARTMENT |
| `rooms-number` | `int` | **Required**. Number of bedrooms |
| `property-subtype` | `string` | See Immoweb subtypes. All uppercase. |
| `equipped-kitchen` | `bool` | |
| `furnished` | `bool` |  |
| `open-fire` | `bool` |  |
| `terrace` | `bool` | |
| `terrace-area` | `int` |  |
| `garden` | `bool` |  |
| `garden-area` | `int` |  |
| `land-area` | `int` |  |
| `facades-number` | `int` |  |
| `swimming-pool` | `bool` | |
| `building-state` | `string` | `NEW`, `GOOD`, `TO RENOVATE`, `JUST RENOVATED` or `TO REBUILD`  |


  