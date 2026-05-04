# ZDI-12-157: Microsoft Excel Series Record Parsing Type Mismatch Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-157
- **ZDI-CAN:** ZDI-CAN-1374
- **Date:** 2012-08-22
- **CVE:** CVE-2012-1847
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-157/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of Series records. The code within Excel.exe makes an assumption about the data types within a Series record and can be made to write beyond the bounds of a heap buffer when a specific combination of fields are set to unexpected values. This corruption can be leveraged to achieve code execution under the context of the user running the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/MS12-030

## Disclosure Timeline

- 2012-01-24 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
