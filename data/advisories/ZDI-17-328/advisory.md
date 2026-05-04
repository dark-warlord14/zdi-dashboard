# ZDI-17-328: (Pwn2Own) Microsoft Edge AudioBuffer Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-328
- **ZDI-CAN:** ZDI-CAN-4628
- **Date:** 2017-05-10
- **CVE:** CVE-2017-0240
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-328/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AudioBuffer objects. By performing actions in JavaScript an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0240

## Disclosure Timeline

- 2017-03-15 - Vulnerability reported to vendor
- 2017-05-10 - Coordinated public release of advisory
