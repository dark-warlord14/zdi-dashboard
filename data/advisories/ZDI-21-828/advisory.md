# ZDI-21-828: Microsoft SharePoint SetVariableActivity Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-828
- **ZDI-CAN:** ZDI-CAN-13358
- **Date:** 2021-07-19
- **CVE:** CVE-2021-34520
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-828/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the Microsoft.SharePoint.WorkflowActions.SetVariableActivity class. A crafted SetVariableActivity element can result in instantiation of an arbitrary .NET type. An attacker can leverage this vulnerability to execute code in the context of the web service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2021-34520

## Disclosure Timeline

- 2021-03-26 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
