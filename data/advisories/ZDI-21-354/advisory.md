# ZDI-21-354: (0Day) Lepide Active Directory Self Service Backup Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-354
- **ZDI-CAN:** ZDI-CAN-12008
- **Date:** 2021-03-23
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Lepide
- **Affected Products:** Active Directory Self Service
- **Credit:** Nabeel Ahmed (@rogue_kdc) and Eric Schayes of NTT Belgium
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-354/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Lepide Active Directory Self Service. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of backup functionality. The issue results from the lack of proper authentication when creating and importing backups. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/08/20 – ZDI reported the vulnerability to the vendor/ICS-CERT 02/10/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 02/18/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-10-09 - Vulnerability reported to vendor
- 2021-03-23 - Coordinated public release of advisory
