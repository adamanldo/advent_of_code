from collections import deque

with open('input/10', 'r') as f:
    lines = f.read().split('\n')

chunk_dict = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
}

closing_chunk_dict = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<"
}

illegal_char_score = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

autocomplete_tool_score = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

opening_chars = {"(", "[", "{", "<"}

def part1():
    syntax_error_score = 0

    for line in lines:
        q = deque()
        for char in line:
            if char in opening_chars:
                q.append(char)
            else:
                opening = q.pop()
                if opening != closing_chunk_dict[char]:
                    print(f"Expected {chunk_dict[opening]}, got {char}")
                    syntax_error_score += illegal_char_score[char]
                    break

    print(syntax_error_score)

def part2():
    incomplete_chunks = []
    corrupt_chunks = []
    
    for line in lines:
        q = deque()
        for char in line:
            if char in opening_chars:
                q.append(char)
            else:
                opening = q.pop()
                if opening != closing_chunk_dict[char]:
                    corrupt_chunks.append(line)
                    break
    
    incomplete_chunks = [line for line in lines if line not in corrupt_chunks]
    total_scores = []

    for line in incomplete_chunks:
        total_score = 0
        q = deque()
        for char in line:
            if char in opening_chars:
                q.append(char)
            else:
                q.pop()
        while q:
            char = q.pop()
            total_score = total_score * 5 + autocomplete_tool_score[chunk_dict[char]]
        total_scores.append(total_score)

    print(sorted(total_scores)[len(total_scores) // 2])


part2()