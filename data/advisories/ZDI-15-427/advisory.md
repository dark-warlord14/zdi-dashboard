# ZDI-15-427: Microsoft Internet Explorer CImgTaskSvgDoc Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-427
- **ZDI-CAN:** ZDI-CAN-3025
- **Date:** 2015-09-08
- **CVE:** CVE-2015-2501
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sean Verity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-427/
## Vulnerability Details

This vulnerability allows remote attackers to cause a use-after-free condition on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of svg images. A specially crafted svg image can cause Internet Explorer to reuse a CImgTaskSvgDoc object in memory after it has been freed. An attacker may be able to leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms15-094

## Disclosure Timeline

- 2015-07-02 - Vulnerability reported to vendor
- 2015-09-08 - Coordinated public release of advisory
