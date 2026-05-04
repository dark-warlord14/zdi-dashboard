# ZDI-26-116: TensorFlow HDF5 Library Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-116
- **ZDI-CAN:** ZDI-CAN-25480
- **Date:** 2026-02-19
- **CVE:** CVE-2026-2492
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TensorFlow
- **Affected Products:** TensorFlow
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-116/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of TensorFlow. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of plugins. The application loads plugins from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

TensorFlow has issued an update to correct this vulnerability. More details can be found at: https://github.com/tensorflow/tensorflow/commit/46e7f7fb144fd11cf6d17c23dd47620328d77082

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2026-02-19 - Coordinated public release of advisory
- 2026-02-19 - Advisory Updated
