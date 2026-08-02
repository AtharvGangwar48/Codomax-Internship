import shutil
import subprocess
import sys


def check_python():
    """Checks the running Python version."""
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"✅ Python is installed. Version: {version}")
    print(f"   Executable path: {sys.executable}")
    return True


def check_git():
    """Checks if Git is installed and available in the system PATH."""
    if not shutil.which("git"):
        print("❌ Git is NOT installed or not added to PATH.")
        return False

    try:
        version = (
            subprocess.check_output(["git", "--version"])
            .decode("utf-8")
            .strip()
        )
        print(f"✅ Git is available. ({version})")
        return True
    except Exception as e:
        print(f"❌ Failed to run Git: {e}")
        return False


def check_github_setup():
    """Checks Git configuration for GitHub or the GitHub CLI."""
    github_ready = False

    # 1. Check if GitHub CLI (gh) is installed and authenticated
    if shutil.which("gh"):
        try:
            status = subprocess.check_output(
                ["gh", "auth", "status"], stderr=subprocess.STDOUT
            ).decode("utf-8")
            if "Logged in to github.com" in status:
                print("✅ GitHub CLI is installed and authenticated.")
                github_ready = True
        except subprocess.CalledProcessError:
            pass

    # 2. Fallback: Check local Git config for a GitHub email/user
    if not github_ready:
        try:
            email = (
                subprocess.check_output(
                    ["git", "config", "--global", "user.email"]
                )
                .decode("utf-8")
                .strip()
            )
            name = (
                subprocess.check_output(
                    ["git", "config", "--global", "user.name"]
                )
                .decode("utf-8")
                .strip()
            )

            if email and name:
                print(
                    f"✅ GitHub is configured via Git global settings ({name} <{email}>)."
                )
                github_ready = True
            else:
                print(
                    "❌ GitHub is NOT configured. Set your global name and email in Git."
                )
        except Exception:
            print("❌ GitHub is NOT configured. Git global configurations missing.")

    return github_ready


def check_vscode():
    """Checks if the VS Code 'code' command line interface is available."""
    if shutil.which("code"):
        try:
            version = (
                subprocess.check_output(["code", "--version"])
                .decode("utf-8")
                .splitlines()[0]
            )
            print(f"✅ VS Code command line interface is available. Version: {version}")
            return True
        except Exception as e:
            print(f"❌ VS Code command found but failed to respond: {e}")
            return False
    else:
        print("❌ VS Code command line interface ('code') is NOT available in PATH.")
        print("   💡 Fix for macOS: Open VS Code, press Cmd+Shift+P, and run 'Shell Command: Install \"code\" command in PATH'.")
        print("   💡 Fix for Windows: Reinstall VS Code and ensure 'Add to PATH' is checked.")
        return False


def run_env_check():
    print("=" * 60)
    print("DEVELOPMENT ENVIRONMENT CHECK")
    print("=" * 60)

    checks = [check_python(), check_git(), check_github_setup(), check_vscode()]

    print("=" * 60)
    if all(checks):
        print("🎉 All systems go! Your environment is completely set up.")
    else:
        print("⚠️  Some components are missing or misconfigured. See errors above.")
    print("=" * 60)


if __name__ == "__main__":
    run_env_check()
