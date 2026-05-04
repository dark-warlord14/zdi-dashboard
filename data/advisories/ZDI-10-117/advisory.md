# ZDI-10-117: Microsoft Office Access AccWizObjects ActiveX Control Uninitialized Imports Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-117
- **ZDI-CAN:** ZDI-CAN-599
- **Date:** 2010-07-13
- **CVE:** CVE-2010-0814
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Access
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-117/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required in that a user must browse to a malicious website. The specific flaws exists in the instantiation of three specific ActiveX controls. The combination of loading all three controls in a particular order results in a transfer of control to unallocated memory which can be leveraged by remote attackers to execute arbitrary code under the context of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-044.mspx

## Disclosure Timeline

- 2009-10-20 - Vulnerability reported to vendor
- 2010-07-13 - Coordinated public release of advisory
