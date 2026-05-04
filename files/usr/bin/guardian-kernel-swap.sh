#!/bin/bash
set -euo pipefail

echo "🛡️ Guardian OS: CachyOS Kernel Installer"
echo "Replacing stock Fedora kernel with the performance-tuned CachyOS kernel..."
echo ""

rpm-ostree override replace \
  --experimental \
  --from repo=copr:copr.fedorainfracloud.org:bieszczaders:kernel-cachyos \
  kernel kernel-core kernel-modules kernel-modules-extra

echo ""
echo "✅ Kernel replacement staged successfully!"
echo "A reboot is required to boot into the CachyOS kernel."
