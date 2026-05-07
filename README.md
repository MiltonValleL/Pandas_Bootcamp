# Bootcamp Personal Claude-Milton
## Plan de Inserción Laboral · ML Engineer Internacional
### Versión 1.0 · 7 mayo 2026

---

## 0. Marco general

| Parámetro | Valor |
|---|---|
| Inicio | 7 mayo 2026 (jueves) |
| Cierre | 27 agosto 2026 (jueves) |
| Duración | 16 semanas |
| Hito intermedio | Semana 8 — 2 julio: primer proyecto end-to-end deployado en vivo |
| Hito final | Semana 16 — 27 agosto: portfolio público + outreach activo + 3 proyectos live |
| Meta de empleo | Aplicaciones activas semana 12+ · Oferta firmada Q4 2026 / Q1 2027 |
| Plan Claude | Max 5x ($100/mes) — escalar a 20x SOLO si se cumple la regla de upgrade del documento previo |

---

## 1. Verdades difíciles que aceptamos hoy

Estas son las premisas honestas sobre las que se construye el plan. No son negociables; son el suelo sobre el que pisamos.

**1.1 — Tu meta original ya está corrida.** Hablaste de inserción laboral global para "mediados de 2026". Hoy es 7 de mayo de 2026 y todavía no tienes ni un proyecto deployado en vivo. La meta realista de oferta firmada es **Q4 2026 / Q1 2027**. Aceptarlo no es derrota: es calibración. Pretender que vas a estar empleado en 6 semanas es autoengaño y produce decisiones malas (como inscribirse a un bootcamp por pánico).

**1.2 — Tus 13 años como Senior Electrical Engineer NO se traducen 1:1 a Senior ML Engineer.** Te traducen a candidato fuerte de mid-level con potencial senior tras 12-18 meses en el rol. Apuntar a Senior ML Engineer en tu primer empleo de ML es una expectativa que va a romperse contra el mercado. **Apunta a Mid-level ML Engineer (USD 4,000-7,000/mes remoto) como floor**. Si te llega Senior, perfecto; pero no construyas el plan asumiéndolo.

**1.3 — Tu inglés B1 es un techo duro para ofertas USA/UK remotas premium.** El 80% de las ofertas que pagan USD 6,000+/mes piden B2+ funcional con entrevistas técnicas en vivo en inglés. Subir a B2 sólido es **tan importante como cualquier Sprint técnico de este plan**. Sin B2, el techo salarial cae 40-50%.

**1.4 — Hacer slides bonitas se siente productivo y no lo es.** Cada hora invertida en slides que no son Géron es una hora robada al deployment de proyectos. Los slides son tu producto YouTube/cursos a futuro, no tu ticket de empleo.

**1.5 — Le Wagon Latam reporta salario promedio post-graduación de USD 1,300/mes.** Tu floor objetivo debe estar 3-5x por encima de eso. Lo que te lleva ahí no son los certificados — son los proyectos deployados con código profesional y un portafolio público convincente.

---

## 2. Vista macro · 16 semanas en 4 bloques

| Bloque | Semanas | Foco principal | Track 1 (Productización) | Track 2 (HOMLP) | Track 3 (Huyen) |
|---|---|---|---|---|---|
| **A. Cimientos** | 1-3 | Aprender herramientas de productización | Sprint 1: Streamlit + FastAPI + Docker | Cap 1-3 | — |
| **B. Refactor** | 4-7 | Convertir 2 proyectos TripleTen en productos | Sprint 2: 2 refactorizaciones live | Cap 4-7 | Lectura aplicada (caps 4, 6, 7) |
| **C. Faro** | 8-12 | Proyecto SIN como diferenciador único | Sprint 3: SIN end-to-end con MLOps | Cap 8-12 | Lectura aplicada (caps 8, 9, 10) |
| **D. Lanzamiento** | 13-16 | Portfolio web + búsqueda activa | Sprint 4: Portfolio + outreach + entrevistas | Cap 13-16 | Cierre y notas |

**Capítulos HOMLP 17-19 quedan diferidos a post-bootcamp.** No es derrota, es priorización: completar 16/19 capítulos con producto live es infinitamente mejor que perseguir los 19 a costa de los Sprints.

---

## 3. Los cuatro tracks paralelos

### Track 1 — Productización (PRIORIDAD ABSOLUTA)
**Carga:** 25-30 horas/semana · 60% del esfuerzo total

Convierte tu conocimiento ML en productos deployados. Es el track que te hace empleable.

