# Configuration Management Plan

Project: Restaurant POS and Order Management System
Author and CM owner: Baichuan Tian
Scope: individual CISC 594 academic development and generic CM examples

## Configuration items

Track source code, generic JSON configuration, sample data, tests, workflow YAML,
setup instructions, requirements, change requests, and release notes in Git.
Keep machine-specific configuration, secrets, generated caches, real customer
information, and company-proprietary materials outside tracked files.

## Naming and ownership

Use descriptive lower-case file names and directories. Store configuration in
`config`, fixtures in `data`, tests in `tests`, and controlled documents in `docs`.
Baichuan Tian maintains the baseline and records change decisions. The approved
Engineering Code Name will identify the school repository after instructor
assignment; this package does not assume approval of either suggested name.

## Branches and change control

`master` contains verified work. Create `feature/<topic>` for new work and
`fix/<topic>` for corrections. Each change request records its identifier,
reason, affected files, risk, test requirements, and decision. Reference that
identifier in commits and, when hosted, the pull request.

Process: document request, branch, implement, review diff, execute affected tests
and regression tests, record outcome, then merge. On GitHub, use a PR and request
review when a reviewer is available. For individual work, record self-review
honestly. Never represent self-review as independent approval. Enable required
checks and review rules only where permitted by the organization.

## Baselines and versioning

Use annotated `cm-start` and `cm-v0.1.0` tags for this local CM demonstration.
Do not move published tags. The planned product `v1.0.0` is the complete core POS:
login, menu, dine-in/takeout orders, pricing, simulated payment, status and history.
The planned `v2.0.0` adds table management, split payments, discounts and inventory.
Build and system-test V1 before starting V2. Establish those product tags only
when their requirements and complete system tests pass. Neither is delivered here.

## Reproducibility and audit

Record runtime version, commit, configuration, test command, results and known
limitations for every baseline. Review tracked configuration whenever it changes.
This demo uses only Python's standard library. If dependencies are introduced,
track explicit versions and update setup instructions and CI together.

## Rollback and recovery

Inspect a baseline with `git switch --detach cm-v0.1.0`; return with
`git switch master`. Do not edit a detached checkout as an ordinary feature branch.
For a faulty ordinary commit already shared, create a fix branch, use
`git revert <commit>` and review/test the resulting new commit. Merge commits
require a deliberate parent choice; do not blindly revert them. Avoid force-push
or history rewriting on shared branches. Database migration and restoration
procedures will be added when persistent storage exists.

The bundle preserves local history for this submission. After school-repository
connection, retain the remote history and a separately stored release bundle or
archive. Verify recovery by cloning and rerunning the tests, not merely by
checking that an archive exists.

## Test automation and hosted status

The prepared CI runs the same real unittest command on Python 3.11 for pushes and
pull requests. A failing test must block release approval. Hosted Actions,
required reviews, a GitHub PR, instructor access and remote publication have not
been demonstrated in this local package. Add real URLs and outcomes after setup.

## CM-002 release procedure

The integration branch was renamed locally from main to master without rewriting
old commits. Existing cm-start and cm-v0.1.0 tags remain unchanged. New development
uses fix/CM-002-order-line-validation, with the request and gate committed before
implementation. Gate evaluation and diff inspection are AI-assisted local checks,
not independent approval. After all gates pass, record acceptance, merge with
--no-ff, rerun the suite on master, and create annotated tag cm-v0.1.1.
Student review and instructor repository access are separate outstanding actions.

Record a new request for each baseline change. Do not start implementation until
scope, impact, disposition authority and acceptance criteria are recorded. A
failed gate returns the request to implementation on its branch. Rejected or
withdrawn requests do not change master. Keep requests, result logs, commits,
merges and tags traceable by the same CM identifier. Do not delete prior records.
