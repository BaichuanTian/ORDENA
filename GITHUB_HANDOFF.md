# GitHub publication and instructor access

Status: no GitHub repository has been created for this package. No remote push,
pull request, Actions run, branch protection or instructor access is claimed.
The local origin in a bundle clone is not a hosted code repository.

## Assigned empty repository

Obtain the approved repository in HarrisburgU-SE using the instructor-assigned
Engineering Code Name. Do not invent either. From the extracted ZIP root:

```sh
git clone pos_cm_history.bundle restored-pos-cm
cd restored-pos-cm
git branch feature/sample-menu origin/feature/sample-menu
git branch fix/CM-002-order-line-validation origin/fix/CM-002-order-line-validation
git remote remove origin
git remote add origin ACTUAL_ASSIGNED_GITHUB_URL
git push -u origin master
git push origin feature/sample-menu fix/CM-002-order-line-validation
git push origin cm-start cm-v0.1.0 cm-v0.1.1
```

ACTUAL_ASSIGNED_GITHUB_URL is a replacement marker, not an executable URL.
Create the local feature/fix branches before removing the bundle origin.
For an existing school repository, do not replace its history or force-push.
Clone it and import these files on a new branch, test and use a real PR.

## Access and hosted verification

Set master as the default integration branch. Check whether the instructor
already inherits read access through HarrisburgU-SE. If access is not inherited,
use the organization-approved process to grant access to the instructor's
verified account. Record the repository URL, instructor account, permission
source and successful access confirmation. This cannot be inferred from a ZIP.

Inspect the first real Actions run. Where permissions allow, require successful
tests before merging PRs and prevent direct development on master. All new
code changes start on feature/* or fix/* branches. Do not create a fake PR or
retroactively describe the local merge as a hosted PR.

## Evidence to append to the report

- Actual repository URL and approved Engineering Code Name.
- Instructor access confirmation and date.
- First successful hosted Actions URL and commit.
- Next real change request, branch and PR URL with actual review disposition.
- Published tag references; a GitHub Release page is optional for this assignment.
