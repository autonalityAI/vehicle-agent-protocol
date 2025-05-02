---

## 🔍 Message Key Reference

This section provides a detailed explanation of the keys used in the message structure defined by the Vehicle Agent Standard (VAS).

---

### 🔑 Common Top-Level Keys

| Key           | Type     | Required | Description                                                                 |
|---------------|----------|----------|-----------------------------------------------------------------------------|
| `message_id`  | string   | No       | Unique ID of the message (UUID or short ID). Useful for logging/tracking. |
| `timestamp`   | string   | Yes      | ISO 8601 timestamp of when the message was generated.                      |
| `sender_id`   | string   | Yes      | Unique agent ID that sends the message. Format: `vehicle:X`, `fleet:Y`, etc. |
| `receiver_id` | string   | Yes      | Target agent ID. Can be another vehicle, a fleet, a user, or the system.   |
| `message_type`| string   | Yes      | Type of the message: `event`, `query`, `response`, etc.                    |

---

### 🧩 `event` Object

Used when an agent reports a detected condition or signal.

| Key         | Type     | Required | Description                                                |
|-------------|----------|----------|------------------------------------------------------------|
| `name`      | string   | Yes      | Identifier of the event (e.g., `engine_noise_detected`)    |
| `severity`  | string   | No       | Event importance: `low`, `medium`, `high`                  |
| `location`  | string   | No       | Where the event occurred (e.g., `engine_bay`)              |
| `confidence`| number   | No       | Confidence score (0–1) about the accuracy of the event     |

---

### ❓ `query` Object

Used when an agent wants to ask another agent for a recommendation, data or state.

| Key         | Type     | Required | Description                                                      |
|-------------|----------|----------|------------------------------------------------------------------|
| `type`      | string   | Yes      | Purpose of the query (`recommendation`, `data_request`, etc.)    |
| `topic`     | string   | Yes      | What the query is about (`maintenance_shop`, `battery_status`)   |
| `location`  | string   | No       | Optional: geographic scope for the query                         |

---

### ✅ `response` Object

Used to respond to a `query`.

| Key     | Type     | Required | Description                                  |
|---------|----------|----------|----------------------------------------------|
| `type`  | string   | Yes      | Matches the type from the original query     |
| `data`  | object   | Yes      | The actual response content                  |

---

### ℹ️ `metadata` Object

Optional object to describe the context in which the message was generated.

| Key             | Type     | Description                          |
|------------------|----------|--------------------------------------|
| `vehicle_model`  | string   | e.g., `Hyundai Ioniq 5 2023`         |
| `agent_version`  | string   | e.g., `1.2.4`                        |
| `language`       | string   | ISO language code (e.g., `en-US`)    |

---

## 📚 Supported Query Types (Proposal)

You are encouraged to extend this list depending on your implementation.

| Query Type         | Description                                                |
|--------------------|------------------------------------------------------------|
| `recommendation`   | Ask for advice based on another agent's experience         |
| `data_request`     | Request specific metrics or state from another agent       |
| `vehicle_identity` | Query another agent to identify itself                     |
| `proximity_alert`  | Ask which vehicles are nearby                              |
| `fleet_status`     | Request summary from a fleet agent                         |

---

## 🛠️ Extensibility

All keys not marked as "required" are optional and may be omitted.  
Custom fields can be added in `metadata` or in nested structures if needed — ideally using prefixes (e.g., `custom_`) to avoid conflicts.

