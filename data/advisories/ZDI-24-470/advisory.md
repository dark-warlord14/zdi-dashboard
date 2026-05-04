# ZDI-24-470: (Pwn2Own) QNAP TS-464 QR Code Device CRLF Injection Arbitrary Configuration Change Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-470
- **ZDI-CAN:** ZDI-CAN-22493
- **Date:** 2024-05-19
- **CVE:** CVE-2024-21899
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** LJP (@ljp_tw) and YingMuo (@YingMuo), working with DEVCORE Internship Program
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-470/
## Vulnerability Details

This vulnerability allows remote attackers to make arbitrary changes to configuration on affected installations of QNAP TS-464 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the privWizard API endpoints. The issue results from the lack of proper validation of a user-supplied string before using it to update configuration. An attacker can leverage this vulnerability to change the configuration of the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-24-09

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-05-19 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
