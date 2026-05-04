# ZDI-17-912: Microsoft Chakra Regular Expression Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-912
- **ZDI-CAN:** ZDI-CAN-5198
- **Date:** 2017-11-20
- **CVE:** CVE-2017-11858
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Huang Anwen of ichunqiu Ker Team(https://www.ichunqiu.com/ )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-912/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of regular expressions. A crafted regular expression can trigger an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-11858

## Disclosure Timeline

- 2017-09-05 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
