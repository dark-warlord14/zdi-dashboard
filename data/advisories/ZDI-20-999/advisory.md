# ZDI-20-999: Microsoft Outlook EML Rendering Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-999
- **ZDI-CAN:** ZDI-CAN-10914
- **Date:** 2020-08-13
- **CVE:** CVE-2020-1493
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Outlook
- **Credit:** 0neb1n
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-999/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Outlook. User interaction is required to exploit this vulnerability in that the target must open a malicious email. The specific flaw exists within the rendering of emails. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1493

## Disclosure Timeline

- 2020-05-07 - Vulnerability reported to vendor
- 2020-08-13 - Coordinated public release of advisory
