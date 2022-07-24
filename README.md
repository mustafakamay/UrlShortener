# UrlShortener

This is a url shortener api that I made with python. I use Django Rest Framework.
## Build and run
You can run the server with
`
docker-compose up --build -d
`

## Endpoints

### CreateShortUrl
-   method: `POST`
-   path: `createShortUrl/`
-   body: 
    ```js
    {
        ""originUrl": string,
    }
    ```
-   response:
    ```js
    {
    "Origin_Url": string,
    "Short_Url": string,
    }
    ```

### AllUrlList
-   method: `GET`
-   path: `listUrl/`

-   response:
    ```js
    {
        "id": integer,
        "originUrl": string,
        "shortUrl": string,
        "visit": integer
    }
    ```
### RedirectUrl
-   method: `GET`
-   path: `<str:shorturl>`
