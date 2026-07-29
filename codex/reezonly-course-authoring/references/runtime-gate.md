# Runtime gate

Перед созданием курса установить, что именно умеет текущий MCP, а не исходный репозиторий.

## Порядок authority

1. Вызвать `tools/list`. Его список и текущие input/output schemas имеют высший приоритет над resource, manifest, исходным кодом и сохранённым профилем.
2. Вызвать `lesson_authoring_get_runtime_info` с одним новым stable nonsecret `runId` и прочитать `authoringPolicy`, capability/feature statuses и identity metadata.
3. Прочитать текущий getting-started resource; перед RichText — `reezonly://authoring-guide/rich-text-v1`, перед Active HTML24 — `reezonly://authoring-guide/active-html-v1`.
4. Сопоставить нужный action с exact tool schema: required fields, unions, literals, opt-ins, confirmation и output shape.
5. Классифицировать action: standard, conditional, disabled, legacy или unavailable. Выполнять только standard либо явно разрешённый conditional action.

Static manifest и resources — ориентиры для подготовки, не runtime authority. При resource/manifest drift действовать только по actual tools/list schema. Не хардкодить tool counts, build IDs, profile availability или historical profile claim.

## Выбор курса и точные IDs

- Сначала определить intent. При явном intent создать новый Course проверить current create Course schema и создать его без `courseId`; не выполнять `lesson_authoring_list_courses` или иной discovery.
- Для ordinary existing Course: если пользователь уже выбрал `courseId`, подтвердить его fresh hierarchy/readback перед mutation. После явного выбора использовать только selected explicit IDs, которые принимает ordinary bearer/canonical schema. Наблюдение list не создаёт grant, selector, candidate или authority для write.
- Внешний existing Course не усыновлять и не переводить в ordinary bearer branch. Использовать его только через published `lesson_authoring_prepare_existing_course_authority` и его exact schema; returned authority остаётся server-issued и scope-bound.
- Для legacy/raw/publisher/cleanup/finalization передавать только exact server-issued references и prerequisites, которые требует current schema. Не добавлять их в ordinary canonical flow.

## Scope и transport

- Создать один `runId` на запуск и передавать его во все schema-required calls; не подменять ID между actor/session/run.
- Вызывать только MCP tools/resources. Не делать direct HTTP к LMS/service и не передавать bearer, token, cookie, local path или credential-bearing URL в tool arguments.
- Использовать current schema как единственный способ создать, обновить, переместить, удалить, reconcile или cleanup сущность.

## Authority ответа

| Класс                                                       | Разрешённое действие                                                                                                                                                                           |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Verified authoritative readback                             | Использовать exact ID/value только в его declared scope и только для следующего schema-authorized шага.                                                                                        |
| Verified no-op                                              | Считать состояние подтверждённым после required readback; не создавать duplicate.                                                                                                              |
| Candidate, observation, selector, ACK без required readback | Не считать owned и не использовать для mutation. Разрешён только явно опубликованный read/reconcile path.                                                                                      |
| Pre-dispatch `rejected` (`mutationDispatches:0`)            | Mutation не была отправлена. Исправить schema/input либо остановиться; не считать candidate/ACK authority.                                                                                     |
| Declared `rejected` after dispatch                          | Это terminal server outcome, не unknown. Не выдавать target как owned и не переотправлять вслепую.                                                                                             |
| `unknown` / transport ambiguity                             | Только здесь ожидать `retrySafe:false` и returned `nextAction`. Не resend; до любой новой mutation вызвать ровно все `nextAction.tools` в возвращённом порядке/shape. Не изобретать reconcile. |

## External `delete_once`

Ordinary owned cleanup и external `delete_once` — разные lanes. Не подменять external lane `lesson_authoring_preview_cleanup`, не смешивать `full_access` и `delete_once`, не усыновлять external Course и не конструировать selector/receipt/confirmation.

Если current catalog публикует `lesson_authoring_prepare_existing_course_authority`, выполнить external delete только в exact sequence: prepare preview with `mode:'delete_once'` → verbatim fresh server confirmation in the same actor/session/run → returned server selector → exactly one direct `lesson_authoring_execute_cleanup` → authoritative absence. При отсутствии published tool/schema остановиться до mutation.

После delete closed `lesson_authoring_get_course_content` ErrorEnvelope `NOT_FOUND` / `validation` / `rejected` / `retryable:false` with zero mutation — authoritative absence, не `unknown`; delete не повторять. Любой реальный unknown остаётся no-retry и требует exact returned `nextAction`.

## Canonical structural delete

Это отдельный conditional lane от ordinary owned `preview_cleanup` и external `delete_once`. Выполнять его только если actual `tools/list` публикует exact branch `lesson_authoring_delete_entity`; schema этой ветки — единственная authority. Для selected exact IDs перед dispatch получить fresh exact Course/parent chain и сверить current confirmation `action` и `entityId`. Сделать ровно один dispatch, затем подтвердить authoritative absence; `unknown` никогда не resend и разрешает только exact returned `nextAction`.

Course branch допускается только для selected `courseId` с literal `delete_course`. Не выполнять client cascade и не добавлять ownership/grant/selector. Подтверждать отсутствие только через current authoritative course-index read path. Module/Lesson/Page/Block допустимы только по их exact published branch и fresh matching parent chain; не угадывать fallback или совместимость между branch.
