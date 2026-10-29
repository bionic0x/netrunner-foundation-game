> Current standalone project: [NETRUNNER FOUNDATION GAME](../../README.md). This document retains the consolidation context.

# NETRUNNER FOUNDATION — entrega de desarrollo Ante

**Fecha:** 2026-10-29 · **Estado:** v0.2, consolidación ampliada (27 fuentes). Prototipo offline conservado de v0.1.

## Ampliación v0.2

Se han añadido 18 fuentes al corpus previo de 9, con fingerprints SHA-256 en el manifiesto interno. Documentos nuevos: `strategy/netrunner-foundation/MASTER-BLUEPRINT.md` (síntesis integral), `SOURCE-CROSSWALK.md` (cobertura de las 27 fuentes), `CLAIM-ADJUDICATION.md` (conflictos y aritmética), `DECISION-RECORD.md` y `DESIGN-BRIEF.md` (handoff para Product Design en Work). La especificación no equivale a un prototipo de Work ni a validación empírica.

## Resultado

Consolidación de APEX COSMIC CHAOS ENGINE, CRASHOVERRIDE, HACK THE PLANET, WOLF PACK, ANTI-FRAGILE y LEGAL FORTRESS bajo el método de Ante. La doctrina de estrategia general sirve como marco de assurance y la arquitectura HTP Gate 0 del repositorio Ante como punto de partida para Solana y Arbitrum One.

**Artefactos ejecutables:** motor de reproducción de eventos simulados, fixture de seis casos, consola retro autocontenida y 23 casos de prueba (22 pasan; uno se omite sin el manifiesto privado). No acceden a Internet, no procesan fondos, no firman ni envían transacciones ni ejecutan acciones ofensivas.

**Artefactos de gobierno:** object/non-object, arquitectura, mapa de agentes, registro de 14 afirmaciones y conflictos, hoja de ruta con criterios de aceptación.

## Inicio

```bash
python3 examples/netrunner-foundation/replay.py examples/netrunner-foundation/fixture.json
python3 -m unittest discover -s examples/netrunner-foundation -p 'test_*.py' -v
```

Abre `examples/netrunner-foundation/index.html` en tu navegador para explorar el prototipo. Sus datos son sintéticos; el terminal solo admite `help`, `status`, `scan`, `claims` y `clear`.

## Estado de integración

Los ficheros forman la base independiente de `netrunner-foundation-game`; Ante es una referencia externa. El dossier no altera el `HOLD` de Gate 0, no es un sistema de producción y ningún PR o documentación concede autoridad operacional. La asignación de agentes es una planificación basada en perfiles reales del repositorio, **no** una certificación de que hayan emitido aprobaciones independientes.

## Documentos fuente

Los originales NO se redistribuyen en este ZIP; `source-manifest.internal.json` contiene los nombres y digests de los 27 documentos inventariados para controlar versiones. Si se coloca este paquete en un repositorio público, mantener privado el manifiesto interno salvo consentimiento explícito.
