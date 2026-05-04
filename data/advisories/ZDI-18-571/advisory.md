# ZDI-18-571: (Pwn2Own) Microsoft Edge WebRTC Parameters Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-571
- **ZDI-CAN:** ZDI-CAN-5815
- **Date:** 2018-06-08
- **CVE:** CVE-2018-8179
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-571/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of parameters to WebRTC APIs. By performing actions in JavaScript an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8179

## Disclosure Timeline

- 2018-03-18 - Vulnerability reported to vendor
- 2018-06-08 - Coordinated public release of advisory
- 2018-06-08 - Advisory Updated
