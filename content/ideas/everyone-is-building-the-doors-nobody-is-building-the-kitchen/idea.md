---
title: "Everyone Is Building the Doors. Nobody Is Building the Kitchen."
summary: "Everyone is racing to standardize how AI agents get through the door. The missing layer is the kitchen call-outs: how a group of agents knows what to do next. That's Quorum Signaling."
date: 2026-10-16
tags: [agents, quorum, coordination, protocols]
status: published
---

## The race to build the front door

On October 6, Meta and Sierra announced something called the Personal Agent Protocol. Walmart, Shopify and Stripe signed on as founding partners. The pitch is simple: if your AI assistant wants to shop, book or return something on your behalf, there should be one standard way for it to knock on a store's door and say who it is.

The timing wasn't an accident. About two weeks earlier, Amazon had started blocking Meta's new assistant, Muse, from its site. Meta's response, roughly: if you turn away my agent, you're turning away the customer behind it.

That little standoff is a good snapshot of where AI is right now. Everyone agrees agents are coming. So everyone is racing to agree on the doors: how agents get in, what they're allowed to touch, and how they prove who sent them.

Those doors matter. But I think the industry is skipping a harder question. Once a bunch of agents are inside, working on the same problem, how do they know what the group as a whole should do next?

## Think of it as a restaurant kitchen

The alphabet soup of agent standards gets confusing fast, so here's the picture I use. Imagine a busy restaurant kitchen where every cook is an AI agent.

Over the past two years, the industry has standardized three big pieces of that kitchen:

- **The pantry and the tools.** Anthropic's Model Context Protocol, usually called MCP, is how a single agent reaches its tools and data: a database, a calendar, a file. In kitchen terms, it's how a cook grabs a knife or pulls something from the walk-in. It answers one question: *what can this cook do?*
- **The ticket rail.** Google's Agent-to-Agent protocol, or A2A, is how one agent finds another and hands it a job. It's the ticket that goes from one station to the next. It answers: *which cook should handle this order?*
- **The front door.** The new Personal Agent Protocol is about identity. It lets a store check that a visiting agent is really working for a real customer, and decide what it's allowed to do. It answers: *who is this, and are they allowed in?*

All three are useful. All three are basically plumbing. They move requests, tools and tickets from one place to another.

What none of them does is help the kitchen *run*.

## The missing layer

Anyone who has worked a real kitchen knows the hard part isn't the knives or the ticket printer. It's the running conversation. "Behind!" "Eighty-six the salmon." "Two minutes on table six." That steady stream of short call-outs is how a dozen people who can each see only their own station act like one team.

Agents don't have that yet. And I'm not the only one who thinks so.

