# Active HTML 24

Перед authoring type 24 прочитать current MCP resource `reezonly://authoring-guide/active-html-v1`. Runtime schema и resource остаются authority.

- Active HTML — unrestricted HTML/CSS/JavaScript pass-through, не RichText; не добавлять local sanitizer, allowlist или invented URL restriction.
- Выбирать любую semantic tab по учебной цели. После create/update выполнять authoritative typed readback; unknown mutation не повторять.
- До первого HTML block определить shared visual system: tokens, palette, typography, spacing, radii, shadows и component patterns.
- Каждый block — self-contained fragment с одним semantic root; полностью дублировать base CSS, scope selectors внутри root и не зависеть от global/cross-block state.
- Использовать responsive desktop/mobile composition, semantic HTML, readable contrast и text-equivalent meaning. JavaScript применять только когда нужен learning interaction, сохраняя multi-instance safety.

Это authoring defaults, не content validator; request/session authority, no blind retry, authoritative readback, privacy audit и destructive cleanup остаются обязательными.
