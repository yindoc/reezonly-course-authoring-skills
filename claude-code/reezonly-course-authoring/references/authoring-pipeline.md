# Authoring pipeline

1. Start with runtime gate and a stable `runId`; create a new Course without `courseId`/discovery or use ordinary selected IDs plus fresh hierarchy. External existing Course only uses prepared server authority.
2. Create a draft hierarchy by exact schema. After every metadata, module, lesson, page, block, asset or Testing mutation, obtain required authoritative typed readback and verify parent, type, position and normalized intended fields.
3. Reuse an unambiguous default page; `createAdditional:true` only when current schema and blueprint justify another page. Choose block/profile by current schema, not static catalog. Assets use only server-issued opaque references; never local path/raw bytes.
4. Run compatible draft QA and canonical reads. Strict validation, activation and publication occur only with explicit finalization intent and exact runtime gates; activate lessons last.
5. Candidate/observation/selector remain non-owned. Genuine unknown has no resend: exact returned `nextAction` only.

Cleanup is separately user-authorized. Ordinary owned cleanup is only `preview_cleanup`. External `delete_once` is only prepare preview → verbatim confirmation same actor/session/run → returned selector → exactly one direct execute cleanup → authoritative absence; no adoption, forged receipt, `full_access` mixing, or repeat after closed post-delete `NOT_FOUND`.

Canonical structural delete is a separate conditional lane, never a cleanup substitute. Use it only when the actual catalog publishes the exact `lesson_authoring_delete_entity` branch. For selected exact IDs, fresh-read the exact Course/parent chain, match current confirmation `action`/`entityId`, dispatch exactly once, then read authoritative absence. Course allows only selected `courseId` + literal `delete_course`: no client cascade, ownership/grant/selector, and absence only through the current authoritative course-index read path. Module/Lesson/Page/Block use only their exact published branch. `unknown` has no resend: honour only the exact returned `nextAction`.
