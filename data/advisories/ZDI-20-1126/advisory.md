# ZDI-20-1126: Microsoft Visual Studio DDS File Parsing Integer Overflow Remote Code Execution Multiple Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-20-1126
- **ZDI-CAN:** ZDI-CAN-11214
- **Date:** 2020-09-10
- **CVE:** CVE-2020-16874
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1126/
## Vulnerability Details

These vulnerabilities allow remote attackers to execute arbitrary code on affected installations of Microsoft Visual Studio. User interaction is required to exploit these vulnerabilities in that the target must visit a malicious page or open a malicious file. The specific flaws exist within the dxtex module. Crafted data in a DDS file can trigger an integer overflow before allocating a buffer. An attacker can leverage these vulnerabilities to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-16874

## Disclosure Timeline

- 2020-06-17 - Vulnerability reported to vendor
- 2020-09-10 - Coordinated public release of advisory
