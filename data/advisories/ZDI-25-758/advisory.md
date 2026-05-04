# ZDI-25-758: (Pwn2Own) QNAP TS-464 Samba Command Argument Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-758
- **ZDI-CAN:** ZDI-CAN-25612
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** YingMuo (@YingMuo), working with DEVCORE Internship Program.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-758/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of QNAP TS-464 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the provided username during authentication. The issue results from the lack of proper validation of a user-supplied string before using it to construct command line arguments. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of admin.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
