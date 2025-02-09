# Pokémon Card Storage Web App Documentation

## Overview
This document outlines the design of a Pokémon Card Storage Web Application. It includes diagrams and specifications for user roles, core features, and system architecture.

---

## User Roles

### Users:
- View all Pokémon cards
- Submit new cards (pending admin approval)
- Assemble and manage a deck (add/remove cards)

### Admins:
- Approve user-submitted cards
- Add new cards
- Modify and delete existing cards

---

## Core Features
- **Card Database**: Store Pokémon cards with relevant stats
- **Deck Management**: Users can create, edit, and remove decks
- **Role-Based Permissions**: Admins can manage cards, users can only submit or assemble decks
- **Approval System**: New cards require admin approval before being visible

---

## Entity-Relationship Diagram (ERD)
```mermaid
erDiagram
    USER {
        int id
        string username
        string email
    }
    ADMIN {
        int id
        string username
        string email
    }
    CARD {
        int id
        string name
        string type
        string rarity
        int attack
        int defense
    }
    DECK {
        int id
        string name
    }
    
    USER ||--o{ DECK : owns
    DECK ||--o{ CARD : contains
    ADMIN ||--|{ CARD : manages
```

---

## User Flow Diagram
```mermaid
flowchart TD
    A[User] -->|View Cards| B[Card Database]
    A -->|Submit New Card| C[Pending Approval]
    C -->|Admin Approves| B
    C -->|Admin Rejects| D[Rejected Cards]
    A -->|Create/Edit Deck| E[Deck Management]
    A -->|Add Cards to Deck| F[Deck with Cards]
    Admin -->|Approve/Reject Submissions| C
    Admin -->|Modify/Delete Cards| B
```

---

## System Architecture Diagram
```mermaid
graph LR
    User -->|Requests| UI
    UI -->|API Calls| Backend
    Backend -->|Database Queries| Database
    Admin -->|Access Admin Dashboard| UI
    Backend -->|Manages Permissions| AuthService
```

---

## API Endpoints Table
| Endpoint | Method | Description | Access |
|----------|--------|-------------|---------|
| `/cards` | GET | Fetch all cards | All Users |
| `/cards` | POST | Submit a new card | Users (Approval Required) |
| `/cards/{id}` | PUT | Modify an existing card | Admins |
| `/cards/{id}` | DELETE | Remove a card | Admins |
| `/decks` | GET | Fetch all decks | Users |
| `/decks` | POST | Create a new deck | Users |
| `/decks/{id}` | PUT | Edit a deck | Users |
| `/decks/{id}` | DELETE | Delete a deck | Users |

---

## Optional Artifacts

### Database Schema
```mermaid
erDiagram
    USER ||--o{ DECK : owns
    DECK ||--o{ CARD : contains
    ADMIN ||--|{ CARD : manages
```

### User Stories
- **As a user**, I want to browse Pokémon cards so I can find the best ones for my deck.
- **As a user**, I want to create and manage decks so I can prepare for matches.
- **As an admin**, I want to approve submitted cards to maintain the quality of the database.

### Requirements List
#### Need to Have
- Pokémon card database with relevant stats
- User-submitted card approval system
- Deck management feature

#### Nice to Have
- Card search and filtering by type
- User profile customization
- Deck-sharing feature

---

This document serves as a foundational design plan for a Pokémon Card Storage Web App.
