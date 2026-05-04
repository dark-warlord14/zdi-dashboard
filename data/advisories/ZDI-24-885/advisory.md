# ZDI-24-885: Progress Software WhatsUp Gold LoadUsingBasePath Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-885
- **ZDI-CAN:** ZDI-CAN-23760
- **Date:** 2024-07-03
- **CVE:** CVE-2024-5018
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Abdessamad Lahlali of Trend Micro.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-885/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Progress Software WhatsUp Gold. Authentication is not required to exploit this vulnerability. The specific flaw exists within the LoadUsingBasePath method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-June-2024

## Disclosure Timeline

- 2024-03-27 - Vulnerability reported to vendor
- 2024-07-03 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
