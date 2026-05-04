# ZDI-19-848: (0Day) Microsoft Windows Storage Service Link Resolution Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-848
- **ZDI-CAN:** ZDI-CAN-9312
- **Date:** 2019-09-24
- **CVE:** N/A
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Jeong Oh Kyea(@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-848/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Storage Service. By creating a junction, an attacker can abuse the service to delete the contents of a chosen folder. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 08/29/19 – ZDI disclosed the vulnerability report to the vendor 08/30/19 – The vendor acknowledged receipt of the report 09/11/19 – The vendor advised ZDI that the report does not meet the bar for servicing 09/12/19 – ZDI advised the vendor of the intent to 0-day the report on 09/24/19 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2019-08-29 - Vulnerability reported to vendor
- 2019-09-24 - Coordinated public release of advisory
