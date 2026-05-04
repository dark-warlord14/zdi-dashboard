# ZDI-18-165: Microsoft Chakra String Concatenation Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-165
- **ZDI-CAN:** ZDI-CAN-5324
- **Date:** 2018-02-21
- **CVE:** CVE-2018-0758
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** 010
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-165/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the generation of JIT code for functions that perform string concatenations. By performing actions in JavaScript, an attacker can trigger an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0758

## Disclosure Timeline

- 2017-11-07 - Vulnerability reported to vendor
- 2018-02-21 - Coordinated public release of advisory
- 2018-02-21 - Advisory Updated
