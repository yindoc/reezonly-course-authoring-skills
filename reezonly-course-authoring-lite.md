# Reezonly course authoring

Use MCP tools and resources only. Never make direct LMS/service HTTP calls. Never place credentials, bearer values, cookies, or local paths in tool arguments, journals, audits, or reports. Supply educational content only in exact published mutation fields; never write raw educational content or block content to journals, audits, or reports.

## Start from the live catalog

1. Call `tools/list`; treat its available tools and current input/output schemas as runtime authority over source, manifests, saved guidance, or historical capabilities.
2. Call the published runtime-info operation with one new non-secret `runId`; retain that run ID for the same actor/session/run.
3. Read the published getting-started resource and each required block/resource guide. Check capability status, opt-ins, confirmations, and exact schema immediately before action.
4. Stop before mutation on a missing, disabled, conditional-without-opt-in, or drifting capability. Do not hardcode tool counts, build IDs, profile availability, IDs, or live data.

## Choose the authority lane

- For a new Course, use the current create schema without `courseId` or discovery.
- For ordinary bearer work on an existing Course, use only user-selected explicit IDs and a fresh authoritative hierarchy. Re-read and verify the exact parent, type, position, and intended state before each mutation; do not change another or unselected entity.
- Treat list/discovery output, candidates, partial output, ACKs, and selectors as observed, not owned.
- An external existing Course is not ordinary bearer authority and must not be adopted. Use it only through the published `lesson_authoring_prepare_existing_course_authority` schema.
- Keep `full_access` and `delete_once` as separate authority lanes. Never mix their inputs, receipts, or permissions.
- Canonical structural delete is a separate conditional lane from ordinary owned `preview_cleanup` and external `delete_once`. Use it only when the live catalog publishes exact `lesson_authoring_delete_entity`: fresh-read the exact selected Course/parent chain, match current confirmation `action`/`entityId`, dispatch exactly once, then confirm authoritative absence. Course uses only selected `courseId` + literal `delete_course`, no client cascade or ownership/grant/selector, and the current authoritative course-index absence path. Module/Lesson/Page/Block use only their exact published branch. `unknown` is never resent; honour only its exact returned `nextAction`.

## Author deliberately

Get audience, outcomes, constraints, assessment evidence, materials, and explicit activation/publication intent. Prepare a course plan and a separate lesson blueprint before writes. Use only block, asset, testing, and validation operations published by the live schemas.

Create draft hierarchy in current schema order. Reuse an unambiguous default page; request an additional page only when the plan and schema justify it. After every create, update, move, delete, upload, or settings mutation, obtain the required authoritative typed readback. Verify existence (or absence), parent, type, position, and intended normalized fields before using anything for the next step.

## Cleanup external Course with `delete_once`

Treat cleanup as a separate, user-authorized destructive stage with exact selected scope. Ordinary owned cleanup uses only its published `preview_cleanup` lane. Do not substitute `preview_cleanup` for external cleanup.

When the catalog publishes `lesson_authoring_prepare_existing_course_authority`, external `delete_once` has one fixed sequence:

1. Request its prepare preview with the exact `delete_once` schema.
2. Send the fresh server confirmation verbatim in the same actor/session/run.
3. Use only the returned server selector; never construct a selector, receipt, or confirmation.
4. Invoke exactly one direct `lesson_authoring_execute_cleanup`.
5. Confirm authoritative absence.

Do not adopt the external Course, issue a second delete, or construct a cascade. After deletion, `lesson_authoring_get_course_content` may return a closed zero-mutation ErrorEnvelope: `NOT_FOUND`, `validation`, `rejected`, and `retryable:false`. That is authoritative absence, not `unknown`, and is never grounds to repeat delete.

For Webinar11 and Integration13, use only the current rich-media schema. Before Webinar create, provide every current schema-required field, including `type` and `duration`; typed canonical readback is authority. Do not copy, use as authority, traverse, project, or log server-owned opaque extensions. Stop on typed drift/error; do not guess a payload adaptation.

## Interpret outcomes safely

- Verified success or no-op still requires the schema-required authoritative readback.
- A pre-dispatch rejection means no mutation was sent. A declared post-dispatch rejection is terminal; neither proves ownership.
- For any real `unknown`, timeout, or ambiguous ACK, do not blindly retry or resend. Honour the exact returned `nextAction` and run only its returned tools in its returned order and shape before any new mutation. Do not invent recovery.
- Never present a candidate or partial result as owned.

## Finish

Run only published, compatible QA. Activate lessons last and only on explicit intent after successful QA and readback. Publish only on explicit intent, the exact runtime gate/confirmation, and independent required readbacks. Report selected scope, verified outcomes, skipped capabilities, warnings, activation/publication state, and safe next actions—without credentials, raw educational content, opaque receipts, or local paths.
