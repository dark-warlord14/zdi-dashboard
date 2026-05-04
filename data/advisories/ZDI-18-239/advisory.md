# ZDI-18-239: Microsoft Chakra Array.splice Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-239
- **ZDI-CAN:** ZDI-CAN-5067
- **Date:** 2018-03-19
- **CVE:** CVE-2017-0228
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** 01
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-239/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the Array.splice method. By performing actions in JavaScript an attacker can trigger a memory corruption condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0228

## Disclosure Timeline

- 2017-07-27 - Vulnerability reported to vendor
- 2018-03-19 - Coordinated public release of advisory
- 2018-03-19 - Advisory Updated
