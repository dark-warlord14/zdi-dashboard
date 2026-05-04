# ZDI-23-658: (Pwn2Own) Synology DiskStation Manager api.php Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-658
- **ZDI-CAN:** ZDI-CAN-19609
- **Date:** 2023-05-17
- **CVE:** CVE-2022-45188
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation Manager
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-658/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Synology DiskStation Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the api.php endpoint. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-global/security/advisory/Synology_SA_22_23

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
- 2023-07-27 - Advisory Updated
