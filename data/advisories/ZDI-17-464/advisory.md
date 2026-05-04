# ZDI-17-464: (Pwn2Own) Microsoft Chakra ArrayBuffer Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-464
- **ZDI-CAN:** ZDI-CAN-4611
- **Date:** 2017-07-10
- **CVE:** CVE-2017-0236
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Tencent Security - Lance Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-464/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ArrayBuffer objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0236

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-07-10 - Coordinated public release of advisory
