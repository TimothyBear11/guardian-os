Guardian OS: A Marchborn Masterpiece

Guardian OS is a personalized, immutable Fedora-based operating system built for high-performance software development and immersive, low-latency gaming. Utilizing the power of BlueBuild, it combines the ironclad reliability of atomic systems with a lightning-fast, modern Wayland compositor stack.
🛡️ Core Philosophy

Guardian OS is designed to be Lean & Mean. It focuses on a declarative, reproducible environment that prioritizes developer productivity, zero-overhead window management, and raw system responsiveness.

    Umbriel & Noctalia Stack: Powered by the ultra-responsive Umbriel Wayland compositor paired with the clean, modular Noctalia shell for peerless gaming performance and window handling.

    Marchborn Aesthetics: The system is styled around a custom palette featuring Aquamarine (#7FFFD4) and Bloodstone Red (#FF4D4D).

    Immutable Foundation: Built on Fedora’s atomic infrastructure to ensure a robust, reproducible, and "no-break" system state.

    Developer Ready: Pre-configured for Boot.dev students and Linux power users, featuring tools like Helix, Zed, Fish, and Kitty.

🚀 Key Features

    Advanced Scheduling (scx-scheds): Integrated support for modern schedulers via scx_bpfland, optimizing CPU thread prioritization and reducing task latency under heavy load.

    SecureBoot Compatible: Full custom signing infrastructure for SecureBoot compatibility using personal MOK keys.

    Custom Identity: Completely overhauled system branding, including a custom Plymouth boot splash and tailored Fastfetch ASCII art.

    Hardware Optimized: Fine-tuned for AMD Ryzen 7 processors, Radeon RX 6700 XT GPUs, and high-speed NVMe storage with direct GPU scanout and VRR support.

🛠️ Repository Structure

The repository follows the standard BlueBuild layout:

    files/ — Custom system-wide overrides, configs, and assets for Plyumouth, fonts, and window rules.

    recipes/recipe.yml — The primary declarative definition of the OS packages, repositories, and systemd services.

⚓ Installation & Updates

To rebase your current Fedora-based atomic system to Guardian OS:
Bash

rpm-ostree rebase ostree-unverified-registry:ghcr.io/timothybear11/guardian-os:latest

🤝 Special Thanks

A special thanks goes out to the BlueBuild community and the maintainers of Umbriel and Noctalia for providing the modular architecture and tooling that made this setup possible.
👤 Author

Timothy Brian Criddle (T-Bear)

Software Development Student @ Boot.dev

Note: All builds include automated provenance tracking and are managed via GitHub Actions for full auditability.
