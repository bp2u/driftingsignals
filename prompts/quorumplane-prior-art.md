# Rebuild prompt: Quorum Signaling Isn't New. The Control Plane Might Be.

Use this prompt to rebuild the essay from scratch.

## Goal

Publish a Drifting Signals follow-up to **The Case for Quorum Signaling**. Title: **Quorum Signaling Isn't New. The Control Plane Might Be.** Quorum Signaling is the calling-out. **QuorumPlane** is the head chef / reusable control plane. Do not use QuorumOS.

## Inputs

- Folder: `content/ideas/quorum-signaling-isnt-new/`
- Hub: `idea.md` (frontmatter + full essay)
- Date: `2026-09-11`
- Tags: `agents`, `quorum`, `coordination`, `control-plane`
- Status: `published`
- Source draft: `quorumplane-prior-art-v2.md`
- Depends on: `content/ideas/when-ai-agents-need-to-know-when/` (The Case for Quorum Signaling)

## Outputs

- Title and card summary about prior art vs the missing control plane
- Body without a duplicate H1 (the template already shows the title)
- Relative link back to `/ideas/when-ai-agents-need-to-know-when/`
- Kitchen metaphor; robotics/security prior art; MACI, BNE, pressure fields, stigmergy; tool-layer gap (LangGraph, AutoGen, CrewAI, Temporal, observability); absorption risk; three spec changes (MACI plateau default, signal visibility, economic termination); references; author’s note
- A follow-up line on the original Quorum Signaling essay

## Dependencies

- The blog’s Markdown idea-folder format (`idea.md` hub)

## Constraints

- Keep the URL slug `quorum-signaling-isnt-new` unless the author asks to change it.
- Always write **QuorumPlane**, never QuorumOS.
- Keep existing `/ideas/` URLs even though the nav says “Blog entries”.
