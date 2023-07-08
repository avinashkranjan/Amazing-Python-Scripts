## Stack Overflow

### Scrape questions, views, votes, answer counts, and descriptions from Stack Overflow website regarding a topic

Create an instance of `StackOverflow` class.

```python
questions = StackOverflow("topic")
```

| Methods        | Details                                                                             |
| -------------- | ----------------------------------------------------------------------------------- |
| `.getQuestions()` | Returns the questions, views, votes, answer counts, and descriptions in JSON format |

**Example**

```python
que = StackOverflow("github")
scrape = que.getQuestions()
json = json.loads(scrape)
questions = json["questions"]
for q in questions:
    print("\nQuestion: ", q["question"])
    print("Views: ", q["views"])
    print("Votes: ", q["vote_count"])
    print("Answers: ", q["answer_count"])
    print("Description: ", q["description"])

```