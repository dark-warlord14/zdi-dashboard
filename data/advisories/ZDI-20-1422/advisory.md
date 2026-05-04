# ZDI-20-1422: Microsoft Outlook MSG File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1422
- **ZDI-CAN:** ZDI-CAN-11887
- **Date:** 2020-12-11
- **CVE:** CVE-2020-17119
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Outlook
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1422/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Outlook. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MSG files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17119

## Disclosure Timeline

- 2020-09-18 - Vulnerability reported to vendor
- 2020-12-11 - Coordinated public release of advisory
