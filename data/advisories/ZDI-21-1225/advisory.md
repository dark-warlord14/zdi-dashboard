# ZDI-21-1225: Microsoft SharePoint SetVariableActivity Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1225
- **ZDI-CAN:** ZDI-CAN-14787
- **Date:** 2021-10-21
- **CVE:** CVE-2021-40487
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1225/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the Microsoft.SharePoint.WorkflowActions.SetVariableActivity class. A crafted SetVariableActivity element can result in instantiation of an arbitrary .NET type. An attacker can leverage this vulnerability to execute code in the context of the web service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40487

## Disclosure Timeline

- 2021-08-25 - Vulnerability reported to vendor
- 2021-10-21 - Coordinated public release of advisory
