# Vehicle Agent Protocol – Message Specification

This document provides a detailed specification of the message structure used in the Vehicle Agent Protocol (VAP).  
It defines the required and optional fields, valid types, and how to extend the standard in a structured way.

---

## 1. 📦 Message Overview

All VAP messages are JSON objects with a standard set of top-level fields and an optional nested payload, depending on the message type.

---

## 2. 🔑 Top-Level Fields

| Key            | Type     | Required | Description                                                                 |
|----------------|----------|----------|-----------------------------------------------------------------------------|
| `message_id`   | string   | No       | Unique ID of the message (e.g., UUID or internal ref).                     |
| `timestamp`    | string   | Yes      | ISO 8601 format datetime when the message was generated.                   |
| `sender_id`    | string   | Yes      | Unique ID of the agent sending the message. Format: `vehicle:X`, `fleet:Y`, etc. |
| `receiver_id`  | string   | Yes      | ID of the target agent. Can be another vehicle, fleet, user, or system.    |
| `message_type` | string   | Yes      | One of: `event`, `query`, `response`, `sync_state`, `notification`.        |

---

## 3. 🧩 Message Type Definitions

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

| Field       | Type     | Required | Description                                       |
|-------------|----------|----------|---------------------------------------------------|
| `name`      | string   | Yes      | Event identifier (e.g., `brake_pad_wear`)         |
| `severity`  | string   | No       | `low`, `medium`, `high`                           |
| `location`  | string   | No       | Physical or logical location                      |
| `confidence`| number   | No       | Value from 0.0 to 1.0                             |

---

### 3.2 `query`

Used when an agent requests information, suggestions, or status.

```json
"query": {
  "type": "recommendation",
  "topic": "maintenance_shop",
  "location": "Zaragoza"
}
```

| Field      | Type     | Required | Description                                            |
|------------|----------|----------|--------------------------------------------------------|
| `type`     | string   | Yes      | `recommendation`, `data_request`, `fleet_status`, etc.|
| `topic`    | string   | Yes      | The subject of the query                              |
| `location` | string   | No       | Optional context                                       |

---

### 3.3 `response`

Used to return data in response to a query.

```json
"response": {
  "type": "recommendation",
  "data": {
    "name": "Bosch Service Zaragoza",
    "rating": 4.7,
    "last_used": "2024-12-10"
  }
}
```

| Field   | Type     | Required | Description                                  |
|---------|----------|----------|----------------------------------------------|
| `type`  | string   | Yes      | Must match the original query’s `type`       |
| `data`  | object   | Yes      | Payload with the response                    |

---

## 4. ℹ️ `metadata` Object

Provides contextual information about the sending agent.

```json
"metadata": {
  "vehicle_model": "Hyundai Ioniq 5",
  "agent_version": "1.2.4",
  "language": "en-US"
}
```

| Field           | Type     | Description                                |
|------------------|----------|--------------------------------------------|
| `vehicle_model`  | string   | e.g., `Toyota Corolla 2021`                |
| `agent_version`  | string   | e.g., `1.3.2`                              |
| `language`       | string   | Language code (e.g., `en-US`, `es-ES`)     |

---

### 4.1 🌍 About `language` and Multilingual Support

The `metadata.language` field specifies the preferred language for human-facing communication.

#### ✅ Keys and Values Stay in English

Even when `language` is `es-ES` or another non-English value, all **field names and enum values remain in English**. This ensures:

- Global interoperability
- Stable validation against schemas
- Avoiding ambiguity in parsing

| Element            | Language   | Example                       |
|--------------------|------------|-------------------------------|
| Keys / field names | English    | `event`, `query.topic`, etc.  |
| Enum values        | English    | `"brake_pad_wear"`, `"high"`  |
| Language metadata  | Any valid  | `"language": "es-ES"`         |
| Generated output   | User's lang| Response in Spanish, if needed|

---

## 5. 📚 Supported `query.type` Values

This table lists common supported query types. Extend freely.

| Type              | Description                                               |
|-------------------|-----------------------------------------------------------|
| `recommendation`  | Ask for suggestions based on experience                   |
| `data_request`    | Request technical/vehicle data                            |
| `fleet_status`    | Ask for status summary from a fleet agent                 |
| `vehicle_identity`| Ask for metadata about another vehicle                    |
| `proximity_alert` | Ask for nearby agents                                     |

---

## 6. ⚙️ Extending the Standard

- Use `custom_` prefixes for custom fields
- Ignore unknown fields by default (agents must be tolerant)
- Use [`schema/vap-message-schema.json`](../schema/vap-message-schema.json) for validation

---

## 7. 🧪 Message Validation

Use the included Python script:

```bash
python validate_message.py examples/query.json
```

---

## 8. 📬 Feedback & Contributions

The standard is open and community-driven.  
Open an issue or PR at: [https://github.com/autonalityAI/vehicle-agent-standard](https://github.com/autonalityAI/vehicle-agent-standard)
