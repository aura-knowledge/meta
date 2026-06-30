#!/usr/bin/env bash
# Install the aura-export skill and CLI onto the current system.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="aura-export"
SKILL_TARGET_DIR="${HOME}/.kimi-code/skills/${SKILL_NAME}"
USER_CONFIG_DIR="${HOME}/.config/${SKILL_NAME}"
DRY_RUN=false
FORCE=false

usage() {
    echo "Usage: $0 [--dry-run] [--force]"
    exit 1
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --force)
            FORCE=true
            shift
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

run() {
    if [[ "$DRY_RUN" == "true" ]]; then
        echo "[dry-run] $*"
    else
        "$@"
    fi
}

echo "Installing aura-export skill..."
echo "Source: ${SCRIPT_DIR}"
echo "Target: ${SKILL_TARGET_DIR}"

# 1. Ensure target directories exist.
run mkdir -p "$(dirname "${SKILL_TARGET_DIR}")"
run mkdir -p "${USER_CONFIG_DIR}"

# 2. Register skill in ~/.kimi-code/skills/ via symlink.
if [[ -L "${SKILL_TARGET_DIR}" ]]; then
    echo "Removing existing skill symlink at ${SKILL_TARGET_DIR}"
    run rm "${SKILL_TARGET_DIR}"
elif [[ -e "${SKILL_TARGET_DIR}" ]]; then
    if [[ "${FORCE}" == "true" ]]; then
        echo "Removing existing skill directory at ${SKILL_TARGET_DIR} because --force was provided"
        run rm -rf "${SKILL_TARGET_DIR}"
    else
        echo "Error: ${SKILL_TARGET_DIR} already exists and is not a symlink."
        echo "Move it aside manually or rerun with --force if it is safe to replace."
        exit 1
    fi
fi
run ln -s "${SCRIPT_DIR}" "${SKILL_TARGET_DIR}"

# 3. Install the Python package in editable mode.
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "Warning: Python not found. Please install Python 3.9+ and run 'pip install -e ${SCRIPT_DIR}'."
    exit 1
fi

echo "Installing Python package (editable mode)..."
run "${PYTHON}" -m pip install -q -e "${SCRIPT_DIR}"

# Try to make the CLI discoverable by symlinking into ~/.local/bin.
PIP_BIN_DIR="$(${PYTHON} -c 'import site, os; print(os.path.join(site.USER_BASE, "bin"))' 2>/dev/null || true)"
AURA_EXPORT_SCRIPT="${PIP_BIN_DIR}/aura-export"
LOCAL_BIN="${HOME}/.local/bin"
if [[ -x "${AURA_EXPORT_SCRIPT}" ]]; then
    run mkdir -p "${LOCAL_BIN}"
    if [[ ! -L "${LOCAL_BIN}/aura-export" && ! -e "${LOCAL_BIN}/aura-export" ]]; then
        echo "Linking aura-export into ${LOCAL_BIN}"
        run ln -s "${AURA_EXPORT_SCRIPT}" "${LOCAL_BIN}/aura-export"
    fi
    # Make the current shell session find it for the smoke test below.
    export PATH="${LOCAL_BIN}:${PATH}"
fi

# 4. Create a default user config if it does not exist.
USER_CONFIG="${USER_CONFIG_DIR}/config.yaml"
if [[ ! -f "${USER_CONFIG}" ]]; then
    echo "Creating default user config at ${USER_CONFIG}"
    run cp "${SCRIPT_DIR}/config.yaml" "${USER_CONFIG}"
else
    echo "User config already exists at ${USER_CONFIG}; skipping."
fi

# 5. Verify gh CLI.
if command -v gh &>/dev/null; then
    echo "GitHub CLI found: $(gh --version | head -n 1)"
    if gh auth status &>/dev/null; then
        echo "GitHub CLI is authenticated."
    else
        echo "Warning: GitHub CLI is not authenticated. Run 'gh auth login' before submitting issues."
    fi
else
    echo "Warning: GitHub CLI ('gh') not found. Install it from https://cli.github.com/ to submit issues."
fi

# 6. Smoke test.
echo "Running smoke test..."
if command -v aura-export &>/dev/null; then
    run aura-export --version
    run aura-export --help >/dev/null
else
    run "${PYTHON}" -m aura_export.cli --version
    run "${PYTHON}" -m aura_export.cli --help >/dev/null
fi

if [[ "$DRY_RUN" == "true" ]]; then
    echo ""
    echo "Dry-run complete. No changes were made."
else
    echo ""
    echo "aura-export skill installed successfully."
    echo ""
    if command -v aura-export &>/dev/null; then
        echo "The 'aura-export' command is available in this session."
    else
        echo "The CLI was installed but is not on your PATH yet."
        echo "Add the following to your shell profile (e.g. ~/.bashrc or ~/.zshrc):"
        echo "  export PATH=\"${LOCAL_BIN}:\$PATH\""
        echo "Then open a new shell, or run:"
        echo "  ${PYTHON} -m aura_export.cli --help"
    fi
    echo ""
    echo "Next steps:"
    echo "  1. Ensure 'gh auth login' is complete."
    echo "  2. Edit ${USER_CONFIG} if you need custom sensitive patterns or abstraction hints."
    echo "  3. From any project, run:"
    echo "       aura-export pipeline --from-file README.md --dry-run"
fi
