# ZDI-16-283: (Pwn2Own) Microsoft Edge JavaScript fill Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-283
- **ZDI-CAN:** ZDI-CAN-3626
- **Date:** 2016-05-10
- **CVE:** CVE-2016-0193
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Zhen Feng Wen Xu of KeenLab Tencent
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-283/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the JavaScript fill method. By performing certain operations in script, an attacker can cause JavaScript to access outside the bounds of an array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-052.aspx

## Disclosure Timeline

- 2016-03-12 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
