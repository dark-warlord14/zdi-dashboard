# ZDI-17-327: (Pwn2Own) Microsoft Chakra Array unshift Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-327
- **ZDI-CAN:** ZDI-CAN-4625
- **Date:** 2017-05-10
- **CVE:** CVE-2017-0238
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Yuki Chen of Qihoo 360 Vulcan Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-327/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Array.unshift method. The issue results from the lack of proper validation of an error condition, which can result in an an Array's length not matching the size of the underlying buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0238

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-05-10 - Coordinated public release of advisory
