# ZDI-26-198: (Pwn2Own) QNAP TS-453E malware_remover Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-198
- **ZDI-CAN:** ZDI-CAN-28324
- **Date:** 2026-03-16
- **CVE:** CVE-2025-11837
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-453E
- **Credit:** Chumy Tsai (github.com/Jimmy01240397) @ CyCraft Technology Intern
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-198/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of QNAP TS-453E devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the malware_remover.cgi endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute Python code. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-25-47

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
