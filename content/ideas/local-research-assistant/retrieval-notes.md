---
title: Retrieval notes
summary: How to chunk, index, and cite local files without overbuilding the stack.
---

# Retrieval notes

Start with files you already trust.

1. Split on headings and paragraphs, not arbitrary token windows.
2. Store the source path and heading path with every chunk.
3. Return citations before the model writes a sentence.

A SQLite FTS index is enough until the corpus is large. Embeddings can wait until keyword search stops finding the right page.

```text
query -> search chunks -> rerank -> prompt with quotes -> answer
```

If a chunk cannot be quoted, the assistant should say it does not know.
