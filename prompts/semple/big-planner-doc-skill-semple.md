# Create Improvement document.
I want to update this skill.  this is old and I haven't gone through full document. But here are the changes I need.

- Use attached document as a reference. it's not the Final rulebook.
- I need a document at `/docs/PLAN__{name}.md`.
- skill name should be as it is: `create-improvement-doc`
- Don't just create one file. Create full fledged Skill for claude.
- This skill should not work as a fork and should define model that serve this purpose at best.
- This skill should be auto-load whenever we need. and also work for specific calls.

## Process

While Working on Big task, Design shifts, Architectural change, Specific Improvements (e.g. User accessibility, Mobile Experiance, SEO). I prefer to have big plan documented instead of just on-fly, one shot plan. Here is the ideal process that I would like to follow:

1. User Ask to create document for improvement or big task.
2. AI Understand the goal thoroughly, Make their own research on goal and then analyze repo.
3. AI Create a document in `/docs` folder.
4. User check document and go through checklist and understand it.
5. User (in same or separate session) ask AI to work on checklist by ID or sequance or series of IDs to start working or ask some questions.
6. AI either work on the ID. but if the task is risky or make big impact make user aware of it and ask for confirmation
7. AI done the job as per user's consent. and update document with marking current part as done.


### Research
1. Understand the goal, identify the type of change, If goal is unclear, ask user before going furthur.
2. Research the Goal online: Look up for current best practices and standards, (For e.g. Search engine guideline for SEO, common patterns for Mobile UX, WCAG etc...)
3. Check for PROJECT_ARCHITECT.md file and other file inside `/docs` folder. do read it. and also check files, components, routes, styles, libraries we used that goal touches.
4. Estimate how many files each part affects. This helps you judge the size and risk of each checklist item.
5. Once plan is ready, check and validate that each point are correct and workable actions and worth doing it.


### The Document

The document is saved at /docs/PLAN__{name}.md. It has two parts: a Checklist the user reads, and Instructions for Vibe Coding that tell the AI or coder how to work through the checklist.

#### Part 1: Checklist
Need Checklist (Not Table) So it have enough space for explaination or having different formats.

There can be more than one checklist if logically grouped.

CheckList should have:
- **Task ID:** T-001, T-002, SE-001 … (or GRP-NN if grouped in multiple checklist)
- **Priority:** Must (the goal fails without it), Should (important but not essential), Could (nice to have).
- **Effort and Risk:** Fibonacci scale: 1, 2, 3, 5, 8. Use 13 only as a signal to split the task. No 13s are allowed in the final table.
- **Business Value:**: Number or indicator that suggest how effective this checklist to complete in order to achive main goal.
- **Decision ID:** D-01; Finding ID: F-01

Here are some charactrastics while writing checlists.
- Human first language.
- **Tone** : Cheerful, humorsly, use emojies (Don't overuse it), Fun to read.
- **Language** : Simple english for non-native english speaker. simple words
	- avoid too much technical language, user might have technical background but not experties. explain terms if requre.
- Sort by business values.
- You can use sub-point checklists but don't overuse it.
- Must be honest
- Don't include code as far as possible.




#### Part 2: Detailed Plan to implement those checklists.

This part will never read by human. This is for more details on checklist items and plan to implement it by Vibe Coding.

1. Should have clear goal to follow while thinking/planning/working on any task from the checklist.
2. Have clear plan to implement the checklist item including describing changes, mention filenames etc.
3. Mention any blocking change, calculate impact and state guideline to complete task successfuly and efficiantly



## Working on checklist
1. Read entire document and clearly understand the big goal before start
2. Work on requested IDs only. Do the task the user asked for, in checklist order unless told otherwise. Do not start a second task on your own.
3. Check before starting. If the task is BLOCKED, or a dependency is not DONE, stop and tell the user.
4. Ask before risky work. If the task is marked “Confirm first? Yes”, or touches auth, payments, the database, deletes data, public APIs, or shared core code, explain the plan in simple English and wait for a clear “yes” before changing anything.
5. Stay in scope. Change only the files listed in the detail block. If you need another file, say so before editing it.
6. Keep changes small. No unrelated refactors, renames, or style changes.
7. Follow the repo. Match the existing patterns, folder structure, and naming. Do not add a new library without asking first.
8. Found a new problem? Add it as a new task at the end of the checklist with a new ID. Do not fix it silently.
9. Task too big? Stop, explain why, and suggest how to split it.
10. Unsure or blocked? Set the status to BLOCKED, write the reason in the detail block, and stop.
11. After finishing: tick the box
12. Never delete tasks. Use SKIPPED with a reason.
13. Reply in this format: Task ID, result, impacts and the next task ID. Keep the reply short. Write in simple English. Short sentences. Explain any technical term the first time it appears.
14. Consider (user instructions + Checklist plan) while executing.