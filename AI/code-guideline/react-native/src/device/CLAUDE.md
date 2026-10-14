# src/device - Native API Wrappers

Small typed functions that wrap a native API with side effects: secure storage, notifications, permissions, haptics, deep links, the camera and location. The rest of the app calls these functions and never imports the native module.

## Structure

```text
device/
  secure-storage.ts    get, set, and delete a secret, on top of expo-secure-store
  storage.ts           plain key-value storage for the persisted stores
  permissions.ts       ask for a permission and read its state
  notifications.ts     register for push, schedule and clear local notifications
  haptics.ts           the few feedback types the app uses
  linking.ts           open a URL, the phone dialer, the settings screen
```

- Group by native capability and name the file for what it handles. One capability per file. A file that needs "and" to describe it is two files.
- This is the web template's `utils/` split in two: `utils/` keeps the pure helpers, and this folder keeps what touches the device. A pure helper file must stay pure, so it can run with no mocks and no native runtime.

## Rules

- Expose what the app needs, not the whole native API. `getToken()` and `saveToken()`, not the secure store's options.
- Named exports. Type the arguments and the return value. Give every export a short doc comment.
- No React and no JSX. Anything that needs state or an effect is a hook in `hooks/` that calls these functions.
- An async function that can fail returns a typed result or throws a typed error. It never fails silently, and it never returns a half-valid value.
- Secure storage holds the token and any secret. Plain storage holds preferences and drafts, never a token or personal data.
- A permission is requested at the moment the user needs the feature, with a short reason shown first. Never request one at startup. When the user denies it, the feature explains why it needs it and offers to open the settings screen.
- Keep a platform difference inside the file. Where the two platforms differ a lot, ship a `.ios.ts` and `.android.ts` sibling instead of branching on `Platform.OS`. The caller never knows which one it got.
- A native module that is missing in Expo Go: say so in the doc comment. The user needs to know the app needs a dev build.

## Boundaries

- Follow the `device/` row in the import table in `src/CLAUDE.md`.
- Not here: a pure helper with no native API in it goes in `utils/`. A hook goes in `hooks/`. A module that only renders, such as `expo-image`, is used directly in a component.

## Existing Wrappers

Read this list before wrapping a native API - the app may already have one. When you add, rename, or remove a wrapper, or change what it exports, update this list in the same change.

| File | Exports | What they do |
|------|---------|--------------|
