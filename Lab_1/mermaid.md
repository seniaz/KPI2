```
erDiagram

    USERS {
        serial UserID PK
        varchar Username
        varchar Email
        varchar Password
        varchar Nickname
        text AvatarURL
    }

    PUBLISHER {
        serial PublisherID PK
        varchar Name
        varchar Country
        text Website
        int FoundedYear
    }

    AUTHOR {
        serial AuthorID PK
        varchar FullName
        varchar Country
        date BirthDate
        date DeathDate
        text PhotoURL
        text Biography
    }

    GENRE {
        serial GenreID PK
        varchar Name
        text Description
    }

    BOOK {
        serial BookID PK
        varchar Title
        varchar ISBN
        date PublicationDate
        text Description
        int PageCount
        varchar Language
        text CoverURL
        int PublisherID FK
    }

    RATING {
        serial RatingID PK
        int UserID FK
        int BookID FK
        decimal Score
    }

    REVIEW {
        serial ReviewID PK
        int UserID FK
        int BookID FK
        text ReviewText
        timestamp ReviewDate
        timestamp LastEditDate
    }

    BOOK_AUTHOR {
        int BookID PK,FK
        int AuthorID PK,FK
        int AuthorOrder
    }

    BOOK_GENRE {
        int BookID PK,FK
        int GenreID PK,FK
    }

    USERS ||--o{ RATING : places
    USERS ||--o{ REVIEW : writes
    BOOK ||--o{ RATING : receives
    BOOK ||--o{ REVIEW : has
    BOOK }o--o| PUBLISHER : "published by"
    BOOK ||--|{ BOOK_AUTHOR : "written by"
    BOOK ||--|{ BOOK_GENRE : "categorized as"
    AUTHOR ||--o{ BOOK_AUTHOR : writes
    GENRE ||--o{ BOOK_GENRE : describes
```

![ER Diagram](./Lab_1/mermaid_chart.png)