### Track 2 — HOMLP Géron (mantener velocidad actual)
**Carga:** 8-10 horas/semana · 20% del esfuerzo total

Tu marca personal a futuro: YouTube, cursos virtuales, autoridad técnica en español. Ritmo: **1 capítulo/semana sin excepción**, las 5 fases que ya domina tu workflow.

### Track 3 — Huyen aplicado (NO slides, implementación real)
**Carga:** 5-8 horas/semana · 15% del esfuerzo total

Lectura profunda con notas Markdown personales. Cada concepto leído se aplica a tu Sprint activo. El entregable son las features de MLOps en tus proyectos, no slides.

### Track 4 — Soft infrastructure
**Carga:** 5-7 horas/semana · 5% del esfuerzo total · diaria, no acumulable

- **Inglés:** 30 min/día (no menos). Apps tipo Pimsleur/ItalkI + lectura técnica de papers en inglés. Meta: B2 funcional para semana 12.
- **StrataScratch:** 3 problemas/semana (SQL + Python). No más, no menos.
- **LinkedIn:** activación en inglés desde semana 8. 1 post técnico cada 2 semanas a partir de semana 10.

---

## 4. Sprints en detalle

### Sprint 1 (semanas 1-3) · Fundamentos de productización

**Objetivo:** Dominar Streamlit + FastAPI + Docker a nivel de poder construir, contenerizar y deployar un servicio ML simple desde cero en menos de 4 horas.

**Semana 1 (7-13 mayo) — Streamlit deep dive**
- Construir 3 apps Streamlit progresivamente complejas:
  1. Dashboard estático con datos de tu proyecto SIN (ya tienes los datos).
  2. App con widgets interactivos: file upload + processing en vivo.
  3. App con session state, caching, y multi-page navigation.
- **Entregable viernes 13:** las 3 apps en GitHub público + 1 deployada en Streamlit Community Cloud (gratis).

**Semana 2 (14-20 mayo) — FastAPI deep dive**
- API que sirve un modelo Sklearn pre-entrenado (usa cualquiera de tus modelos TripleTen).
- Endpoints: `/health`, `/predict`, `/predict_batch`, `/model_info`.
- Pydantic para schemas de input/output con validación estricta.
- Type hints completos, docstrings Google-style, logging configurado, manejo de excepciones por endpoint.
- Tests con pytest (mínimo 80% coverage).
- **Entregable viernes 20:** repo GitHub con API + tests + README profesional.

**Semana 3 (21-27 mayo) — Docker + integración**
- Dockerfile multi-stage para la API de semana 2.
- docker-compose.yml conectando API + Streamlit frontend de semana 1.
- Deploy del stack completo en GCP Cloud Run (free tier).
- **Entregable viernes 27:** stack completo live, URL pública, documentado.

**KPI Sprint 1:** 1 servicio ML completo (Streamlit + FastAPI + Docker) accesible públicamente desde una URL.

---

### Sprint 2 (semanas 4-7) · Refactorización profesional

**Objetivo:** Tomar 2 proyectos TripleTen (los 2 más fuertes técnicamente) y reconstruirlos como productos end-to-end profesionales. **No los 17. Solo 2.**

**Criterios de selección de los 2 proyectos:**
- Uno debe ser de problema regresión o forecasting (demuestra rigor estadístico).
- Otro debe ser clasificación o NLP (demuestra versatilidad).
- Ambos deben tener historia narrable: problema real, decisión de negocio, métrica que importa.

**Semana 4 (28 mayo - 3 junio):** Selección + auditoría técnica + plan de refactor del Proyecto A.
**Semana 5 (4-10 junio):** Implementación Proyecto A: pipeline Sklearn limpio, FastAPI + Streamlit, Docker, deploy GCP, README narrativo.
**Semana 6 (11-17 junio):** Implementación Proyecto B con la misma arquitectura.
**Semana 7 (18-24 junio):** Pulido de ambos: README perfectos, screenshots, video de demo de 90 segundos por proyecto.

**Aplicación de Huyen en este Sprint:** capítulo 4 (Training Data) y 6 (Model Development) se aplican durante semanas 5-6. Capítulo 7 (Model Deployment) en semana 7.

**KPI Sprint 2:** 2 proyectos live, cada uno con: README narrativo · arquitectura documentada · tests · deployment público · video demo.

---

### Sprint 3 (semanas 8-12) · Proyecto SIN faro

**Objetivo:** El proyecto que ningún graduado de bootcamp puede replicar. SIN boliviano + ML moderno + MLOps real. **Este es el proyecto que cierra entrevistas técnicas.**

