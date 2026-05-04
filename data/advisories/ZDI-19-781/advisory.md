# ZDI-19-781: (0Day) Microsoft Windows user32 Cursor Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-781
- **ZDI-CAN:** ZDI-CAN-8748
- **Date:** 2019-09-04
- **CVE:** CVE-2019-1283
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-781/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of cursor files in the user32 library. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/02/2019 - ZDI reported the vulnerability to the vendor 07/02/2019 - The vendor acknowledged the report 07/31/2019 - The vendor acknowledged reproduction of the report 08/12/2019 - The vendor advised that the report does not meet their bar for servicing and the report would be closed 08/28/2019 - ZDI notified the vendor of the intention to disclose the report as a 0-day advisory -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2019-07-02 - Vulnerability reported to vendor
- 2019-09-04 - Coordinated public release of advisory
- 2019-09-06 - Advisory Updated
