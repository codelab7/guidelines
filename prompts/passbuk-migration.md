# Passbuk Context

### Overview

Passbuk is a double-entry accounting system that helps users track their day-to-day finances, accounting, billing, sales reporting, etc.

### History

* This software was built on Laravel + InertiaJS + React. InertiaJS connects the Laravel backend with the React frontend and provides Ziggy routes, data passing, form handling, etc.
	* You can check the `dev` branch for the original structure.
* But we have decided to split the frontend and backend for various reasons.
  * The frontend will be a pure React app.
  * The backend will provide an API to power the frontend.

## Current Status

In the current branch (`connect-front-with-api`), we have built multiple things that are explained below:

* We have moved the Laravel setup into the `/api` folder.
* We created a new React app in the `/portal` folder.
* We also have an `/admin` folder, which is a React project for the admin panel, and it is working fine.
* Since this is a big migration, we also switched from **Tailwind + Shadcn** to **Mantine UI**, and we are very satisfied with it.
* We also copied all the page UIs and layouts and made adjustments to refresh the design.
* We were using WorkOS, but it logs users out very often. So we decided to move away from it and use plain Auth.
* We are releasing this as a beta version on a separate subdomain while keeping the old version working as it is.
* So the existing Laravel setup should continue to work as it is and also serve the frontend with the API.
* Since we have fully migrated to React, we have restructured the folder structure.
* We have also created some APIs in Laravel that provide some data. But this was an AI-driven task, so I haven't tested it yet.
* We used mock data to show data in `portal` while working on the design.

#### Terminology

* **Laravel** or **API** - The Laravel setup in the `/api` folder, which serves the existing software and provides the API for the new version.
* **Portal** - The React frontend setup in the `/portal` folder.

## The Task

The core goal of this task is to connect Portal and API and make everything work so that we are ready to launch the beta version for users to test the new version of Passbuk.

1. **The Auth**: We will continue to use WorkOS for the existing setup. But for the beta version, we will allow users to log in with our own Laravel auth system. So the setup should support the older version as it is and the new version with our own auth system.
   * We will ask users to reset their password when they start using the beta version.
   * Laravel should support both WorkOS for the existing Inertia setup and built-in auth for API access.
   * I prefer the same-domain Sanctum authorization, but if that is not possible, we can use a bearer token.
2. **The Frontend Pages**: Also make sure that all pages from Laravel's setup are available in Portal. If any pages are missing, create them in Portal and maintain an equivalent design that matches the theme.
3. **API & DTOs** - We can use the `TanStack Query` library for this.
   1. For the API, instead of making APIs that serve pages, I would like to detach the API from the pages. Basically, instead of calling an API for each page action, it should be resource-based, like one endpoint per DTO with multiple request types and other related functionality.
   2. (*Optional*) Also, to keep the API fast and lightweight and reduce the risk of N+1 queries, we can pass references and IDs for repeatable data (like the account object in our accounting software) and use local state to attach that data.
   3. We want to connect the API with Portal.
4. **Local State Management** - We use Zustand for this. This is not mandatory, but use it if needed. Zustand is the way to go.
5. **Invoice Print** - I am not 100% sure how we should handle this, but we need to manage the printing pages that we built using Laravel's Blade views. These are public pages that can also be shared through URLs.
6. **File Uploading** - Make sure that asset fetching and uploading works correctly.

Make sure that you don't miss anything. You can ask me if you need my help with any decisions.