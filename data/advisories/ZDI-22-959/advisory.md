# ZDI-22-959: (0Day) Vinchin Backup and Recovery MySQL Server Use of Hard-coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-959
- **ZDI-CAN:** ZDI-CAN-17139
- **Date:** 2022-07-08
- **CVE:** CVE-2022-35866
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Vinchin
- **Affected Products:** Backup and Recovery
- **Credit:** Esjay
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-959/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Vinchin Backup and Recovery. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the MySQL server. The server uses a hard-coded password for the administrator user. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120-day deadline. 04/29/22 – ZDI attempted to contact the vendor PSIRT and obtain secure keys via the contact information on their website as well as using the chat support feature. 05/17/22 – ZDI made another attempt to contact the vendor with no response back. 05/25/22 – ZDI made one final attempt to contact the vendor’s key leadership. 06/30/22 – ZDI confirmed that this vulnerability is still exploitable and has not been patched. 07/01/22 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 07/8/22 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-07-08 - Vulnerability reported to vendor
- 2022-07-08 - Coordinated public release of advisory
- 2022-07-14 - Advisory Updated
