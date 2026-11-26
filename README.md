# Restaurant POS Configuration Management Demonstration

Prepared for CISC 594 by Baichuan Tian. This is an independently created academic
CM example. Menu entries, restaurant details, prices, and the 6% demonstration
tax rate are fictional. They do not represent a real restaurant or tax policy.

## Scope

This package demonstrates version control and reproducible configuration using a
small checkout calculator. It does not implement the full proposed restaurant
POS, payment processing, authentication, or persistent order storage.

## Run

Use Python 3.11 or newer and Git. No third-party Python dependencies are required.
From this directory:

```sh
python -m unittest discover -s tests -v
python -m src.pos_demo
```

The sample order has a subtotal of 2225 cents, tax of 134 cents, and total of
2359 cents. All amounts are integer cents. Tax is rounded half up at order level.

## Files

- `src/`: calculator and command-line demonstration.
- `config/`: tracked generic settings; local overrides are ignored.
- `data/`: fictional menu and order inputs.
- `tests/`: actual automated tests.
- `docs/CM_Plan.md`: configuration and change-control policy.
- `.github/workflows/ci.yml`: prepared test workflow; hosted execution is pending.
- `CHANGELOG.md`: changes to this demonstration.

## Restore the actual Git history

The submission includes `../pos_cm_history.bundle` alongside this source folder.
Clone it into a new directory; do not initialize a second repository inside this
folder or copy an existing repository's `.git` directory.

```sh
git clone ../pos_cm_history.bundle restored-pos-cm
cd restored-pos-cm
git log --oneline --graph --all
git tag -n
```

The bundle is a local transport file, not a GitHub remote. School repository
connection instructions are in `docs/GITHUB_HANDOFF.md`.

## Current local CM release

CM-002 adds structural line validation. Malformed lines now raise ValueError;
valid totals and the sample remain unchanged. The integration branch is master
(previously main). Release cm-v0.1.1 is a demo patch, not product V1 or V2.
The recorded Git author explicitly identifies automated coursework assistance.
Review docs/CR_002.md and the supplied evidence before student submission.
Run the 13-method suite with the command above; some methods contain subtests.

To restore the submitted history from the extracted ZIP root:

```sh
git clone pos_cm_history.bundle restored-pos-cm
cd restored-pos-cm
git switch master
git log --graph --oneline --all
git tag -n
python -m unittest discover -s tests -v
python -m src.pos_demo
```

The bundle is transport history only. There is no hosted school repository yet;
teacher access and hosted CI must be completed using docs/GITHUB_HANDOFF.md.
