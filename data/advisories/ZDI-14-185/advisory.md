# ZDI-14-185: Microsoft Internet Explorer textContent Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-185
- **ZDI-CAN:** ZDI-CAN-2199
- **Date:** 2014-06-11
- **CVE:** CVE-2014-2772
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-185/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the textContent element property. The issue lies in the failure to properly calculate the length of the buffer during a call to memcpy. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms14-035

## Disclosure Timeline

- 2014-03-07 - Vulnerability reported to vendor
- 2014-06-11 - Coordinated public release of advisory
