# ZDI-19-670: (0Day) Microsoft Windows ole32 OleCreateFontIndirectExt Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-670
- **ZDI-CAN:** ZDI-CAN-7959
- **Date:** 2019-07-22
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-670/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of Icon files in the ole32 library. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/11/19 – ZDI reported the vulnerability to the vendor 02/10/19 – The vendor acknowledged 02/18/19 – The vendor requested further details 02/20/19 – ZDI provided the requested information 02/22/19 – The vendor requested more details 02/22/19 – ZDI provided the requested information 02/25/19 – The vendor requested further details 02/26/19 – ZDI provided the requested information 06/07/19 – The vendor requested more details 06/11/19 – ZDI provided the requested information 04/22/19 – The vendor indicated the case did not meet their bar for servicing 04/30/19 – ZDI confirmed the intention to 0-day the case and that the vendor would be notified at that time 07/09/19 – ZDI notified the vendor of the intention to publish the 0-day on 7/22/19 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2019-02-12 - Vulnerability reported to vendor
- 2019-07-22 - Coordinated public release of advisory
