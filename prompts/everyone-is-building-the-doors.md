# Rebuild prompt: Everyone Is Building the Doors. Nobody Is Building the Kitchen.

Use this prompt to rebuild the essay from scratch.

## Goal

Publish a Drifting Signals essay titled **Everyone Is Building the Doors. Nobody Is Building the Kitchen.** The argument: agent standards (MCP, A2A, Personal Agent Protocol) are plumbing — pantry, ticket rail, and front door. The missing layer is kitchen call-outs, which is **Quorum Signaling**. Governance-style voting is a staff meeting; most agent decisions should come from accumulating short signals. Do not use QuorumOS.

## Inputs

- Folder: `content/ideas/everyone-is-building-the-doors-nobody-is-building-the-kitchen/`
- Hub: `idea.md` (frontmatter + full essay)
- Date: `2026-10-16`
- Tags: `agents`, `quorum`, `coordination`, `protocols`
- Status: `published`
- Source draft: `Everyone Is Building the Doors. Nobody Is Building the Kitchen.md`
- Depends on: `content/ideas/when-ai-agents-need-to-know-when/` (The Case for Quorum Signaling)
- Series neighbor: `content/ideas/quorum-signaling-isnt-new/` links forward to this essay

## Outputs

- Title and card summary: doors are being standardized; the missing layer is call-outs (Quorum Signaling)
- Body without a duplicate H1 or a date/byline line (the template already shows those)
- Kitchen mapping: MCP = pantry and tools, A2A = ticket rail, Personal Agent Protocol = front door, Quorum Signaling = call-outs
- Kang & Diponegoro governance-gap paper (arXiv 2606.31498), linked once as “a great paper,” not letter by letter
- Four-step signaling layer, fair objections, Tanenbaum standards line, bet on the kitchen
- Relative link back to `/ideas/when-ai-agents-need-to-know-when/`
- A follow-up line on the prior-art essay pointing here

## Dependencies

- The blog’s Markdown idea-folder format (`idea.md` hub)
- Frozen static build via `python freeze.py` into `build/` for Cloudflare

## Constraints

- Keep the URL slug `everyone-is-building-the-doors-nobody-is-building-the-kitchen` unless the author asks to change it.
- Always write **Quorum Signaling** for the model. **QuorumPlane** is the control plane from earlier essays; this essay does not need to introduce it.
- The source export’s embed marker (“The agent kitchen · three layers built, one missing”) is not an image. Do not publish that placeholder. The three bullets above it already carry the figure.
- Keep existing `/ideas/` URLs even though the nav says “Blog entries”.
