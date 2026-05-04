# ZDI-19-766: Apple macOS securityd Heap-based Buffer Overflow Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-766
- **ZDI-CAN:** ZDI-CAN-8360
- **Date:** 2019-08-27
- **CVE:** CVE-2019-8604
- **CVSS:** 9.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** fluoroacetate (@fluoroacetate)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-766/
## Vulnerability Details

This vulnerability allows remote attackers to escape the sandbox on affected installations of Apple Safari. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the securityd service. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210119

## Disclosure Timeline

- 2019-08-20 - Vulnerability reported to vendor
- 2019-08-27 - Coordinated public release of advisory
