# Preferred Libraries

A list of libraries to use when a project needs one. Each is well tested and was checked against its competitors before we picked it.

Use these by default. If a project needs something else, confirm it first.

## React Libraries

1. [**Zustand**](https://zustand.docs.pmnd.rs/learn/getting-started/introduction) - Local state management. We prefer it over full Redux because it is simpler and faster to write.
2. [**Phosphor Icons**](https://phosphoricons.com/) - System icons.
3. [**es-toolkit**](https://es-toolkit.dev/) - Collection, object, and math helpers. Replaces Lodash. Prefer it over hand-written code.
4. [**date-fns**](https://date-fns.org/) - Dates.
5. [**TanStack Query**](https://tanstack.com/query/latest) - Server data: fetching, caching, retries.
6. [**TanStack Router**](https://tanstack.com/router/latest) - Routing for a new standalone React app, with code-based routes. Existing apps may keep React Router.
7. [**React Hook Form**](https://react-hook-form.com/) with [**Zod**](https://zod.dev/) - Forms and validation, when the UI library has no form package of its own.
8. [**react-i18next**](https://react.i18next.com/) - Translations, only when a project needs them.

The UI library (for example Mantine or MUI) is chosen per project.

## React Native Libraries

React Native apps are built on Expo. Install with `pnpm exec expo install <package>` so the version matches the SDK, and ask before adding any native library, because it can force a rebuild and block Expo Go.

These React libraries apply as they are: Zustand, es-toolkit, date-fns, TanStack Query, React Hook Form with Zod, and react-i18next. The rest differ:

1. [**Expo Router**](https://docs.expo.dev/router/introduction/) - File-based routing. It replaces TanStack Router.
2. [**Expo SecureStore**](https://docs.expo.dev/versions/latest/sdk/securestore/) (`expo-secure-store`) - Tokens and other secrets. Never plain async storage.
3. [**Phosphor Icons**](https://github.com/duongdev/phosphor-react-native) (`phosphor-react-native`) - System icons. It needs `react-native-svg`.
4. [**Expo Localization**](https://docs.expo.dev/versions/latest/sdk/localization/) (`expo-localization`) - The device language, used with react-i18next when a project needs translations.
5. [**Expo Image**](https://docs.expo.dev/versions/latest/sdk/image/) (`expo-image`) - Remote images, with caching.

The styling system (StyleSheet with a theme file, NativeWind, or a UI kit) is chosen per project.

## Laravel Libraries

Before the list, one company is worth knowing: [Spatie](https://spatie.be/). They build a large number of [packages](https://spatie.be/open-source/packages) and publish their own [guidelines](https://spatie.be/guidelines). Check their packages first before looking elsewhere.

1. [**Laravel Data**](https://spatie.be/docs/laravel-data/v4/introduction) - DTOs (data transfer objects) when building an API from Laravel. Use it for the objects that carry request input into services and service results back out to API responses, instead of hand-written DTO classes.
2. [**Laravel One Time Passwords**](https://github.com/spatie/laravel-one-time-passwords) (`spatie/laravel-one-time-passwords`) - One-time passwords (OTP), for example for passwordless login or verification codes.
