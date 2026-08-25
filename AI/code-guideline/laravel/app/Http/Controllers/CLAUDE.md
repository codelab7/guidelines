# app/Http/Controllers - Writing Controllers

- Name a controller after the plural resource: `PostsController`, `ContactsController`.
- Stick to the standard method set:
  - `index` - list resources.
  - `create` - show the create form (merge into `index` for a small UI).
  - `store` - create a resource.
  - `single` - show one resource.
  - `edit` - show the edit form.
  - `update` - update a resource.
  - `destroy` - delete a resource.
- An action that doesn't fit that set gets its own controller. Don't invent extra method names.
- Keep each method short. It reads input, calls one or two collaborators, returns a response.
- Break a long method into private methods on the same controller. A private method:
  - Takes its inputs as arguments and returns a value.
  - Never reads `request()` or `$this->request`.
- Return whatever the project uses: an Inertia response, a Blade view, a redirect, or a JSON
  resource. Stay consistent with the controllers already in the project.
- After a successful POST, the default is a redirect back with a flash message:

  ```php
  return redirect()->back()->with('status', 'Contact created.');
  ```

  Use a different flow only when the user asks for one.

## Never in a Controller

- Business logic or a domain workflow. That's a service.
- Complex branching over domain state.
- Logic reused by another controller, a command, or a job.
- Validation rules. Those live in a `FormRequest`.
