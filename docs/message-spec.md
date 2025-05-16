# Vehicle Agent Protocol – Message Specification (v2)

This document provides a detailed specification of the message structure used in the Vehicle Agent Protocol (VAP). It defines the required and optional fields, valid types, and how to extend the standard in a structured way.

---

## 1. 📦 Message Overview

All VAP messages are JSON objects with a standard set of top-level fields and an optional nested payload, depending on the `message_type`.

---

## 2. 🔑 Top-Level Fields

| Key             | Type     | Required | Description                                                                 |
|----------------|----------|----------|-----------------------------------------------------------------------------|
| `message_id`   | string   | No       | Unique ID of the message (e.g., UUID or internal ref).                     |
| `timestamp`    | string   | Yes      | ISO 8601 format datetime when the message was generated.                   |
| `sender_id`    | string   | Yes      | Unique ID of the agent sending the message. Format: `vehicle:X`, `fleet:Y`, etc. |
| `receiver_id`  | string   | Yes      | ID of the target agent. Can be another vehicle, fleet, user, or system.    |
| `message_type` | string   | Yes      | One of: `event`, `query`, `response`, `sync_state`, `notification`.        |

---

## 3. 🪠 Message Type Definitions

Each message type must include one nested object with a name matching the `message_type`. This keeps the protocol clean, extensible, and predictable.

### 3.1 `event`

Used when an agent reports a detected condition or signal.

```json
"event": {
  "name": "engine_noise_detected",
  "severity": "medium",
  "location": "engine_bay",
  "confidence": 0.87
}
```

### 3.2 `query`

Used when an agent requests information, suggestions, or status.

```json
"query": {
  "type": "recommendation",
  "topic": "maintenance_shop",
  "location": "Zaragoza",
  "context": "Clutch slipping when going uphill. Owner says it smells like toast."
}
```

### 3.3 `response`

Used to return data in response to a query.

```json
"response": {
  "type": "recommendation",
  "data": {
    "name": "Taller Clutch&Go",
    "rating": 4.9,
    "last_used": "2025-04-08",
    "note": "Fast, honest, didn’t treat my owner like a wallet on wheels."
  }
}
```

### 3.4 `sync_state`

Used to share current state or status between a vehicle and a system (e.g., fleet backend or nearby peers).

```json
"sync_state": {
  "fuel_level": 36,
  "battery_health": "good",
  "mileage": 48720,
  "next_inspection_due": "2025-06-30"
}
```

Fields are flexible, but must be simple key-value pairs.

### 3.5 `notification`

Used for global messages or non-targeted alerts.

```json
"notification": {
  "type": "recall_advisory",
  "topic": "brake_hose_inspection",
  "models_affected": ["CUPRA Leon 2021-2022", "Golf 8 2020-2021"],
  "source": "official_bulletin_132/2025",
  "note": "Early signs detected by 17 agents. Recommended to inspect before summer."
}
```

---

## 4. ℹ️ `metadata` Object

Provides contextual information about the sending agent.

```json
"metadata": {
  "vehicle_model": "Hyundai Ioniq 5",
  "agent_version": "1.2.4",
  "language": "es-ES"
}
```

| Field           | Type     | Description                                |
|----------------|----------|--------------------------------------------|
| `vehicle_model`| string   | e.g., `Toyota Corolla 2021`                |
| `agent_version`| string   | e.g., `1.3.2`                              |
| `language`     | string   | Language code (e.g., `en-US`, `es-ES`)     |

---

## 5. 📃 Supported `query.type` Values

| Type              | Description                                               |
|-------------------|-----------------------------------------------------------|
| `recommendation`  | Ask for suggestions based on experience                   |
| `data_request`    | Request technical/vehicle data                            |
| `fleet_status`    | Ask for status summary from a fleet agent                 |
| `vehicle_identity`| Ask for metadata about another vehicle                    |
| `proximity_alert` | Ask for nearby agents                                     |

You are encouraged to propose more types via GitHub Issues or Pull Requests.

---

## 6. ⚙️ Extending the Standard

- Use `custom_` prefixes for any new fields.
- Agents must ignore unknown fields to remain forward-compatible.
- Validate messages using the official schema: [`schema/vap-message-schema.json`](../schema/vap-message-schema.json)

---

## 7. 🤮 Message Validation

Use the provided Python script to validate example messages:

```bash
python validate_message.py examples/query.json
```

---

## 8. 📩 Feedback & Contributions

Submit ideas, issues, or PRs at: [https://github.com/autonalityAI/vehicle-agent-protocol](https://github.com/autonalityAI/vehicle-agent-protocol)

---

## 9. 📄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of releases and updates to the standard.
