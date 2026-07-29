---
name: reezonly-course-authoring
description: 'Проектировать и создавать качественные курсы в Reezonly LMS через MCP: от образовательного брифа и модульно-урочного blueprint до безопасной сборки, typed readback, QA, активации и публикации. Использовать при создании или переработке курса, модулей, уроков, семантических вкладок/страниц, Lesson Blocks и итоговой проверки в подключённом Reezonly LMS MCP.'
---

# Создание курсов Reezonly

Вести курс как последовательность **brief → blueprint → mutation → readback → QA → activation/publish**. Работать только через подключённые MCP-инструменты; не выполнять direct LMS/service HTTP. Credentials, bearer, cookies и local paths никогда не передавать в tool arguments и не писать в journal/audit/reports. Учебный content разрешён только в точных опубликованных mutation-полях current schema; raw учебный или block content не записывать в journal/audit/reports.

## Сначала установить текущую возможность

1. Вызвать `tools/list`; считать его и возвращённые input/output schemas единственным источником доступности. При расхождении tools/list/schema выигрывает у resource, manifest и исходного кода.
2. Вызвать `lesson_authoring_get_runtime_info` с одним новым непустым, не секретным `runId`; сохранить этот `runId` неизменным для всего запуска.
3. Прочитать `reezonly://authoring-guide/getting-started-v1`; при любом RichText прочитать `reezonly://authoring-guide/rich-text-v1`, при Active HTML type 24 — `reezonly://authoring-guide/active-html-v1`.
4. Сверить `authoringPolicy`, feature/capability flags, contract/runtime identity, resource status и schemas. Не выводить build IDs/counts как обещание доступности.
5. Остановиться до mutation, если обязательный tool, resource или schema отсутствует, отключён, условен без нужного opt-in либо противоречит runtime. Объяснить, какой безопасный ручной или последующий шаг нужен.
6. Сначала разделить intent курса. При явном intent создать новый Course проверить current create Course schema и создать его без `courseId` и без discovery. Не выполнять `lesson_authoring_list_courses` для new-course intent. Для ordinary existing Course использовать только selected explicit IDs и fresh hierarchy. Внешний existing Course не усыновлять: переходить к нему только через опубликованный `lesson_authoring_prepare_existing_course_authority` и только по его exact schema.

Прочитать [runtime-gate.md](references/runtime-gate.md) до первого вызова и всякий раз при source/runtime drift, partial/error или смене ветки workflow.

## Спроектировать до записи

Получить бриф: аудитория и стартовый уровень, измеримые outcomes, ограничения времени/формата, критерии качества, нужные материалы и явное намерение активировать/публиковать. Превратить его в course content plan: модули, уроки, outcomes, evidence, practice/assessment и вкладки/страницы.

Прочитать [course-design.md](references/course-design.md) при составлении или ревизии программы. Прочитать [block-catalog.md](references/block-catalog.md) при выборе, заполнении или размещении блоков. При Active HTML прочитать [active-html.md](references/active-html.md) до authoring первого блока. Catalog — только educational baseline: read/write availability каждого profile определяют actual tools/list и current schema.

Для каждого lesson отдельно сформировать `SemanticLessonV1` с ровно четырьмя semantic tabs. Вызывать `lesson_authoring_validate_blueprint` до writes, только когда semantic QA действительно нужна цели пользователя и current published schema поддерживает совместимый validator; иначе продолжать по exact schema и content plan. Любой вызванный invalid/partial result останавливает writes. Исправлять blueprint, а не компенсировать педагогические ошибки случайными последующими блоками; course content plan не является lesson blueprint.

## Собрать курс контролируемыми шагами

Прочитать [authoring-pipeline.md](references/authoring-pipeline.md) перед первой mutation. Выполнять порядок из него, сверяя точный schema каждого tool непосредственно перед вызовом. Создавать draft Course, обновлять metadata по одному полю, затем modules/lessons/pages/blocks; после каждой mutation немедленно выполнять authoritative typed readback.

