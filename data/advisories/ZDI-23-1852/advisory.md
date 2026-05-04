# ZDI-23-1852: (0Day) Honeywell Saia PG5 Controls Suite CAB File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1852
- **ZDI-CAN:** ZDI-CAN-18592
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51603
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Honeywell
- **Affected Products:** Saia PG5 Controls Suite
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1852/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Honeywell Saia PG5 Controls Suite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CAB files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

09/02/22 – ZDI reported the vulnerability to the vendor. 08/30/23 – ZDI asked for an update. 08/30/23 – ZDI re-submitted the report to the vendor. 12/13/23 – ZDI made multiple attempts to contact the vendor PSIRT about these reports, and we have not received a response. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2022-09-08 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
