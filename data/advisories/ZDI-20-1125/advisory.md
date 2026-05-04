# ZDI-20-1125: Microsoft Visual Studio DDS File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1125
- **ZDI-CAN:** ZDI-CAN-11213
- **Date:** 2020-09-10
- **CVE:** CVE-2020-16856
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** Wen guang Jiao
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1125/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Visual Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the dxtex module. Crafted data in a DDS file can trigger an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16856

## Disclosure Timeline

- 2020-06-11 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory
