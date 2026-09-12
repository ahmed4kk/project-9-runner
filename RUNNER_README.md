# Project 9 Runner

Public, non-proprietary execution wrapper for Project 9.

## GitHub secret required
`PROJECT9_CORE_READ_TOKEN` must be a least-privilege token that can read only the private `ahmed4kk/project-9-core` repository.

Other runtime secrets belong in GitHub Actions Secrets, never in source.

## Workflow security
The worker workflow intentionally uses only `workflow_dispatch`. Do not add `pull_request`, `pull_request_target`, or untrusted checkout triggers. GitHub documents that secrets are not passed to fork-triggered workflows, and recommends least-privilege permissions; privileged triggers with untrusted code can create serious security risks.
