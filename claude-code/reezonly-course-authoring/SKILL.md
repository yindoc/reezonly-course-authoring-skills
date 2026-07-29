---
name: reezonly-course-authoring
description: 'Проектировать и создавать качественные курсы в Reezonly LMS через MCP: от образовательного брифа и модульно-урочного blueprint до безопасной сборки, typed readback, QA, активации и публикации. Использовать при создании или переработке курса, модулей, уроков, семантических вкладок/страниц, Lesson Blocks и итоговой проверки в подключённом Reezonly LMS MCP.'
---

# Создание курсов Reezonly

Вести курс как последовательность **brief → blueprint → mutation → readback → QA → activation/publish**. Работать только через подключённые MCP-инструменты; не выполнять direct LMS/service HTTP. Credentials, bearer, cookies и local paths никогда не передавать в tool arguments и не писать в journal/audit/reports. Учебный content разрешён только в точных опубликованных mutation-полях current schema; raw учебный или block content не записывать в journal/audit/reports.

## Сначала установить текущую возможность

1. Вызвать `tools/list`; считать его и возвращённые input/output schemas единственным источником доступности. В Claude Code использовать точное fully-qualified MCP tool name из фактически доступного каталога для каждой операции: не выдумывать MCP server prefix и не считать operation доступной только потому, что она названа в этом skill.
2. Вызвать published runtime-info operation с одним новым nonsecret `runId`; сохранить его неизменным в том же actor/session/run. Прочитать getting-started и current resource для RichText/Active HTML.
3. Сверить authoringPolicy, capability/feature flags, resource status и exact schemas. Остановиться до mutation на missing/disabled/unsupported conditional capability или runtime drift; не хардкодить counts, build IDs, profile availability, IDs или live data.
4. При new Course использовать current create schema без `courseId`/discovery. Для ordinary existing Course использовать selected explicit IDs и fresh hierarchy. External existing Course не усыновлять: только published operation corresponding to `lesson_authoring_prepare_existing_course_authority` и its exact schema.

Прочитать [runtime-gate.md](references/runtime-gate.md) до первого вызова и при drift, partial/error или смене workflow branch.

## Спроектировать и собрать

Получить бриф, outcomes, ограничения, assessment evidence, materials и explicit activation/publication intent. Подготовить course plan и отдельный `SemanticLessonV1` с Theory, Testing, Practice, Materials для каждого lesson. Semantic validation вызывать только когда она нужна цели и current published schema совместима.

Перед первой mutation прочитать [authoring-pipeline.md](references/authoring-pipeline.md). При планировании прочитать [course-design.md](references/course-design.md); при выборе blocks — [block-catalog.md](references/block-catalog.md); перед HTML24 — [active-html.md](references/active-html.md). Каждая create/update/move/delete требует authoritative typed readback. Для ordinary bearer/canonical flow использовать только selected IDs и fresh hierarchy; observed/candidate/partial/ACK/selector не считать owned.

## Cleanup external Course

Ordinary owned cleanup и external `delete_once` — несовместимые lanes. Не substitute external lane `preview_cleanup`, не adopt external Course, не mix `full_access`/`delete_once` и не construct selector/receipt/confirmation.

Canonical structural delete — отдельный conditional lane, не cleanup substitute. Использовать его только если actual catalog публикует exact branch corresponding to `lesson_authoring_delete_entity`. Для selected exact IDs получить fresh exact Course/parent chain, сверить current confirmation `action`/`entityId`, сделать ровно один dispatch и read authoritative absence. Course допускает только selected `courseId` + literal `delete_course`: no client cascade, no ownership/grant/selector и absence только через current authoritative course-index read path. Module/Lesson/Page/Block — только exact published branch. `unknown` не resend; honour только exact returned `nextAction`.

Если available catalog публикует operation corresponding to `lesson_authoring_prepare_existing_course_authority`, выполнить строго: prepare preview `delete_once` → verbatim fresh server confirmation same actor/session/run → returned server selector → exactly one direct operation corresponding to `lesson_authoring_execute_cleanup` → authoritative absence. Closed zero-mutation `NOT_FOUND`/`validation`/`rejected`/`retryable:false` после operation corresponding to `lesson_authoring_get_course_content` — authoritative absence, не unknown и не повод повторять delete. Genuine unknown не resend: honour exact returned `nextAction` в returned order/shape before any new mutation.

## Завершить

Выполнить compatible QA и canonical readbacks. Активировать lessons последними только при explicit intent; publish — только при explicit intent, exact runtime gate и independent required readbacks. Report selected scope, verified outcomes, skipped capabilities, warnings и safe next actions; не включать credentials, raw content, local paths, opaque receipts или candidates как ownership.
