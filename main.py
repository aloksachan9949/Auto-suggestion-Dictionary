from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0

class DictionaryTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, freq: int = 1):
        node = self.root
        word = word.lower().strip()
        if not word:
            return
            
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if node.is_end:
            node.frequency += 1
        else:
            node.is_end = True
            node.frequency = freq

    def get_suggestions(self, prefix: str) -> List[dict]:
        node = self.root
        prefix = prefix.lower()
        
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        self._dfs(node, prefix, results)
        
        results.sort(key=lambda x: (-x['freq'], x['word']))
        
        return results[:5]  

    def _dfs(self, node, path, results):
        if node.is_end:
            results.append({"word": path, "freq": node.frequency})
        
        for char in sorted(node.children.keys()):
            self._dfs(node.children[char], path + char, results)



trie = DictionaryTrie()

initial_words = [
    ("apple", 10), 
    ("apply", 10), 
    ("app", 20), 
    ("ball", 5), 
    ("bat", 15), 
    ("battery", 12),
    ("banana", 10),
    ("band", 8)
]

for word, freq in initial_words:
    trie.insert(word, freq)


@app.get("/search")
def search(prefix: str = ""):
    if not prefix:
        return []
    return trie.get_suggestions(prefix)

@app.get("/debug")
def debug():
    """Check if the Trie is actually populated"""
    return {
        "trie_root_chars": list(trie.root.children.keys()),
        "total_words_loaded": len(initial_words)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

@app.post("/add-word")
def add_word(word: str):
    trie.insert(word)
    return {"status": "success", "word": word}