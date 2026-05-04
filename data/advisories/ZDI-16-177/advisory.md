# ZDI-16-177: Microsoft Edge CAsyncTpWorker Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-177
- **ZDI-CAN:** ZDI-CAN-3408
- **Date:** 2016-03-08
- **CVE:** CVE-2016-0118
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Jaanus Kp - Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-177/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code that renders PDF documents. By supplying a malformed PDF document an attacker can cause Microsoft Edge to use a Infra::CAsyncTpWorker object in memory after it has been freed. An attacker can leverage this to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS16-028

## Disclosure Timeline

- 2015-11-12 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory
