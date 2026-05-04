# ZDI-23-1341: Synology RT6600ax uistrings.cgi Path Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1341
- **ZDI-CAN:** ZDI-CAN-19743
- **Date:** 2023-09-07
- **CVE:** CVE-2023-41740
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Synology
- **Affected Products:** RT6600ax
- **Credit:** Discovered by: Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1341/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Synology RT6600ax routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the uistrings.cgi file. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-global/security/advisory/Synology_SA_23_10

## Disclosure Timeline

- 2022-12-02 - Vulnerability reported to vendor
- 2023-09-07 - Coordinated public release of advisory
