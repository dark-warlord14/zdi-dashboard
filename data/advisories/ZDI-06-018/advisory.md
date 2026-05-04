# ZDI-06-018: Microsoft Internet Explorer DXImageTransform ActiveX Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-018
- **ZDI-CAN:** ZDI-CAN-044
- **Date:** 2006-06-13
- **CVE:** CVE-2006-2383
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-018/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. Successful exploitation requires that the target user browse to a malicious web page. The specific flaw exists in the Microsoft ActiveX object DXImageTransform.Microsoft.MMSpecialEffect1Input. Due to improper garbage collection when another object is assigned to any property, code execution is possible. This object implements the IObjectSafety interface and thus the default Internet Explorer settings allow for arbitrary code execution without any further user interaction. Several related ActiveX objects suffer from the same problem including: * DXImageTransform.Microsoft.MMSpecialEffect1Input.1 * DXImageTransform.Microsoft.MMSpecialEffect2Inputs * DXImageTransform.Microsoft.MMSpecialEffect2Inputs.1 * DXImageTransform.Microsoft.MMSpecialEffectInplace1Input * DXImageTransform.Microsoft.MMSpecialEffectInplace1Input.1

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS06-021.mspx

## Disclosure Timeline

- 2006-04-27 - Vulnerability reported to vendor
- 2006-06-13 - Coordinated public release of advisory
