# Runtime gate

`tools/list` и current input/output schemas — runtime authority над source, manifest и saved guidance. В Claude Code для каждой операции использовать exact fully-qualified name из actual MCP catalog; не invent server prefix. Вызвать published runtime-info operation с stable nonsecret `runId`, прочитать required resources, сверить exact schema, opt-ins, confirmations и output shape. Missing, disabled или drifted capability останавливает writes.

Для ordinary existing Course требуются selected explicit IDs и fresh hierarchy; list/candidate/ACK/selector остаются non-owned. External existing Course не adopt: только published operation corresponding to `lesson_authoring_prepare_existing_course_authority`. Передавать server-issued references verbatim и только в same actor/session/run.

`unknown`/ambiguous outcome не retry: выполнить ровно returned `nextAction.tools` в returned order/shape. Pre-dispatch rejection не dispatches mutation; declared post-dispatch rejection terminal и не даёт ownership.

External `delete_once`: ordinary owned `preview_cleanup` lane не substitute. Prepare preview → verbatim fresh confirmation same actor/session/run → returned server selector → exactly one direct operation corresponding to `lesson_authoring_execute_cleanup` → authoritative absence. Не mix `full_access`/`delete_once` и не construct selector/receipt/confirmation. Post-delete closed zero-mutation `NOT_FOUND`/`validation`/`rejected`/`retryable:false` is authoritative absence, not unknown; do not repeat delete.

## Canonical structural delete

Это отдельный conditional lane от ordinary owned `preview_cleanup` и external `delete_once`. Выполнять его только если actual `tools/list` публикует exact branch `lesson_authoring_delete_entity`; schema этой ветки — единственная authority. Для selected exact IDs перед dispatch получить fresh exact Course/parent chain и сверить current confirmation `action` и `entityId`. Сделать ровно один dispatch, затем подтвердить authoritative absence; `unknown` никогда не resend и разрешает только exact returned `nextAction`.

Course branch допускается только для selected `courseId` с literal `delete_course`. Не выполнять client cascade и не добавлять ownership/grant/selector. Подтверждать отсутствие только через current authoritative course-index read path. Module/Lesson/Page/Block допустимы только по их exact published branch и fresh matching parent chain; не угадывать fallback или совместимость между branch.
