Guardian OS: A Marchborn Masterpiece

Guardian OS is a personalized, immutable Fedora-based operating system built for high-performance software development and immersive gaming. Utilizing the power of BlueBuild, it combines the reliability of atomic systems with the bleeding-edge optimizations of the CachyOS-LTO kernel.
🛡️ Core Philosophy

Guardian OS is designed to be Lean & Mean. It focuses on a declarative, reproducible environment that prioritizes developer productivity and system transparency.

    Custom Kernel: Powered by the CachyOS-LTO kernel for superior responsiveness and low-latency performance.

    Marchborn Aesthetics: The system is themed around an Aquamarine (#4DB8FF) and Bloodstone Red (#FF4D4D) palette.

    Immutable Foundation: Built on Fedora’s atomic infrastructure to ensure a "no-break" system state.

    Developer Ready: Pre-configured for Boot.dev students and Linux power users, featuring tools like Helix, Qtile, and Fish.

🚀 Key Features

    Advanced Scheduling: Integrated support for modern schedulers (EEVDF/BORE) with real-time tracking in Fastfetch.

    SecureBoot Signed: Full custom signing infrastructure for SecureBoot compatibility using personal MOK keys.

    Custom Identity: Completely overhauled system branding, including a custom Plymouth boot splash and Fastfetch ASCII art.

    Hardware Optimized: Specific optimizations for AMD RX 6700 XT and high-speed NVMe storage.

🛠️ Structure

The repository follows the BlueBuild standard with several custom modules:

    modules/custom-kernel: A specialized bash suite for kernel replacement and module signing.

    files/system: Custom system-wide overrides for logos, backgrounds, and terminal presets.

    recipes/recipe.yml: The primary declarative definition of the OS.

⚓ Installation & Updates

To rebase your current Fedora-based atomic system to Guardian OS:
Bash

rpm-ostree rebase ostree-unverified-registry:ghcr.io/timothybear11/guardian-os:latest

🤝 Special Thanks

A special thanks goes out to Origami for providing the architectural inspiration and the foundational module logic that made the migration to a custom signed kernel possible. This project stands on the shoulders of their excellent work in the BlueBuild community.

👤 Author

Timothy Brian Criddle (T-Bear)
Software Development Student @ Boot.dev

    Note: All builds include SynthID watermarking and are managed via GitHub Actions for full auditability.
