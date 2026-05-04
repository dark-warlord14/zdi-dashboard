# ZDI-25-250: (0Day) Cloudera Hue Ace Editor Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-250
- **ZDI-CAN:** ZDI-CAN-24332
- **Date:** 2025-04-23
- **CVE:** CVE-2025-3884
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Cloudera
- **Affected Products:** Hue
- **Credit:** Hamidreza Hamidi and Jafar Akhoundali
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-250/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cloudera Hue. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Ace Editor web application. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

08/01/24 – ZDI reported the vulnerability to the vendor 08/01/24 – the vendor acknowledged the receipt of the report 09/11/24 - ZDI asked for updates 11/17/24 - ZDI asked for updates 04/15/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory

## Disclosure Timeline

- 2024-08-01 - Vulnerability reported to vendor
- 2025-04-23 - Coordinated public release of advisory
- 2025-04-23 - Advisory Updated
