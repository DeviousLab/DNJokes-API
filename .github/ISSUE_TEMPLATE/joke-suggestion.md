---
name: Joke suggestion
about: Got a joke you'd like to add to the database?
title: "[Suggestion] "
labels: enhancement
assignees: DeviousLab

---

**The jokes are stored in the PostgreSQL database in the following format:**
```
{
  "id": 1,
  "prompt": "Excuse me but do you Bofa?",
  "reply": {
    "first": "Bofa? I don't think so?",
    "second": "Bofa deez nuts!"
  }
  }
},
``` 
**You can format your suggestion in according to this layout**
"prompt": "{Your message here}",
  "reply": {
    "first": "{Your message here}",
    "second": "{Your message here}" 

*Additional responses can be added by using `third`, `fourth` parameters in `reply` as well*

**Additional context**
Add any other context or screenshots about the feature request here.
