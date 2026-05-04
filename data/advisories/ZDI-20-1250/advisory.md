# ZDI-20-1250: Microsoft Outlook HTML Email Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1250
- **ZDI-CAN:** ZDI-CAN-11250
- **Date:** 2020-10-19
- **CVE:** CVE-2020-16947
- **CVSS:** 3.7
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Outlook
- **Credit:** 0neb1n
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1250/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Outlook. User interaction is required to exploit this vulnerability in that the target must open a malicious email or view it in the preview pane. The specific flaw exists within the parsing of HTML content in email. A crafted email can trigger a read before the start of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-16947

## Disclosure Timeline

- 2020-07-01 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
