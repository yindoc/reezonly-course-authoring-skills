# Проектирование курса

Превращать бриф в последовательность доказуемых учебных действий, а не в перечень тем.

1. Зафиксировать аудиторию, входные навыки, рабочий контекст, длительность и ограничения устройства/доступа.
2. Сформулировать 3–7 измеримых outcomes и критерии наблюдаемого действия.
3. Сгруппировать outcomes в модули и разложить их на lessons: контекст → модель/пример → практика → проверка/feedback → перенос в работу.
4. Для каждого outcome предусмотреть evidence: practice artefact, Test/Blanks/Poll signal, Criterion/rubric или CodeBox result.
5. Спроектировать минимальную page map; не заменять пробелы дизайна пустыми страницами.

## Четыре semantic tabs

| Tab       | Назначение                                     |
| --------- | ---------------------------------------------- |
| Theory    | Объяснение, worked example, decision rule      |
| Testing   | Retrieval, диагностическая проверка, feedback  |
| Practice  | Выполнение в контексте, artefact, разбор       |
| Materials | Job aids и источники для повторного применения |

Использовать baseline page каждой tab; additional page создавать только при смене учебной цели, activity или cognitive mode. Связывать title, practice и assessment с одним главным outcome урока. Использовать ясные headings, logical order, descriptive links, alt text и text alternative для media.

RichText — current bounded LMS editor HTML pass-through без локального tag/attribute allowlist; inline image возможен только через existing Text type 8 `content.text`. Active HTML24 — отдельный unrestricted HTML/CSS/JS profile: прочитать current resource, выбрать tab по учебной цели и не подменять им RichText. Plan хранить в рабочем контексте пользователя, не в audit/journal; `SemanticLessonV1` валидировать только при нужде пользователя и compatible published schema.
