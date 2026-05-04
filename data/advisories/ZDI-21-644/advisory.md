# ZDI-21-644: Bosch B426 Web Configuration Use of Hard-coded Password Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-644
- **ZDI-CAN:** ZDI-CAN-13074
- **Date:** 2021-06-03
- **CVE:** CVE-2021-23845
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bosch
- **Affected Products:** B426
- **Credit:** Chizuru Toyama of TXOne IoT/ICS Security Research Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-644/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Bosch B426. Authentication is not required to exploit this vulnerability. The specific flaw exists within the lgs.cgi module. This issue results from the use of hard-coded session token. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Bosch has issued an update to correct this vulnerability. More details can be found at: https://psirt.bosch.com/security-advisories/bosch-sa-196933-bt.html

## Disclosure Timeline

- 2021-01-29 - Vulnerability reported to vendor
- 2021-06-03 - Coordinated public release of advisory
- 2021-06-07 - Advisory Updated
