# Drill: Number to Month

**Concept:** Dictionary as a lookup table.  

**Key idioms:** `dict.get()` for safe lookup.  

**Why it matters:** Avoids chained `if/elif`. Easier to extend.

**Extra Notes:** 
dict.get() is only a lookup. 
But it can modify the list if adding something like dict[w] = dict.get(w, 0) + 1, which will write back into dict[w].