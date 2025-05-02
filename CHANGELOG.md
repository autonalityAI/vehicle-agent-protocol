# Changelog

All notable changes to the Vehicle Agent Standard will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] – 2025-05-02

### Added

- Initial public release of the Vehicle Agent Standard (VAS).
- Defined top-level message structure and metadata.
- Supported `message_type`: `event`, `query`, `response`.
- Reserved `message_type`: `sync_state`, `notification`.
- Supported `query.type`: `recommendation`, `data_request`, `fleet_status`, `vehicle_identity`, `proximity_alert`.
- JSON Schema file for message validation.
- Example messages: `event.json`, `query.json`, `response.json`.
- Full message specification (`docs/message-spec.md`).
- Python validator script: `validate_message.py`.

---

## [Unreleased]

- Placeholder for upcoming changes.
