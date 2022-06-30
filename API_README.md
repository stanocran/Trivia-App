# Trivia API Development and Documentation

## API Reference
1. Error Handling
Errors are returned as JSON objects in the following format:

{
    "success": False, 
    "error": 400,
    "message": "bad request"
}

The API can return up to 5 error types when requests fail:

400: Bad Request
404: Resource Not Found 
422: Not Processable 
500: Internal Server Error 
405: Method Not Allowed

2. Endpoints
`GET /categories`

Fetches a dictionary of all available categories.
Returns an object with a single key, categories, that contains a object of id: category_string key:value pairs.
Sample: curl http://127.0.0.1:5000/categories
{
  "categories: {
    '1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports"
    },
  "success": true
}
` GET '/categories/int:id/questions' `
Gets all questions in a specified category by id using url parameters
Returns a JSON object with paginated questions from a specified category
Sample: curl http://127.0.0.1:5000/categories/3/questions
{
  "current_category": "Geography",
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 3
}

` GET '/questions' `
Returns a list of questions
Includes a list of categories
Paginated in groups of 10
Includes details of question such as category, difficulty, answer and id
Sample: curl http://127.0.0.1:5000/questions
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "6",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": "4",
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "3",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Mona Lisa",
      "category": "2",
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "success": true,
  "total_questions": 17
}

` POST '/questions' `
Creates a new question using JSON request parameters in the database
Sample: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"What was the name of the first man-made satellite launched by the Soviet Union in 1957?", "answer": "Sputnik 1","category" :"4", "difficulty":"2"}'
{
  "created": 29,
  "question_created": "What was the name of the first man-made satellite launched by the Soviet Union in 1957?",
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "6",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": "4",
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "3",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Mona Lisa",
      "category": "2",
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": "2",
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }
  ],
  "success": true,
  "total_questions": 19
}


` POST '/search' `
Searches for questions using a search term,
Returns a JSON object with paginated questions matching the search term
Sample: curl http://127.0.0.1:5000/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":"title"}'
{
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 2
}


` DELETE '/questions/int:id' `
Deletes a question by id using url parameters
Returns id of deleted questions if successful
Sample: curl -X DELETE http://127.0.0.1:5000/questions/2
{
  "success": true,
}

` POST '/quizzes' `
Allows user to play the trivia game
Uses JSON request parameters of a chosen category and previous questions
Returns JSON object with random available questions which are not among previous used questions
Sample: curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category":{"type":"Geography","id":"3"}, "previous_questions":[10]}'
{
  "question": {
    "answer": "Agra",
    "category": "3",
    "difficulty": 2,
    "id": 15,
    "question": "The Taj Mahal is located in which Indian city?"
  },
  "success": true
}
