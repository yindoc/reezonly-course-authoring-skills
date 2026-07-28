# Authoring pipeline

## Runtime gate and blueprint

1. Выполнить runtime gate: `tools/list` → `lesson_authoring_get_runtime_info` → required resources → exact schemas.
2. Для new Course создать без `courseId`/discovery. Для ordinary existing Course после explicit choice использовать selected IDs и fresh hierarchy. External existing Course не усыновлять: использовать только published `lesson_authoring_prepare_existing_course_authority` по current exact schema.
3. Создать stable nonsecret `runId`; не менять его в запуске.
4. Подготовить один course content plan и отдельный `SemanticLessonV1` для каждого lesson; каждый lesson blueprint обязан содержать ровно Theory, Testing, Practice и Materials.
5. Вызывать `lesson_authoring_validate_blueprint` до writes только когда semantic QA действительно нужна цели пользователя и current published schema публикует совместимый validator.

## Draft hierarchy, blocks и readback

1. Создать draft Course, затем сразу прочитать hierarchy/content; продолжать только с verified authoritative ID.
2. Обновлять metadata, создавать modules/lessons/pages и blocks только по current schema. После каждой mutation подтверждать parent, position, kind/status и intended normalized fields authoritative typed readback.
3. Переиспользовать однозначную default page; `createAdditional:true` передавать только когда schema и blueprint обосновывают вторую/последующую страницу.
4. Выбирать tool/type по current schema, а не static catalog. Для blocks читать `lesson_authoring_read_block_content`; читать page/course content для parent/order.
5. Выполнять specialized/file/experimental flows только при current tool, resource, opt-in и exact schema. Не передавать local path/raw bytes; server-issued `fileRef` не применять как RichText image source.

## QA, activation и publication

1. После заполнения урока выполнить typed canonical page/course readbacks.
2. Для ordinary draft QA предпочесть published compatible `lesson_authoring_validate_canonical_course(mode:'current_draft')`; semantic validator вызывать только когда он нужен цели и published schema совместима.
3. Строгий `lesson_authoring_validate_course`, activation и publish — только при explicit finalization intent и exact current gate. Активировать lessons последними; publication требует independent course-tree + course-index readback.

## Envelopes и cleanup

Verified success/no-op требует required authoritative readback. Pre-dispatch rejection не отправляла mutation; declared rejection terminal и не доказывает ownership. `unknown`, timeout или ambiguous ACK не resend: до любой новой mutation выполнить ровно returned `nextAction.tools` без invented reconcile. Candidate/observed/selector остаются non-owned.

Cleanup — отдельный user-authorized stage. Ordinary owned cleanup использует только published `preview_cleanup` lane. External `delete_once` при published `lesson_authoring_prepare_existing_course_authority`: prepare preview → verbatim fresh server confirmation in the same actor/session/run → returned server selector → exactly one direct `lesson_authoring_execute_cleanup` → authoritative absence. Не substitute `preview_cleanup`, не adopt Course, не mix `full_access`/`delete_once` и не construct selector/receipt/confirmation. Closed zero-mutation `NOT_FOUND`/`validation`/`rejected`/`retryable:false` после `lesson_authoring_get_course_content` — authoritative absence, не unknown и не permission повторить delete.