In June, [a great paper](https://arxiv.org/pdf/2606.31498) was published that checked five of the major agent protocols, including MCP and A2A, against a list of things a group of agents would need to make decisions together. Things like: who's part of this decision? How do agents disagree with each other? When does a human get pulled in? Can we replay what happened afterward?

The results were interesting. Not one protocol could handle voting or keep a record of disagreement. Most of the other items were missing or only half there. Their conclusion was that this isn't a feature someone forgot. It's an entire layer that doesn't exist yet.

In kitchen terms: we've built a great pantry, a great ticket rail and a great front door. Nobody has built the call-outs.

## Staff meeting, or call-outs?

Here's what I'm seeing. The paper agrees a layer is missing, but its idea of what belongs there looks a lot like a meeting. The authors borrow from parliamentary procedure. Agents get admitted to a decision, raise formal challenges, cast votes and file dissents for the record.

For some decisions, that makes sense. If five agents are deciding whether a system passes a compliance review, I want a formal vote, a written record and the dissenting opinion preserved. That's a decision worth slowing down for.

But most of what happens in a kitchen isn't a meeting. Nobody calls a vote on whether the fryer is too hot. A cook says "fryer's running hot," another says "yeah, I'm seeing it too," and the kitchen adjusts. No single call-out decides anything. Enough of them, pointing to the same thing, and the whole room changes what it's doing.

Nature figured this out long ago. Bacteria use something called quorum sensing: (yeah I'm bringing this up again.) each one releases a tiny chemical signal, and when enough of that signal builds up in the area, the whole colony switches behavior at once. No bacterium sees the big picture. None of them votes. The group still acts together.

That's the model I've been calling **Quorum Signaling**. And I think a lot of agent decisions look more like the fryer than the compliance review:

- Has our research turned up enough to stop searching?
- Are these agents all agreeing because they're right, or because they all read the same bad source?
- Is this task getting expensive enough that we should switch to a cheaper approach?
- Is something going wrong that a human should look at?

None of those should wait for a vote. They should come from a steady stream of small signals that add up.

## What the call-outs would look like

In practice, a signaling layer is simpler than it sounds. It comes down to four steps.

1. **Agents call out what they're noticing.** Not their whole chain of reasoning, just a short labeled signal. "I'm uncertain." "This contradicts what we found earlier." "I'm not finding anything new." "This is getting expensive."
2. **The signals add up.** Each call-out has a strength, and older ones fade over time (decay), the way "fryer's hot" from an hour ago matters less than one from ten seconds ago.
3. **Thresholds trip.** When the right combination of signals crosses a line, the group's state changes. For example: confidence is high, new findings have dried up and nobody's flagging contradictions. That means the research is done.
4. **The kitchen reacts.** Stop searching. Bring in a fact-checker. Switch to a cheaper model. Get a human.

The nice part is that this doesn't replace the plumbing. It rides on top of it. Agents could still use MCP to grab their tools and A2A to pass tickets. The call-outs would just be one more kind of message going across the same rail.

And the two ideas, call-outs and staff meetings, fit together well. The call-outs could be what decides when it's time to *hold* a meeting. The paper itself includes an example of sending a decision to a human when the group's average confidence drops too low. That's a call-out tripping a threshold, sitting right inside a governance design.

## Fair objections

Here are some things I still need to work through. Please send me your thoughts and comments on this stuff.

**"Agent frameworks already handle this."** Partly true. Tools like LangGraph and CrewAI let you build coordination into your own app. But that works best when every agent lives in the same app, built by the same team. The whole point of the new protocols is agents from *different* companies working together. Once that happens, coordination can't live inside any one company's code.

**"Signals can be gamed."** Absolutely. An agent that learns "calling out 'done' ends my task" might start calling out "done" early. A cook who wants to go home could do the same thing. That's one reason the paper's focus on preserving disagreement matters: a lone voice saying "wait, something's off" shouldn't get averaged away. Good signaling has to treat that voice as a feature, not noise.

**"Thresholds are fragile."** Also true. The right line for "research is done" will differ between a quick question and a legal review. Setting those lines well is real work, and it's still an open problem. I'm working on a theory for setting and testing thresholds in a changing environment like this. Look for a future post on this.

None of these kills the idea. They're the to-do list.

## The clock is running

The paper's authors estimate this gap could start closing in the next six to twelve months, most likely through add-ons to Google's A2A protocol. That's both good news and a warning. Standards tend to get set by whoever shows up first with something that works, not by whoever has the best idea. I can also see a lot of 'standards' being published in hopes to control the decision plane. *"The nice thing about standards is that you have so many to choose from."*  - Andrew Tanenbaum

So here's my bet. The next big fight in AI agents won't be over who gets through the front door. It'll be over who builds the call-outs. Will that layer look like a parliament, a kitchen, or (most likely) some mix of both?

I'm betting on the kitchen. Not because meetings are bad, but because most of the time a team doesn't need to vote. It needs to hear "behind!" and get out of the way.

---

*Quorum Signaling is a concept I've been developing here on Drifting Signals. If you want the deeper version, start with* [The Case for Quorum Signaling](/ideas/when-ai-agents-need-to-know-when/)*.*

## Sources

- Kang & Diponegoro, [Governance Gaps in Agent Interoperability Protocols](https://arxiv.org/pdf/2606.31498) (arXiv, June 2026)
- [Meta and Sierra's Personal Agent Protocol starts with login, not payments](https://datafloq.com/meta-and-sierras-personal-agent-protocol-starts-with-login-not-payments/) (Datafloq)
- [Shopify and Stripe join Meta's Personal Agent Protocol](https://ecommerceparadise.com/personal-agent-protocol-shopify-stripe/)
- [MCP vs A2A protocol](https://pickaxe.co/post/mcp-vs-a2a-protocol) (Pickaxe)
