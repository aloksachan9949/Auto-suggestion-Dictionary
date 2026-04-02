# Auto-suggestion-Dictionary
This project is a backend-powered auto suggestion dictionary system with a simple UI that supports


Overview

This project is a backend-powered dictionary system with a simple UI that supports:

Fast prefix-based search
Autosuggestions like search engines
Sorting by:
Higher frequency first
Lexicographical order (if frequency is same)
Add new words dynamically

The system is optimized for efficient lookup in large datasets using a Trie (Prefix Tree).

Data struture Used:
Trie (Prefix Tree)
A Trie is used to store and search words efficiently.
Structure:
Each node contains:
children → dictionary of characters
is_end → marks end of a word
frequency → how often the word appears



Logic & Approach:
step 1 :
Searching (Prefix-Based)
Traverse Trie using prefix
If prefix not found → return empty
Perform DFS (Depth First Search) to get all words
Sort results:
Frequency (descending)
Lexicographically (ascending)

Step 2:
2. Adding Words
When user adds a word:
If word already exists → return "already exists"
Else:
Insert into Trie
Set frequency = 1

3. Sorting Rule
1. Higher frequency first
2. If equal → alphabetical order

Example:
app (20)
apple (10)
apply (10)


Tech Stack
Backend: FastAPI (Python)
Frontend: HTML, CSS, JavaScript
Data Structure: Trie


 How to Run the Project
 Step 1: Install Dependencies
pip install fastapi uvicorn
Step 2: Run Backend
python main.py

Server runs at:

(http://127.0.0.1:5500/)
Step 3: Open Frontend
Open index.html in browser
OR use Live Server in VS Code
How to Test
Test Search
Type: app

Output:
app (20)
apple (10)
apply (10)
Test Add Word
Case 1:

Input: apple
Output: "apple already exists"

Case 2:

Input: apricot
Output: "apricot added with freq = 1"

Test Sorting

Try adding multiple words and check order:

Higher frequency first
Then alphabetical
Project Structure
project/
│
├── main.py        # FastAPI backend
├── index.html     # Frontend UI
└── README.md      # Documentation
