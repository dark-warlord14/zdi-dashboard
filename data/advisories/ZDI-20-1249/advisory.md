# ZDI-20-1249: Microsoft Outlook HTML Email Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1249
- **ZDI-CAN:** ZDI-CAN-11249
- **Date:** 2020-10-19
- **CVE:** CVE-2020-16947
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Outlook
- **Credit:** 0neb1n
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1249/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Outlook. User interaction is required to exploit this vulnerability in that the target must open a malicious email or view it in the preview pane. The specific flaw exists within the parsing of HTML content in email. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-16947

## Disclosure Timeline

- 2020-07-01 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
