# ZDI-10-034: Microsoft Internet Explorer Tabular Data Control ActiveX Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-034
- **ZDI-CAN:** ZDI-CAN-589
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0805
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer 6. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the Tabular Data Control ActiveX module. Specifically, if provided a malicious DataURL parameter a stack corruption may occur in the function CTDCCtl::SecurityCHeckDataURL. This can be leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-018.mspx

## Disclosure Timeline

- 2009-10-20 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
