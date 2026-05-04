# ZDI-24-474: (Pwn2Own) QNAP TS-464 Exposed Dangerous Method Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-474
- **ZDI-CAN:** ZDI-CAN-22495
- **Date:** 2024-05-19
- **CVE:** CVE-2024-32766
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Tri and Bien Pham (@bienpnn) from Team Orca of Sea Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-474/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of QNAP TS-464 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the privWizard.cgi endpoint. The issue results from an exposed dangerous method. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-24-09

## Disclosure Timeline

- 2023-11-15 - Vulnerability reported to vendor
- 2024-05-19 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
