# ZDI-23-659: (Pwn2Own) Synology DiskStation Manager dnsauth.php Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-659
- **ZDI-CAN:** ZDI-CAN-19828
- **Date:** 2023-05-17
- **CVE:** CVE-2022-45188
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation Manager
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-659/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Synology DiskStation Manager. This vulnerability does not require authentication, but does require some user interaction. The specific flaw exists within the dnsauth.php endpoint. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-global/security/advisory/Synology_SA_22_23

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
- 2023-07-27 - Advisory Updated
