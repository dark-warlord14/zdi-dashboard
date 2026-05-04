# ZDI-21-755: Microsoft SharePoint WorkflowCompilerInternal Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-755
- **ZDI-CAN:** ZDI-CAN-13349
- **Date:** 2021-06-23
- **CVE:** CVE-2021-26420
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-755/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the System.Workflow.ComponentModel.Compiler.WorkflowCompilerInternal class. This class allows an attacker to specify a path to an arbitrary workflow definition file. An attacker can leverage this vulnerability to execute code in the context of the web service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26420

## Disclosure Timeline

- 2021-03-26 - Vulnerability reported to vendor
- 2021-06-23 - Coordinated public release of advisory
