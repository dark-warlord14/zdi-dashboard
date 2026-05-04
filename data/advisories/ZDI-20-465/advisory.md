# ZDI-20-465: Microsoft SharePoint Scorecards Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-465
- **ZDI-CAN:** ZDI-CAN-10089
- **Date:** 2020-04-15
- **CVE:** CVE-2020-0931
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-465/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of controls in the Microsoft.PerformancePoint.Scorecards.Client module. Instantiating the ExcelDataSet control can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the SharePoint web server process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0931

## Disclosure Timeline

- 2020-01-17 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
