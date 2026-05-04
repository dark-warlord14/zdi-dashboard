# ZDI-24-473: (Pwn2Own) QNAP TS-464 Authentication Service Improper Certificate Validation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-473
- **ZDI-CAN:** ZDI-CAN-22378
- **Date:** 2024-05-19
- **CVE:** CVE-2024-27124
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** @vcslab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-473/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to compromise the integrity of downloaded information on affected installations of QNAP TS-464 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authentication functionality, which operates over HTTPS. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-24-09

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-05-19 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
