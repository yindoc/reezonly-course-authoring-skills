# Lesson Block catalog

Catalog — educational baseline, не authority: read/write availability каждого profile определяют actual `tools/list`, current schema, runtime policy и required opt-ins.

| Profile | Цель | Обычная tab | Dynamic availability |
| --- | --- | --- | --- |
| Text 8 | RichText explanation | Theory | Ordinary JSON only if schema permits |
| Test 7 / Poll 16 / Blanks 18 | Проверка знания | Testing | Current ordinary/specialized schema only |
| Practice 3 / CodeBox 25 | Контекстная практика | Practice | Current schema only; CodeBox Practice only |
| Document/Image/Audio/SCORM | Материалы | Materials/Practice | Specialized file flow |
| Video 5 | Демонстрация | Theory | Current rich-media schema only |
| Criterion 12 | Rubric | Practice | Conditional/specialized; no direct assumption |
| HTML 24 | Active interaction | Any tab by objective | Current rich-media schema only |
| AI Assistant 20 / IDE 21 | Experimental authoring | Practice | Conditional; no AI-generation implication |

После create/update всегда читать exact block content и проверять type/kind, parent, position и LMS normalization. Для assets подтверждать current create/stage/upload sequence, использовать only server-issued opaque ref и не передавать local paths, raw bytes или secret-bearing URLs. Для HTML24 прочитать active-html resource; для RichText — current rich-text resource.
