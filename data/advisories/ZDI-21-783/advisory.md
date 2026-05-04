# ZDI-21-783: QNAP NAS Hybrid Backup Missing Authentication for Critical Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-783
- **ZDI-CAN:** ZDI-CAN-13810
- **Date:** 2021-07-08
- **CVE:** CVE-2021-28809
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** NAS
- **Credit:** Ta-Lun Yen of TXOne IoT/ICS Security Research Labs (Trend Micro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-783/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of QNAP NAS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RTSS server, which listens on TCP port 8899 by default. The issue results from the lack of authentication prior to allowing alterations to the system configuration. An attacker can leverage this vulnerability to execute arbitrary code in the context of the Administrator.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisory/QSA-21-19

## Disclosure Timeline

- 2021-05-05 - Vulnerability reported to vendor
- 2021-07-08 - Coordinated public release of advisory
