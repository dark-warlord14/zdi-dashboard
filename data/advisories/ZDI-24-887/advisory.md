# ZDI-24-887: Progress Software WhatsUp Gold GetASPReport Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-887
- **ZDI-CAN:** ZDI-CAN-23564
- **Date:** 2024-07-03
- **CVE:** CVE-2024-5014
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Abdessamad Lahlali of Trend Micro.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-887/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Progress Software WhatsUp Gold. Authentication is required to exploit this vulnerability. The specific flaw exists within the GetASPReport method. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose information in the context of the application.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-June-2024

## Disclosure Timeline

- 2024-03-07 - Vulnerability reported to vendor
- 2024-07-03 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
