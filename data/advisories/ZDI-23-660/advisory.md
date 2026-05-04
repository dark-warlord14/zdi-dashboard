# ZDI-23-660: (Pwn2Own) Synology DiskStation Manager Serv.php Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-660
- **ZDI-CAN:** ZDI-CAN-19829
- **Date:** 2023-05-17
- **CVE:** CVE-2022-45188
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation Manager
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-660/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Synology DiskStation Manager. This vulnerability does not require authentication, but does require some user interaction. The specific flaw exists within the Serv.php endpoint. The issue results from incorrect implementation of the authentication mechanism. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-global/security/advisory/Synology_SA_22_23

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
- 2023-07-27 - Advisory Updated
