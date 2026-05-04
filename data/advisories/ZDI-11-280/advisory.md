# ZDI-11-280: Microsoft Office Excel Conditional Expression Ptg Type Confusion Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-280
- **ZDI-CAN:** ZDI-CAN-1223
- **Date:** 2011-10-13
- **CVE:** CVE-2011-1989
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-280/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses expressions used for determining formatting requirements. Due to the application not handling certain components of the expression correctly, the application will treat one of the structures as a different type and consequently treat one of its arguments as a pointer. This pointer is used to fetch a virtual method table and can be used to achieve code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms11-072

## Disclosure Timeline

- 2011-06-01 - Vulnerability reported to vendor
- 2011-10-13 - Coordinated public release of advisory