Использовать canonical reads: `lesson_authoring_get_course_content`, `lesson_authoring_get_page_content` и `lesson_authoring_read_block_content`; structure reads использовать для hierarchy, placement и порядка. Для ordinary bearer/canonical операций authority — выбранные явные IDs и свежая hierarchy, ровно в форме current schema: не добавлять ownership/grant/selector/candidate. Legacy/raw/publisher/cleanup/finalization требуют только exact server-issued prerequisites, опубликованные current schema. Для Testing применять только текущую schema; canonical branch, если он опубликован, использует `courseId + lessonId`.

Создавать или переиспользовать page по текущей read hierarchy: default page переиспользовать, если schema/runtime подтверждает его однозначность; `createAdditional:true` передавать только для явно обоснованной второй или последующей страницы. Не создавать pages «на всякий случай».

## Сохранять authority и безопасность

- Считать только verified authoritative IDs, readback values и exact server-issued references authority для следующей mutation; переносить их дословно и только в том же actor/session/run scope.
- Не считать observed, candidate, partial, selector или ACK без required readback owned и не использовать их как mutation authority.
- Различать pre-dispatch rejection, declared rejection после dispatch и unknown. Только `unknown` несёт `retrySafe:false` и returned `nextAction`: не resend и до любой новой mutation выполнить ровно `nextAction.tools`. Не придумывать recovery.
- Не менять невыбранные/чужие сущности, не записывать raw name, description, HTML или block content в audit/journal summary и не выполнять destructive cleanup без exact scope и required confirmation.
- Подтверждать create/update/move/delete актуальным authoritative readback: existence + parent + type + intended field/order либо authoritative absence для delete.

## Очистка external Course

Разделять ordinary owned cleanup и external `delete_once` как несовместимые lanes. Ordinary owned flow использует только опубликованный `preview_cleanup` flow. Для external Course не вызывать и не подменять им `preview_cleanup`, не запрашивать/не смешивать `full_access` с `delete_once` и не считать Course своим.

Canonical structural delete — отдельный conditional lane, не ordinary cleanup и не external `delete_once`. Использовать его только если actual `tools/list` публикует точную ветку `lesson_authoring_delete_entity`. Для exact selected IDs сначала получить fresh exact Course/parent chain и сверить current confirmation `action` и `entityId`; затем сделать ровно один dispatch и подтвердить authoritative absence. Для Course допустима только literal `delete_course` ветка selected `courseId`: без client cascade, ownership/grant/selector и только с current authoritative course-index absence read. Module, Lesson, Page и Block удалять только через их exact опубликованные ветки. Любой `unknown` не resend: выполнить только exact returned `nextAction`.

Для published `lesson_authoring_prepare_existing_course_authority` выполнить строго: `mode:'delete_once'` prepare preview → передать дословно fresh server confirmation в том же actor/session/run → взять только returned server selector → ровно один direct `lesson_authoring_execute_cleanup` → authoritative absence readback. Не конструировать selector, receipt или confirmation вручную. При unavailable tool/schema остановиться до delete.

После этого delete `lesson_authoring_get_course_content` может вернуть closed `NOT_FOUND` / `validation` / `rejected` / `retryable:false` с zero mutation. Это authoritative absence, не `unknown` и не повод повторять delete. Любой настоящий `unknown` не повторять: выполнить ровно returned `nextAction` и honour its exact order/shape before any new mutation.

## Завершить и отчитаться

После blocks выполнить typed page/course readbacks. Для ordinary draft QA предпочесть опубликованный совместимый `lesson_authoring_validate_canonical_course(mode:'current_draft')`; semantic lesson validation выполнять, только когда её публикует compatible schema и она нужна цели. Строгий `lesson_authoring_validate_course` — только точный gate finalization перед явно запрошенными activation/publish, с current schema-required authority, warning dispositions и product gates. Исправлять только подтверждённые gaps и снова читать изменённую сущность.

Активировать уроки последними и только после успешной QA. Публиковать курс только при явном намерении пользователя, текущем exact gate/confirmation schema и независимом course-tree + course-index readback. Cleanup вести отдельной стадией и только по exact current lane; не угадывать legacy/new delete compatibility.

Вернуть краткий user-facing audit: scope (course/modules/lessons), verified outcomes/readbacks, skipped/conditional capabilities, warning/partial status, activation/publication state и следующие безопасные действия. Не включать credentials, raw учебный контент, локальные пути, opaque secrets или кандидаты как ownership.
