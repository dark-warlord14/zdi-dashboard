# ZDI-24-472: (Pwn2Own) QNAP TS-464 Netmgr Endpoint CRLF Injection Arbitrary Configuration Update Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-472
- **ZDI-CAN:** ZDI-CAN-22457
- **Date:** 2024-05-19
- **CVE:** CVE-2024-32764
- **CVSS:** 7.4
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Team ECQ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-472/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary configurations on affected installations of QNAP TS-464 NAS devices. An attacker must first obtain the ability to access the device's localhost interface, which can be accomplished using a malicious TURN server. The specific flaw exists within the legacy_cgi endpoints. The issue results from the lack of proper validation of a user-supplied string before using it to update configurations. An attacker can leverage this in conjunction with other vulnerabilities to create arbitrary configurations on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-24-09

## Disclosure Timeline

- 2023-11-15 - Vulnerability reported to vendor
- 2024-05-19 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
