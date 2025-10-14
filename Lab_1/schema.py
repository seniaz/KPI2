from dataclasses import dataclass
from typing import Optional
from datetime import date, datetime

@dataclass
class User:
    user_id: str
    username: str
    email: str
    password: str
    nickname: str
    avatar_url: Optional[str] = None

@dataclass
class Publisher:
    publisher_id: str
    name: str
    country: str
    website: Optional[str] = None
    founded_year: Optional[int] = None

    def __post_init__(self):
        if self.founded_year is not None and self.founded_year < 1450:
            raise ValueError(f"Publisher '{self.name}': Founded year must be >= 1450")

@dataclass
class Book:
    book_id: str
    title: str
    isbn: str
    publication_date: date
    description: str
    page_count: int
    language: str = "English"
    cover_url: Optional[str] = None
    publisher_id: Optional[str] = None

    def __post_init__(self):
        if self.page_count <= 0:
            raise ValueError(f"Book '{self.title}': Page count must be greater than 0")

@dataclass
class Author:
    author_id: str
    full_name: str
    country: str
    birth_date: date
    biography: str
    death_date: Optional[date] = None
    photo_url: Optional[str] = None

    def __post_init__(self):
        if self.death_date and self.death_date < self.birth_date:
            raise ValueError(f"Author '{self.full_name}': Death date cannot be earlier than birth date")

@dataclass
class Genre:
    genre_id: str
    name: str
    description: str

@dataclass
class Rating:
    rating_id: str
    user_id: str
    book_id: str
    score: float

    def __post_init__(self):
        if not (1.0 <= self.score <= 5.0):
            raise ValueError(f"Rating score {self.score} must be between 1.0 and 5.0")

class Review:
    def __init__(self, review_id: str, user_id: str, book_id: str, review_text: str):
        self.review_id = review_id
        self.user_id = user_id
        self.book_id = book_id
        self.review_text = review_text
        self.review_date = datetime.now()
        self.last_edit_date: Optional[datetime] = None

        if not (10 <= len(review_text) <= 5000):
            raise ValueError(f"Review text length must be between 10 and 5000 characters")

    def update_review(self, new_text: str):
        if not (10 <= len(new_text) <= 5000):
            raise ValueError(f"Review text length must be between 10 and 5000 characters")
        self.review_text = new_text
        self.last_edit_date = datetime.now()

@dataclass
class BookAuthor:
    book_id: str
    author_id: str
    author_order: int

    def __post_init__(self):
        if self.author_order < 1:
            raise ValueError(f"Author order must be at least 1")

@dataclass
class BookGenre:
    book_id: str
    genre_id: str

if __name__ == "__main__":
    print("--- Initializing Book Rating System (Python) ---\n")

    user1 = User("u001", "jdoe", "john@example.com", "hashed_pass_123", "ReaderJohn")
    
    publisher1 = Publisher("p001", "Penguin Books", "UK", "https://penguin.co.uk", 1935)

    author1 = Author("a001", "George Orwell", "UK", date(1903, 6, 25), "English novelist, essayist, journalist", date(1950, 1, 21))
    author2 = Author("a002", "J.K. Rowling", "UK", date(1965, 7, 31), "British author, best known for Harry Potter")

    genre1 = Genre("g001", "Dystopian", "Society related fiction")
    genre2 = Genre("g002", "Fantasy", "Magic and supernatural elements")

    book1 = Book(
        book_id="b001",
        title="1984",
        isbn="9780451524935",
        publication_date=date(1949, 6, 8),
        description="A dystopian social science fiction novel",
        page_count=328,
        cover_url="https://example.com/1984.jpg",
        publisher_id=publisher1.publisher_id
    )

    book2 = Book(
        book_id="b002",
        title="Harry Potter and the Philosopher's Stone",
        isbn="9780747532743",
        publication_date=date(1997, 6, 26),
        description="First book about young wizard Harry Potter",
        page_count=223,
        publisher_id=publisher1.publisher_id
    )

    book_author1 = BookAuthor(book1.book_id, author1.author_id, 1)
    book_author2 = BookAuthor(book2.book_id, author2.author_id, 1)

    book_genre1 = BookGenre(book1.book_id, genre1.genre_id)
    book_genre2 = BookGenre(book2.book_id, genre2.genre_id)

    rating1 = Rating("r001", user1.user_id, book1.book_id, 4.5)

    review1 = Review(
        review_id="rev001",
        user_id=user1.user_id,
        book_id=book1.book_id,
        review_text="An absolute masterpiece! Orwell's vision is chilling and relevant."
    )

    print(f"User: {user1.username} (Nickname: {user1.nickname})")
    print(f"Book: {book1.title} (Publisher: {publisher1.name})")
    print(f"Author: {author1.full_name} ({author1.country})")
    print(f"Genre: {genre1.name} - {genre1.description}")
    print(f"Rating Score: {rating1.score}")
    print(f"Review Text: {review1.review_text}")
    
    print("\n--- Updating Review ---")
    review1.update_review("An absolute masterpiece! Still relevant today after many years.")
    print(f"Updated Review Text: {review1.review_text}")
    print(f"Last Edit Date: {review1.last_edit_date}")