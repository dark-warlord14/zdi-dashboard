# ZDI-21-1235: (0Day) Vinchin Backup and Recovery Use of Hard-coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1235
- **ZDI-CAN:** ZDI-CAN-14046
- **Date:** 2021-10-27
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Vinchin
- **Affected Products:** Backup and Recovery
- **Credit:** Esjay
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1235/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Vinchin Backup and Recovery. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of API access keys. The issue results from the use of a hard-coded access key to validate API requests. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/04/21 – ZDI requested PSIRT contact 08/12/21 – ZDI requested an update 08/16/21 – Vendor sent an automation reply that a ticket had been created 09/06/21 – Vendor mentioned that a salesperson would be responding soon 09/06/21 – ZDI asked them to provide PGP key to send them the vulnerability reports, but there was no reply 10/20/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 10/27/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-10-27 - Vulnerability reported to vendor
- 2021-10-27 - Coordinated public release of advisory
