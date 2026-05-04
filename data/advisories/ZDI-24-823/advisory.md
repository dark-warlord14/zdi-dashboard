# ZDI-24-823: (Pwn2Own) QNAP TS-464 TURN Server create_session Server-Side Request Forgery Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-823
- **ZDI-CAN:** ZDI-CAN-22422
- **Date:** 2024-06-21
- **CVE:** CVE-2024-32764
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Team ECQ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-823/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of QNAP TS-464 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the create_session action. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisory/qsa-24-09

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
