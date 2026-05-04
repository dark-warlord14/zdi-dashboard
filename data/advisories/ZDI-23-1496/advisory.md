# ZDI-23-1496: A10 Thunder ADC FileMgmtExport Directory Traversal Arbitrary File Read and Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1496
- **ZDI-CAN:** ZDI-CAN-17905
- **Date:** 2023-10-04
- **CVE:** CVE-2023-42130
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:H
- **Affected Vendors:** A10
- **Affected Products:** Thunder ADC
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1496/
## Vulnerability Details

This vulnerability allows remote attackers to read and delete arbitrary files on affected installations of A10 Thunder ADC. Authentication is required to exploit this vulnerability. The specific flaw exists within the FileMgmtExport class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to read and delete files in the context of the service account.

## Additional Details

A10 has issued an update to correct this vulnerability. More details can be found at: https://support.a10networks.com/support/security_advisory/a10-acos-file-access-vulnerability/

## Disclosure Timeline

- 2022-09-20 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
