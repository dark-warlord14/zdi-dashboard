# ZDI-23-1495: A10 Thunder ADC ShowTechDownloadView Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1495
- **ZDI-CAN:** ZDI-CAN-17899
- **Date:** 2023-10-04
- **CVE:** CVE-2023-42129
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** A10
- **Affected Products:** Thunder ADC
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1495/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of A10 Thunder ADC. Authentication is required to exploit this vulnerability. The specific flaw exists within the ShowTechDownloadView class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

A10 has issued an update to correct this vulnerability. More details can be found at: https://support.a10networks.com/support/security_advisory/a10-acos-file-access-vulnerability/

## Disclosure Timeline

- 2022-09-20 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