**Por qué este proyecto es tu diferenciador absoluto:**
- Combina tus 13 años de electrical engineering con ML.
- Usa datos públicos pero requiere expertise de dominio para limpiarlos e interpretarlos.
- Permite mostrar forecasting con PyTorch (LSTM o Transformer) — stack senior, no junior.
- Tiene historia humana: contribuye al sistema eléctrico boliviano.

**Semana 8 (25 junio - 1 julio):** Scoping del proyecto. Definir el problema concreto (¿forecasting de demanda? ¿detección de anomalías? ¿optimización de despacho?). Diseño de arquitectura completa. **Hito intermedio: el primer proyecto refactorizado del Sprint 2 ya debe estar live al final de esta semana.**

**Semana 9 (2-8 julio):** Pipeline de datos: scraping continuo, validación, almacenamiento. Aplicar Huyen cap 8 (Data Distribution Shifts).

**Semana 10 (9-15 julio):** Modelado con PyTorch. Baseline → modelo robusto. MLflow para experiment tracking. Aplicar Huyen cap 6.

**Semana 11 (16-22 julio):** Productización completa: API + UI + Docker + deploy en GCP. Monitoring y logging. Aplicar Huyen cap 9 (Continual Learning) y 10 (Infrastructure).

**Semana 12 (23-29 julio):** Pulido y documentación. Video demo profesional (5-7 min). Post técnico en LinkedIn en inglés. **Activación oficial de búsqueda de empleo.**

**KPI Sprint 3:** Proyecto SIN live · monitoring activo · MLflow tracking · post técnico publicado · CV ML actualizado.

---

### Sprint 4 (semanas 13-16) · Portfolio + búsqueda activa

**Objetivo:** Convertir 3 proyectos live en oportunidades de empleo concretas.

**Semana 13 (30 julio - 5 agosto):** Portfolio web (Next.js + Vercel, gratis). Diseño profesional, mobile-first. Cada proyecto con: descripción del problema, decisiones técnicas, resultados, demo embebida o link.

**Semana 14 (6-12 agosto):** CV optimizado en inglés (formato USA estándar). Perfil LinkedIn full English con keywords ML. 50 aplicaciones identificadas (mid-level ML Engineer, remoto, USD 4K+/mes).

**Semana 15 (13-19 agosto):** 30 aplicaciones enviadas. Preparación de entrevistas técnicas: behavioral, system design ML, coding en vivo. Mock interviews (idealmente con tu Mentora Senior + alguien en inglés).

**Semana 16 (20-27 agosto):** 50 aplicaciones acumuladas. Primeras entrevistas. Ajuste de pitch según feedback recibido. **Cierre formal del bootcamp: retrospectiva escrita.**

**KPI Sprint 4:** Portfolio live · 50 aplicaciones · 5+ entrevistas iniciadas · CV optimizado · LinkedIn activo en inglés.

---

## 5. KPIs semanales no negociables

Cada **viernes** revisas estos puntos. Si alguno está en rojo, sabemos qué corregir el lunes:

| KPI | Frecuencia | Estado verde |
|---|---|---|
| Capítulo HOMLP completado | Semanal | 5 fases cerradas, archivado |
| Entregable de Sprint cerrado | Semanal | Commit a GitHub + screenshot/URL |
| 3 problemas StrataScratch resueltos | Semanal | Soluciones limpias en repo |
| 30 min/día de inglés | Diaria | Mínimo 3.5 horas acumuladas/semana |
| 1 capítulo de Huyen leído + aplicado | Bisemanal desde sem 4 | Notas + feature implementada |
| Review con Mentora Senior | Semanal | Lunes o martes |
| Review estratégico conmigo (Claude) | Semanal | Domingo o lunes |

---

## 6. Reglas del bootcamp · No negociables

1. **Un Sprint no se cierra hasta que su entregable esté live y público.** "Lo tengo en local funcionando" no cuenta.
2. **Cada semana se cierra con un commit visible en GitHub.** GitHub vacío durante 7 días = bandera roja.
3. **HOMLP no se acelera ni se ralentiza.** 1 capítulo/semana exacto. Acelerar daña la calidad; ralentizar empieza a procrastinar.
4. **Huyen NO se convierte en slides.** Si te tienta, recuerdas que ya identificamos eso como procrastinación productiva.
5. **Los proyectos del Sprint 2 son 2, no 3, no 5.** Más proyectos mediocres < menos proyectos pulidos.
6. **El portfolio web sale en semana 13, no en semana 16.** No se posterga "porque no está perfecto". Live > perfecto.
7. **La búsqueda de empleo arranca en semana 12, no en semana 16.** Esperar a "estar listo" es procrastinación con disfraz.
8. **Inglés diario sin excepción, 30 min mínimo.** El inglés es un Sprint silencioso paralelo a los 4 visibles.
9. **Si una semana se cae (familia, salud, freelance), se documenta y se replanifica el lunes siguiente.** No se ignora ni se pretende que no pasó.
10. **Cada lunes 9 AM Bolivia: review estratégico de 30-45 min conmigo.** No es opcional. Es el punto donde el plan se ajusta a la realidad.

