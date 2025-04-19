- **Purpose**: The `.nvmrc` file "pins" a specific Node.js version for a project, ensuring consistency across systems.
- **Location**: Place the `.nvmrc` file in the root of your project directory.
- **Creation Steps**:
  1. Open a text editor in the project root.
  2. Create a file named `.nvmrc` (with the leading dot).
  3. Add the desired Node.js version (e.g., `v18.16.0`)—check the official Node.js site for LTS or latest versions.
  4. Save and close the file.
- **Usage**: Run `$ fnm use --version-file-strategy local` to install and activate the version specified in `.nvmrc`.
- **Collaboration**: Commit the `.nvmrc` file to your project repository to ensure all collaborators use the same Node version.