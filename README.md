## The Core Philosophy

The reason people fail interviews isn't lack of pattern knowledge—it's that under pressure, they can't decompose problems or reason about tradeoffs. We're going to train those mental muscles directly.

### The 8-Week Transformation Plan

**Week 1-2: Build Your Foundation (The Thinking Framework)**

Goal: Learn to break down ANY problem into manageable pieces.

Daily Practice (90 min):

Problem Decomposition Drills (30 min) - Take 3 medium LC problems. DON'T solve them. Instead:


1. Write out what the problem is really asking in plain English

2. List 2-3 different approaches you could try (even bad ones)

3. For each approach, write the time/space complexity BEFORE coding
Only then pick one and implement

Constraint Analysis (30 min) - Critical skill most people skip:

Take the problem constraints (n ≤ 10^5, etc.)
Work BACKWARDS: "If n ≤ 100, I could do O(n²). If n ≤ 10^5, I need O(n log n) or better"
This trains you to immediately know what complexity you're aiming for

*Practice on 5 problems daily*, just analyzing constraints → viable approaches
Verbalization Practice (30 min):

*Solve 1 easy problem while explaining your thought process OUT LOUD*
Record yourself or explain to a rubber duck
This simulates interview pressure and exposes gaps in your reasoning
Why this works: You're training the meta-skill of problem-solving, not memorizing solutions.

**Week 3-4: Master the Fundamental Patterns (But Properly)**

Don't learn patterns by doing 20 similar problems. Learn them by understanding the core mechanism.

For each pattern, do this 3-step process:

Step 1 - Understand the Mechanism (Day 1):

Two Pointers: Why does it work? (It maintains an invariant while reducing search space)
Sliding Window: What makes a problem "windowable"? (Contiguous subarray + optimization)

Binary Search: Not just sorted arrays—understand "monotonic decision spaces"
Step 2 - Implement from Scratch (Day 2):

*Code the pattern template WITHOUT looking at solutions*
Mess up. Debug. Understand WHY your version failed
This builds real understanding

Step 3 - Variation Training (Days 3-4):

*Solve 2 problems that are DIFFERENT takes on the pattern*

Focus on: "How did I need to adapt the core mechanism?"
Cover these patterns:

- Two Pointers / Sliding Window
- Binary Search (including "binary search on answer")
- Fast/Slow Pointers
- Modified Binary Search
- Top K Elements (heap patterns)
- Tree BFS/DFS (and when to use each)
- Graph BFS/DFS + basic cycle detection
- Backtracking fundamentals
- Dynamic Programming (save for week 5-6)

**Week 5-6: Dynamic Programming (The Final Boss)**

DP destroys people because they try to memorize problem types. Instead:

Daily Structure (2 hours):

Pattern Recognition Training (45 min):
Before touching code, answer: "What are my states? What does dp[i] represent?"
Practice identifying: "Is this 1D DP, 2D DP, or something else?"

Key signals: "Optimization problem + overlapping subproblems"

The Translation Exercise (45 min):
Take a recursive solution (brute force)

Manually convert to memoization, and then convert to bottom-up

Understanding this pipeline is 80% of DP mastery

Deliberately Varied Problems (30 min):

Don't do 10 "longest subsequence" problems

Do: one subsequence, one knapsack variant, one string 
matching, one grid path

This forces your brain to think, not pattern-match

Critical DP Problems for Understanding (not memorization):

Longest Common Subsequence (understand the 2D table logic)
Coin Change (unbounded knapsack)
House Robber (understand state transitions)
Edit Distance (complex state transitions)
Word Break (understand why this is DP)
Week 7-8: Integration & Interview Simulation
Now you put it together:

Mock Interviews (3x per week):

Use Pramp, Interviewing.io, or a friend
45-minute sessions under real conditions
Focus on: explaining your thinking, handling hints, adapting when stuck

Curveball Training:

*Intentionally do problems from tags you haven't seen*
*Or do medium/hard without looking at tags at all*
Goal: "Can I figure out what pattern this needs?"

*The Post-Mortem Process (Most Important)*: After every problem, spend 10 minutes on:

What was the key insight I missed? (not the solution—the INSIGHT)
What question could I have asked myself to get unstuck?
What pattern was this, and how was it disguised?
Your Daily Schedule (Adjust to Your Life)
Weekdays (90-120 min):


### The Anti-Memorization Tactics
1. The "No Peeking" Rule:

Struggle for 25 minutes before looking at hints
If you look at solution, CLOSE IT, then implement from memory
Next day, redo the problem without any reference
2. The Variation Game:

After solving a problem, change the constraints: "What if they asked for the count instead of the list?" "What if the array could have negatives?"
This builds adaptability
3. Teach It:

Write a short explanation of each pattern you learn
Explain problems to others (or your rubber duck)
Teaching forces real understanding
Measuring Progress
Week 2: You should be able to identify 2-3 possible approaches for most medium problems before coding

Week 4: You should recognize the pattern in 70% of problems within 2 minutes

Week 6: You should be able to solve most medium problems (maybe slowly, but correctly)

Week 8: You should feel confident walking into an interview, knowing you can handle curveballs

The Mental Game
Your past failures weren't about intelligence—they were about trained thinking patterns. You're not building a library of solutions; you're building the skill of systematic problem decomposition under pressure.

Every time you feel stuck: "What information do I have? What am I trying to find? What's the gap between them?"

Resources (Minimal but Effective)
NeetCode Roadmap (for pattern organization, not to do every problem)
"Grokking" courses (for pattern understanding, not solutions)
Your Own Problem Journal (most important—write down your insights)
You've got 8 weeks to transform. The key isn't volume—it's intentional practice on the skills that actually matter in interviews.

You've failed before because you didn't have a system. Now you have one. Execute it.