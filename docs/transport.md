# Transport Layer for Vehicle Agent Standard (VAS)
*Work in Progress — Not part of v0.1.0 specification*

---

## 🚧 Status

This document outlines potential directions for message transport in VAS.  
It is **not yet part of the official protocol**, but serves as a discussion basis for future versions.

---

## 🧭 Purpose

While the VAS specification defines the **structure** and **semantics** of messages exchanged between agents, it does **not prescribe how those messages are transmitted**.

This transport layer discussion addresses that question:  
> "How do agents discover each other and exchange messages across networks?"

---

## 📦 Transport Options (Candidates)

### 1. **MQTT (Message Queue Telemetry Transport)**

- Pub/Sub model (agents publish and subscribe to topics)
- Lightweight and scalable
- Ideal for vehicle-to-cloud and agent-to-agent communication
- Could use topic structure like:  
  ```
  vas/event/vehicle:XYZ123
  vas/query/fleet:RENTACAR_1
  ```

### 2. **WebSocket**

- Persistent bi-directional connection (e.g. for apps or dashboards)
- Lower latency than REST
- Good for agent-to-server or frontend-to-agent communication

### 3. **REST API**

- Simple and ubiquitous
- Suitable for async message submission (`POST /vas/messages`)
- Useful as a fallback or ingestion gateway

### 4. **Federated architecture (future idea)**

- Agents communicate across different servers, but all speak VAS
- Similar to ActivityPub, Matrix or Fediverse
- Would require identity, authentication, and relays

---

## 🧩 Implementation-Defined Transport

For now, **each implementation decides how to transport VAS messages**.  
Your system can choose:

- Fully local (in-memory, IPC)
- Centralized (via backend API)
- Public (via shared MQTT or WebSocket broker)

We recommend including in your implementation guide:
- Transport method used
- Topic or route structure
- Security/authentication model

---

## 📘 Future Direction

In a future version (e.g. `v0.2.0` or `v1.0.0`), this document may be promoted to define:
- A standard MQTT topic hierarchy
- WebSocket message framing
- Guidelines for message routing and discovery

---

## 💬 Contribute

Do you use MQTT, REST or WebSockets to implement VAS?  
Open an issue or pull request to help shape the future of this layer.

