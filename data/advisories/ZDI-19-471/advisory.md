# ZDI-19-471: Microsoft Edge DownloadOperation Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-471
- **ZDI-CAN:** ZDI-CAN-8377
- **Date:** 2019-05-15
- **CVE:** CVE-2019-0938
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Arthur Gerkis of Exodus Intelligence (@ax330d)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-471/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of messages passed from the renderer process to the broker process of Microsoft Edge. A crafted message can trigger execution of a privileged operation. An attacker can leverage this vulnerability to escalate privileges and escape the Microsoft Edge sandbox.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0938

## Disclosure Timeline

- 2019-05-15 - Vulnerability reported to vendor
- 2019-05-15 - Coordinated public release of advisory
