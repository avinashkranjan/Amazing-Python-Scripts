## Ask Ubuntu

### Scrape questions, views, votes, answer counts, and descriptions from Ask Ubuntu website regarding a topic

Create an instance of `AskUbuntu` class.

```python
questions = AskUbuntu("topic")
```

| Methods        | Details                                                                             |
| -------------- | ----------------------------------------------------------------------------------- |
| `.getQuestions()` | Returns the questions, views, votes, answer counts, and descriptions in JSON format |


**Example**

```python
que = AskUbuntu("github")
scrape = que.getQuestions()

```