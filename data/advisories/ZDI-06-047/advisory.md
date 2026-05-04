# ZDI-06-047: Microsoft Visual Studio WmiScriptUtils.dll Cross-Zone Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-047
- **ZDI-CAN:** ZDI-CAN-068
- **Date:** 2006-12-12
- **CVE:** CVE-2006-4704
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio 2005
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. Successful exploitation requires that the target user browse to a malicious web page. The specific flaw exists in the Microsoft WMIScriptUtils.WMIObjectBroker2 ActiveX control which is bundled with Visual Studio 2005. An attacker can utilize this control to bypass Internet zone security restrictions and instantiate other dangerous objects that can be leveraged to result in arbitrary code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS06-073.mspx

## Disclosure Timeline

- 2006-06-15 - Vulnerability reported to vendor
- 2006-12-12 - Coordinated public release of advisory
