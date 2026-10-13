# Create Architectural document.
I want to update this skill.  this is old and I haven't gone through full document. But here are the changes I need.

- Use attached document as a reference. it's not the Final rulebook.
- I need 2 documents (PROJECT_ARCHITECTURE.md and PROJECT_OVERVIEW_FOR_HUMAN.md) Both are describe letter in this document.
- name should be as it is: `update-arch-doc`
- Don't just create one file. Create full fledged Skill for claude.
- This skill should work as a fork and should define model that serve this purpose at best.
- Along with this document, It should update readme.md file at root as well. So it mention these two document and share up to date information along with it.
	+ Readme.md is for human so keep it light, use emojies (don't overload) and keep cheerful tone.
- Both document should have stemp at top which indicate freshness of the doc and metadata (Like last commit it covers, updated date)



### "Project Architecture" Document

This is the attached doc is all about. So you can have a breif context from that. But here is the final goal of the document.

1. I need a document that well define the current repo's architecture at whole.
2. This should be standalone document to understand the architecture.
3. I will use it to provide context to AI Chat & Projects to Give core idea about everything in my project when I want to do some research or planning for new feature or chore or want to validate adjustment or planning.
4. This document will mostly used by AI. So choose writing style accordinly. So it can be read and understandable by any AI Model.
5. This document might occasinally (Not always) read by AI Agents as well, when they want to have an idea about full repo and don't know where to read.
6. If this is back-end, it must have database architecutre. and if front-end it should have Data Layer and Design philosophy.

### "Project Overview for Human" Document

This is the Guideline document for Human. Here are some final goal of the document (In random order).

1. This is Human first document.
2. This document should give good idea to Fresher and New developer to understand what this is all about.
3. **Tone** : Cheerful, humorsly, use emojies (Don't overuse it), Fun to read.
4. **Language** : Simple english for non-native english speaker. simple words
	- avoid too much technical language, user might have technical background but not experties. explain terms if requre.
5. Use mermaind diagrams wherever applicable. (Like C4, ER, Sequence, Modules, etc...)
	+ It's not mendetory to draw all. but nice to have what are required.
6. Use Top-down approch. means first give top overview and then dig deeper.
7. This document should answer, what is this project, who is it for, how code organized (short)
8. Use Proprt md formatting including hirarchical headings, short lists, tables, graphs. avoid long peragraphs. can use interlink if needed.
9. Must be honest
10. Don't include code. (Only if required: include copy safe commands)