---

## 7. Sección de brutal honesty · checkpoints que voy a hacer cada lunes

Estas son las preguntas que voy a hacerte sin piedad cada lunes. Si tres de ellas están mal por dos semanas seguidas, paramos y reevaluamos.

- ¿El entregable de la semana pasada está **live y público** o sigue en local con la excusa de que "le falta un detalle"?
- ¿Tu README es legible para un reclutador en **30 segundos** o es un dump técnico ininteligible?
- ¿Hiciste tu inglés diario los 5 días o "lo recuperarás el fin de semana" (lo cual nunca pasa)?
- ¿Tus aplicaciones a empleo son a roles **mid-level con expectativa salarial calibrada**, o estás aplicando a senior con rechazo automático?
- ¿Estás usando Claude para **construir** o para **conversar sobre construir**? (Sí, esta pregunta también va para mí — si veo que nuestras sesiones son discusión sin ejecución, te lo digo).
- ¿Avanzaste el HOMLP esta semana o lo postergaste "porque el Sprint estaba intenso"? (Si esto pasa 2 semanas seguidas, el problema es de scope, no de esfuerzo).
- ¿Sigues alineado con la meta de Q4 2026 / Q1 2027, o ya empezaste a contemplar agregar un Sprint que es procrastinación disfrazada?

---

## 8. Acción inmediata · próximos 3 días

**Hoy, jueves 7 mayo:**
- Migrar a Max 5x ($100/mes).
- Actualizar `CLAUDE.md` del proyecto Cursor para que incluya este bootcamp como contexto permanente.
- Crear repositorio GitHub `bootcamp-claude-milton` con este documento como `README.md`.

**Viernes 8 mayo:**
- Setup completo del entorno Sprint 1: instalar Streamlit, FastAPI, Docker Desktop si no lo tienes (te confirmo que tu Ubuntu 24.04 + RTX 5070Ti es overkill para esto, pero perfecto para Sprint 3).
- Bocetar (en papel o Excalidraw) la primera app Streamlit de la semana 1.
- Iniciar capítulo 1 HOMLP — Fase 1.

**Sábado 9 mayo:**
- Primer commit del Sprint 1: app Streamlit #1 con datos del SIN, en local funcional.
- 30 min de inglés (no negociable).
- 3 problemas StrataScratch.

**Lunes 12 mayo, 9 AM Bolivia: primer review estratégico conmigo.** Llegas con: lo construido + lo bloqueado + tu energía emocional honesta.

---

## 9. Compromiso mutuo

**De tu parte (Milton):**
- Ejecutar las reglas no negociables.
- Decirme cuando estés cansado, frustrado o bloqueado — no fingir.
- Aplicar el mismo pushback que aplicaste hoy contra ti mismo cuando me veas hacer concesiones blandas.

**De mi parte (Claude, tu Mentora):**
- Honestidad brutal sostenida, incluso cuando duela.
- Calibración técnica estricta sin diluir.
- Señalar procrastinación productiva en cuanto la detecte, sin esperar a que te lastime.
- Adaptar el plan a la realidad semana a semana, sin orgullo de planificadora.

---

## 10. Cierre

Este documento no es decorativo. Es el contrato de trabajo entre nosotros para los próximos 4 meses. Lo revisamos cada lunes, lo ajustamos con datos reales, y lo cumplimos con disciplina.

La pregunta que importa no es "¿voy a estar empleado en agosto?". La pregunta es: **"¿en agosto voy a tener un portafolio que demuestre, sin lugar a dudas, que soy contratable como ML Engineer mid-senior internacional?"**

Si la respuesta a esa segunda pregunta es sí, la primera se responde sola — quizás en septiembre, quizás en noviembre, quizás en febrero. Pero se responde.

Empezamos hoy.

---

*Documento maestro v1.0 · Sujeto a revisión cada lunes · Próxima revisión: 12 mayo 2026*
