# 🎯 Markdown Mastery 🧠

Markdown is a way to **write plain text** that turns into **formatted content** on GitHub, VS Code, Notion, etc

Think: easy to **read**, easy to **write**, no fancy editor needed



## 1️⃣ Headings

Use `#` symbols. More `#` = smaller heading

```markdown
# Big Heading (H1)
## Medium Heading (H2)
### Small Heading (H3)
```

Preview:

# Big Heading

## Medium Heading

### Small Heading



## 2️⃣ Paragraphs & Line Breaks

Separate paragraphs with an empty line
Force a line break with **two spaces** at the end

```markdown
This is the first paragraph

This is the second paragraph
This line breaks here
```


## 3️⃣ Text Styling

| Style         | Markdown            |
| ------------- | ------------------- |
| Bold          | `**bold**`          |
| Italic        | `*italic*`          |
| Bold+Italic   | `***bold+italic***` |
| Strikethrough | `~~wrong~~`         |
| Inline code   | `` `code` ``        |

Example:

```markdown
Use **bold**, *italic*, ***both***, ~~wrong~~, and `inline code`.
```



## 4️⃣ Lists

### Ordered List

```markdown
1. First
2. Second
3. Third
```

### Unordered List

```markdown
- Apple
- Banana
  - Green
  - Ripe
* Another bullet
+ One more style
```

### Task List (GitHub Only)

```markdown
- [x] Done
- [ ] Pending
```



## 5️⃣ Links & Images

**Link:**

```markdown
[GitHub](https://github.com)
```

**Image:**

```markdown
![Alt text](https://example.com/image.png)
```

**Clickable Image:**

```markdown
[![Logo](https://example.com/logo.png)](https://example.com)
```



## 6️⃣ Code

**Inline code:** `` `print("Hello")` ``

**Code block:**

````markdown
```python
def hello():
    print("Hello, world!")
```
````

💡 Always specify the language for **syntax highlighting**.



## 7️⃣ Blockquotes

```markdown
> This is a quote.
> 
> > Nested quote.
```

Preview:

> This is a quote.
>
> > Nested quote.



## 8️⃣ Tables

```markdown
| Name  | Age |
|-------|----|
| Alice | 30 |
| Bob   | 25 |
```

Preview:

| Name  | Age |
| ----- | --- |
| Alice | 30  |
| Bob   | 25  |



## 9️⃣ Horizontal Line

```markdown
---
```



## 🔟 Extras

**Emojis:** `:rocket:` → 🚀
**Footnotes:**

```markdown
Text with footnote.[^1]

[^1]: Footnote text
```

**Collapsible Sections:**

```markdown
<details>
<summary>Click to expand</summary>
Hidden content here.
</details>
```



