# Changelog

All notable changes to the Vehicle Agent Protocol will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] – 2025-05-02

### Added

- Initial public release of the Vehicle Agent Protocol (VAP).
- Defined top-level message structure and metadata.
- Supported `message_type`: `event`, `query`, `response`.
- Reserved `message_type`: `sync_state`, `notification`.
- Supported `query.type`: `recommendation`, `data_request`, `fleet_status`, `vehicle_identity`, `proximity_alert`.
- JSON Schema file for message validation.
- Example messages: `event.json`, `query.json`, `response.json`.
- Full message specification (`docs/message-spec.md`).
- Python validator script: `validate_message.py`.

---

## [0.2.0] - 2025-05-16

### Added
- OneOf rule for message types to enforce structural consistency.
- Field validation: `confidence` must be between 0.0 and 1.0 in `event`.
- Pattern validation for `sender_id` and `receiver_id`.
- `context` field in `query` and `note` field in `response.data`.
- New examples in `message-spec.md` with complete top-level structure.

### Changed
- Documentation unified: all message examples now show complete structures.
- Allowed `additionalProperties: true` only in appropriate blocks (`event`, `response`, `metadata`...).
- Improved validation script with clearer error outputs.

### Compatibility
- Mostly backward compatible, but messages without `message_type` or with multiple content blocks will now be invalid.

---

## [Unreleased]

- Placeholder for upcoming changes.
