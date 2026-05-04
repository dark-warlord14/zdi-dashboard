# ZDI-18-948: Microsoft Chakra Floating Point Array Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-948
- **ZDI-CAN:** ZDI-CAN-6154
- **Date:** 2018-08-14
- **CVE:** CVE-2018-0953
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-948/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of floating-point arrays in JIT code. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0953

## Disclosure Timeline

- 2018-05-04 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
